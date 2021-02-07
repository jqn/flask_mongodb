# app/models.py
from app import db_engine
import json


class User(db_engine.Document):
    name = db_engine.StringField()
    email = db_engine.StringField()

    def to_json(self):
        return {"name": self.name,
                "email": self.email}
