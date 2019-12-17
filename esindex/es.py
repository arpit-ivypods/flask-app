import env
from elasticsearch import Elasticsearch, helpers
import json
import uuid


def create(index_name, model):
    # print("hello")
    es_object = env.esConnect()
    created = False
    # print(index_name, model)
    try:
        if not es_object.indices.exists(index_name):
            # Ignore 400 means to ignore "Index Already Exist" error.
            es_object.indices.create(
                index=index_name, ignore=400, body=model)
            # print('Created Index')
            created = True
    except Exception as ex:
        print(str(ex))
    finally:
        return created


def delete(index_name):
    es_object = env.esConnect()
    try:
        es_object.indices.delete(
            index=index_name)
        # print('Deleted Index')
    except Exception as ex:
        print(str(ex))


def insertDoc(index_name, data):
    es_object = env.esConnect()
    try:
        res = es_object.index(index=index_name, body=data)
    except Exception as ex:
        print(str(ex))


def insertBulk(index_name, data):
    es_object = env.esConnect()
    actions = [
        {
            "_id": uuid.uuid4(),  # random UUID for _id
            "doc_type": "person",  # document _type
            "doc": {  # the body of the document
                "nafullNameme": "George Peterson",
                "age": 34+doc
            }
        }
        for doc in range(100)
    ]

    try:
        response = helpers.bulk(
            es_object, data, index=index_name)

        print(response)
    except Exception as ex:
        print(str(ex))
