from flask_restful import Resource
from flask import Response, request, jsonify
from models.apimodel import ApiModel
from models.prediction import Prediction
import requests

class ApiModelsApi(Resource):
    def get(self) -> Response:
        output = ApiModel.objects()
        return jsonify({'result': output})
    def post(self) -> Response:
        #add new api with no prediction
        data = request.get_json()
        post = ApiModel(**data).save()
        output = {'id': str(post.id)}
        return jsonify({'result': output})

class ApiModelApi(Resource):
    def get(self, apimodel_id: str) -> Response:
        output = ApiModel.objects.get(id=apimodel_id)
        return jsonify({'result': output})
    def put(self, apimodel_id: str) -> Response:
        api_obj = ApiModel.objects.get(id=apimodel_id)
        URL = api_obj.url
        r = requests.get(url = URL)
        api_data = r.json()
        preds = []
        # loop over all areas in the api
        for value in api_data["areas"]:
            risk = value["risk"]
            lats = []
            longs = []
            for v in value["area"]:
                lats.append(v[0])
                longs.append(v[1])
            pred = Prediction(risk_score=risk,latitudes=lats,longitudes=longs).save()
            preds.append(pred)
        api_obj.update(predictions=preds)
        return jsonify({'result': api_obj})

class ApiModelScoreApi(Resource):
    def get(self, apimodel_id: str) -> Response:
        output = ApiModel.objects.get(id=apimodel_id).get_score()
        return jsonify({'result': output})
