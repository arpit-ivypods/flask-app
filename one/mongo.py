from pymongo import MongoClient
from flask_restful import Resource, Api
from flask_restful import reqparse
import json

class mongotest(Resource):
    def post(self):
        try:
            client = MongoClient("mongodb+srv://ivyprodadmin:ayj1RQmL9tp27Bkz@sandbox-ciuh2.mongodb.net/test?retryWrites=true&w=majority")
            db = client.get_database("beta")
            records = db['users']
            mydoc = records.find()
            for x in mydoc:
                return json.dumps(str(x['_id']))
        except Exception as e:
            return {'status': '400', 'Message': str(e)}


