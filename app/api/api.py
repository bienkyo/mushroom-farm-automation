from flask import Blueprint
from flask import request, jsonify
from app.utils import split_time
import app.models as dbhelper

api = Blueprint('api', __name__)


@api.route('/env')
def get_avg_env():
    num_ranges = request.args.get('num_ranges') or 10
    intervals = split_time(num_ranges)
    response = []
    for i in range(1,num_ranges):
        avg_temp,avg_humidity = dbhelper.get_avg_temp_humidity_in_range(start=intervals[i], end=intervals[i - 1])
        item = {}
        item['start'] = intervals[i]
        item['end'] = intervals[i-1]
        item['avg_temp'] = avg_temp
        item['avg_humidity'] = avg_humidity
        response.append(item)
    return jsonify(response)



