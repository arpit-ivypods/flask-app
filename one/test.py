from flask_restful import Resource, Api
from flask_restful import reqparse
from elasticsearch import Elasticsearch


class HelloWorld(Resource):
    def post(self):
        try:
            es_object = Elasticsearch(
                ['https://26a418083cab4f02933a878450866715.us-east-1.aws.found.io'], port=9243, http_auth=('elastic', 'M1t0Nda4IySU7nbLoownEnHW'))

            # return "arpit"
            query = {"match": {"fullName": "Ritika Subba"}}
            res = es_object.search(
                index="users", body=query)
            for hit in res['hits']['hits']:
                return hit["_source"]['fullName']
            # parser = reqparse.RequestParser()
            # parser.add_argument('email', type=str, help='to email address')
            # args = parser.parse_args()
            # _email = args['email']
            # subject = "Welcome to Roofpik "+_email+"!"
            # return subject

        except Exception as e:
            return {'status':'400','Message':str(e)}

		# return "arpit"

