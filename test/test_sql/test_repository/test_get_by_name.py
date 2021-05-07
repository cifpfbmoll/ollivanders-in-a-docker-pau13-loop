import json
import pytest

from service.service_sql.service import Service

from repository.repository_sql.models.items import Items


@pytest.mark.db_test
@pytest.mark.db_filter_by_name
def test_get_by_name_db(session):
    """Test if through session we can get an item by its name

    Args:
        session (SQLAlchemy Object Session): It's the session object from SQLALchemy Instance
    """

    # Añadimos el item
    add_item = Items("Conjured Mana Cake", 5, 8)

    session.add(add_item)
    session.commit()

    # Get el item por su nombre, en este caso como solo hay un item de esa calidad, retornará el del conjured mana cake
    get_conjured_by_name = (
        session.query(Items).filter(Items.name == "Conjured Mana Cake").first()
    )

    assert get_conjured_by_name.name == "Conjured Mana Cake"
    assert get_conjured_by_name.sell_in == 5
    assert get_conjured_by_name.quality == 8