from user.controller import UserController

from base.test import WithMongoTestCase


class UserControllerTest(WithMongoTestCase):
    def test_create_user(self):
        alias = self.faker.name()
        username = self.faker.user_name()
        email = self.faker.email()
        password = self.faker.password()

        user_controller = UserController()
        new_user = user_controller.create(
            alias=alias,
            username=username,
            password=password,
            email=email,
        )

        self.assertEqual(new_user["email"], email)
        self.assertEqual(new_user["password"], password)
        self.assertEqual(new_user["accounts"][0]["alias"], alias)
        self.assertEqual(new_user["accounts"][0]["username"], username)
