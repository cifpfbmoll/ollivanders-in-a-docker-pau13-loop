from domain.Sulfuras import Sulfuras
import pytest


def test_sulfuras_properties():
    sulfuraItem = Sulfuras(name="Sulfuras, Hand of Ragnaros", sell_in=0)

    assert sulfuraItem.get_name() == "Sulfuras, Hand of Ragnaros"
    assert sulfuraItem.get_sell_in() == 0
    assert sulfuraItem.get_quality() == 80


def test_sulfuras_day_one():

    sulfuraItem = Sulfuras(name="Sulfuras, Hand of Ragnaros", sell_in=6)

    sulfuraItem.update_quality()

    assert sulfuraItem.get_quality() == 80


def test_sulfuras_day_two():

    sulfuraItem = Sulfuras(name="Sulfuras, Hand of Ragnaros", sell_in=5)

    sulfuraItem.update_quality()

    assert sulfuraItem.get_quality() == 80


def test_sulfuras_day_three():

    sulfuraItem = Sulfuras(name="Sulfuras, Hand of Ragnaros", sell_in=4)

    sulfuraItem.update_quality()

    assert sulfuraItem.get_quality() == 80


def test_sulfuras_day_four():

    sulfuraItem = Sulfuras(name="Sulfuras, Hand of Ragnaros", sell_in=3)

    sulfuraItem.update_quality()

    assert sulfuraItem.get_quality() == 80


def test_sulfuras_day_five():

    sulfuraItem = Sulfuras(name="Sulfuras, Hand of Ragnaros", sell_in=2)

    sulfuraItem.update_quality()

    assert sulfuraItem.get_quality() == 80


def test_sulfuras_day_six():

    sulfuraItem = Sulfuras(name="Sulfuras, Hand of Ragnaros", sell_in=1)

    sulfuraItem.update_quality()

    assert sulfuraItem.get_quality() == 80
