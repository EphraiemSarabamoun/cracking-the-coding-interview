class Deck:
    def __init__(self):
        self.cards = []
    def build(self):
        for suit in ["hearts", "diamonds", "clubs", "spades"]:
            for value in range(1, 14):
                if value <= 10:
                    value = str(value)
                elif value == 11:
                    value = "J"
                elif value == 12:
                    value = "Q"
                elif value == 13:
                    value = "K"
                self.cards.append(Card(suit, value))

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


if __name__ == "__main__":
    deck = Deck()
    deck.build()
    print(deck.cards)