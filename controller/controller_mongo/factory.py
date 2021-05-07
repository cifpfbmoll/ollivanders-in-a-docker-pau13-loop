# FLASK
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_restful import Resource

# MONGO
from repository.repository_mongo.mock_db import db_mock_atlas

# Import package resources
from resources.resources_mongo.item import Item
from resources.resources_mongo.stock import Stock
from resources.resources_mongo.welcome import Welcome
from resources.resources_mongo.sell_in import SellIn
from resources.resources_mongo.quality import Quality
from resources.resources_mongo.update_quality import UpdateQuality


def create_app():
    # Flask Object
    app = Flask(__name__)

    # Cross Origin Resource Sharing
    CORS(app)

    # Init db
    with app.app_context():
        db_mock_atlas.init_app(app)

    # Flask API-REST
    api = Api(app, catch_all_404s=True)

    # endpoints
    api.add_resource(Welcome, "/")
    api.add_resource(Stock, "/stock")
    api.add_resource(Item, "/items/name/<name>", "/items")
    api.add_resource(SellIn, "/items/sell-in/<int:item_sell_in>")
    api.add_resource(Quality, "/items/quality/<int:item_quality>")
    api.add_resource(UpdateQuality, "/items/update-quality")

    return app


# Exclude lines of code from code Coverage
if __name__ == "__main__":  # pragma: no cover
    app = create_app()
    app.run(debug=True)
