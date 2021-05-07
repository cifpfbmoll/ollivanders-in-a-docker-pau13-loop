from flask_restful import Resource, reqparse
from service.service_mongo.service import Service
from flask import make_response, jsonify


class SellIn(Resource):

    # http://localhost:5000/items/sell-in/<item_sell_in>
    # curl http://localhost:5000/items/sell-in/<item_sell_in>
    def get(self, item_sell_in):
        """Get the items from the data base that have the same sell_in

        Args:
            item_sell_in (int): sell_in requested of the item

        Returns:
             make_response Object: return a custom response and display all
             requested items
        """

        response = make_response(jsonify((Service.get_sell_in(item_sell_in))))
        response.headers["Content-Type"] = "application/json"
        response.headers["custom-response"] = (
            "Items matching sell_in " "criteria returned"
        )
        response.status_code = 200
        response.headers["warning"] = (
            "Custom warning, just appears when " "it's a warning"
        )

        return response
