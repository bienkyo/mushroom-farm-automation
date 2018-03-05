from flask import Blueprint
from flask import request, jsonify
from app.utils.utils import split_time
import app.models as dbhelper

api = Blueprint('api', __name__)


@api.route('/shelves')
def get_list_shelves():
    return 'Pass'
