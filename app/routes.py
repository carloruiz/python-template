from flask_restful import Resource
from APP import api
from APP.resources.helloworld import HelloWorld

api.add_resource(HelloWorld, '/helloworld')

