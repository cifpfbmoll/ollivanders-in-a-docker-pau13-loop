from flask_restful import Resource, Api
from flask import make_response, jsonify


class Welcome(Resource):

    # # http://localhost:5000/
    # curl http://localhost:5000/
    def get(self):
        """Display greeting from the shop that belongs the software

        Returns:
             make_response Object: return a custom response and display
             greeting from the shop that belongs the software
        """

        response = make_response(jsonify({"Welcome!": "Ollivanders"}))
        response.headers["Content-Type"] = "application/json"
        response.headers["custom-response"] = (
            "Welcome resource is returned " "successfully"
        )
        response.status_code = 200
        response.headers["warning"] = (
            "Custom warning, just appears when " "it's a warning"
        )

        return response
