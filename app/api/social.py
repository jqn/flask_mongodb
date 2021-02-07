# app/admin/social.py
from . import api
from flask import current_app, redirect, session
from authlib.integrations.requests_client import OAuth2Session
from authlib.oauth2.rfc7523 import ClientSecretJWT

VERSION = "1.0"


@api.route(f'{VERSION}/facebook', methods=['GET', 'POST'])
def facebook():
    # for local testing use http://localhost:5000/auth/facebook/
    # Facebook Oauth Config
    FACEBOOK_CLIENT_ID = current_app.config['FACEBOOK_APP_ID']
    FACEBOOK_CLIENT_SECRET = current_app.config['FACEBOOK_APP_SECRET']
    token_endpoint = 'https://graph.facebook.com/oauth/access_token'
    scope = "email"
    account_url = "https://graph.facebook.com/me?fields=id,name,email"

    session = OAuth2Session(
        FACEBOOK_CLIENT_ID, FACEBOOK_CLIENT_SECRET, scope=scope
    )
    session.fetch_access_token(token_endpoint)

    token = session.fetch_token(
        token_endpoint, grant_type='client_credentials')
    print(token)

    session = OAuth2Session(
        FACEBOOK_CLIENT_ID, FACEBOOK_CLIENT_SECRET, token=token)
    resp = session.get(account_url)
    print(resp.json())

    return "/"
    # github = OAuth2Session(FACEBOOK_CLIENT_ID)
    # authorization_url, state = github.authorization_url(
    # )

    # # State is used to prevent CSRF, keep this for later.
    # session['oauth_state'] = state
    # return redirect(authorization_url)
