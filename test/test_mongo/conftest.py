import pytest
from controller.controller_mongo.factory import create_app


@pytest.fixture
def client():
    """
    Create the configuration that we will have to use to be able to run our test cases, with this method we won't be able to run our test cases
    """
    app = create_app()
    return app.test_client()
