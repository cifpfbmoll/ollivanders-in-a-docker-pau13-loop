from flask_restful import Resource, Api

# Importamos el contenido de Service
from service.service_sql.service import Service

# Importamos Jsonify y Make_Response()
from flask import jsonify, make_response


class UpdateQuality(Resource):
    def get(self):
        """Gets a list of all items with their quality updated

        Returns:
            make_response Object: Returns a custom make_response() object with items, each item is a dictionary
        """

        response = make_response(jsonify(Service.update_quality()))
        response.headers["custom-response"] = "All items were updated successfully!"
        response.headers["Content-Type"] = "application/json"
        response.status_code = 200
        response.headers["warning"] = "Custom Warning, just appears when it' an warning"

        return response
