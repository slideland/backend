from flask_restful import Resource
from flask import Response, request, jsonify
from models.userinput import UserInput
from models.apimodel import ApiModel
import requests
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from api.model_eval import Model_eval

class UserInputsApi(Resource):
    def get(self) -> Response:
        output = UserInput.objects()
        return jsonify({'result': output})
    def post(self) -> Response:
        user_data = request.get_json()
        post = UserInput(**user_data).save()
        output = {'id': str(post.id)}

        #build a polygon where the landslide took place
        slide_points = []
        for i,v in enumerate(user_data["latitudes"]):
            slide_points.append((v,user_data["longitudes"][i]))
        slide_polygon = Polygon(points)

        #loop over all apis of models we have
        for api in ApiModel.objects:
            # loop over all areas in the api
            had_area = False
            for value in api_data.predictions:
                #build a polygon of that area
                points = []
                for i,v in enumerate(api["latitudes"]):
                    points.append((v,api["longitudes"][i]))
                polygon = Polygon(points)
                #if the areas crosses we evaluate the model's prediction and update it's score
                if polygon.crosses(slide_polygon):
                    had_area = True
                    risk = value["risk"]
                    score = value["score"]
                    #TODO:
                    #    newscore = send to sebbi's func
                    #api.update(score=newscore) 
            if not had_area:
                #TODO:
                #    newscore = send to sebbi's func
                #api.update(score=newscore) 
                pass
        return jsonify({'result': output})

class UserInputApi(Resource):
    def get(self, userinput_id: str) -> Response:
        output = UserInput.objects.get(id=userinput_id)
        return jsonify({'result': output})
