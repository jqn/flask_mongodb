# app/auth/routes.py

import os
from flask import current_app, url_for, \
    session, redirect
from . import auth
from .. import oauth
from ..models import User


@auth.route('/google/')
def google():
    # Google Oauth Config
    # Get client_id and client_secret from environment variables
    # For developement purpose you can directly put it here
    GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET')
    CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
    oauth.register(
        name='google',
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        server_metadata_url=CONF_URL,
        client_kwargs={
            'scope': 'openid email profile'
        }
    )
    # Redirect to google_auth funcion
    redirect_uri = url_for('google_auth', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)


@auth.route('/google/auth/')
def google_auth():
    token = oauth.google.authorize_access_token()
    user = oauth.google.parse_id_token(token)
    print(" Google User ", user)
    return redirect('/')


@auth.route('/facebook/')
def facebook():
    # for local testing use http://localhost:5000/auth/facebook/
    # Facebook Oauth Config
    FACEBOOK_CLIENT_ID = current_app.config['FACEBOOK_APP_ID']
    FACEBOOK_CLIENT_SECRET = current_app.config['FACEBOOK_APP_SECRET']
    oauth.register(
        name='facebook',
        client_id=FACEBOOK_CLIENT_ID,
        client_secret=FACEBOOK_CLIENT_SECRET,
        access_token_url='https://graph.facebook.com/oauth/access_token',
        access_token_params=None,
        authorize_url='https://www.facebook.com/dialog/oauth',
        authorize_params=None,
        api_base_url='https://graph.facebook.com/',
        client_kwargs={'scope': 'email'},
    )
    redirect_uri = url_for('auth.facebook_auth', _external=True)
    return oauth.facebook.authorize_redirect(redirect_uri)


@auth.route('/facebook/auth/')
def facebook_auth():
    token = oauth.facebook.authorize_access_token()
    resp = oauth.facebook.get(
        'https://graph.facebook.com/me?fields=id,name,email,picture{url}')
    profile = resp.json()
    print("Facebook User ", profile["picture"])

    # DON'T DO IT IN PRODUCTION, SAVE INTO DB IN PRODUCTION
    session['token'] = token
    session['user'] = profile
    user = User.objects(email=profile['email']).first()
    print("user", user)
    if not user:
        print("user not in database")
        user = User(name=profile['name'], email=profile['email'])
        user.save()
    else:
        print('user already in database')
        user.update(name=profile['name'])

    return redirect('/')
