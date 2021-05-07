import pytest
import json


expected_updated_inventory = [
    {"name": "+5 Dexterity Vest", "quality": 18, "sell_in": 9},
    {"name": "Aged Brie", "quality": 1, "sell_in": 1},
    {"name": "Elixir of the Mongoose", "quality": 6, "sell_in": 4},
    {"name": "Sulfuras Hand of Ragnaros", "quality": 80, "sell_in": 0},
    {"name": "Sulfuras Hand of Ragnaros", "quality": 80, "sell_in": -1},
    {"name": "Backstage passes to a TAFKAL80ETC concert", "quality": 21, "sell_in": 14},
    {"name": "Backstage passes to a TAFKAL80ETC concert", "quality": 50, "sell_in": 9},
    {"name": "Backstage passes to a TAFKAL80ETC concert", "quality": 50, "sell_in": 4},
    {"name": "Conjured Mana Cake", "quality": 4, "sell_in": 2},
]


@pytest.mark.resource_test
def test_update_quality(client):
    """Test the GET request of UpdateQuality resource, test if since a request it can get all items with their quality updated

    Args:
        client (test_client Flask): It's the test_client() object from APP Flask
    """

    response = client.get("/update_quality")

    assert json.loads(response.data) == expected_updated_inventory
    assert response.status_code == 200
