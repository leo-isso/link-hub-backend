from unittest import TestCase

from faker import Faker
from mongoengine import connect, disconnect


class WithMongoTestCase(TestCase):
    faker = Faker()

    @classmethod
    def setUpClass(cls):
        connect("mongoenginetest", host="mongomock://localhost")

    @classmethod
    def tearDownClass(cls):
        disconnect()
