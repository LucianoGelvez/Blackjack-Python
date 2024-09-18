import unittest
from clases.card import Card

class TestCard(unittest.TestCase):
    def test_card_creation(self):
        card = Card("Hearts", "Ace")
        self.assertEqual(card.suit, "Hearts")
        self.assertEqual(card.rank, "Ace")

    def test_card_string_representation(self):
        card = Card('Spades', 'King')
        self.assertEqual(str(card), 'King de Spades')

if __name__ == "__main__":
    unittest.main()