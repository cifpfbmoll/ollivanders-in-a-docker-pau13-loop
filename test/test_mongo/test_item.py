import pytest


# Item inside db
@pytest.mark.item
@pytest.mark.existent_item
def test_item(client):
    """
    Test to get the elements martching the criteria. The user has to specify the requested name of the elements and the test case check that returns a list with all the elements that match the requested criteria
    """
    rv = client.get("/items/name/Aged Brie")
    assert rv.data in b'[{"_id":"111111","name":"Aged Brie","quality":0,"sell_in":2}]\n'
    assert rv.status_code == 200


# Request without Item Name
@pytest.mark.item
@pytest.mark.non_name
def test_nonItemName(client):
    """
    Test to get an element without name. If an element from the data base has been request but has not specified the name it will return a message giving information to the user explaining that to get an element from de db has to specify the name of the requested element
    """
    rv = client.get("/items/name/<name>")
    assert rv.status_code == 404
    assert rv.data in b'{"message": "The name of the item is required"}\n'


# Item that doesn't exist in the DB
@pytest.mark.item
@pytest.mark.non_item
def test_nonItem(client):
    """
    Test to get an element from the data base that doen't exist or doesn't axist anymore. In case the request element it can't be found isnide the db will display a message giving information to the user explainig that the requested element it can't be found isnide the db
    """
    rv = client.get("/items/name/Non existent")
    assert rv.status_code == 404
    assert (
        rv.data
        in b'{"message": "Sorry, right now we are out of stock of the item Non existent comeback later and try again"}\n'
    )
