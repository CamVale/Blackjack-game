import unittest
from src.deck import Deck
from src.card import Card


class DeckTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.deck = Deck()

    def tearDown(self):  # this method will be run after each test
        pass

    def test_number_of_cards(self):  # any method beginning with 'test_' will be run by unittest
        number_of_cards = len(self.deck.cards)
        self.assertEqual(number_of_cards, 52)

    def test_deck_contents(self):
        for card in self.deck.cards:
            self.assertIsInstance(card, Card, f"Non-card object found in deck here: {card}")

    def test_deck_contents_unique(self):
        unique_cards = set()
        for card in self.deck.cards:
            self.assertNotIn((card.rank, card.suit), unique_cards, f"Duplicate found here: {card.rank} of {card.suit}")
            unique_cards.add((card.rank, card.suit))
        self.assertEqual(len(unique_cards), 52, f"Deck does not contain 52 unique cards")

    def test_deck_shuffle(self):
        deck = Deck()
        initial_order_copy = deck.cards.copy()
        deck.shuffle()
        self.assertNotEqual(deck.cards, initial_order_copy)

    def test_deal_card(self):
        deck = Deck()
        initial_count = len(deck.cards)
        card = deck.deal()
        self.assertEqual(len(deck.cards), initial_count - 1) 
        self.assertIsInstance(card, Card)


if __name__ == '__main__':
    unittest.main()
