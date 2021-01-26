from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__)

# connect to database
client = MongoClient(
    'mongodb+srv://{username}:{password}@cluster0.zy54o.mongodb.net'.format(username=os.getenv('DB_USERNAME'),  password=os.getenv('DB_PASSWORD')))

# connect to gameDB database
db = client.gameDB

from app import routes  # noqa
