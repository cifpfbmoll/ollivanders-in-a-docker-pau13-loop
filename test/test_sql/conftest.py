import pytest

# APP Flask Factory
from controller.controller_sql.factory import create_app

# Repo.py Factory para poblar la base de datos test
from repository.repository_sql.models.db_model import db as _db
from repository.repository_sql.repo import Factory

# Importamos también el modelo
from repository.repository_sql.models.items import Items

# Para la conexión de la DB test, importó el objeto G de Flask
from repository.repository_sql.db_connection import init_app


class TestConfig(object):
    """TestConfig Class: Class with the configuration constants of Testing Envronment of APP Flask"""

    # DEBUG debe ser Falso para que no haya error del método SETUP al intentar ejecutar el APP Flask, por ahora es mejor dejarlo en False
    DEBUG = False
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENV = "test"
    TESTING = True


@pytest.fixture
def app():
    """Get the APP Flask from the create_app() method from Factory of Controller Package

    Yields:
        Flask Intance: Yields a APP Flask
    """
    app = create_app()
    yield app


@pytest.fixture
def client(app):
    """Get the test_client of APP Flask, where before of Yield sentence, it adds the basic items into database and models with the main goal of each test use this data/items to test it and after each test the data of models and database restart by default. This help us to isolate each test from another test

    Args:
        app (Flask instance): APP Flask

    Yields:
        test_client: Yields a test_client from APP Flask to test our test cases
    """

    with app.test_client() as client:
        with app.app_context():
            _db.init_app(app)
            # _db.drop_all()
            _db.create_all()

            #         Obtenemos la lista con los items
            inventario = Factory.loadInventory()

            # Poblamos la Base de datos introduciendo los datos
            for item in inventario:
                add_item = Items(
                    name=item["name"], sell_in=item["sell_in"], quality=item["quality"]
                )

                _db.session.add(add_item)
                _db.session.commit()

            yield client

            _db.session.query(Items).delete()
            _db.session.commit()
            # _db.session.close()
            # _db.drop_all()


@pytest.fixture(scope="function")
def db(app):
    """Get the Database Object of SQLAlchemy, where before get the _db it's open the app_context() and init the app in the DB and create all Models, after the Models and database is filled in with the basic items from loadInventory(), after each test the data of models and database restart by default. The scope of this fixture is for each test function

    Args:
        app (flask instance): App Flask

    Yields:
        SQLAlchemy Instance: Yields a SQLAlchemy Object with the session init
    """
    with app.test_client() as client:
        with app.app_context():
            _db.init_app(app)
            # _db.drop_all()
            _db.create_all()

            #         Obtenemos la lista con los items
            inventario = Factory.loadInventory()

            # Poblamos la Base de datos introduciendo los datos
            for item in inventario:
                add_item = Items(
                    name=item["name"], sell_in=item["sell_in"], quality=item["quality"]
                )

                _db.session.add(add_item)
                _db.session.commit()

            yield _db

            _db.session.query(Items).delete()
            _db.session.commit()


# Tiene el scope='function' para que su alcance solo sea cada test
@pytest.fixture(scope="function", autouse=True)
def session(db):
    """Session fixture help us to do a transaction SQL for each test of repository test cases, this means that for each test function of repository package, session fixture opens a transaction in SQLAlchemy and Database MySQL where after finished the test, the transaction finished with a rollback, this means that all changes of each test actually don't affect the models and database at the finished because of Transactions SQL. Due to this fixture is for each test function, then the scope is function and the autouse is True

    Args:
        db (SQLAlchemy instance): It's a SQLALchemy Object

    Yields:
        SQLALchemy session: Yields a session of the SQLAlchemy Object for each test function
    """
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session_ = db.create_scoped_session(options=options)

    db.session = session_

    yield session_

    transaction.rollback()
    # connection.close()
    session_.remove()

