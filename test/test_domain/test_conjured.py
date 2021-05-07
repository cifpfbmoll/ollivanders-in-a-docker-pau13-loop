from domain.Conjured import Conjured
import pytest


def test_conjured_properties():

    conjured_item = Conjured("Conjured Item", 15, 50)

    assert conjured_item.get_name() == "Conjured Item"
    assert conjured_item.get_sell_in() == 15
    assert conjured_item.get_quality() == 50
    assert (
        conjured_item.__str__()
        == "***************Item*************** \n Name: Conjured Item,\n Sell in: 15,\n Quality: 50"
    )


def test_conjured_day_six():

    conjured_item = Conjured("Conjured Item", 6, 30)

    conjured_item.update_quality()

    assert conjured_item.get_sell_in() == 5
    assert conjured_item.get_quality() == 28


def test_conjured_day_five():

    conjured_item = Conjured("Conjured Item", 5, 28)

    conjured_item.update_quality()

    assert conjured_item.get_sell_in() == 4
    assert conjured_item.get_quality() == 26


def test_conjured_day_four():

    conjured_item = Conjured("Conjured Item", 4, 26)

    conjured_item.update_quality()

    assert conjured_item.get_sell_in() == 3
    assert conjured_item.get_quality() == 24


def test_conjured_day_three():

    conjured_item = Conjured("Conjured Item", 3, 24)

    conjured_item.update_quality()

    assert conjured_item.get_sell_in() == 2
    assert conjured_item.get_quality() == 22


def test_conjured_day_two():

    conjured_item = Conjured("Conjured Item", 2, 22)

    conjured_item.update_quality()

    assert conjured_item.get_sell_in() == 1
    assert conjured_item.get_quality() == 20


def test_conjured_day_one():

    conjured_item = Conjured("Conjured Item", 1, 20)

    conjured_item.update_quality()

    assert conjured_item.get_sell_in() == 0
    assert conjured_item.get_quality() == 18


def test_conjured_no_sell_in():

    conjured_item = Conjured("Conjured Item", 0, 18)

    conjured_item.update_quality()

    assert conjured_item.get_sell_in() == -1
    assert conjured_item.get_quality() == 16

    conjured_item_two = Conjured("Conjured Item", -1, 16)

    conjured_item_two.update_quality()

    assert conjured_item_two.get_sell_in() == -2
    assert conjured_item_two.get_quality() == 12

    conjured_item_three = Conjured("Conjured Item", -2, 12)

    conjured_item_three.update_quality()

    assert conjured_item_three.get_sell_in() == -3
    assert conjured_item_three.get_quality() == 8

    conjured_item_four = Conjured("Conjured Item", -3, 8)

    conjured_item_four.update_quality()

    assert conjured_item_four.get_sell_in() == -4
    assert conjured_item_four.get_quality() == 4

    conjured_item_five = Conjured("Conjured Item", -4, 4)

    conjured_item_five.update_quality()

    assert conjured_item_five.get_sell_in() == -5
    assert conjured_item_five.get_quality() == 0
