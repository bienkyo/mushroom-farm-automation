from flask import Flask, redirect, url_for
from .views.dashboard import dash
from .api.api import api
from flask_mqtt import Mqtt
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.default')
app.config.from_pyfile('config.py')
app.config.from_envvar('APP_CONFIG_FILE')
app.register_blueprint(dash, url_prefix='/dashboard')
app.register_blueprint(api, url_prefix='/api')

mqtt = Mqtt(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# @mqtt.on_connect()
# def subscribe_topic(client, userdata, flags, rc):
#     mqtt.subscribe('/data')
#

@app.route('/')
def index():
    return redirect(url_for('/dashboard'))
