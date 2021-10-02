from mongoengine import Document, FloatField, ListField

class Prediction(Document):
    risk_score = FloatField(default=0)
    longitudes = ListField(FloatField())
    latitudes = ListField(FloatField())
