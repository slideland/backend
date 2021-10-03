from flask_restful import Api
#from api.predictions import PredictionsApi, PredictionApi
from api.history import HistoriesApi, HistoryApi
from api.userinput import UserInputsApi, UserInputApi
from api.apimodel import ApiModelApi, ApiModelsApi
from api.nasatranslate import NasaTranslateApi
from api.dummyapi import DummyApi

def create_routes(api: Api):
    api.add_resource(HistoriesApi, '/history/')
    api.add_resource(HistoryApi, '/history/<history_id>')
    
    #api.add_resource(PredictionsApi, '/prediction/')
    #api.add_resource(PredictionApi, '/prediction/<prediction_id>')

    api.add_resource(UserInputsApi, '/userinput/')
    api.add_resource(UserInputApi, '/userinput/<userinput_id>')

    api.add_resource(ApiModelsApi, '/apimodel/')
    api.add_resource(ApiModelApi, '/apimodel/<apimodel_id>')

    api.add_resource(NasaTranslateApi, '/nasatranslate/')
    api.add_resource(DummyApi, '/dummyapi/')
