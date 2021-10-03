from flask_restful import Resource
from flask import Response, request, jsonify
from models.userinput import UserInput
from models.apimodel import ApiModel
import requests
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import shapely.ops as ops
import pyproj
from api.model_eval import Model_eval

class UserInputsApi(Resource):
    def get(self) -> Response:
        output = UserInput.objects()
        return jsonify({'result': output})
    def post(self) -> Response:
        user_data = request.get_json()
        post = UserInput(**user_data).save()
        output = {'id': str(post.id)}

        geom_area = ops.transform(
            partial(
                pyproj.transform,
                pyproj.Proj(init='EPSG:4326'),
                pyproj.Proj(
                    proj='aea',
                    lat_1=polygon.bounds[1],
                    lat_2=polygon.bounds[3]
                )
            ),
            polygon)

        #build a polygon where the landslide took place
        slide_points = []
        for i,v in enumerate(user_data["latitudes"]):
            slide_points.append((v,user_data["longitudes"][i]))
        slide_polygon = Polygon(points)

        #loop over all apis of models we have
        for api in ApiModel.objects:
            # loop over all areas in the api, 
            risk_at_slide = 0
            high_area = 0;
            moderate_area = 0;
            for value in api_data.predictions:
                #build a polygon of that area
                points = []
                for i,v in enumerate(api["latitudes"]):
                    points.append((v,api["longitudes"][i]))
                polygon = Polygon(points)
                
                risk = value["risk"]
                
                if risk is 2:
                    high_area += geom_area(polygon)
                elif risk is 1:
                    moderate_area += geom_area(polygon)

                #if the areas crosses we get it's prediction
                if polygon.crosses(slide_polygon):
                    risk_at_slide = risk
            # % of total land area on earth
            low_area = (510100000 - high_area - moderate_area)/510100000
            moderate_area = moderate_area/510100000
            high_area = high/510100000
            low_area = (510100000 - high_area - moderate_area)/510100000
            score = value["score"]
            api.add_slide(risk_at_slide, high_area, moderate_area, low_area, 1) 
            #api.update(score=newscore) 
        return jsonify({'result': output})

class UserInputApi(Resource):
    def get(self, userinput_id: str) -> Response:
        output = UserInput.objects.get(id=userinput_id)
        return jsonify({'result': output})
