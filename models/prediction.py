from mongoengine import Document, FloatField, ListField

class Prediction(Document):
    risk_score = FloatField(default=0)
    latitudes = ListField(FloatField())
    longitudes = ListField(FloatField())
