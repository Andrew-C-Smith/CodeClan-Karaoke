class Guest:
    def __init__(self, name, fav_song, cash):
        self.name = name
        self.fav_song = fav_song
        self.cash = cash
        # self.age = age

    def reduce_cash(self, cash_reduction):
        self.cash -= cash_reduction
