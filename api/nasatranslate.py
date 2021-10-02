from flask_restful import Resource
from flask import Response, request, jsonify
from models.nasatranslate import NasaTranslate
import json

class NasaTranslateApi(Resource):
    def get(self) -> Response:
        #this url gives the url with the areas
        #we take the most recent prediction from the last 20 years
        URL = "https://pmmpublisher.pps.eosdis.nasa.gov/opensearch?q=global_landslide_nowcast_3hr&lat=0&lon=0&limit=1&startTime=2000-10-2&endTime=2021-10-2"
        r = requests.get(url = URL)
        data = r.json()
        #TODO: dangerous? change from time to time?
        URL = data["items"][0]["action"][0]["using"][5]["using"][0]["url"]
        r = requests.get(url = URL)
        data = r.json()
        areas = []
        for value in data["features"]:
            risk = value["properties"]["nowcast"]
            points = []
            for v in value["geometry"]["coordinates"][0]:
                points.append([v[0],v[1]])
            areas.apped({"risk": risk, "area":points})
        output = {"areas": areas}
        return jsonify({'result': output})

