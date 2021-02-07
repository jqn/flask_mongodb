import sentry_sdk
import os
from flask import Flask
from pymongo import MongoClient
from sentry_sdk.integrations.flask import FlaskIntegration
from authlib.integrations.flask_client import OAuth
from flask_mongoengine import MongoEngine

# local imports
from config import app_config

oauth = OAuth()

# connect to database
client = MongoClient(
    "mongodb+srv://{username}:{password}@cluster0.zy54o.mongodb.net"
    .format(username=os.getenv("DB_USERNAME"),  password=os.getenv("DB_PASSWORD")))

# connect to gameDB database
db = client.gameDB

db_engine = MongoEngine()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile("config.py")

    # add facebook secrets to oauth
    app.config['FACEBOOK_CLIENT_ID'] = app.config['FACEBOOK_APP_ID']
    app.config['FACEBOOK_CLIENT_SECRET'] = app.config['FACEBOOK_APP_SECRET']

    # mongodb connection
    app.config['MONGODB_SETTINGS'] = {
        'host': 'mongodb+srv://flaskmongo_user:React0r2008@triviacluster.jfsa8.mongodb.net/gamesTrivia?retryWrites=true&w=majority',
        'connect': True,
    }

    # add facebook secrets to oauth
    app.config['FACEBOOK_CLIENT_ID'] = app.config['FACEBOOK_APP_ID']
    app.config['FACEBOOK_CLIENT_SECRET'] = app.config['FACEBOOK_APP_SECRET']

    # Initialize sentry
    sentry_sdk.init(
        dsn=app.config["SENTRY_DSN"],
        integrations=[FlaskIntegration()],

        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=1.0,

        # By default the SDK will try to use the SENTRY_RELEASE
        # environment variable, or infer a git commit
        # SHA as release, however you may want to set
        # something more human-readable.
        # release="myapp@1.0.0",
    )

    # initialize oauth
    oauth.init_app(app)
    # initialize mongoengine
    db_engine.init_app(app)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix="/api")

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,  url_prefix="/auth")

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app
