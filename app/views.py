from app import app
from flask import render_template, redirect, session, request
import config
import tweepy


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/connect/")
def connect():
    auth = tweepy.OAuthHandler(config.API_Key,
                               config.API_Secret)

    auth_url = auth.get_authorization_url()
    session['request_token'] = auth.request_token
    # import IPython; IPython.embed()
    return redirect(auth_url)


@app.route("/callback/")
def callback():
    verifier = request.args.get('oauth_verifier')
    auth = tweepy.OAuthHandler(config.API_Key,
                               config.API_Secret,
                               config.Callback_url)
    token = session.get('request_token')
    auth.request_token = token

    try:
        auth.get_access_token(verifier)
    except tweepy.TweepError:
        print 'Error! Failed to get access token.'

    api = tweepy.API(auth)
    return "Welcome " + str(api.me().name)
