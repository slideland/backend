from flask_restful import Resource
from flask import Response, request, jsonify
from models.apimodel import ApiModel

class ApiModelsApi(Resource):
    def get(self) -> Response:
        output = ApiModel.objects()
        return jsonify({'result': output})
    def post(self) -> Response:
        data = request.get_json()
        post = ApiModel(**data).save()
        output = {'id': str(post.id)}
        return jsonify({'result': output})

class ApiModelApi(Resource):
    def get(self, apimodel_id: str) -> Response:
        output = ApiModel.objects.get(id=apimodel_id)
        return jsonify({'result': output})
    def put(self, apimodel_id: str) -> Response:
        data = request.get_json()
        put = ApiModel.objects(id=apimodel_id).update(**data)
        return jsonify({'result': put})
