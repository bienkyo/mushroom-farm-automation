from flask_pymongo import PyMongo

mongo = PyMongo()


def get_avg_temp_humidity_in_range(start, end):
    cursor = mongo.db.data.aggregate([{'$match': {
        "date": {
            "$gte": start,
            "$lte": end}}},
        {'$group': {
            "_id": None,
            'avg_temp': {'$avg': "$temp"}},
            'avg_humidity': {'$avg': '$humidity'}
        }])
    for result in cursor:
        return (result['avg_temp'],result['avg_humidity'])
    return (0,0)
