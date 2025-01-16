class Hand:

    def __init__(self):

        self.cards_in_hand = []
        self.player_score = 0

    def add_card(self, card):

        self.cards_in_hand.append(card)

    def score_hand(self):
        score = 0
        aces = 0

        for card in self.cards_in_hand:
            if card.rank == "Ace":
                score += card.value()
                aces += 1
            else:
                score += card.value()

        while aces > 0 and score > 21:
            score -= 10
            aces -= 1

        self.player_score = score

    def check_bust(self):
        return self.player_score > 21

    def __str__(self):
        return ", ".join(str(card) for card in self.cards_in_hand)
