# Import Item classes that we use to create objects from them
from domain.normal_item import NormalItem
from domain.aged_brie import AgedBrie
from domain.backstagePasses import BackstagePasses
from domain.Sulfuras import Sulfuras
from domain.Conjured import Conjured


class Factory:
    @staticmethod
    def create_object_item(item):
        """
        Create an object from each item included inside the data base.
        Depending which one are the names of the items, they will have one
        class or other assigned to them and it will create and object from
        the selected class. This method was created by @dfleta from github

        Args:
            item(list): Is a list that contains all the required info of each item, it has three different aspects: name, sell_in and quality.

        Return:
            [Object]: Returns an object that have assigned a class and the
            class has been assigned to the object by the name of this one
        """

        dict_class_items = {
            "Sulfuras, Hand of Ragnaros": "Sulfuras",
            "Aged Brie": "AgedBrie",
            "Backstage passes to a TAFKAL80ETC concert": "BackstagePasses",
            "Conjured Mana Cake": "Conjured",
            "+5 Dexterity Vest": "Conjured",
            "Normal Item": "NormalItem",
        }

        try:
            item_class = dict_class_items[item[0]]
        except KeyError:
            item_class = dict_class_items["Normal Item"]

        return eval(item_class + str(tuple(item)))
