from .player import Player
from .deck import Deck


def play_blackjack_round(player_name):

    # Initialise the game with a new Deck, creating the Dealer player, and dealing 2 cards to both

    # need to shuffle the deck

    game_deck = Deck()
    game_deck.shuffle()
    player = Player(player_name)
    dealer = Player("Dealer")

    player.hit(game_deck)
    player.hit(game_deck)
    dealer.hit(game_deck)
    dealer.hit(game_deck)

    # Show player their starting hand

    player.hand.score_hand()
    dealer.hand.score_hand()
    print(f"Your hand: {str(player.hand)}. {player.hand.player_score} points.\n")
    print(
        f"Dealer's face-up card: {dealer.hand.cards_in_hand[0]}, worth {dealer.hand.cards_in_hand[0].value()} points.\n"
    )

    while True:
        player_input = input(f"{player.name}, enter 1 to HIT, or 2 to STAND.\n")
        if player_input == "1":
            player.hit(game_deck)
            print(
                f"You are dealt a card. Your hand: {str(player.hand)}. {player.hand.player_score} points.\n"
            )
            if player.hand.check_bust():
                print("Bust! Dealer wins :( Better luck next time.\n")
                return False
        elif player_input == "2":
            print(
                f"You chose to stand. Your score remains at {player.hand.player_score}\n"
            )
            break
        else:
            print("Invalid input. Enter 1 to HIT or 2 to STAND.\n")

    print(
        f"Dealer's turn...\n\nDealer reveals their face-down card, their hand: {str(dealer.hand)}. {dealer.hand.player_score} points.\n"
    )
    while dealer.hand.player_score < 17:
        print("Dealer hits.\n")
        dealer.hit(game_deck)
        print(
            f"Dealer's hand: {str(dealer.hand)}. {dealer.hand.player_score} points!\n"
        )
        if dealer.hand.check_bust():
            print("Dealer bust! You win!!!\n")
            return True

    print("Dealer stands.\n")

    if player.hand.player_score > dealer.hand.player_score:
        print("You win!\n")
        return True
    elif player.hand.player_score < dealer.hand.player_score:
        print("Dealer wins :( Better luck next time.\n")
        return False
    else:
        print("It's a tie!\n")
        return None


def play_blackjack_game():

    player_points = 0
    dealer_points = 0

    # Start game by prompting user for a name, with some constraints

    while True:
        player_name = input("Welcome to Blackjack! Enter your name: ")

        if 0 < len(player_name) < 50:
            print(f"Ok {player_name}, let's play!")
            break
        else:
            print("Name must be between 1 and 50 characters. Try again.")

    while True:

        result = play_blackjack_round(player_name)

        if result == None:
            player_points += 1
            dealer_points += 1
        elif result:
            player_points += 1
        else:
            dealer_points += 1

        while True:
            replay = input(
                "\nWould you like to play again? Enter 1 to play or 2 to end the game.\n"
            )
            if replay == "1":
                print(
                    f"Starting a new round! Current points - {player_name}: {player_points}. Dealer: {dealer_points}\n"
                )
                break
            elif replay == "2":
                print(
                    f"Thanks for playing, {player_name}! Final points - {player_name}: {player_points}. Dealer: {dealer_points} {'Well done!' if player_points > dealer_points else 'Better luck next time!'}"
                )
                return
            else:
                print(
                    "Invalid entry, please enter 1 to play again, or 2 to exit the game."
                )


if __name__ == "__main__":
    play_blackjack_game()
