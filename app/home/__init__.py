# app/home/__init__.py

from . import views
from flask import Blueprint

home = Blueprint('home', __name__)
