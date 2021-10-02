from flask_restful import Resource
from flask import Response, request, jsonify
from models.userinput import UserInput
from models.apimodel import ApiModel
import requests
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from model_eval import Model_eval

class UserInputsApi(Resource):
    def get(self) -> Response:
        output = UserInput.objects()
        return jsonify({'result': output})
    def post(self) -> Response:
        user_data = request.get_json()
        #TODO: check input validity, len long = lat ect
        post = UserInput(**user_data).save()

        #build a polygon where the landslide took place
        slide_points = []
        for i,v in enumerate(user_data["latitudes"]):
            slide_points.append((v,user_data["longitudes"][i]))
        slide_polygon = Polygon(points)

        #loop over all apis of models we have
        for api in ApiModel.objects:
            r = requests.get(url = api.url)
            api_data = r.json()
            # loop over all areas in the api
            had_area = False
            for value in api_data["areas"]:
                #build a polygon of that area
                points = []
                for v in value["area"]:
                    points.append((v[0],v[1]))
                polygon = Polygon(points)
                #if the areas crosses we evaluate the model's prediction and update it's score
                if polygon.crosses(slide_polygon):
                    had_area = True
                    risk = value["risk"]
                    score = api_data["score"]
                    #TODO:
                    #    newscore = send to sebbi's func
                    api.update(score=newscore) 
            if not had_area:
                #TODO:
                #    newscore = send to sebbi's func
                api.update(score=newscore) 

        #TODO: add to history(?)
        output = {'id': str(post.id)}
        return jsonify({'result': output})

class UserInputApi(Resource):
    def get(self, userinput_id: str) -> Response:
        output = UserInput.objects.get(id=userinput_id)
        return jsonify({'result': output})
