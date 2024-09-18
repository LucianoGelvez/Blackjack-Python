import unittest
from clases.deck import Deck
from clases.card import Card

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_deck_creation(self):
        self.assertEqual(len(self.deck.deck, 52))

    def suffle(self):
        original_order = self.deck.deck.copy()
        self.deck.shuffle()
        self.assertNotEqual(original_order, self.deck.deck)

    def test_deal(self):
        card = self.deck.deal()
        self.assertIsInstance(card, Card)
        self.assertEqual(len(self.deck.deck), 51)

if __name__ == '__main__':
    unittest.main()
