from flask import Blueprint
from flask import request, jsonify
from app.utils import split_time
import app.models as dbhelper

api = Blueprint('api', __name__)


@api.route('/env')
def get_avg_env():
    num_ranges = request.args.get('num_ranges') or 10
    shelf_id = request.args.get('shelf_id')
    intervals = split_time(num_ranges)

    if shelf_id == None:
        shelf_ids = dbhelper.get_list_shelf_ids()
    else:
        shelf_ids = [shelf_id]
    response = []
    for shelf in shelf_ids:
        shelf_data = []
        for i in range(1, num_ranges):
            avg_temp, avg_humidity = dbhelper.get_avg_temp_humidity_in_range(intervals[i], intervals[i - 1], shelf)
            item = {}
            item['start'] = intervals[i]
            item['end'] = intervals[i - 1]
            item['avg_temp'] = avg_temp
            item['avg_humidity'] = avg_humidity
            shelf_data.append(item)
        response.append({'shelf_id': shelf,
                         'data': shelf_data})
    return jsonify(response)


@api.route('/shelves')
def get_list_shelves():
    return jsonify(dbhelper.get_list_shelf_ids())
