from domain.Inventory import Inventory
from domain.Conjured import Conjured
from domain.aged_brie import AgedBrie
from domain.backstagePasses import BackstagePasses
import pytest


def test_inventory_properties():

    conjured_item = Conjured("Conjured Item", 6, 30)
    aged_brie_item = AgedBrie("AgedBrie", 2, 0)
    backstage_passes = BackstagePasses("BackstagePasses", 15, 20)

    items = [conjured_item, aged_brie_item, backstage_passes]

    inventory = Inventory()

    inventory.add_items(items)

    assert inventory.get_items() == items


def test_add_items():

    conjured_item = Conjured("Conjured Item", 6, 30)
    aged_brie_item = AgedBrie("AgedBrie", 2, 0)
    backstage_passes = BackstagePasses("BackstagePasses", 15, 20)

    items = [conjured_item, aged_brie_item, backstage_passes]

    inventory = Inventory()

    inventory.add_items(items)

    assert len(inventory.get_items()) == 3


def test_to_string_items():

    conjured_item = Conjured("Conjured Item", 6, 30)
    aged_brie_item = AgedBrie("AgedBrie", 2, 0)
    backstage_passes = BackstagePasses("BackstagePasses", 15, 20)

    items = [conjured_item, aged_brie_item, backstage_passes]

    inventory = Inventory()

    inventory.add_items(items)

    assert (
        inventory.__str__()
        == "***************Item*************** \n Name: Conjured Item,\n Sell in: 6,\n Quality: 30 \n ***************Item*************** \n Name: AgedBrie,\n Sell in: 2,\n Quality: 0 \n ***************Item*************** \n Name: BackstagePasses,\n Sell in: 15,\n Quality: 20 \n "
    )


def test_update_quality_items():

    conjured_item = Conjured("Conjured Item", 6, 30)
    aged_brie_item = AgedBrie("AgedBrie", 2, 0)
    backstage_passes = BackstagePasses("BackstagePasses", 15, 20)

    items = [conjured_item, aged_brie_item, backstage_passes]

    inventory = Inventory()

    inventory.add_items(items)

    inventory.update_quality_items()

    assert (
        inventory.__str__()
        == "***************Item*************** \n Name: Conjured Item,\n Sell in: 5,\n Quality: 28 \n ***************Item*************** \n Name: AgedBrie,\n Sell in: 1,\n Quality: 1 \n ***************Item*************** \n Name: BackstagePasses,\n Sell in: 14,\n Quality: 21 \n "
    )
