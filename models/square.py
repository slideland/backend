from mongoengine import Document, StringField, FloatField

class Square(Document):
#    square_id = StringField(required=True)
    long = FloatField()
    lat = FloatField()
    risk_score = FloatField()
    num_slides = FloatField()
