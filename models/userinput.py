from mongoengine import Document, StringField, FloatField, ListField, ImageField

class UserInput(Document):
    longitudes = ListField(FloatField())
    latitudes = ListField(FloatField())
    date = StringField()
    image = ImageField()
