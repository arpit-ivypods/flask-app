import uuid
from elasticsearch import Elasticsearch
import json
from esindex import models
from esindex import es
from esindex import mongo
from flask_restful import Resource, Api
from flask_restful import reqparse
from esindex import validate

class createUserIndex(Resource):
    def post(self):
        try:
            createAllUsersData()
        except Exception as e:
            return {'status': '400', 'Message': str(e)}

def createAllUsersData():
    deleteEsUserIndex()
    createEsUserIndex()
    data = mongo.allRecords('users')
    saveEsUser(data)

def deleteEsUserIndex():
    es.delete('users')

def createEsUserIndex():
    userModel = models.user()
    userIndex = es.create('users', userModel)

def saveEsUser(data):
    allUsers = []
    count = 0
    for user in data:
        attr = ''
        if user.get('currentJourney') != None:
            if (user['currentJourney'] == 'D'):
                try:
                    attr = mongo.recordsById('userId',user['_id'], 'userattributes')
                except Exception as e:
                    print(e)
                if attr == None:
                    attr = {}
                userObj = createUserObj(user, attr)
                count += 1
                allUsers.append(userObj)

    print(count)
    es.insertBulk('users', allUsers)

def createUserObj(user, attr):
    user = validate.dUser(user)
    attr = validate.dUserAttr(attr)
    userObj = {
     
            'id': str(user['_id']),
            'fullName': user['fullName'],
            'age': user['age'],
            'author': user['author'],
            'college': user['college'],
            'company': user['company'],
            'coverPicture': {"url":user['coverPicture']['url']},
            'createdAt': user['createdAt'],
            'dPrefBudget': {'min': attr['dPrefBudget']['min'], 'max': attr['dPrefBudget']['max']},
            'address': attr['dPrefLocality']['name'],
            'coordinates': {
                'lat': attr['dPrefLocation']['coordinates']['lat'],
                'lon': attr['dPrefLocation']['coordinates']['lng']
            }
    }
    
    return userObj
