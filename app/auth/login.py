# app/auth/login.py
from . import auth
# from .. import facebook
from flask import url_for, jsonify, redirect, session, render_template
from sentry_sdk import capture_exception
from authlib.integrations.flask_client import OAuth, OAuthError


# @auth.route('/login', methods=["GET", "POST"])
# def login():
#     redirect_uri = url_for('auth.authorize', _external=True)
#     return facebook.authorize_redirect(redirect_uri)


# @auth.route('/authorize', methods=["GET", "POST"])
# def authorize():
#     try:
#         token = facebook.authorize_access_token()
#         print("token", token["access_token"])
#         # url = 'user'
#         access_token = token["access_token"]
#         resp = facebook.get(
#             f'https://graph.facebook.com/me')
#         print("resp", resp.content)
#         # user = resp.json()
#         # DON'T DO IT IN PRODUCTION, SAVE INTO DB IN PRODUCTION
#         # session['token'] = token
#         # session['user'] = user
#         return redirect('/')
#     except Exception as e:
#         print(e)
#         capture_exception(e)
#         return redirect('/index')


# @ auth.route('/logout')
# def logout():
#     session.pop('user', None)
#     return "logged out"


# @ auth.errorhandler(OAuthError)
# def handle_error(error):
#     return render_template('error.html', error=error)


# @ auth.route('/oauth/access_token')
# def access_token():
#     """
#     Render the homepage template on the / route
#     """
#     user = session.get('user')
#     print(user)
#     return render_template('home/index.html', title="Welcome")
