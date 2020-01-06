from flask_restful import Resource, Api
from flask_restful import reqparse
from elasticsearch import Elasticsearch
import json
from pymongo import MongoClient
import boto3
import env
class delete(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument(
                'dbName', type=str, help='Name of the database',  required=True, location='args')
            parser.add_argument(
                'code', type=int, help='pass the longitude', required=True, location='args')
            args = parser.parse_args()
            _dbName = args['dbName']
            _code = args['code']
            status = validate(_dbName, _code)
            if status == True:
                db = getdb(_dbName)
                bucket = getS3()
                imgDir = 'upload-'+_dbName
                deleteData(bucket, imgDir, db)
                return {'status': 200, 'message': 'success'}
            else:
                return {'status':400,'message':'invalid params'}
        except Exception as e:
            return {'status': 400, 'message': str(e)}

def validate(dbName, code):
    status = True
    if dbName == 'ankit' or dbName == 'anshu' or dbName == 'beta' or dbName == 'local-db':
        status = True
    else:
        status = False
    if code != 9910252444:
        status = False
    return status

def getdb(_dbName):
    try:
        db = env.mongoConnect(_dbName)
        return db
    except Exception as e:
        return None

def getS3():
    try:
        bucket = env.s3()
        return bucket
    except Exception as e:
        return None

def deleteData(bucket, imgDir, db):
    cols = db.list_collection_names()
    for c in cols:
        records = db[c]
        x = records.delete_many({})
    bucket.objects.filter(Prefix=imgDir).delete()
    return True