from user.controller import UserController

from flask import request
from flask_restful import Resource


class UserApi(Resource):
    user_controller = UserController()

    def get(self, id=None):
        if not id:
            return self.user_controller.get()

        return self.user_controller.get_one(id)

    def post(self):
        json_data = request.json
        return self.user_controller.create(json_data)
