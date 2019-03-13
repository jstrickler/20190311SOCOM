#!/usr/bin/env python

class CardDeck():
    SUITS = 'C D H S'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self, dealer):
        self.dealer = dealer
        self._create_deck()

    def _create_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = (rank, suit)
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards


    @property
    def dealer(self):
        return self._dealer

    @dealer.setter
    def dealer(self, dealer):
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")

    @classmethod
    def get_ranks(cls):
        return cls.RANKS

if __name__ == '__main__':
    d1 = CardDeck("Bob")
    print(d1.dealer)
    d1.dealer = 'Frank'
    print(d1.dealer)
    try:
        d1.dealer = 37
    except TypeError as err:
        print(err)
    else:
        print(d1.dealer)

    print(d1.cards)
    print(d1.get_ranks())

    print(CardDeck.get_ranks())
