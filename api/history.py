from flask_restful import Resource
from flask import Response, request, jsonify
from models.history import History


class HistoriesApi(Resource):
    def get(self) -> Response:
        output = History.objects()
        return jsonify({'result': output})
    def post(self) -> Response:
        data = request.get_json()
        post = History(**data).save()
        output = {'id': str(post.id)}
        return jsonify({'result': output})

class HistoryApi(Resource):
    def get(self, history_id: str) -> Response:
        output = History.objects.get(id=history_id)
        return jsonify({'result': output})
