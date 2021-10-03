import sys
sys.path.append("..")
from flask_restful import Resource
from flask import Response, request, jsonify
import json
import requests
from datetime import datetime

class DummyApi(Resource):
    def get(self) -> Response:
        with open("resources/nasa_static_predictions.geojson", "r") as file:
            data = json.load(file)
            areas = []
            for value in data["features"]:
                risk = value["properties"]["nowcast"]
                points = []
                for v in value["geometry"]["coordinates"][0]:
                    points.append([v[0],v[1]])
                areas.append({"risk": risk, "area":points})
            output = {"areas": areas}
            return jsonify(output)

