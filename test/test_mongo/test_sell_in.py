import pytest


@pytest.mark.sell_in
def test_sell_in(client):
    """
    Test to get the elements martching the criteria. The user has to specify the requested sell_in and the test case check that returns a list with all the elements that match the requested criteria
    """
    rv = client.get("/items/sell-in/15")
    assert rv.status_code == 200
    assert (
        rv.data
        in b'[{"_id":"111116","name":"Backstage passes to a TAFKAL80ETC concert","quality":20,"sell_in":15}]\n'
    )


@pytest.mark.sell_in
def test_sell_in_fail(client):
    """
    Test to check that if the requested elements by their sell_in doesn't match any criteria into the db, in this case it will display a message giving information to the user that the requested elements matching the sell_in can't be found inside the db
    """
    rv = client.get("/items/sell-in/200")
    assert rv.status_code == 404
    assert (
        rv.data
        in b'{"message": "Sorry, the item with sell_in 200 currently is out of stock comeback later and try again"}\n'
    )
