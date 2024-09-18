import unittest

# Import test modules
from test_card import TestCard
from test_deck import TestDeck
from test_hand import TestHand
from test_chips import TestChips

def suite():
    test_suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    test_suite.addTests(loader.loadTestsFromTestCase(TestCard))
    test_suite.addTests(loader.loadTestsFromTestCase(TestDeck))
    test_suite.addTests(loader.loadTestsFromTestCase(TestHand))
    test_suite.addTests(loader.loadTestsFromTestCase(TestChips))
    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())