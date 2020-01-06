import uuid
from elasticsearch import Elasticsearch
import json
from esindex import models
from esindex import es
from esindex import mongo
from flask_restful import Resource, Api
from flask_restful import reqparse
from esindex import validate
import uuid


class createRoomsIndex(Resource):
    def post(self):
        try:
            createAllRoomsData()
            return {'status':200, 'message':'success'}
        except Exception as e:
            return {'status': 400, 'message': str(e)}

def createAllRoomsData():
    deleteEsRoomsIndex()
    createEsRoomsIndex()
    dataHouses = mongo.allRecords('houses')
    saveEsRoom(dataHouses)

def deleteEsRoomsIndex():
    es.delete('rooms')

def createEsRoomsIndex():
    roomModel = models.rooms()
    createRoomIndex = es.create('rooms', roomModel)

def saveEsRoom(dataHouses):
    allRooms = []
    for house in dataHouses:    
        room = mongo.recordsById('houseId', house['_id'], 'rooms')
        user = mongo.recordsById('_id',house['users'][0]['id'], 'users')
        roomObj = createRoomObj(house, room, user) 
        allRooms.append(roomObj)
    es.insertBulk('rooms', allRooms)

def createRoomObj(house, room, user):
    user = validate.user(user)
    house = validate.house(house)
    room = validate.room(room)
    roomObj = {
        'userId': str(user['_id']),
        'fullName': user['fullName'],
        'age': user['age'],
        'college': user['college'],
        'company': user['company'],
        'author': user['author'],
        'userCoverPicture': {'url': user['coverPicture']['url']},
        'houseId': str(house['_id']),
        'locality': house['locality']['name'],
        'genderPref': house['genderPref'],
        'city': house['city']['name'],
        'coordinates': {
            'lat': house['location']['coordinates']['lat'],
            'lon': house['location']['coordinates']['lng']
        },
    'id': str(room['_id']),
    'roomCoverPicture': {'url': room['coverPicture']['url']},
    'rent': room['rent'],
    'title': room['title'],
    'createdAt': room['createdAt']
    }
    return roomObj


