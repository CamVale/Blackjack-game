from .hand import Hand


class Player:

    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def hit(self, deck):
        self.hand.add_card(deck.deal())
        self.hand.score_hand()

    def stand(self):
        self.hand.score_hand()

    def __str__(self):
        return (
            f"Player: {self.name}. Hand: {self.hand}. Score: {self.hand.player_score}"
        )
