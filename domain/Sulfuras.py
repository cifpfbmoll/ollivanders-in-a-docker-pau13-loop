from domain.normal_item import NormalItem


class Sulfuras(NormalItem):
    def __init__(self, name="", sell_in=0, quality=80):

        super().__init__(name, sell_in, quality)
        self.legendary = True

    def is_legendary(self):
        return self.legendary

    def set_legendary(self, legendary):
        self.legendary = legendary

    def update_quality(self):

        assert (
            self.get_quality() == 80
        ), f"The Quality of {self.__class__.__name__} is different of 80"
        pass
