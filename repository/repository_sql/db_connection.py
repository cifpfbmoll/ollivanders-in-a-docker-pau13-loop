from flask_sqlalchemy import SQLAlchemy
from flask import g

# Import current_app for using inside of SQLAlchemy Object
from flask import current_app as app

# Click Package
import click
from flask.cli import with_appcontext

# Models
from repository.repository_sql.models.items import Items
from repository.repository_sql.models.db_model import db
from repository.repository_sql.models.users import User

# Factory Class
from repository.repository_sql.repo import Factory


def get_db():

    # Si la propiedad "db" no está en el objeto G, entonces:
    if "db" not in g:

        # SQLite
        # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databaseCarpeta/nombreDB.db'
        # MYSQL
        # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:power2021@127.0.0.1/ollivanders'
        # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        # En el caso de que el "Environment" del APP de FLASK es TEST, entonces la configuración de conexión a la Base de Datos está dirigida a la Base de datos: "ollivanderstest"
        if app.config["ENV"] == "test":

            app.config["ENV"] = "test"
            # Configuration APP Flask
            # app.config.from_object("config.TestingConfig")
            # "mysql+pymysql://root:localhost: 3306"
            app.config[
                "SQLALCHEMY_DATABASE_URI"
            ] = "mysql+pymysql://root:power2021@127.0.0.1/ollivanderstest"
            app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

        # En el caso contrario de que no sea TEST entonces redirige la conexión a la base de datos "ollivanders"
        else:
            # SQLite
            # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databaseCarpeta/nombreDB.db'
            # MYSQL
            app.config[
                "SQLALCHEMY_DATABASE_URI"
            ] = "mysql+pymysql://root:power2021@127.0.0.1/ollivanders"
            app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

        # Agrego el current_app con la APP de flask dentro del objeto SQLAlchemy
        db.init_app(app)
        g.db = db

        # Agregamos al objeto G, la propiedad ITEMS con el valor del modelo Items
        g.Items = Items
        g.User = User

        return g.db


def close_db(e=None):
    # Si la conexión existe, se cierra.
    # Este método lo he visto también en la documentación oficial
    # https://flask.palletsprojects.com/en/1.1.x/appcontext/
    db = g.pop("db", None)

    if db is not None:
        db.session.close()


def init_db():

    # Obtenemos la DB
    db = get_db()

    # Obtenemos la lista con los items
    inventario = Factory.loadInventory()

    # Creo todos los Models
    db.create_all()

    # Poblamos la Base de datos introduciendo los datos
    for item in inventario:

        add_item = Items(
            name=item["name"], sell_in=item["sell_in"], quality=item["quality"]
        )

        db.session.add(add_item)
        db.session.commit()


@click.command("init-db")
@with_appcontext
def init_db_command():
    """Comando para la linea de comandos
    llamado init-db que invoca a la función init_db"""
    init_db()
    # Mensaje para cuando se ejecute init-db
    click.echo("Base de datos inicializada en MySQL")


def init_app(app):
    # close_db se invoca tras cada request
    app.teardown_appcontext(close_db)
    # Llamamos al método init_db_command()
    app.cli.add_command(init_db_command)
