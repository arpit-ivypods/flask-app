from flask_restful import Resource, Api
from flask_restful import reqparse
from elasticsearch import Elasticsearch
import env
import json


class userlisting(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument(
                'lat', type=float, help='pass the latitude', default=28.4498494)
            parser.add_argument(
                'lng', type=float, help='pass the longitude', default=77.0566885)
            parser.add_argument('page', type=int, help='page of listing', default=1)
            parser.add_argument('count', type=int, help='total number of listings', default=20)
            args = parser.parse_args()
            _lat = args['lat']
            _lng = args['lng']
            _page = args['page']
            _count = args['count']
            query = userQueryBuilder(_lat, _lng, _page, _count)
            # return query
            es_object = env.esConnect()
            res = es_object.search(
                index="users", body=query)
            users = []
            count = res['hits']['total']['value']
            # print(count)
            for hit in res['hits']['hits']:
                users.append(hit["_source"])
            return {'records':count, 'data':users}

            # # _email = args['email']
            # # subject = "Welcome to Roofpik "+_email+"!"
            # # return subject

        except Exception as e:
            return {'status': '400', 'Message': str(e)}


def userQueryBuilder(lat, lon, page, size):
    page = page - 1
    start = page * size
    query = {}
    query["from"] = start
    query["size"] = size
    query["query"] = {}
    query["query"]["bool"] = {"filter": {
        "geo_distance": {
            "distance": "30km",
            "coordinates": {
                "lat": lat,
                "lon": lon
            }
        }
    }}
    query["sort"] = [{
        "_geo_distance": {
            "coordinates": {
                "lat": lat,
                "lon": lon
            },
            "order": "asc",
            "unit": "m"
        }
    }]
    return query
