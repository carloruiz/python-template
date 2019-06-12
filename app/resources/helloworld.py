from flask_restful import Resource
from flask import request

class HelloWorld(Resource):
    def get(self):
        print(request.json())
        return "Hello World!"
