import json
import pytest

from service.service_sql.service import Service

from repository.repository_sql.models.items import Items

from repository.repository_sql.repo import Factory


@pytest.mark.db_test
@pytest.mark.update_quality_db
def test_udpate_quality_items_db(session):
    """Test if through session we can update the quality of all items

    Args:
        session (SQLAlchemy Object Session): It's the session object from SQLALchemy Instance
    """

    # Añadimos el item
    add_item = Items("Conjured Mana Cake", 5, 8)

    session.add(add_item)
    session.commit()

    for item in session.query(Items).all():

        # Creamos el objeto Item a partir de la info de la Lista que insertamos en los párametros del método: createObjectItem()
        itemObject = Factory.createObjectItem([item.name, item.sell_in, item.quality])

        # Actualizamos la calidad del item
        itemObject.update_quality()

        # Actualizamos los datos de cada item
        item.sell_in = itemObject.get_sell_in()
        item.quality = itemObject.get_quality()
        # Guardamos los datos actualizados
        session.commit()

        # Testeamos si efectivamente se actualizo el item
        assert item.name == "Conjured Mana Cake"
        assert item.sell_in == 4
        assert item.quality == 6