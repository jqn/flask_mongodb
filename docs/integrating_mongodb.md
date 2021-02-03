# flask_mongodb

Create an account on MongoDB Atlas

Create a cluster

Create a MongoDB User

Whitelist your IP

Choose connect your application method

Choose Python driver

Get connection string

Create a flask app

```
flask_mongoddb/
  flask_mongodb_venv/
  app/
    __init__.py
    routes.py
  flaskmongo.py
```

Create virtual environment. Python 3 has built in virtual environment support.

```
$ python3 -m venv flaskmongo_venv
```

Activate your virtual environment

```
$ source flaskmongo_venv/bin/activate
```

Set environment variables. Edit the activate file

```
flaskmongo_venv/bin/activate
```

Or create a config.py file at the root of your project.

```
# Environment
export FLASK_APP=run.py
export FlASK_ENV=development
export FLASK_DEBUG=True

# MongoDB
export DB_USERNAME = ""
export DB_PASSWORD = ""
export DB_ClUSTER = ""

# Sentry
export SENTRY_DSN = ""
```

Install requirements

```
$ pip install Flask
$ pip install pymongo
$ pip install dnspython
```

Set the following environment variables

```
export FLASK_APP=flaskmongo.py
export FLASK_DEBUG=True

```

Add the connection string to your app

```
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

db = MongoClient('mongodb+srv://jqn:React0r2008@flaskmongocluster.w5g8r.mongodb.net/sample_airbnb?retryWrites=true&w=majority')


from app import routes

```
