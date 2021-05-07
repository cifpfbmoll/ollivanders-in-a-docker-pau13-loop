import json
import pytest

from service.service_sql.service import Service

from repository.repository_sql.models.items import Items



@pytest.mark.db_test
@pytest.mark.db_filter_by_sell_in
def test_get_by_sellin_db(session):
    """Test if through session we can get an item by its sell_in

    Args:
        session (SQLAlchemy Object Session): It's the session object from SQLALchemy Instance
    """

    # Añadimos el item
    add_item = Items("Conjured Mana Cake", 5, 8)

    session.add(add_item)
    session.commit()

    # Get el item por su sell_in, en este caso como solo hay un item de esa calidad, retornará el del conjured mana cake
    get_conjured_by_sellin = session.query(Items).filter(Items.sell_in == 5).first()

    assert get_conjured_by_sellin.name == "Conjured Mana Cake"
    assert get_conjured_by_sellin.sell_in == 5
    assert get_conjured_by_sellin.quality == 8
