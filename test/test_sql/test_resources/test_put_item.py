import pytest

import json



@pytest.mark.resource_test
def test_put_item(client):
    """Test the PUT request of Items resource, test if since a request it can update the content of an item

    Args:
        client (test_client Flask): It's the test_client() object from APP Flask
    """

    response = client.put(
        "/items/id/9/?name=Sulfuras Hand of Ragnaros&sell_in=3&quality=6"
    )

    assert json.loads(response.data) == {"message": "Item content updated successfully"}
    assert response.status_code == 201
