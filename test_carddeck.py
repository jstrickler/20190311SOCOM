#!/usr/bin/env python
import unittest
import sys
from carddeck import CardDeck

class TestCardDeck(unittest.TestCase):

    @classmethod
    def setUpclass(cls):
        pass


    def setUp(self):
        self.d = CardDeck("TEST USER")

    def test_deck_has_52_cards(self):
        self.assertEqual(len(self.d), 52, "Deck did not have 52 cards")

    def test_empty_deck_raises_error(self):
        for i in range(52):
            self.d.draw()

        with self.assertRaises(ValueError):
            self.d.draw()

    @unittest.skipUnless(sys.platform == 'win32', "Only implemented on Windows")
    def test_shuffling_preserves_cards(self):
        old_cards = list(self.d.cards)
        self.d.shuffle()
        new_cards = self.d.cards
        assert(set(old_cards) == set(new_cards))


if __name__ == '__main__':
    unittest.main(verbosity=11)
