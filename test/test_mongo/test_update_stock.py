import pytest
import json


update_stock = [
    {"_id": "111111", "name": "Aged Brie", "quality": 1, "sell_in": 1},
    {"_id": "111112", "name": "+5 Dexterity Vest", "quality": 18, "sell_in": 9},
    {"_id": "111113", "name": "Elixir of the Mongoose", "quality": 6, "sell_in": 4},
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
        "quality": 21,
        "sell_in": 14,
    },
    {
        "_id": "111117",
        "name": "Backstage passes to a TAFKAL80ETC concert",
        "quality": 50,
        "sell_in": 9,
    },
    {
        "_id": "111118",
        "name": "Backstage passes to a TAFKAL80ETC concert",
        "quality": 50,
        "sell_in": 4,
    },
    {"_id": "111119", "name": "Conjured Mana Cake", "quality": 4, "sell_in": 2},
]


@pytest.mark.update_stock
def test_update_stock(client):
    """
    Test to check if the elements from the data base have been update their quality correctly. This test case access to the endpoint with the duty to update the quality of the elements that are included into the db. And after we request the stock included inside the data base. Finally we compare if the stock that we got from the db is equal to the stock that has update the quality of his elements
    """
    rv = client.get("/items/update-quality")
    assert rv.status_code == 200
    assert json.loads(rv.data) == update_stock
