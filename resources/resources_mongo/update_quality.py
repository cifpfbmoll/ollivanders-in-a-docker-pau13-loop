from flask_restful import Resource, Api
from service.service_mongo.service import Service
from flask import make_response, jsonify


class UpdateQuality(Resource):

    # http://localhost:5000/items/update-quality
    # curl http://localhost:5000/items/update-quality
    def get(self):
        """Update the quality and sell_in from all the items saved into the
        data base and once the process is finished will display all the items
        of the data base updated

        Returns:
             make_response Object: return a custom response and display all
             items saved and updated into the data base
        """

        response = make_response(jsonify((Service.update_quality())))
        response.headers["Content-Type"] = "application/json"
        response.headers["custom-response"] = "Return all the current stock"
        response.status_code = 200
        response.headers["warning"] = (
            "Custom warning, just appears when " "it's a warning"
        )

        return response
