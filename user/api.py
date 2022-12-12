from user.controller import UserController

from flask import request
from flask_restful import Resource


class UserApi(Resource):
    def get(self):
        return {"hello": "world"}

    def post(self):
        json_data = request.json
        user_controller = UserController()
        return user_controller.create(json_data)
