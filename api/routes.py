from flask_restful import Api
from api.history import HistoriesApi, HistoryApi


def create_routes(api: Api):
    api.add_resource(HistoriesApi, '/history/')
    api.add_resource(HistoryApi, '/history/<history_id>')
