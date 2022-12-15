from user.controller import UserController

from base.test import WithMongoTestCase


class UserControllerTest(WithMongoTestCase):
    controller = UserController()

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

        new_user = self.controller.create(data)

        self.assertEqual(new_user["email"], data["email"])
        self.assertEqual(new_user["password"], data["password"])
        self.assertEqual(
            new_user["accounts"][0]["alias"], data["accounts"][0]["alias"]
        )
        self.assertEqual(
            new_user["accounts"][0]["username"],
            data["accounts"][0]["username"],
        )

    def test_get_all_users_with_password(self):
        data = self.generate_user()
        self.controller.create(data)

        users = self.controller.get(with_password=True)
        self.assertGreater(len(users), 0)
        self.assertIn("password", users[0])

    def test_get_all_users_without_password(self):
        users = self.controller.get()
        self.assertGreater(len(users), 0)
        self.assertNotIn("password", users[0])
