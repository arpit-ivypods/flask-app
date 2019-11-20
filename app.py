from flask import Flask
from flask_restful import Resource, Api

from one import test

app = Flask(__name__)
api = Api(app)

api.add_resource(test.HelloWorld,'/')

if __name__ == "__main__":
	app.debug = True
	app.run()