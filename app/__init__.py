import sentry_sdk
import os
from flask import Flask
from pymongo import MongoClient
from sentry_sdk.integrations.flask import FlaskIntegration
from authlib.integrations.flask_client import OAuth

# local imports
from config import app_config

oauth = OAuth()

facebook = oauth.register("facebook",
                          base_url="https://graph.facebook.com/",
                          request_token_url=None,
                          access_token_url="https://graph.facebook.com/oauth/access_token",
                          authorize_url="https://www.facebook.com/dialog/oauth",
                          request_token_params={
                              "scope": "email, public_profile"},
                          app_key='FACEBOOK'
                          )

# connect to database
client = MongoClient(
    "mongodb+srv://{username}:{password}@cluster0.zy54o.mongodb.net"
    .format(username=os.getenv("DB_USERNAME"),  password=os.getenv("DB_PASSWORD")))

# connect to gameDB database
db = client.gameDB


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile("config.py")

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

    # add facebook secrets to oauth
    app.config['FACEBOOK_CLIENT_ID'] = app.config['FACEBOOK_APP_ID']
    app.config['FACEBOOK_CLIENT_SECRET'] = app.config['FACEBOOK_APP_SECRET']

    # initialize oauth
    oauth.init_app(app)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix="/api")

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,  url_prefix="/auth")

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app
