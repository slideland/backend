from flask_restful import Api
from api.predictions import PredictionsApi, PredictionApi

def create_routes(api: Api):
    api.add_resource(HistoriesApi, '/history/')
    api.add_resource(HistoryApi, '/history/<history_id>')
    
    api.add_resource(PredictionsApi, '/prediction/')
    api.add_resource(PredictionApi, '/prediction/<prediction_id>')
