from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

# connect to database
client = MongoClient(
    'mongodb+srv://danielhaukaas:mongo1234509D@cluster0.zy54o.mongodb.net')

# connect to gameDB database
db = client.gameDB

from app import routes  # noqa
