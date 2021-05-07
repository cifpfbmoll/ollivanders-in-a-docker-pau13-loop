# FLASk
from flask import g

# MONGO
from mongoengine import *

# Model
from repository.repository_mongo.db_model import Stock


db_name = "ollivanders_testing"
URI = (
    "mongodb+srv://adminUser:adminPassword@sandbox.jh5ph.mongodb.net"
    "/ollivanders?retryWrites=true&w=majority"
)

# To establish a connection with the db


def get_db():
    if "db" not in g:
        g.db = connect(db=db_name, host=URI, alias="default")
        g.Stock = Stock
    return g.db


# To close the connection with the db
def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()


# To fill the db with items
def init_db():
    db = get_db()

    # Before comeback to fill the db we should make sure that this one is
    # empty to avoid duplicate items in our db with same id fields
    Stock.drop_collection()

    default_stock = [
        {
            "_id": "111111",
            "name": "Aged Brie",
            "sell_in": 2,
            "quality": 0,
        },
        {
            "_id": "111112",
            "name": "+5 Dexterity Vest",
            "sell_in": 10,
            "quality": 20,
        },
        {
            "_id": "111113",
            "name": "Elixir of the Mongoose",
            "sell_in": 5,
            "quality": 7,
        },
        {
            "_id": "111114",
            "name": "Sulfuras, Hand of Ragnaros",
            "sell_in": 0,
            "quality": 80,
        },
        {
            "_id": "111115",
            "name": "Sulfuras, Hand of Ragnaros",
            "sell_in": -1,
            "quality": 80,
        },
        {
            "_id": "111116",
            "name": "Backstage passes to a TAFKAL80ETC concert",
            "sell_in": 15,
            "quality": 20,
        },
        {
            "_id": "111117",
            "name": "Backstage passes to a TAFKAL80ETC concert",
            "sell_in": 10,
            "quality": 49,
        },
        {
            "_id": "111118",
            "name": "Backstage passes to a TAFKAL80ETC concert",
            "sell_in": 5,
            "quality": 49,
        },
        {
            "_id": "111119",
            "name": "Conjured Mana Cake",
            "sell_in": 3,
            "quality": 6,
        },
    ]

    # Saving items into the db
    for item in default_stock:
        Stock(
            id=item["_id"],
            name=item["name"],
            sell_in=item["sell_in"],
            quality=item["quality"],
        ).save()


def init_app(app):
    init_db()
    app.teardown_appcontext(close_db)
