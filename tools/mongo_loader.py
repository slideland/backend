import mongoengine
from app import default_config
from types import FunctionType

def mongo(function: FunctionType) -> FunctionType:
    def load():
        mongoengine.connect(**default_config['MONGODB_SETTINGS'])
        function()
    return load
