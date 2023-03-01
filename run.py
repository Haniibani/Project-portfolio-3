from classes.Deck import Deck
from classes.Players import Players
from time import sleep
import sys

def animate_text(text):
    """
    Function to animate the text as a typewriter.
    """
    for i in text:
        print(i ,end="")
        sys.stdout.flush()
        sleep(0.1)

def main():
    """
    Run all program functions
    """
    pokerhands = []
    deck = Deck()
    deck.shuffle()
    number_of_players = int(input('How many players (1-7)? ',))

    for index in range(number_of_players):
        players = Players(deck.deal())
        pokerhands.append({**players.best_hand(), 'players_nr': index})

    sorted_hands = sorted(
    pokerhands,
    key=lambda hand: (-hand['rank'], -hand['highest_rank'])
    )

    for players in sorted_hands:
        print(
        f' players: {players["players_nr"] + 1}: {players["hand_str"]} =',
        *players["hand"])

animate_text("Welcome to Hannas Poker!\n")
main()
