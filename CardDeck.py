class CardDeck:
    def __init__(self):
        self.ranks = [i for i in range(2, 14)] + [i for i in "JQKA"]
        self.suits = ["Spades", "Heart", "Diamond", "Club"]
        self.cards = [
            f"{suit} {rank}" for suit in self.suits for rank in self.ranks]
    

