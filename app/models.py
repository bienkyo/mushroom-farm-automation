from flask_influxdb import InfluxDB
from .utils import influx

influx_db = InfluxDB()


#
#
# def get_temp_humidity_in_range(start, end, shelf_id):
#     cursor = mongo.db.data.find({"date": {
#         "$gte": start,
#         "$lte": end},
#         "shelf_id": shelf_id})
#     data = {}
#
#
# def get_list_shelf_ids():
#     shelves = mongo.db.shelves.find({})
#     result = []
#     for shelf in shelves:
#         result.append(shelf['_id'])
#     return result
#
#

def insert_sensor_data(data):
    influx.insert_measure_influxdb(data['shelf_id'], {'temp': data['temp'],
                                                      'humidity': data['humidity']})
