import random
from .Cards import Card
from constants.suits import suits
from constants.ranks import ranks


class Deck:
    def __init__(self):
        self.deck = []
        # loop over each suit
        for suit in suits:
            # loop over each rank
            for rank in ranks.keys():
                # create a Card instance with the current rank and suit
                card = Card(rank, suit)
                # add the Card instance to the deck list
                self.deck.append(card)

    def shuffle(self):
        random.shuffle(self.deck)  # shuffle the deck

    def deal(self):
        deal_cards = []  # initialize empty list to hold dealt cards
        if len(self.deck) == 0:  # check if deck is empty
            return None  # if deck is empty, return None
        else:
            for i in range(7):  # deal 7 cards
                # remove card from top of deck and add to deal_cards list
                deal_cards.append(self.deck.pop(0))
            return deal_cards  # return list of dealt cards
