from flask import Flask, redirect,url_for
from .views.dashboard import dash
app = Flask(__name__,instance_relative_config=True)
app.config.from_object('config.default')
app.config.from_pyfile('config.py')
app.config.from_envvar('APP_CONFIG_FILE')
app.register_blueprint(dash,url_prefix='/dashboard')

@app.route('/')
def index():
    return redirect(url_for('/dashboard'))