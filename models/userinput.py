from mongoengine import Document, StringField, FloatField, ListField

class UserInput(Document):
    latitudes = ListField(FloatField())
    longitudes = ListField(FloatField())
    date = StringField()
