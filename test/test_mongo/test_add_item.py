import pytest
import json


add_item_stock = [
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
    {"_id": "123123", "name": "newItem", "quality": 5, "sell_in": 5},
]


# Add an item inside the db
@pytest.mark.add_item
def test_add_item(client):
    """
    Test that an item has added into the db successfully. Compare the actual stock with an stock that alredy has the new inserted into the db
    """
    rv_add = client.post("/items?id=123123&name=newItem&sell_in=5&quality=5")
    rv_stock = client.get("/stock")
    assert rv_add.status_code == 201
    assert rv_add.data in b'"New item added successfully !"\n'
    assert json.loads(rv_stock.data) == add_item_stock
