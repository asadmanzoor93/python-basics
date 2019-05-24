from datetime import datetime


class WeatherRecord(object):
    def __init__(self, record):
        self.date = datetime.strptime(record.get('PKST', record.get('PKT')), '%Y-%m-%d')
        self.max_temp = int(record['Max TemperatureC'])
        self.low_temp = int(record['Min TemperatureC'])
        self.max_humid = int(record['Max Humidity'])
        self.mean_humid = int(record[' Mean Humidity'])
