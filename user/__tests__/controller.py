from user.controller import UserController

from base.test import WithMongoTestCase


class UserControllerTest(WithMongoTestCase):
    def test_create_user(self):
        data = dict(
            accounts=[
                dict(
                    alias=self.faker.name(),
                    username=self.faker.user_name(),
                )
            ],
            email=self.faker.email(),
            password=self.faker.password(),
        )

        user_controller = UserController()
        new_user = user_controller.create(data)

        self.assertEqual(new_user["email"], data["email"])
        self.assertEqual(new_user["password"], data["password"])
        self.assertEqual(
            new_user["accounts"][0]["alias"], data["accounts"][0]["alias"]
        )
        self.assertEqual(
            new_user["accounts"][0]["username"],
            data["accounts"][0]["username"],
        )
