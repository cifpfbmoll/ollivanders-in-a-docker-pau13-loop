from mongoengine import *


# Create the model structure that must follow the items that are inside the db
class Stock(Document):
    _id = StringField(primary_key=True)
    name = StringField(required=True)
    sell_in = IntField()
    quality = IntField()
