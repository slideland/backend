from mongoengine import Document, StringField

class Prediction(Document):
    name = StringField()
    url = StringField()
    current_score = FloatField()
