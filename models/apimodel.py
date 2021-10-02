from mongoengine import Document, StringField

class ApiModel(Document):
    name = StringField(required=True)
    url = StringField(required=True)
    score = FloatField(required=True, default=0)
