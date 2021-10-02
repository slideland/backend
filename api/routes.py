# flask packages
from flask_restful import Api

# project resources
from api.square import SquaresApi, SquareApi


def create_routes(api: Api):
    api.add_resource(SquaresApi, '/square/')
    api.add_resource(SquareApi, '/square/<square_id>')
