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
        except Exception as e:
            return {'status': '400', 'Message': str(e)}

def createAllRoomsData():
    deleteEsRoomsIndex()
    createEsRoomsIndex()
    dataHouse = mongo.allRecords('houses')
    saveEsRoom(dataHouse)

def deleteEsRoomsIndex():
    es.delete('rooms')

def createEsRoomsIndex():
    roomModel = models.rooms()
    createRoomIndex = es.create('rooms', roomModel)

def saveEsRoom(dataHouse):
    allRooms = []
    for house in dataHouse:
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
        'roomId': str(room['_id']),
        'houseId': str(house['_id']),
        'fullName': user['fullName'],
        'age': user['age'],
        'college': user['college'],
        'company': user['company'],
        'userCoverPicture': {'url': user['coverPicture']['url']},
        'locality': house['locality']['name'],
        'genderPref': house['genderPref'],
        'city': house['city']['name'],
        'coordinates': {
            'lat': house['location']['coordinates']['lat'],
            'lon': house['location']['coordinates']['lng']
        },
        'roomCoverPicture': {'url': room['coverPicture']['url']},
        'rent': room['rent'],
        'title': room['title'],
        'createdAt': room['createdAt']
    }
    return roomObj


