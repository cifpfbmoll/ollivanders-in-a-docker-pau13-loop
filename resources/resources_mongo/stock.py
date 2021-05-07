from flask_restful import Resource
from service.service_mongo.service import Service
from flask import make_response, jsonify


class Stock(Resource):

    # http://localhost:5000/stock
    # curl http://localhost:5000/stock
    def get(self):
        """Get all the items from the data base

        Returns:
             make_response Object: return a custom response and display all
             items saved into the data base
        """

        response = make_response(jsonify((Service.get_stock())))
        response.headers["Content-Type"] = "application/json"
        response.headers["custom-response"] = "Return all the current stock"
        response.status_code = 200
        response.headers["warning"] = (
            "Custom warning, just appears when " "it's a warning"
        )

        return response
