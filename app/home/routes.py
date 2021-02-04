# app/home/routes.py
from flask import render_template, session

from . import home


@home.route('/')
@home.route('/index')
def homepage():
    """
    Render the homepage template on the / route
    """
    user = session.get('user')
    print(user)
    return render_template('home/index.html', title="Welcome")


@home.route('/debug-sentry')
def trigger_error():
    # Test sentry logs
    division_by_zero = 1 / 0


@home.route('/oauth/access_token')
def access_token():
    """
    Render the homepage template on the / route
    """
    user = session.get('user')
    print(user)
    return render_template('home/index.html', title="Welcome")
