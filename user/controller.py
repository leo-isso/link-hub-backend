import json
from user.document import User

from auth.utils import encrypt_password, generate_salt_key


class UserController:
    def create(self, data):
        user_data = data

        salt = generate_salt_key()
        user_data["salt"] = salt

        encrypted_password = encrypt_password(data["password"], salt)
        user_data["password"] = encrypted_password

        user = User(**user_data)
        user.save()

        return json.loads(user.to_json())

    def get(self, id=None):
        if not id:
            return User.objects().to_json()

        return User.objects().get(_id=id)
