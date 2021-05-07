# DB SQLAlchemy Object
# from repository.models.db_model import db
from flask import g
from repository.repository_sql.models.db_model import db

# Cada Item irá dentro del Items Model
class Items(db.Model):
    """This class is Model from SQLAlchemy ORM to preparing Inventory Model which is going to store Items

    Args:
        db (SQLAlchemy): SQLAlchemy Object is use for desing the model, where is use to create Columns and their types and other details.

    """

    __tablename__ = "items"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    sell_in = db.Column(db.Integer, nullable=False)
    quality = db.Column(db.Integer, nullable=False)

    def __init__(self, name, sell_in, quality):

        """Constructor where the values for a new Object which will be a Item

        Args:
            name (string): Name of the Item
            sell_in (int): Sell_in of the Item
            quality (int): Quality of the item
        """
        # The reason of because ID is not put here is because in MySQL the primary Key is done automatically
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "id: {0} | name: {1} | sell_in: {2} | quality: {3}".format(
            self.id, self.name, self.sell_in, self.quality
        )

    def to_json(self):
        """Return the Item in a Dictionary with the reason of use this Item more useful when it managed with JSON.

        Returns:
            (dict): Returns a representation of the Item of JSON in format Python Dictionary
        """

        return {"name": self.name, "sell_in": self.sell_in, "quality": self.quality}


# if __name__ == "__main__":
