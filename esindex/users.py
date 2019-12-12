import uuid
from elasticsearch import Elasticsearch
import json
from esindex import models
from esindex import es
from esindex import mongo
from flask_restful import Resource, Api
from flask_restful import reqparse
import threading

def createEsUserIndex():
    userModel = models.user()
    print(userModel)
    userIndex = es.create('users', userModel)
    print(userIndex)

def deleteUserIndex():
    es.delete('users')

async def saveEsUser(data):
    for user in data:
        if (user['currentJourney'] == 'D'):
            attr = mongo.recordsById(user['_id'], 'userattributes')
            createUserObj(user, attr)

def getAllUsers():
    deleteUserIndex()
    createEsUserIndex()
    data = mongo.allRecords('users')
    saveEsUser(data)





def createUserObj(user, attr):
    userObj = {
        'userId': str(user['_id']),
        'fullName': user['fullName'],
        'age': user['age'],
        'college': user['college'],
        'company': user['company'],
        'coverPicture': {"url":user['coverPicture']['url']},
        'dPrefBudget': {'min': attr['dPrefBudget']['min'], 'max': attr['dPrefBudget']['max']},
        'address': attr['dPrefLocality']['name'],
        'coordinates': {
            'lat': attr['dPrefLocation']['coordinates']['lat'],
            'lon': attr['dPrefLocation']['coordinates']['lng']
        },
        'createdAt': user['createdAt']
    }
    es.insertDoc('users', userObj)

class createUserIndex(Resource):
    def post(self):
        try:
            # print("one")
            getAllUsers()
        except Exception as e:
            return {'status': '400', 'Message': str(e)}
