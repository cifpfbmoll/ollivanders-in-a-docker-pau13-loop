from flask_restful import Resource, reqparse
from service.service_mongo.service import Service
from flask import make_response, jsonify


class Quality(Resource):

    # http://127.0.0.1:5000/items/quality/<item_quality>
    # curl http://127.0.0.1:5000/items/quality/<item_quality>
    def get(self, item_quality):
        """Get the items from the data base that have the same quality

        Args:
            item_quality (int): quality requested of the item

        Returns:
             make_response Object: return a custom response and display all
             requested items
        """

        response = make_response(jsonify((Service.get_quality(item_quality))))
        response.headers["Content-Type"] = "application/json"
        response.headers["custom-response"] = (
            "Items matching quality " "criteria returned"
        )
        response.status_code = 200
        response.headers["warning"] = (
            "Custom warning, just appears when " "it's a warning"
        )

        return response
