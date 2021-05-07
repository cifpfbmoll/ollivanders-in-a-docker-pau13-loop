import pytest
import json


default_stock = [
    {"_id": "111111", "name": "Aged Brie", "quality": 0, "sell_in": 2},
    {"_id": "111112", "name": "+5 Dexterity Vest", "quality": 20, "sell_in": 10},
    {"_id": "111113", "name": "Elixir of the Mongoose", "quality": 7, "sell_in": 5},
    {
        "_id": "111114",
        "name": "Sulfuras, Hand of Ragnaros",
        "quality": 80,
        "sell_in": 0,
    },
    {
        "_id": "111115",
        "name": "Sulfuras, Hand of Ragnaros",
        "quality": 80,
        "sell_in": -1,
    },
    {
        "_id": "111116",
        "name": "Backstage passes to a TAFKAL80ETC concert",
        "quality": 20,
        "sell_in": 15,
    },
    {
        "_id": "111117",
        "name": "Backstage passes to a TAFKAL80ETC concert",
        "quality": 49,
        "sell_in": 10,
    },
    {
        "_id": "111118",
        "name": "Backstage passes to a TAFKAL80ETC concert",
        "quality": 49,
        "sell_in": 5,
    },
    {"_id": "111119", "name": "Conjured Mana Cake", "quality": 6, "sell_in": 3},
]


# I chose to use json.loads() instead the rv.data methods to run this test
# case because if i have to use rv.data to run this test case at the moment
# to transform the data to bytes it become a really hard work fix all the
# indentations and spaces to get exactly the same number of bytes from the
# expected to the actual object that we want to test
@pytest.mark.stock
def test_stock(client):
    """
    Test to get all the stock of the data base. This test case check that the default stock match the stock that the data base should contain
    """
    rv = client.get("/stock")
    assert rv.status_code == 200
    assert json.loads(rv.data) == default_stock
