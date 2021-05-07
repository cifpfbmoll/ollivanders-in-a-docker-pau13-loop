class Inventory:
    def __init__(self):

        self.items = []

    def get_items(self):

        return self.items

    def add_items(self, items):

        assert isinstance(items, list) == True

        for item in items:
            self.items.append(item)

    def update_quality_items(self):

        for item in self.items:

            item.update_quality()

    def __str__(self):

        items_seccion = ""
        for item in self.items:
            items_seccion += item.__str__() + " \n "

        return items_seccion
