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

    def get(self, with_password=False):
        if not with_password:
            return json.loads(
                User.objects().fields(password=0, salt=0).to_json()
            )

        return json.loads(User.objects().to_json())

    def get_one(self, id, with_password=False):
        if not with_password:
            return json.loads(
                User.objects().fields(password=0, salt=0).get(id=id).to_json()
            )

        return json.loads(User.objects().get(id=id).to_json())
