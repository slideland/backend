from mongoengine import NotUniqueError, ValidationError
from models.square import Square
from tools.mongo_loader import mongo
import csv
from random import randint


@mongo
def csv_to_square(filepath: str = 'resources/ggli2020public.csv', delimiter: str = ','):
    with open(filepath, 'r') as file:
        data = csv.DictReader(file, delimiter=delimiter)
        for data_point in data:
            sq = Square(**data_point, __auto_convert=True).save()
            print(f"Added: {sq.landslides} | {sq.longitude} | {sq.latitude} | {sq.date} => {sq.id}")


def load_all(config: dict = None):
    from tools.mongo_loader import default_config
    if config:
        default_config.update(config)
    csv_to_square()

load_all()
