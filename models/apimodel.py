from mongoengine import Document, StringField, ListField, FloatField, ReferenceField
from models.prediction import Prediction

class ApiModel(Document):
    name = StringField(required=True)
    url = StringField(required=True)
    score = FloatField(required=True, default=0)
    predictions = ListField(ReferenceField(Prediction))
