from mongoengine import Document, StringField, FloatField, ListField

class UserInput(Document):
    longitudes = ListField(FloatField())
    latitudes = ListField(FloatField())
    date = StringField()
    #TODO more fields? input options for area?
