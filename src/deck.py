from .card import Card
import random


class Deck:
    def __init__(self):

        possible_suits = ["Clubs", "Spades", "Diamonds", "Hearts"]

        possible_ranks = [
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "Jack",
            "Queen",
            "King",
            "Ace",
        ]

        self.cards = [
            Card(rank, suit) for rank in possible_ranks for suit in possible_suits
        ]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop() if self.cards else None
