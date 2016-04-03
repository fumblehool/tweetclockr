from app import app
from flask import render_template, redirect
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
	return redirect(auth_url)
