# FLASk
import click
from flask import g
from flask.cli import with_appcontext

# MONGO
from mongoengine import *

# Model
from repository.repository_mongo.db_model import Stock


"""
    To connect with Mongo-Atlas you'll have to follow the next steps:
        1.- Check the port is free and accessible to make a connection with your db, run your app and execute the following command:
        - curl portquiz.net:27017
        2.-  If the port it's free will display a message saying "Test successful !" and it will show your current public IP that you'll have to use to connect with the Atlas Cluster Service
"""

db_name = "ollivanders"
URI = (
    "mongodb+srv://adminUser:adminPassword@sandbox.jh5ph.mongodb.net"
    "/ollivanders?retryWrites=true&w=majority"
)


# To establish a connection with the db
def get_db():
    """
    Create a connection to the db to be able to perform any queries and
    operations. It creates the special object 'g' that is unique for each request

    Returns: g, global object storing the data that have to be accesse during the request. This connection will be stored and reused for the next request
    """
    if "db" not in g:
        g.db = connect(db=db_name, host=URI, alias="default")
        g.Stock = Stock
    return g.db


# To close the connection with the db
def close_db(e=None):
    """
    Check if a connection has been created. If the connection exists this one will be closed. This function will be called after each request to close the connection in case is set up
    """
    db = g.pop("db", None)

    if db is not None:
        db.close()


# To fill the db with items
def init_db():
    """
    After make a connection with the db, this one will be filled with all the items that has to include the default stock of the db. It will run the db syntax commands to fill it
    """
    db = get_db()

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


# Initialize the db
@click.command("init-db")
@with_appcontext
def init_db_command():
    """
    It register the command 'init-db' to initialize the db with the app and display a message when the connection has been created successfully
    """
    init_db()
    click.echo("Successfully connected to the Mongo Atlas Cluster !")


def init_app(app):
    """
    Register the functions 'close_db' and 'init_db_command' with the
    application instance, otherwise they won't be used by the application. 'close_db' is called after each request, this means that the db will close the connection after each request. 'init-db' command has been registered with the app, and now it can be called using in this order the below flask commands:
        1.-set FLASK_APP=<app.py>
        2.-set FLASK_ENV=development
        3.-flask init-db

    Args:
        'app.teardown_appcontext()', tells flask to call the function when cleaning up after returning the response
        'app.cli.add_command()', adds a new command that can be called with the flask command
    """
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
