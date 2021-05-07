import pytest
import json


@pytest.mark.resource_test
def test_quality(client):
    """Test the GET request of Quality resource, test if since a request it can get an item by its quality

    Args:
        client (test_client Flask): It's the test_client() object from APP Flask
    """
    rv = client.get("/items/quality/80")
    assert rv.status_code == 200
    assert json.loads(rv.data) == [
        {"name": "Sulfuras Hand of Ragnaros", "quality": 80, "sell_in": 0},
        {"name": "Sulfuras Hand of Ragnaros", "quality": 80, "sell_in": -1},
    ]



@pytest.mark.resource_test
def test_quality_fail(client):
    """Test the GET request of Quality resource, test if since a request it can get an item by its quality, but this quality isn't belong to any items

    Args:
        client (test_client Flask): It's the test_client() object from APP Flask
    """
    rv = client.get("/items/quality/150")
    assert rv.status_code == 404
    assert json.loads(rv.data) == {
        "message": "There is not items that satisfied this criteria"
    }
