from flask import Blueprint
from flask import request, jsonify
from myapp.utils.utils import split_time

api = Blueprint('api', __name__)


@api.route('/shelves')
def get_list_shelves():
    return 'Pass'
