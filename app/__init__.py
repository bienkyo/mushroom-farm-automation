from flask import Flask, redirect, url_for
from .views.dashboard import dash
from .api.api import api
from .models import influx_db
from flask_mqtt import Mqtt
import json

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.default')
app.config.from_pyfile('config.py')
app.config.from_envvar('APP_CONFIG_FILE')
app.register_blueprint(dash, url_prefix='/dashboard')
app.register_blueprint(api, url_prefix='/api')

influx_db.init_app(app)
mqtt = Mqtt(app)


@mqtt.on_connect()
def subscribe_topic(client, userdata, flags, rc):
    mqtt.subscribe('/data')


@mqtt.on_topic('/data')
def handle_data_sensor(client, userdata, message):
    try:
        data = json.loads(message.payload.decode())
        print('Handle sensor data: ' , json.dumps(data))
        with app.app_context():
            models.insert_sensor_data(data)
    except json.JSONDecodeError:
        print('Error when parsing json: ' % message.payload.decode())


@app.route('/')
def index():
    return redirect(url_for('/dashboard'))
