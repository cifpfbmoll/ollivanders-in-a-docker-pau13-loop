import pytest

import json



@pytest.mark.resource_test
def test_post_item(client):
    """Test the POST request of Items resource, test if since a request it can add an item

    Args:
        client (test_client Flask): It's the test_client() object from APP Flask
    """

    response = client.post("/items?name=Conjured%20Mana%20Cake&sell_in=4&quality=7")

    assert json.loads(response.data) == {"message": "New Item has been added"}
    assert response.status_code == 201
