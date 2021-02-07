# app/home/routes.py

from flask import render_template, session, jsonify

from . import home


@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    user = session.get('user', {})
    return render_template('home/index.html', title="Welcome", user=user)
