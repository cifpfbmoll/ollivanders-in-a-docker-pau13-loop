from domain.normal_item import NormalItem


class Conjured(NormalItem):
    def __init__(self, name="", sell_in=0, quality=50):
        super().__init__(name, sell_in, quality)

    def update_quality(self):

        if self.get_sell_in() >= 0:
            self.set_quality(-2)
        else:
            self.set_quality(-4)

        self.set_sell_in(self.get_sell_in())
