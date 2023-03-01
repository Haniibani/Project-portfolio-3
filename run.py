from classes.Deck import Deck
from classes.Players import Players
from time import sleep
import sys
from termcolor import colored

def animate_text(text):
  for i in text:
    print(i ,end="")
    sys.stdout.flush()
    sleep(0.1)

def main():
  pokerhands = []
  deck = Deck()
  deck.shuffle()
  number_of_players = int(input(colored(' How many players (1-7)? ', 'light_blue')))

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

  play_again = input(colored('Wanna play again? y/n: ', 'magenta'))
  if play_again == "y":
    main()
  else:
    animate_text(colored("Thanks for playing", "blue"))

animate_text(colored("Welcome to Hannas Poker!\n", "magenta"))
main()