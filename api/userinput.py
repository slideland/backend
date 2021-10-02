from flask_restful import Resource
from flask import Response, request, jsonify
from models.userinput import UserInput


class UserInputsApi(Resource):
    def get(self) -> Response:
        output = UserInput.objects()
        return jsonify({'result': output})
    def post(self) -> Response:
        data = request.get_json()
        #TODO: check input validity, len long = lat ect
        post = UserInput(**data).save()
        #TODO: evaluate models
        #TODO: add to history(?)
        output = {'id': str(post.id)}
        return jsonify({'result': output})

class UserInputApi(Resource):
    def get(self, userinput_id: str) -> Response:
        output = UserInput.objects.get(id=userinput_id)
        return jsonify({'result': output})
