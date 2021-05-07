import pytest
import json


@pytest.mark.hello_world
def test_hello_world(client):
    rv = client.get("/")
    assert {"Welcome!": "Ollivanders"} == json.loads(rv.data)
