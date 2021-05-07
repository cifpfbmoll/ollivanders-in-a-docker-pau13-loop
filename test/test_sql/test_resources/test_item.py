import pytest

import json




@pytest.mark.resource_test
def test_item(client):
    """Test the GET request of Items resource, test if since a request it can get an item

    Args:
        client (test_client Flask): It's the test_client() object from APP Flask
    """
    rv = client.get("/items/name/Aged Brie")
    assert json.loads(rv.data) == [{"name": "Aged Brie", "sell_in": 2, "quality": 0}]
    assert rv.status_code == 200




@pytest.mark.resource_test
def test_item_name_fail(client):
    """Test the GET request of Items resource, test if since a request it can get an item that don't exist

    Args:
        client (test_client Flask): It's the test_client() object from APP Flask
    """
    rv = client.get("/items/name/<name>")
    assert rv.status_code == 404
    assert json.loads(rv.data) == {
        "message": "There is not items that satisfied this criteria"
    }
