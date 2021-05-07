import pytest


@pytest.mark.quality
def test_quality(client):
    """
    Test to get the elements martching the criteria. The user has to specify the requested quality and the test case check that returns a list with all the elements that match the requested criteria
    """
    rv = client.get("/items/quality/0")
    assert rv.status_code == 200
    assert rv.data in b'[{"_id":"111111","name":"Aged Brie","quality":0,"sell_in":2}]\n'


@pytest.mark.quality
def test_quality_fail(client):
    """
    Test to check that if the requested elements by their quality doesn't match any criteria into the db, in this case it will display a message giving information to the user that the requested elements matching the quality can't be found inside the db
    """
    rv = client.get("/items/quality/150")
    assert rv.status_code == 404
    assert (
        rv.data
        in b'{"message": "Sorry, the item with quality 150 currently is out of stock comeback later and try again"}\n'
    )
