import json
import pytest

from service.service_sql.service import Service

from repository.repository_sql.models.items import Items

@pytest.mark.db_test
@pytest.mark.add_item_db
def test_add_item_db(session):
    """Test if through session we can add an item

    Args:
        session (SQLAlchemy Object Session): It's the session object from SQLALchemy Instance
    """

    add_item = Items("Conjured Mana Cake", 5, 8)

    session.add(add_item)
    session.commit()

    assert add_item.name == "Conjured Mana Cake"
    assert add_item.sell_in == 5
    assert add_item.quality == 8