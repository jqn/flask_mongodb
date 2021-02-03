import sentry_sdk
import os
from flask import Flask
from pymongo import MongoClient
from sentry_sdk.integrations.flask import FlaskIntegration

app = Flask(__name__)
app.config.from_object('config')

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

# connect to database
client = MongoClient(
    'mongodb+srv://{username}:{password}@cluster0.zy54o.mongodb.net'
    .format(username=os.getenv('DB_USERNAME'),  password=os.getenv('DB_PASSWORD')))

# connect to gameDB database
db = client.gameDB

from app import routes  # noqa
