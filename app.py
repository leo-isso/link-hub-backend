import os
from user.api import UserApi

import pathlib
from dotenv import load_dotenv
from flask import Flask
from flask_restful import Api
from mongoengine import connect

# ENV
load_dotenv(pathlib.Path(".env"))

# Database
connect(
    alias=os.environ.get("MONGO_DB_ALIAS"),
    host=os.environ.get("MONGO_DB_HOST"),
    name=os.environ.get("MONGO_DB_NAME"),
    username=os.environ.get("MONGO_DB_USERNAME"),
    password=os.environ.get("MONGO_DB_PASSWORD"),
)

# Flask
app = Flask(__name__)
api = Api(app)

# flask_restful Routes
api.add_resource(UserApi, "/user")
