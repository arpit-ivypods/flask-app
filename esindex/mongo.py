from pymongo import MongoClient
from bson.objectid import ObjectId
import boto3
from botocore.exceptions import ClientError
import env

def allRecords(col):
    db = env.mongoConnect('')
    records = db[col]
    query = {}
    mydoc = records.find()
    return mydoc

def recordsById(key, val, col):
    db = env.mongoConnect('')
    print(db)
    records = db[col]
    query = {key: val}
    try:
        mydoc = records.find(query)
        for data in mydoc:
            return data
    except Exception as e:
        return {}
