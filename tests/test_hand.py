import unittest
from clases.card import Card
from clases.hand import Hand

class TestHand(unittest.TestCase):
    def setUp(self):
                self.hand = Hand()

    def test_add_card(self):
        card = Card('Hearts', 'Ace')
        self.hand.add_card(card)
        self.assertEqual(len(self.hand.cards), 1)
        self.assertEqual(self.hand.value, 11)
        self.assertEqual(self.hand.aces, 1)

    def test_adjust_for_ace(self):
        self.hand.add_card(Card('Hearts', 'Ace'))
        self.hand.add_card(Card('Spades', 'King'))
        self.hand.adjust_for_ace()
        self.assertEqual(self.hand.value, 21)

if __name__ == '__main__':
    unittest.main()