import env
from elasticsearch import Elasticsearch, helpers
import json
import uuid



def create(index_name, model):
    es_object = env.esConnect()
    created = False
    try:
        if not es_object.indices.exists(index_name):
            es_object.indices.create(
                index=index_name, ignore=400, body=model)
            created = True
    except Exception as ex:
        return created
    finally:
        return created

def delete(index_name):
    es_object = env.esConnect()
    try:
        es_object.indices.delete(
            index=index_name)
        return True
    except Exception as ex:
        return False

def insertDoc(index_name, data):
    es_object = env.esConnect()
    try:
        res = es_object.index(index=index_name, body=data)
        return True
    except Exception as ex:
        return False

def insertBulk(index_name, data):
    es_object = env.esConnect()
    try:
        response = helpers.bulk(
            es_object, data, index=index_name)
        return True
    except Exception as ex:
        return False
