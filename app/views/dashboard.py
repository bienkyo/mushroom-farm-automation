from flask import Blueprint, render_template
import json
import app.models as dbhelper

dash = Blueprint('dashboard', __name__)


@dash.route('/')
def dashboard():
    return 'Hello world'
