from flask import Flask, redirect,url_for
from .views.dashboard import dash
from .api.api import api
from .models import mongo

app = Flask(__name__,instance_relative_config=True)
app.config.from_object('config.default')
app.config.from_pyfile('config.py')
app.config.from_envvar('APP_CONFIG_FILE')
app.register_blueprint(dash,url_prefix='/dashboard')
app.register_blueprint(api,url_prefix='/api')

#set up database
mongo.init_app(app)


@app.route('/')
def index():
    return redirect(url_for('/dashboard'))