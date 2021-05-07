from flask_restful import Resource, Api

# Importamos el contenido de Service
from service.service_sql.service import Service

# Importamos Jsonify y Make_Response()
from flask import jsonify, make_response


class Sellin(Resource):

    # Due to the name of the parameter must be the same as the route: /items/sellin/<item_sell_in>
    def get(self, item_sell_in):
        """Gets those items whose sell_in is the same as the value from the parameter

        Args:
            item_sell_in (int): sell_in of the item

        Returns:
            make_response Object: Returns a custom make_response() object with all item whose have the same sell_in
        """

        response = make_response(jsonify(Service.filter_by_sell_in(item_sell_in)))
        response.headers["custom-response"] = "Item filter by sell_in was returned"
        response.headers["Content-Type"] = "application/json"
        response.status_code = 200
        response.headers["warning"] = "Custom Warning, just appears when it' an warning"

        return response

