from mongoengine import Document, StringField, FloatField, ListField, ImageField

class UserInput(Document):
    latitudes = ListField(FloatField())
    longitudes = ListField(FloatField())
    date = StringField()
    image = ImageField()
