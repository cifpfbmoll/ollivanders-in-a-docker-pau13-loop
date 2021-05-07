class AgedBrie:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_sell_in(self):
        return self.sell_in

    def set_sell_in(self, sell_in):
        self.sell_in = sell_in
        self.sell_in -= 1

    def get_quality(self):
        return self.quality

    def set_quality(self, value):

        if self.quality + value > 50:
            self.quality = 50
        else:
            self.quality += value
        assert (
            0 <= self.quality <= 50
        ), f"The quality of {self.__class__.__name__} overcome the maximun quality"

    def update_quality(self):

        if self.sell_in > 0:
            self.set_quality(1)
        else:
            self.set_quality(2)
        self.set_sell_in(self.get_sell_in())

    def __str__(self):
        return (
            "***************Item*************** \n Name: %s,\n Sell in: %d,\n Quality: %d"
            % (self.get_name(), self.get_sell_in(), self.get_quality())
        )
