from unittest import TestCase

from mongoengine import connect, disconnect


class WithMongoTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        connect("mongoenginetest", host="mongomock://localhost")

    @classmethod
    def tearDownClass(cls):
        disconnect()
