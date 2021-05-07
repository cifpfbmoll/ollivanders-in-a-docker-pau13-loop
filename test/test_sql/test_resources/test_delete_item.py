import pytest

import json

inventory_without_Conjured = [
    {"name": "+5 Dexterity Vest", "quality": 20, "sell_in": 10},
    {"name": "Aged Brie", "quality": 0, "sell_in": 2},
    {"name": "Elixir of the Mongoose", "quality": 7, "sell_in": 5},
    {"name": "Sulfuras Hand of Ragnaros", "quality": 80, "sell_in": 0},
    {"name": "Sulfuras Hand of Ragnaros", "quality": 80, "sell_in": -1},
    {"name": "Backstage passes to a TAFKAL80ETC concert", "quality": 20, "sell_in": 15},
    {"name": "Backstage passes to a TAFKAL80ETC concert", "quality": 49, "sell_in": 10},
    {"name": "Backstage passes to a TAFKAL80ETC concert", "quality": 49, "sell_in": 5},
]



@pytest.mark.resource_test
def test_delete_item(client):
    """Test the DELETE request of Items resource, test if since a request it can delete an item

    Args:
        client (test_client Flask): It's the test_client() object from APP Flask
    """

    response_delete = client.delete(
        "/items?name=Conjured%20Mana%20Cake&sell_in=3&quality=6"
    )


    # Debido a que el HTTP DELETE no retorna ninguna respuesta por defecto, lo mejor es simplemente verificar si el contenido de la Response si está vacía mediante b"" // b = significa byte. Para Transformar el string en Bytes
    assert b"" in response_delete.data
    assert response_delete.status_code == 204

    # Check if the item was deleted
    check_response_items = client.get("/inventory")

    assert json.loads(check_response_items.data) == inventory_without_Conjured
    assert check_response_items.status_code == 200
