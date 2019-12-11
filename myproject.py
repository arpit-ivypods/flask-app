from flask import Flask
from flask_restful import Resource, Api

# from one import test
# from one import mongo
from search import *

app = Flask(__name__)
api = Api(app)

# api.add_resource(test.HelloWorld,'/')
# api.add_resource(mongo.mongotest, '/mongo')
api.add_resource(search.v1.users.listing, '/v1/users/search')

if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0')

