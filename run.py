from classes.Deck import Deck
from classes.Players import Players

def main():
    """
    Run all program functions
    """
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