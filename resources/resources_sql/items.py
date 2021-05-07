from flask_restful import Resource, reqparse, Api

# Importamos el contenido de Service
from service.service_sql.service import Service

# Importamos Jsonify y Make_Response()
from flask import jsonify, make_response


class Items(Resource):

    # Due to the name of the parameter must be the same as the route: /items/<item_name>
    def get(self, item_name):
        """Get an item by its name

        Args:
            item_name (string): name of the item

        Returns:
            make_response Object: Returns a custom make_response() object with with all item whose satified the criteria of hve the same name of the parameter
        """

        response = make_response(jsonify(Service.filter_by_name(item_name)))
        response.headers["custom-response"] = "Item filter by name was returned"
        response.headers["Content-Type"] = "application/json"
        response.status_code = 200
        response.headers["warning"] = "Custom Warning, just appears when it' an warning"

        return response


    def parseRequest(self):
        """Let us validate values from the Request through "reqparse" and its object: RequestParser()

        Returns:
            dict: Returns a Dictionary with the item already validatedº
        """

        # location='json' dentro de add_argument() nos permite indicar que los datos deben estar en un json, la he eliminado porque con curl no erá posible usando el location='json'

        # Nos permite validad el objeto Request y sus valores
        parser = reqparse.RequestParser(bundle_errors=True)
        # Name of item
        parser.add_argument(
            "name", type=str, required=True, help="Name of the Item is required"
        )
        # Sell_in of Item
        parser.add_argument(
            "sell_in", type=int, required=True, help="Sell_in of the Item is required"
        )
        # Quality
        parser.add_argument(
            "quality", type=int, required=True, help="Quality of the Item is required"
        )

        # Dictionary with all args from parser
        return parser.parse_args()

    def post(self):
        """Let us add a new item/resource

        Returns:
            make_response Object: Returns a custom make_response() object with a message of the item has been added
        """

        args_content = self.parseRequest()

        # Llamo al método post_items y le pasó el args_content
        Service.post_item(args_content)

        response = make_response(jsonify({"message": "New Item has been added"}))
        response.headers["custom-response"] = "The item was added successfully!"
        response.headers["Content-Type"] = "application/json"
        response.status_code = 201
        response.headers["warning"] = "Custom Warning, just appears when it' an warning"

        return response


    def delete(self):
        """Let us delete an item/resource

        Returns:
            make_response Object: Returns a custom make_response() object without a message, but the header of the response object have a message of the item has been deleted
        """

        args_content = self.parseRequest()

        Service.delete_item(args_content)

        response = make_response(jsonify({}))
        response.headers["custom-response"] = "The item was delete successfully!"
        response.headers["Content-Type"] = "application/json"
        response.status_code = 204
        response.headers["warning"] = "Custom Warning, just appears when it' an warning"

        return response

        # DELETE Request don't receive a Message Response


    def put(self, id_item):
        """Let us update the content of an item/resource

        Returns:
            make_response Object: Returns a custom make_response() object without a message, but the header of the response object have a message of the item content has been updated
        """

        args_content = self.parseRequest()

        Service.put_item(id_item, args_content)

        response = make_response(
            jsonify({"message": "Item content updated successfully"})
        )
        response.headers["custom-response"] = "The item was delete successfully!"
        response.headers["Content-Type"] = "application/json"
        response.status_code = 201
        response.headers["warning"] = "Custom Warning, just appears when it' an warning"

        return response
