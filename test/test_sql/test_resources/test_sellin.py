import pytest
import json


@pytest.mark.resource_test
def test_sell_in(client):
    """Test the GET request of Sellin resource, test if since a request it can get an item by its sell_in

    Args:
        client (test_client Flask): It's the test_client() object from APP Flask
    """
    rv = client.get("/items/sellin/10")
    assert rv.status_code == 200
    assert json.loads(rv.data) == [
        {"name": "+5 Dexterity Vest", "quality": 20, "sell_in": 10},
        {
            "name": "Backstage passes to a TAFKAL80ETC concert",
            "quality": 49,
            "sell_in": 10,
        },
    ]


@pytest.mark.resource_test
def test_sell_in_fail(client):
    """Test the GET request of Sellin resource, test if since a request it can get an item by its sell_in, but this sell_in isn't belong to any items

    Args:
        client (test_client Flask): It's the test_client() object from APP Flask
    """
    rv = client.get("/items/sellin/150")
    assert rv.status_code == 404
    assert json.loads(rv.data) == {
        "message": "There is not items that satisfied this criteria"
    }
