from mongoengine import Document, FloatField, ListField

class Prediction(Document):
    risk_score = FloatField()
    longitudes = ListField(FloatField())
    latitudes = ListField(FloatField())
