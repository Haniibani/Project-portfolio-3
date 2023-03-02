from classes.Deck import Deck
from classes.Players import Players
from time import sleep
import sys
from termcolor import colored


def animate_text(text):
    for i in text:
        print(i, end="")
        sys.stdout.flush()
        sleep(0.1)


def main():
    pokerhands = []
    deck = Deck()
    deck.shuffle()

    number_of_players = 0
    while number_of_players not in range(1, 8):
        number_of_players = int(input("Please enter a number between 1 and 7: "))
        if number_of_players not in range(1, 8):
            print(colored("Not a valid number", "red"))

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
            *players["hand"]
        )

    while True:
        play_again = input(colored('Wanna play again? y/n: ', 'magenta'))
        if play_again in ["y", "Y"]:
            main()
        elif play_again in ["n", "N"]:
            animate_text(colored("Thanks for playing", "blue"))
            sys.exit()  # Exit the program if the user enters "n" or "N"
        else:
            print(colored("Please answer y or n\n", "blue"))


animate_text(colored("Welcome to Hannas Poker!\n", "magenta"))
main()
