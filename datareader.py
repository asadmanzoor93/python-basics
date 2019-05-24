import glob as gb
import csv

from weatherman_data_structure import WeatherRecord

REQ_FIELDS = ['Max TemperatureC', 'Min TemperatureC', 'Max Humidity', ' Mean Humidity']


def prepare_weather_records(path):
    weather_reading = []

    for f in gb.glob(f'{path}/*.txt'):
        with open(f) as weather_file:
            reader = csv.DictReader(weather_file)
            weather_reading += [WeatherRecord(record) for record in reader if is_valid_record(record)]

    return weather_reading


def is_valid_record(record):
    return all([record[f] for f in REQ_FIELDS] + [record.get('PKST', record.get('PKT'))])
