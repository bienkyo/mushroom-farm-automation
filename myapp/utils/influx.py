from influxdb import InfluxDBClient

from instance.config import INFLUXDB_DATABASE
from instance.config import INFLUXDB_HOST
from instance.config import INFLUXDB_PORT
from instance.config import INFLUXDB_USER
from instance.config import INFLUXDB_PASSWORD
import threading


def insert_measure_influxdb(unique_id, measurements):
    """
    Add a measurement entries to InfluxDB

    :param unique_id:
    :param measurements:
    :return: None
    """
    data = []
    for each_measurement, each_value in measurements.items():
        data.append(format_influxdb_data(unique_id,
                                         each_measurement,
                                         each_value))
    write_db = threading.Thread(
        target=write_influxdb_list,
        args=(data,))
    write_db.start()


def query_string(measurement, unique_id, value=None,
                 start_str=None, end_str=None,
                 past_sec=None, group_sec=None, limit=None):
    """Generate influxdb query string"""
    query = "SELECT "

    if value:
        if value in ['COUNT', 'LAST', 'MEAN', 'SUM']:
            query += "{value}(value)".format(value=value)
        else:
            return 1
    else:
        query += "value"

    query += " FROM {meas} WHERE device_id='{id}'".format(
        meas=measurement, id=unique_id)
    if start_str:
        query += " AND time >= '{start}'".format(start=start_str)
    if end_str:
        query += " AND time <= '{end}'".format(end=end_str)
    if past_sec:
        query += " AND time > now() - {sec}s".format(sec=past_sec)
    if group_sec:
        query += " GROUP BY TIME({sec}s)".format(sec=group_sec)
    if limit:
        query += " GROUP BY * LIMIT {lim}".format(lim=limit)
    return query


def format_influxdb_data(shelf_id, measure_type, value, timestamp=None):
    """
    Format data for entry into an Influxdb database

    example:
        format_influxdb_data('01', 'temperature', 37.5)
        format_influxdb_data('02', 'duration', 15.2)

    :return: list of measurement type, tags, and value
    :rtype: list

    :param shelf_id: 2-character alpha-numeric ID associated with mushroom shelf
    :type shelf_id: str
    :param measure_type: The type of data being entered into the Influxdb
        database (ex. 'temperature', 'duration')
    :type measure_type: str
    :param value: The value being entered into the Influxdb database
    :type value: int or float
    :param timestamp: If supplied, this timestamp will be used in the influxdb
    :type timestamp: datetime object

    """
    if timestamp:
        return {
            "measurement": measure_type,
            "tags": {
                "shelf_id": shelf_id
            },
            "time": timestamp.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
            "fields": {
                "value": value
            }
        }
    else:
        return {
            "measurement": measure_type,
            "tags": {
                "shelf_id": shelf_id
            },
            "fields": {
                "value": value
            }
        }


def write_influxdb_list(data):
    """
    Write an entry into an Influxdb database

    example:
        write_influxdb('localINFLUXDB_HOST', 8086, 'mycodo', 'INFLUXDB_PASSWORD123',
                       'mycodo_db', data_list_of_dictionaries)

    :return: success (0) or failure (1)
    :rtype: bool

    :param data: The data being entered into Influxdb
    :type data: list of dictionaries
    """
    client = InfluxDBClient(INFLUXDB_HOST, INFLUXDB_PORT, INFLUXDB_USER,
                            INFLUXDB_PASSWORD, INFLUXDB_DATABASE)
    try:
        print('Saving data')
        client.write_points(data)
        client.close()
        return 0
    except Exception as except_msg:
        print(
            "Failed to write measurements to influxdb. Data that was "
            "submitted for writing: {data}. Exception: {err}".format(
                data=data, err=except_msg))
        return 1
