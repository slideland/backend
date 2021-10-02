from mongoengine import Document, StringField, FloatField, ListField

class History(Document):
    landslides = FloatField(default=0)
    longitudes = ListField(FloatField())
    latitudes = ListField(FloatField())
    date = StringField()
