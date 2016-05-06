from flask import Flask
from flask_bootstrap import Bootstrap
import config

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = config.secret_key
Bootstrap(app)

from app import views

