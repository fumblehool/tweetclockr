from app import app
from flask import render_template, redirect
import config
import tweepy


@app.route("/")
idef index():
    return "Hello Twitter User!"

