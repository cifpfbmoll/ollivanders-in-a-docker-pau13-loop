import pytest


@pytest.mark.welcome
def test_welcome(client):
    """
    Test case to check that the default endpoint is configured correctly and the test cases can be run correctly without any issue
    """
    rv = client.get("/")
    assert rv.status_code == 200
    assert rv.data in b'{"Welcome!":"Ollivanders"}\n'
