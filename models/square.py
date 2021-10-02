from mongoengine import Document, StringField, FloatField

class Square(Document):
    landslides = FloatField()
    longitude = FloatField()
    latitude = FloatField()
    date = StringField()
