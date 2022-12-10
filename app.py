from user.api import UserApi

from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

api.add_resource(UserApi, "/user")
