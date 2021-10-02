# flask packages
from flask_restful import Resource
from flask import Response, request, jsonify


# mongo-engine models
from models.square import Square


class SquaresApi(Resource):
    def get(self) -> Response:
        output = Square.objects()
        return jsonify({'result': output})
    def post(self) -> Response:
        data = request.get_json()
        post = Square(**data).save()
        output = {'id': str(post.id)}
        return jsonify({'result': output})

class SquareApi(Resource):
    def get(self, square_id: str) -> Response:
        output = Square.objects.get(id=square_id)
        return jsonify({'result': output})
    def put(self, square_id: str) -> Response:
        data = request.get_json()
        put = Square.objects(id=square_id).update(**data)
        return jsonify({'result': put})
