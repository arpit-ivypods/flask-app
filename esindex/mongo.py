from pymongo import MongoClient
from bson.objectid import ObjectId
import boto3
from botocore.exceptions import ClientError
import env

db = env.mongoConnect()

def allRecords(col):
    records = db[col]
    query = {}
    mydoc = records.find()
    return mydoc

def recordsById(id, col):
    records = db[col]
    query = {"userId": id}
    mydoc = records.find(query)
    for x in mydoc:
        return x