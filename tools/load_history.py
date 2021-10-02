import sys
sys.path.append("..")
from mongoengine import NotUniqueError, ValidationError
from models.history import History
from tools.mongo_loader import mongo
import csv


@mongo
def csv_to_history(filepath: str = 'resources/history.csv', delimiter: str = ','):
    with open(filepath, 'r') as file:
        data = csv.DictReader(file, delimiter=delimiter)
        for data_point in data:
            long = []
            long.append(float(data_point["longitude"])-0.000277777778*15)
            long.append(float(data_point["longitude"])-0.000277777778*15)
            long.append(float(data_point["longitude"])+0.000277777778*15)
            long.append(float(data_point["longitude"])+0.000277777778*15)
            lat = []
            lat.append(float(data_point["latitude"])-0.000277777778*15)
            lat.append(float(data_point["latitude"])+0.000277777778*15)
            lat.append(float(data_point["latitude"])+0.000277777778*15)
            lat.append(float(data_point["latitude"])-0.000277777778*15)
            hist = History(
                    landslides=data_point["landslides"],
                    longitudes = long,
                    latitudes = lat,
                    date=data_point["date"]
                    ).save()
            print(f"Added history => {hist.id}")


def load_all(config: dict = None):
    from tools.mongo_loader import default_config
    if config:
        default_config.update(config)
    csv_to_history()

load_all()
