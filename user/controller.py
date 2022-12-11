import json
from user.document import Accounts, User


class UserController:
    def create(self, alias, username, password, email):
        account = Accounts(alias=alias, username=username)

        user = User(
            password=password,  # TODO: encrypt password
            email=email,
            accounts=[account],
        )
        user.save()

        return json.loads(user.to_json())
