from mongoengine import Document, StringField, FloatField, ListField

class History(Document):
    landslides = FloatField(default=0)
    latitudes = ListField(FloatField())
    longitudes = ListField(FloatField())
    date = StringField()
