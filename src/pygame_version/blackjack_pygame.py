import pygame
import sys
import os
from src.deck import Deck
from src.player import Player
from .constants import *


pygame.init()

# all caps to indicate they are global constants

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BBC Blackjack!")


# font constructor, giving it a font and size to use

font = pygame.font.Font(None, 36)

card_images = {}


def load_images():

    base_path = os.path.dirname(__file__)

    for rank in RANKS:
        for suit in SUITS:
            image_path = os.path.join(base_path, f"assets/cards/{rank} of {suit}.png")
            card_images[f"{rank} of {suit}"] = pygame.transform.scale(
                pygame.image.load(image_path), (80, 120)
            )
            card_back = pygame.transform.scale(
                pygame.image.load(os.path.join(base_path, "back.png")), (80, 120)
            )
    return card_back


card_back_image = load_images()


def show_text(text, x, y, colour):
    text = font.render(text, True, colour)
    screen.blit(text, (x, y))


def show_cards(player, x, y, first_turn=False, is_dealer=False):

    player.hand.score_hand()

    for i, card in enumerate(player.hand.cards_in_hand):
        if i == 0 and is_dealer and first_turn:
            screen.blit(card_back_image, (x + i * 30, y))
        else:
            current_image = card_images[str(card).lower()]
            screen.blit(current_image, (x + i * 30, y))


def player_name_input():

    name = ""

    active = True

    while active:
        screen.fill(GREEN)
        show_text("Please enter your name: " + name, 50, 250, BLACK)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_RETURN:
                    active = False
                else:
                    name += event.unicode
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    return name


def game_loop():

    player_name = player_name_input()
    player_points = 0
    dealer_points = 0

    while True:

        game_deck = Deck()
        game_deck.shuffle()
        player = Player(player_name)
        dealer = Player("Dealer")
        first_turn = True
        round_result = False
        winning_message = ""

        player.hit(game_deck)
        player.hit(game_deck)
        dealer.hit(game_deck)
        dealer.hit(game_deck)

        round_running = True
        while round_running:

            screen.fill(GREEN)
            show_text(f"{player_name}'s hand: ", 50, 400, BLACK)
            show_cards(player, 50, 450)
            show_text(f"Score: {player.hand.player_score}", 50, 370, BLACK)

            show_text("Dealer's hand: ", 50, 50, WHITE)
            if first_turn:
                show_cards(dealer, 50, 100, True, True)
                show_text(
                    f"Score: {dealer.hand.cards_in_hand[1].value()}", 50, 70, WHITE
                )
            else:
                show_cards(dealer, 50, 100, False, True)
                show_text(f"Score: {dealer.hand.player_score}", 50, 70, WHITE)

            hit_button = pygame.Rect(600, 250, 100, 50)
            stand_button = pygame.Rect(600, 350, 100, 50)
            play_again_button = pygame.Rect(300, 500, 200, 50)

            pygame.draw.rect(screen, WHITE, hit_button, border_radius=10)
            pygame.draw.rect(screen, WHITE, stand_button, border_radius=10)
            show_text("HIT", 630, 260, BLACK)
            show_text("STAND", 610, 360, BLACK)

            if round_result:
                show_text(winning_message, 300, 300, BLACK)
                show_text(f"{player_name} points: {player_points}", 300, 350, BLACK)
                show_text(f"Dealer points: {dealer_points}", 300, 375, WHITE)
                pygame.draw.rect(screen, WHITE, play_again_button, border_radius=10)
                show_text("Play again?", 325, 515, BLACK)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (
                        hit_button.collidepoint(event.pos)
                        and first_turn
                        and not round_result
                    ):
                        player.hit(game_deck)
                        if player.hand.check_bust():
                            round_result = True
                            winning_message = "You went bust! Dealer wins."
                            dealer_points += 1
                            first_turn = False
                    if (
                        stand_button.collidepoint(event.pos)
                        and first_turn
                        and not round_result
                    ):
                        player.stand()
                        first_turn = False

                        while dealer.hand.player_score < 17:
                            dealer.hit(game_deck)
                        round_result = True

                        if (
                            dealer.hand.check_bust()
                            or dealer.hand.player_score < player.hand.player_score
                        ):
                            winning_message = f"{player_name} wins the round!"
                            player_points += 1
                        elif dealer.hand.player_score > player.hand.player_score:
                            winning_message = f"Dealer wins the round! Better luck next time, {player_name}."
                            dealer_points += 1
                        else:
                            winning_message = "It's a tie! 1 point to everyone"
                            player_points += 1
                            dealer_points += 1
                    elif play_again_button.collidepoint(event.pos) and round_result:
                        round_running = False

            pygame.display.update()
            pygame.display.flip()


if __name__ == "__main__":
    game_loop()
