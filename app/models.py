from flask_pymongo import PyMongo
from datetime import datetime

mongo = PyMongo()


def get_avg_temp_humidity_in_range(start, end, shelf_id):
    query = [{"date": {
        "$gte": start,
        "$lte": end},
        "shelf_id": shelf_id}]
    cursor = mongo.db.data.aggregate([{'$match':
                                            {"date": {"$gte": start, "$lte": end},
                                            "shelf_id": shelf_id}
                                       },
                                      {'$group': {
                                          "_id": None,
                                          'avg_temp': {'$avg': "$temp"},
                                          'avg_humidity': {'$avg': '$humidity'}
                                      }}])
    for result in cursor:
        return (result['avg_temp'], result['avg_humidity'])
    return (0, 0)


def get_list_shelf_ids():
    shelves = mongo.db.shelves.find({})
    result = []
    for shelf in shelves:
        result.append(shelf['_id'])
    return result


def insert_sensor_data(data):
    mongo.db.data.insert_one({
        'shelf_id': data['shelf_id'],
        'temp': data['temp'],
        'humidity': data['humidity'],
        'date': datetime.fromtimestamp(data['date'])
    })
