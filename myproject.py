from flask import Flask
from flask_restful import Resource, Api

# from one import test
# from one import mongo
from search import *
from esindex import *

app = Flask(__name__)
api = Api(app)

# api.add_resource(test.HelloWorld,'/')
# api.add_resource(mongo.mongotest, '/mongo')
api.add_resource(search.v1.users.listing, '/v1/users/search')
api.add_resource(esindex.users.createUserIndex, '/v1/es/users')
api.add_resource(esindex.rooms.createRoomsIndex, '/v1/es/rooms')

if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0')

