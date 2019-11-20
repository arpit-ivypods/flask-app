from flask_restful import Resource, Api
from flask_restful import reqparse


class HelloWorld(Resource):
    def post(self):
        try:
            # return "arpit"
            parser = reqparse.RequestParser()
            parser.add_argument('email', type=str, help='to email address')
            args = parser.parse_args()
            _email = args['email']
            subject = "Welcome to Roofpik "+_email+"!"
            return subject

        except Exception as e:
            return {'status':'400','Message':str(e)}

		# return "arpit"

