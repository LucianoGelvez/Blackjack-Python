import unittest
from clases.chip import Chips

class TestChips(unittest.TestCase):
    def setUp(self):
        self.chips = Chips()

    def test_initial_balance(self):
        self.assertEqual(self.chips.total, 100)

    def test_win_bet(self):
        self.chips.bet = 20
        self.chips.win_bet()
        self.assertEqual(self.chips.total, 120)

    def test_lose_bet(self):
        self.chips.bet = 30
        self.chips.lose_bet()
        self.assertEqual(self.chips.total, 70)

if __name__ == '__main__':
    unittest.main()