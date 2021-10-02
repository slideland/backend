from flask_restful import Resource
from flask import Response, request, jsonify
from models.prediction import Prediction

class PredictionsApi(Resource):
    def get(self) -> Response:
        output = Prediction.objects()
        return jsonify({'result': output})
    def post(self) -> Response:
        data = request.get_json()
        post = Prediction(**data).save()
        output = {'id': str(post.id)}
        return jsonify({'result': output})

class PredictionApi(Resource):
    def get(self, prediction_id: str) -> Response:
        output = Prediction.objects.get(id=prediction_id)
        return jsonify({'result': output})
    def put(self, prediction_id: str) -> Response:
        data = request.get_json()
        put = Prediction.objects(id=prediction_id).update(**data)
        return jsonify({'result': put})
