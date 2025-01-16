# Creating the Card class to populate the Deck which will add more functionality
class Card:
    """
    Initialises a card with two properties from the arguments: a rank (the number or face on the card), and a suit (the category of the card e.g. Spades, Hearts)
    """

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    # Returns the card's value in the game

    def value(self):
        if self.rank in ["Jack", "Queen", "King"]:
            return 10
        if self.rank == "Ace":
            return 11
        return int(self.rank)

    # Defines how the class is represented when str()/print() is called on it

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    # Defines how the class is represented when logging/debugging, providing detail for debugging

    def __repr__(self):
        return f"Card(rank='{self.rank}', suit='{self.suit}')"
