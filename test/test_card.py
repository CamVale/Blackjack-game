import unittest
from src.card import Card

class CardTestCase(unittest.TestCase):
    
    def test_card_creation(self):
        card = Card('Ace', 'Hearts')
        self.assertEqual(card.rank, 'Ace')
        self.assertEqual(card.suit, 'Hearts')
        self.assertEqual(str(card), "Ace of Hearts")

    def test_card_value(self):
        card = Card('King', 'Spades')
        self.assertEqual(card.value(), 10)

        card = Card('7', 'Diamonds')
        self.assertEqual(card.value(), 7)

        card = Card('Ace', 'Clubs')
        self.assertEqual(card.value(), 11)

if __name__ == '__main__':
    unittest.main()