import json
import pytest

from service.service_sql.service import Service

from repository.repository_sql.models.items import Items


@pytest.mark.db_test
@pytest.mark.delete_item_db
def test_delete_item_db(session):
    """Test if through session we can delete an item

    Args:
        session (SQLAlchemy Object Session): It's the session object from SQLALchemy Instance
    """

    # Añadimos el item
    add_item = Items("Conjured Mana Cake", 5, 8)

    session.add(add_item)
    session.commit()

    # Ahora lo eliminamos
    session.query(Items).filter(
        Items.name == "Conjured Mana Cake", Items.sell_in == 5, Items.quality == 8
    ).delete()
    session.commit()

    # Verificamos si efectivamente lo ha eliminado si ningún row es igual al que eliminamos, CAMBIARLO y REFACTORIZARLO
    for item in session.query(Items).all():

        assert item.name != "Conjured Mana Cake"
        assert item.sell_in != 5
        assert item.quality != 8