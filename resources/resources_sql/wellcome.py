from flask_restful import Resource, Api

# Importamos Jsonify y Make_Response()
from flask import jsonify, make_response


class Wellcome(Resource):
    def get(self):
        """Get a message of Welcome Ollivanders

        Returns:
            make_response Object: Returns a custom make_response() object with a dictionary with the wellcome message
        """

        response = make_response(jsonify({"Welcome!": "Ollivanders"}))
        response.headers[
            "custom-response"
        ] = "Welcome Resource is returned successfully!"
        response.headers["Content-Type"] = "application/json"
        response.status_code = 200
        response.headers["warning"] = "Custom Warning, just appears when it' an warning"

        return response
