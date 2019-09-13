class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def __str__(self):
        return "%s of %s" % (str(self.value), self.suit)
    
    def __repr__(self):
        if self.value == "K":
            name = "King"
            real_value = 13
        elif self.value == "Q":
            name = "Queen"
            real_value = 12
        elif self.value == "J":
            name = "Jack"
            real_value = 11
        elif self.value == "A":
            name = "Ace"
            real_value = 14
        else:
            name = str(self.value)
            real_value = int(self.value)

        card = {
            "name": name,
            "value": str(self.value),
            "real_value": real_value,
            "suit": self.suit
        }

        return card