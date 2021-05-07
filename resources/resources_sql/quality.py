from flask_restful import Resource, Api

# Importamos el contenido de Service
from service.service_sql.service import Service

# Importamos Jsonify y Make_Response()
from flask import jsonify, make_response


class Quality(Resource):

    # Due to the name of the parameter must be the same as the route: /items/quality/<item_quality>
    def get(self, item_quality):
        """Gets those items whose quality is the same as the value from the parameter

        Args:
            item_quality (int): quality of the item

        Returns:
            make_response Object: Returns a custom make_response() object with all item whose have the same quality
        """

        response = make_response(jsonify(Service.filter_by_quality(item_quality)))
        response.headers["custom-response"] = "Item filter by quality was returned"
        response.headers["Content-Type"] = "application/json"
        response.status_code = 200
        response.headers["warning"] = "Custom Warning, just appears when it' an warning"

        return response

