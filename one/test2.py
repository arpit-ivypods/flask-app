from flask_restful import Resource, Api
from flask_restful import reqparse
from elasticsearch import Elasticsearch
import env
import json


def userQueryBuilder(lat, lon, start, size):
    print(lat, lon, start, size)
    query = {}
    query["from"] = start
    query["size"] = size
    query["query"] = {}
    query['query']['function_score'] = {}
    query['query']['function_score']['query'] = {"match_all": {}}
    query['query']['function_score']['boost'] = 5
    query['query']['function_score']['functions'] = [
        {

            "filter": {
                "range": {
                    "createdAt": {
                        "gte": "now-7d/d"
                    }
                }
            },
            "weight": 21

        },
        {
            "filter": {
                "geo_distance": {
                    "distance": "30km",
                    "coordinates": {
                        "lat": lat,
                        "lon": lon
                    }
                }
            },
            "weight": 42
        }


    ]
    query['query']['function_score']['max_boost'] = 42
    query['query']['function_score']['score_mode'] = 'max'
    query['query']['function_score']['boost_mode'] = 'multiply'
    query['query']['function_score']['min_score'] = 42
    return query


class listing(Resource):
    def post(self):
        try:
            es_object = env.esConnect()
            parser = reqparse.RequestParser()
            parser.add_argument(
                'lat', type=float, help='pass the latitude', default=28.4498494)
            parser.add_argument(
                'lng', type=float, help='pass the longitude', default=77.0566887)
            parser.add_argument(
                'page', type=int, help='page of listing', default=1)
            parser.add_argument(
                'size', type=int, help='total number of listings', default=20)
            args = parser.parse_args()
            _lat = args['lat']
            _lng = args['lng']
            _page = args['page']
            _size = args['size']
            query = userQueryBuilder(_lat, _lng, _page, _size)

            res = es_object.search(
                index="users", body=query)
            users = []
            count = res['hits']['total']['value']
            for hit in res['hits']['hits']:
                users.append(hit["_source"])
            return {'records': count, 'data': users}

            # # _email = args['email']
            # # subject = "Welcome to Roofpik "+_email+"!"
            # # return subject

        except Exception as e:
            return {'status': '400', 'Message': str(e)}
