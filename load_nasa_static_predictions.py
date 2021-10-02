from mongoengine import NotUniqueError, ValidationError
from models.prediction import Prediction
from tools.mongo_loader import mongo
import json

@mongo
def json_to_prediction(filepath: str = 'resources/nasa_static_predictions.geojson'):
    with open(filepath, 'r') as file:
        data = json.load(file)
        
        for value in data["features"]:
            risk = value["properties"]["nowcast"]
            long = []
            lat = []
            for v in value["geometry"]["coordinates"][0]:
                long.append(v[1])   
                lat.append(v[0])   
            pred = Prediction(
                    risk_score=risk,
                    longitudes = long,
                    latitudes = lat
                    ).save()
            print(f"Added prediction => {pred.id}")


def load_all(config: dict = None):
    from tools.mongo_loader import default_config
    if config:
        default_config.update(config)
    json_to_prediction()

load_all()
