import unittest
from src.player import Player
from src.deck import Deck
from src.card import Card


class PlayerTestCase(unittest.TestCase):

    def setUp(self):
        self.test_player = Player("Test")
        self.test_deck = Deck()

    def test_player_setup(self):
        self.assertEqual(self.test_player.name, "Test")
        self.assertEqual(len(self.test_player.hand.cards_in_hand), 0)

    def test_hit(self):
        self.test_player.hit(self.test_deck)
        self.assertEqual(len(self.test_player.hand.cards_in_hand), 1)
        self.assertEqual(len(self.test_deck.cards), 51)

    def test_stand(self):
        self.test_player.hand.add_card(Card('Queen', 'Hearts'))
        self.test_player.stand()
        self.assertEqual(self.test_player.hand.player_score, 10)

