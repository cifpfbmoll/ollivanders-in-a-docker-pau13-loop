from domain.aged_brie import AgedBrie
import pytest


def test_conjured_properties():
    aged_brie_item = AgedBrie("AgedBrie", 15, 10)

    assert aged_brie_item.get_name() == "AgedBrie"
    assert aged_brie_item.get_sell_in() == 15
    assert aged_brie_item.get_quality() == 10
    assert (
        aged_brie_item.__str__()
        == "***************Item*************** \n Name: AgedBrie,\n Sell in: 15,\n Quality: 10"
    )


def test_aged_brie_day_0():

    aged_brie_item = AgedBrie("AgedBrie", 2, 0)

    aged_brie_item.update_quality()

    assert aged_brie_item.get_sell_in() == 1
    assert aged_brie_item.get_quality() == 1


def test_aged_brie_day_1():

    aged_brie_item = AgedBrie("AgedBrie", 1, 1)

    aged_brie_item.update_quality()

    assert aged_brie_item.get_sell_in() == 0
    assert aged_brie_item.get_quality() == 2


def test_aged_brie_day_2():

    aged_brie_item = AgedBrie("AgedBrie", 0, 2)

    aged_brie_item.update_quality()

    assert aged_brie_item.get_sell_in() == -1
    assert aged_brie_item.get_quality() == 4


def test_aged_brie_day_3():

    aged_brie_item = AgedBrie("AgedBrie", -1, 4)

    aged_brie_item.update_quality()

    assert aged_brie_item.get_sell_in() == -2
    assert aged_brie_item.get_quality() == 6


def test_aged_brie_day_4():

    aged_brie_item = AgedBrie("AgedBrie", -2, 6)

    aged_brie_item.update_quality()

    assert aged_brie_item.get_sell_in() == -3
    assert aged_brie_item.get_quality() == 8


def test_aged_brie_day_5():

    aged_brie_item = AgedBrie("AgedBrie", -3, 8)

    aged_brie_item.update_quality()

    assert aged_brie_item.get_sell_in() == -4
    assert aged_brie_item.get_quality() == 10


def test_aged_brie_day_6():

    aged_brie_item = AgedBrie("AgedBrie", -4, 10)

    aged_brie_item.update_quality()
    assert aged_brie_item.get_sell_in() == -5
    assert aged_brie_item.get_quality() == 12


def test_aged_brie_day_7():

    aged_brie_item = AgedBrie("AgedBrie", -5, 12)

    aged_brie_item.update_quality()

    assert aged_brie_item.get_sell_in() == -6
    assert aged_brie_item.get_quality() == 14


def test_aged_brie_day_8():

    aged_brie_item = AgedBrie("AgedBrie", -6, 14)

    aged_brie_item.update_quality()

    assert aged_brie_item.get_sell_in() == -7
    assert aged_brie_item.get_quality() == 16


def test_aged_brie_day_9():

    aged_brie_item = AgedBrie("AgedBrie", -7, 16)

    aged_brie_item.update_quality()

    assert aged_brie_item.get_sell_in() == -8
    assert aged_brie_item.get_quality() == 18


def test_aged_brie_day_10():

    aged_brie_item = AgedBrie("AgedBrie", -8, 18)

    aged_brie_item.update_quality()

    assert aged_brie_item.get_sell_in() == -9
    assert aged_brie_item.get_quality() == 20
