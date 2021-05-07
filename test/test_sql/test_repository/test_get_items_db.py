import json
import pytest

from service.service_sql.service import Service

from repository.repository_sql.models.items import Items


@pytest.mark.db_test
def test_get_items_db(session):
    """Test if through session we can get all items

    Args:
        session (SQLAlchemy Object Session): It's the session object from SQLALchemy Instance
    """

    add_item = Items("Conjured Mana Cake", 5, 8)

    session.add(add_item)
    session.commit()

    # Funciona, pero al parecer no carga los datos que ya están en la base de datos, por lo cual no tiene ninguno, lo que implica que tengo que agregar un nuevo objeto/row
    items_db = [item for item in session.query(Items).all()]

    assert len(items_db) == 1