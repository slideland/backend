import sys
sys.path.append("..")
from mongoengine import NotUniqueError, ValidationError
from models.prediction import Prediction
from models.apimodel import ApiModel
from tools.mongo_loader import mongo
import json

@mongo
def json_to_api(filepath: str = 'resources/nasa_static_predictions.geojson'):
    with open(filepath, 'r') as file:
        data = json.load(file)
        preds = []
        for value in data["features"]:
            risk = value["properties"]["nowcast"]
            lat = []
            long = []
            for v in value["geometry"]["coordinates"][0]:
                lat.append(v[0])   
                long.append(v[1])   
            pred = Prediction(
                    risk_score=risk,
                    latitudes = lat,
                    longitudes = long
                    ).save()
            preds.append(pred)
        api = ApiModel(
                name="Nasa PMM Publisher",
                url="http://127.0.0.1:5000/nasatranslate/",
                score = 0,
                Prediction=preds
                ).save()
        print(f"Added api => {api.id}")


def load_all(config: dict = None):
    from tools.mongo_loader import default_config
    if config:
        default_config.update(config)
    json_to_api()

load_all()
