import random
from .Cards import Card
from constants.suits import suits
from constants.ranks import ranks


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks.keys():
                card = Card(rank, suit)
                self.deck.append(card)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        deal_cards = []
        if len(self.deck) == 0:
            return None
        else:
            for i in range(7):
                deal_cards.append(self.deck.pop(0))
            return deal_cards
