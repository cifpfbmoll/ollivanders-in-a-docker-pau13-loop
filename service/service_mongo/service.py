# FLASK
from flask_restful import fields, marshal_with, abort
from flask import Response, g

# MONGO
from mongoengine.queryset.visitor import Q
from repository.repository_mongo.db_atlas import get_db
from repository.repository_mongo.db_model import Stock
from repository.repository_mongo.repo import Factory


class Service:
    # Create item json structure that will be accessed by 'marshal_with'
    resource_fields = {
        "_id": fields.String,
        "name": fields.String,
        "sell_in": fields.Integer,
        "quality": fields.Integer,
    }

    # INVENTORY
    @staticmethod
    @marshal_with(resource_fields)
    def get_stock():
        """
        Get all the items saved into the db

        Returns:
            (list): Return a list with all the items saved into the data
            base, each item inside the list will be represented as a
            dictionary
        """
        db = get_db()
        return [stock for stock in g.Stock.objects()]

    # GET ITEM
    @staticmethod
    @marshal_with(resource_fields)
    def get_item(name):
        """
        Iterate thorgh thd db and get a single item saved into the db matching the name of the requested item

        Args:
            name (string): name of the item we are looking for into the db

        Returns:
            item(list): return a collection that we must transform into a list that contains all the elements that had match the criteria and the elements that contain the list will be represented as a dictionary
        """

        db = get_db()

        # In case we do the request without specify a name
        if name == "<name>":
            abort(404, message="The name of the item is required")

        item = g.Stock.objects(name=name)

        # In case the item is not found in the db
        if not item:
            abort(
                404,
                message=(
                    "Sorry, right now we are out of stock of the "
                    "item {} comeback later and try "
                    "again"
                ).format(name),
            )

        return list(item)

    # ADD ITEM
    @staticmethod
    @marshal_with(resource_fields)
    def post_item(args):
        """
        Add a new non existent item inside the db

        Args:
            args(dictionary): Get the new item represented as a dictionary that must be inserted into the db
        """

        db = get_db()

        item = g.Stock(
            id=args["id"],
            name=args["name"],
            sell_in=args["sell_in"],
            quality=args["quality"],
        )
        item.save()

    # DELETE ITEM
    @staticmethod
    @marshal_with(resource_fields)
    def delete_item(args):
        """
        Iterate through all the items saved into the db and delete the first item matching the criteria

        Args:
            args(dictionary): parameters of the item that must be deleted from the db
        """

        db = get_db()

        item = g.Stock.objects(
            Q(_id=args["id"])
            & Q(name=args["name"])
            & Q(sell_in=args["sell_in"])
            & Q(quality=args["quality"])
        ).first()

        if not item:
            abort(404, message="The item that you're trying to delete doesn't " "exist")
        item.delete()

    # SELL_IN
    @staticmethod
    @marshal_with(resource_fields)
    def get_sell_in(sell_in):
        """
        Iterate trhough all the items saved inside the db and return all the elements that match the criteria

        Args:
            sell_in(int): sell_in of the element we are looking for inside the db

        Return:
            item(list): return a collection that we must transform into a list that contains all the elements that had match the criteria and the elements that contain the list will be represented as a dictionary
        """

        db = get_db()

        # Make a list with all the items that match the sell_in specified
        items = [item for item in g.Stock.objects(sell_in=sell_in)]

        # In case the item is not found in the db
        if len(items) == 0:
            abort(
                404,
                message=(
                    "Sorry, the item with sell_in {} currently is out of stock "
                    "comeback later and try again"
                ).format(sell_in),
            )

        return list(items)

    # QUALITY
    @staticmethod
    @marshal_with(resource_fields)
    def get_quality(quality):
        """
        Iterate trhough all the items saved inside the db and return all the elements that match the criteria

        Args:
            quality(int): quality of the element we are looking for inside the db

        Return:
            item(list): return a collection that we must transform into a list that contains all the elements that had match the criteria and the elements that contain the list will be represented as a dictionary
        """

        db = get_db()

        # Make a list with all the items that match the sell_in specified
        items = [item for item in g.Stock.objects(quality=quality)]

        # In case the item is not found in the db
        if len(items) == 0:
            abort(
                404,
                message=(
                    "Sorry, the item with quality {} currently is out of stock "
                    "comeback later and try again"
                ).format(quality),
            )

        return list(items)

    # UPDATE
    @staticmethod
    def update_quality():
        """
        Update the quality and the sell_in of all the items that are inserted into the db at this moment. Each element is updated by his own implemented logic

        Return:
            (list): Return a list with all the items saved into the db, each item inside the list will be represented as a dictionary
        """

        db = get_db()

        # Loop through all the items save into the db
        for item in g.Stock.objects():
            item_object = Factory.create_object_item(
                [item.name, item.sell_in, item.quality]
            )
            item_object.update_quality()

            item.sell_in = item_object.get_sell_in()
            item.quality = item_object.get_quality()

            item.save()

        return Service.get_stock()
