from mongoengine import Document, StringField, FloatField, ListField

class History(Document):
    landslides = FloatField()
    longitudes = ListField(FloatField())
    latitudes = ListField(FloatField())
    date = StringField()
