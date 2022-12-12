from user.controller import UserController

from base.test import WithMongoTestCase


class UserControllerTest(WithMongoTestCase):
    def generate_user(self):
        return dict(
            accounts=[
                dict(
                    alias=self.faker.name(),
                    username=self.faker.user_name(),
                )
            ],
            email=self.faker.email(),
            password=self.faker.password(),
        )

    def test_create_user(self):
        data = self.generate_user()

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

    def test_get_all_users(self):
        user_controller = UserController()

        new_user = self.generate_user()
        user_controller.create(new_user)

        users = user_controller.get()
        self.assertGreater(len(users), 0)
