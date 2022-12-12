import json
from user.document import User


class UserController:
    def create(self, data):
        user = User(**data)
        user.save()

        return json.loads(user.to_json())

    def get(self, id=None):
        if not id:
            return User.objects().to_json()
