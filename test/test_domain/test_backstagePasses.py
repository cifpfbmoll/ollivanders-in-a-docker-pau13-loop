from domain.backstagePasses import BackstagePasses
import pytest


def test_backstage_passes_properties():
    backstage_passes_item = BackstagePasses("BackstagePasses", 15, 20)

    assert backstage_passes_item.get_name() == "BackstagePasses"
    assert backstage_passes_item.get_sell_in() == 15
    assert backstage_passes_item.get_quality() == 20
    assert (
        backstage_passes_item.__str__()
        == "***************Item*************** \n Name: BackstagePasses,\n Sell in: 15,\n Quality: 20"
    )


def test_bakstage_passes_day_0():

    backstage_passes_item = BackstagePasses("BackstagePasses", 15, 20)

    backstage_passes_item.update_quality()

    assert backstage_passes_item.get_sell_in() == 14
    assert backstage_passes_item.get_quality() == 21

    backstage_passes_item = BackstagePasses("BackstagePasses", 10, 49)

    backstage_passes_item.update_quality()

    assert backstage_passes_item.get_sell_in() == 9
    assert backstage_passes_item.get_quality() == 50

    backstage_passes_item = BackstagePasses("BackstagePasses", 5, 49)

    backstage_passes_item.update_quality()

    assert backstage_passes_item.get_sell_in() == 4
    assert backstage_passes_item.get_quality() == 50


def test_bakstage_passes_day_1():

    backstage_passes_item = BackstagePasses("BackstagePasses", 14, 21)

    backstage_passes_item.update_quality()

    assert backstage_passes_item.get_sell_in() == 13
    assert backstage_passes_item.get_quality() == 22

    backstage_passes_item = BackstagePasses("BackstagePasses", 5, 50)

    backstage_passes_item.update_quality()

    assert backstage_passes_item.get_sell_in() == 4
    assert backstage_passes_item.get_quality() == 50

    backstage_passes_item = BackstagePasses("BackstagePasses", 5, 50)

    backstage_passes_item.update_quality()

    assert backstage_passes_item.get_sell_in() == 4
    assert backstage_passes_item.get_quality() == 50


def test_bakstage_passes_day_2():

    backstage_passes_item = BackstagePasses("BackstagePasses", 13, 22)

    backstage_passes_item.update_quality()

    assert backstage_passes_item.get_sell_in() == 12
    assert backstage_passes_item.get_quality() == 23

    backstage_passes_item = BackstagePasses("BackstagePasses", 8, 50)

    backstage_passes_item.update_quality()

    assert backstage_passes_item.get_sell_in() == 7
    assert backstage_passes_item.get_quality() == 50

    backstage_passes_item = BackstagePasses("BackstagePasses", 3, 50)

    backstage_passes_item.update_quality()

    assert backstage_passes_item.get_sell_in() == 2
    assert backstage_passes_item.get_quality() == 50


def test_bakstage_passes_day_3():

    backstage_passes_item = BackstagePasses("BackstagePasses", 12, 23)

    backstage_passes_item.update_quality()

    assert backstage_passes_item.get_sell_in() == 11
    assert backstage_passes_item.get_quality() == 24

    backstage_passes_item = BackstagePasses("BackstagePasses", 7, 50)

    backstage_passes_item.update_quality()

    assert backstage_passes_item.get_sell_in() == 6
    assert backstage_passes_item.get_quality() == 50

    backstage_passes_item = BackstagePasses("BackstagePasses", 2, 50)

    backstage_passes_item.update_quality()

    assert backstage_passes_item.get_sell_in() == 1
    assert backstage_passes_item.get_quality() == 50


def test_bakstage_passes_day_4():

    backstage_passes_item = BackstagePasses("BackstagePasses", 11, 24)

    backstage_passes_item.update_quality()

    assert backstage_passes_item.get_sell_in() == 10
    assert backstage_passes_item.get_quality() == 25

    backstage_passes_item = BackstagePasses("BackstagePasses", 6, 50)

    backstage_passes_item.update_quality()

    assert backstage_passes_item.get_sell_in() == 5
    assert backstage_passes_item.get_quality() == 50

    backstage_passes_item = BackstagePasses("BackstagePasses", 1, 50)

    backstage_passes_item.update_quality()

    assert backstage_passes_item.get_sell_in() == 0
    assert backstage_passes_item.get_quality() == 50


def test_bakstage_passes_day_5():

    backstage_passes_item = BackstagePasses("BackstagePasses", 10, 25)

    backstage_passes_item.update_quality()

    assert backstage_passes_item.get_sell_in() == 9
    assert backstage_passes_item.get_quality() == 27

    backstage_passes_item = BackstagePasses("BackstagePasses", 5, 50)

    backstage_passes_item.update_quality()

    assert backstage_passes_item.get_sell_in() == 4
    assert backstage_passes_item.get_quality() == 50

    backstage_passes_item = BackstagePasses("BackstagePasses", 0, 50)

    backstage_passes_item.update_quality()

    assert backstage_passes_item.get_sell_in() == -1
    assert backstage_passes_item.get_quality() == 0


def test_bakstage_passes_day_6():

    backstage_passes_item = BackstagePasses("BackstagePasses", 9, 27)

    backstage_passes_item.update_quality()

    assert backstage_passes_item.get_sell_in() == 8
    assert backstage_passes_item.get_quality() == 29

    backstage_passes_item = BackstagePasses("BackstagePasses", 4, 50)

    backstage_passes_item.update_quality()

    assert backstage_passes_item.get_sell_in() == 3
    assert backstage_passes_item.get_quality() == 50

    backstage_passes_item = BackstagePasses("BackstagePasses", -1, 0)

    backstage_passes_item.update_quality()

    assert backstage_passes_item.get_sell_in() == -2
    assert backstage_passes_item.get_quality() == 0


def test_bakstage_passes_day_7():

    backstage_passes_item = BackstagePasses("BackstagePasses", 8, 29)

    backstage_passes_item.update_quality()

    assert backstage_passes_item.get_sell_in() == 7
    assert backstage_passes_item.get_quality() == 31

    backstage_passes_item = BackstagePasses("BackstagePasses", 2, 50)

    backstage_passes_item.update_quality()

    assert backstage_passes_item.get_sell_in() == 1
    assert backstage_passes_item.get_quality() == 50

    backstage_passes_item = BackstagePasses("BackstagePasses", -3, 0)

    backstage_passes_item.update_quality()

    assert backstage_passes_item.get_sell_in() == -4
    assert backstage_passes_item.get_quality() == 0


def test_bakstage_passes_day_8():

    backstage_passes_item = BackstagePasses("BackstagePasses", 7, 31)

    backstage_passes_item.update_quality()

    assert backstage_passes_item.get_sell_in() == 6
    assert backstage_passes_item.get_quality() == 33

    backstage_passes_item = BackstagePasses("BackstagePasses", 2, 50)

    backstage_passes_item.update_quality()

    assert backstage_passes_item.get_sell_in() == 1
    assert backstage_passes_item.get_quality() == 50

    backstage_passes_item = BackstagePasses("BackstagePasses", -3, 0)

    backstage_passes_item.update_quality()

    assert backstage_passes_item.get_sell_in() == -4
    assert backstage_passes_item.get_quality() == 0


def test_bakstage_passes_day_9():

    backstage_passes_item = BackstagePasses("BackstagePasses", 6, 33)

    backstage_passes_item.update_quality()

    assert backstage_passes_item.get_sell_in() == 5
    assert backstage_passes_item.get_quality() == 35

    backstage_passes_item = BackstagePasses("BackstagePasses", 0, 50)

    backstage_passes_item.update_quality()

    assert backstage_passes_item.get_sell_in() == -1
    assert backstage_passes_item.get_quality() == 0

    backstage_passes_item = BackstagePasses("BackstagePasses", -5, 0)

    backstage_passes_item.update_quality()

    assert backstage_passes_item.get_sell_in() == -6
    assert backstage_passes_item.get_quality() == 0


def test_bakstage_passes_day_10():

    backstage_passes_item = BackstagePasses("BackstagePasses", 4, 38)

    backstage_passes_item.update_quality()

    assert backstage_passes_item.get_sell_in() == 3
    assert backstage_passes_item.get_quality() == 41

    backstage_passes_item = BackstagePasses("BackstagePasses", -1, 0)

    backstage_passes_item.update_quality()

    assert backstage_passes_item.get_sell_in() == -2
    assert backstage_passes_item.get_quality() == 0

    backstage_passes_item = BackstagePasses("BackstagePasses", -6, 0)

    backstage_passes_item.update_quality()

    assert backstage_passes_item.get_sell_in() == -7
    assert backstage_passes_item.get_quality() == 0
