from flask_restful import Resource, reqparse
from service.service_mongo.service import Service
from flask import make_response, jsonify


class Item(Resource):

    # http://127.0.0.1:5000/item/name/<name>
    # Remember type spaces with '%20'
    # curl http://127.0.0.1:5000/item/name/<name>
    def get(self, name):
        """Get a list with the items matching the criteria of the name and
        makes a custom response object

        Args:
            name (str): name of the item that the user has requested to get
            from the data base

        Return:
            make_response Object: return a custom response for the request
            with the list of items that has matched the criteria of the
            request and each item is represented inside the
            list as a dictionary"""

        response = make_response(jsonify((Service.get_item(name))))
        response.headers["Content-Type"] = "application/json"
        response.headers["custom-response"] = "Items matching name criteria " "returned"
        response.status_code = 200
        response.headers["warning"] = (
            "Custom warning, just appears when " "it's a warning"
        )

        return response

    # http://127.0.0.1:5000/items?name=new Item2&sell_in=5&quality=5
    # curl http://localhost:5000/items -d name="new Item3"
    # -d sell_in=3 -d quality=6
    # Put this right after curl to indicate the method you want to use -->
    # http://127.0.0.1:5000/items -X POST
    def post(self):
        """Add an item to the data base

        Return:
            make_response Object: return a custom response for the request
            when an item is added"""

        args = self.parseRequest()

        Service.post_item(args)

        response = make_response(jsonify("New item added successfully !"))
        response.headers["Content-Type"] = "application/json"
        response.headers["custom-response"] = "Add an item to the stock"
        response.status_code = 201
        response.headers["warning"] = (
            "Custom warning, just appears when " "it's a warning"
        )

        return response

    # http://127.0.0.1:5000/items?name=new Item&sell_in=5&quality=5
    # curl http://127.0.0.1:5000/items -d name="new Item" -d sell_in=5 -d
    # quality=5
    # Put this right after curl to indicate the method you want to use -->
    # http://127.0.0.1:5000/items -X DELETE
    def delete(self):
        """Delete an item from the data base

        Return:
            make_response Object: return a custom response for the request
            when an item is deleted from the data base"""

        args = self.parseRequest()

        Service.delete_item(args)

        response = make_response(jsonify(""))
        response.headers["Content-Type"] = "application/json"
        response.headers["custom-response"] = "Delete an item from the " "stock"
        response.status_code = 204
        response.headers["warning"] = (
            "Custom warning, just appears when " "it's a warning"
        )

        return response
        # Status response 204 by convention MUST NOT include any body message

    # Designed to provide simple and uniform access to any variable on the
    # flask.request object in Flask
    def parseRequest(self):
        # To have the errors bundled together and sent back to the client all
        # at once
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument(
            "id", type=str, required=True, help="The id of the item is required"
        )
        parser.add_argument(
            "name", type=str, required=True, help="the name of the item is required"
        )
        parser.add_argument(
            "sell_in",
            type=int,
            required=True,
            help="The sell in of the item is required",
        )
        parser.add_argument(
            "quality",
            type=int,
            required=True,
            help="the quality of the item is required",
        )
        # args = parser.parse_args() --> this is a dictionary with the
        # specified arguments like keys
        return parser.parse_args()
