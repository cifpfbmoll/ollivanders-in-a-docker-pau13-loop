# marshal_with for validate and filter fields
# abort for check function
from flask_restful import marshal_with, fields, abort
from flask import g

# Importamos el método get_db() para poder manipular la Base de Datos
from repository.repository_sql.db_connection import get_db

# Importamos el método createObjectItem() de repo.py para poder crear un objeto a partir de la info del item
from repository.repository_sql.repo import Factory


class Service:
    """Service Class: This class contains all methods that let us filter, search, update, deleting our database, basically consist of a serie of methods that let us manipulate the dabase. For this reason, this class contains the logic of this manipulation of database. Service module let us There will be less coupling."""

    # Estructura de campos que serán usados en el marshal_with()
    resource_fields = {
        "name": fields.String,
        "sell_in": fields.Integer,
        "quality": fields.Integer,
    }

    @staticmethod
    def check_items(items):
        """Check if the items are not empty or not, if it's empty throw an Abort()

        Args:
            items (list): List of items

        Returns:
            (list): If the list is not empty, returns the same list
        """
        if not items:
            abort(404, message="There is not items that satisfied this criteria")
        return items

    @staticmethod
    @marshal_with(resource_fields)
    def filter_by_name(name):
        """Let us filter an Item by the name of this item

        Args:
            name (string): Name of the Item

        Returns:
            list: Returns a List of Items that satisfies the query of Items Query Model
        """

        db = get_db()


        return Service.check_items(
            [item for item in g.Items.query.filter_by(name=name)]
        )

    @staticmethod
    @marshal_with(resource_fields)
    def filter_by_sell_in(sell_in):
        """Let us filter an Item by the sell_in of this item

        Args:
            sell_in (int): Sell_in of the Item

        Returns:
            list: Returns a List of Items that satisfies the query of Items Query Model, in this case. Those items whose have that sell_in
        """

        db = get_db()

        return Service.check_items(
            [item for item in g.Items.query.filter_by(sell_in=sell_in)]
        )

    @staticmethod
    @marshal_with(resource_fields)
    def filter_by_quality(quality):
        """Let us filter an Item by the quality of this item

        Args:
            quality (int): quality of the Item

        Returns:
            list: Returns a List of Items that satisfies the query of Items Query Model, in this case. Those items whose have that quality
        """

        db = get_db()


        return Service.check_items(
            [item for item in g.Items.query.filter_by(quality=quality)]
        )

    @staticmethod
    @marshal_with(resource_fields)
    def get_items():

        """Get All Items from Database

        Returns:
            (list): Returns a list with all Items
        """

        db = get_db()


        return [item for item in g.Items.query.all()]

    @staticmethod
    def post_item(args_content):
        """Add a new item into de Database Ollivanders into the Items Table, don't return nothing

        Args:
            args_content (dict): Contains the dictionary from parse_args() method, which in the other module let us validate the Request object values
        """
        db = get_db()

        add_item = g.Items(
            name=args_content["name"],
            sell_in=args_content["sell_in"],
            quality=args_content["quality"],
        )

        db.session.add(add_item)
        db.session.commit()

    @staticmethod
    def delete_item(args_content):
        """Delete an item into de Database Ollivanders into the Items Table, don't return nothing

        Args:
            args_content (dict): Contains the dictionary from parse_args() method, which in the other module let us validate the Request object values
        """

        db = get_db()

        db.session.query(g.Items).filter(
            g.Items.name == args_content["name"],
            g.Items.sell_in == args_content["sell_in"],
            g.Items.quality == args_content["quality"],
        ).delete()
        db.session.commit()

    @staticmethod
    def put_item(id_item, args_content):
        """Update the content of an item into de Database Ollivanders into the Items Table, don't return nothing

        Args:
            args_content (dict): Contains the dictionary from parse_args() method, which in the other module let us validate the Request object values
        """

        db = get_db()

        item_by_id = db.session.query(g.Items).filter(g.Items.id == id_item).first()

        if not item_by_id:
            abort(404, message="Don't exist this item")
        else:
            item_by_id.name = args_content["name"]
            item_by_id.sell_in = args_content["sell_in"]
            item_by_id.quality = args_content["quality"]

            db.session.commit()

    @staticmethod
    def update_quality():
        """Update the quality of ALL items that we have in DataBase and after we return the entire Inventory to the Cliente

        Returns:
            (list): Returns a list with all Items, each item is a dictionary
        """

        db = get_db()

        for item in g.Items.query.all():
            # Creamos el objeto Item a partir de la info de la Lista que insertamos en los párametros del método: createObjectItem()
            itemObject = Factory.createObjectItem(
                [item.name, item.sell_in, item.quality]
            )

            # Actualizamos la calidad del item
            itemObject.update_quality()

            # Actualizamos los datos de cada item
            item.sell_in = itemObject.get_sell_in()
            item.quality = itemObject.get_quality()
            # Guardamos los datos actualizados
            db.session.commit()

        return Service.get_items()

    @staticmethod
    def get_user_by_id(user_id):

        get_db()

        return g.User.query.get(int(user_id))


    @staticmethod
    def get_user_by_username(username):

        get_db()

        return g.User.query.filter_by(username=username).first()

    @staticmethod
    def add_user(username, password):

        db = get_db()

        user = Service.get_user_by_username(username)

        if not user:

            new_user = g.User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()

            return True

        else:
            return False

