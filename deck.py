import random
from card import Card

class Deck:

    def __init__(self, shuffled=False):
        """
        Initializes a Deck object.  If shuffled is set, it will initialize in a random order.

        :param: shuffled (bool): If true, deck will be initialized in a random order, else 2-A in each suit
        """
        self.deck = []
        for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for i in range(2, 11):
                self.deck.append(Card(i, suit))
            for face in ["J", "Q", "K", "A"]:
                self.deck.append(Card(face, suit))
        
        if shuffled:
            self.shuffle()
    
    def shuffle(self):
        """
        Shuffles the deck in-place
        """
        random.shuffle(self.deck)

    def next_card(self):
        """
        Gets the next card in the deck (i.e. at the end of the list)

        :returns: str-representation of the card at the end of the deck
        """
        return self.deck[-1].__repr__()
    
    def discard_top(self):
        """
        Discards the top card at the deck (i.e. at the end of the list)
        """
        self.deck = self.deck[:-1]
    
    def print_deck(self):
        """
        Helper function to print a string representation of the deck
        """
        for card in self.deck:
            print(card.__str__())
    
    def length(self):
        return len(self.deck)

