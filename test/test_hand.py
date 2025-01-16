import unittest
from src.hand import Hand
from src.card import Card

class HandTestCase(unittest.TestCase):

    def test_hand_setup(self):
        test_hand = Hand()
        self.assertEqual(len(test_hand.cards_in_hand), 0)
        self.assertEqual(test_hand.player_score, 0)
    
    def test_add_card(self):
        test_hand = Hand()
        test_card = Card('Ace', 'Hearts')
        test_hand.add_card(test_card)
        self.assertIsInstance(test_hand.cards_in_hand[0], Card)
        self.assertEqual(len(test_hand.cards_in_hand), 1)
        self.assertIn(test_card, test_hand.cards_in_hand)

    def test_score_hand(self):
        test_hand = Hand()
        test_card_1, test_card_2, test_card_3 = Card('2', 'Hearts'), Card('King', 'Spades'), Card('Ace', 'Spades')
        test_hand.add_card(test_card_1)
        test_hand.add_card(test_card_2)
        test_hand.score_hand()
        self.assertEqual(test_hand.player_score, 12)
        test_hand.add_card(test_card_3)
        test_hand.score_hand()
        self.assertEqual(test_hand.player_score, 13)
    
    def test_check_bust(self):
        test_hand = Hand()
        test_card_1, test_card_2, test_card_3, test_card_4 = Card('3', 'Hearts'), Card('King', 'Spades'), Card('2', 'Hearts'), Card('9', 'Hearts')
        test_hand.add_card(test_card_1)
        test_hand.add_card(test_card_2)
        test_hand.add_card(test_card_3)
        test_hand.score_hand()
        self.assertFalse(test_hand.check_bust())
        test_hand.add_card(test_card_4)
        test_hand.score_hand()
        self.assertTrue(test_hand.check_bust())

if __name__ == '__main__':
    unittest.main()
