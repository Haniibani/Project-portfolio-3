from constants.ranks import ranks


class Poker:
    def __init__(self, hand):
        # sort the hand in descending order based on card values
        self.sorted_hands = sorted(hand, reverse=True)

    def royal_straight_flush(self):
        # check if the highest card in the hand is an Ace
        if self.sorted_hands[0].value_rank == ranks['A']:
            # check if the hand contains the 10, J, Q, K,
            # and A of the same suit
            if self.sorted_hands[4].value_rank == ranks['10'] and \
               self.sorted_hands[0].suit == self.sorted_hands[1].suit == \
               self.sorted_hands[2].suit == self.sorted_hands[3].suit == \
               self.sorted_hands[4].suit:
                # return the five cards that make up the royal straight flush
                return self.sorted_hands[:5]
        pass

    def straight_flush(self):
        # loop through possible starting positions for a straight flush
        for i in range(3):
            # check if the next five cards form a straight
            # flush starting with this card
            if self.sorted_hands[i].value_rank \
                    == self.sorted_hands[i + 1].value_rank - 1 \
                    == self.sorted_hands[i + 2].value_rank - 2 \
                    == self.sorted_hands[i + 3].value_rank - 3 \
                    == self.sorted_hands[i + 4].value_rank - 4 and \
                    self.sorted_hands[i].suit \
                    == self.sorted_hands[i + 1].suit \
                    == self.sorted_hands[i + 2].suit \
                    == self.sorted_hands[i + 3].suit \
                    == self.sorted_hands[i + 4].suit:
                # return the five cards that make up the straight flush
                return [self.sorted_hands[i + j] for j in range(5)]
        pass

    def four_of_kind(self):
        # loop through possible starting positions for four of a kind
        for i in range(4):
            # check if the next four cards form
            # four of a kind starting with this card
            if self.sorted_hands[i] == self.sorted_hands[i + 1] == \
               self.sorted_hands[i + 2] == self.sorted_hands[i + 3]:
                # return the four cards that make up the four of a kind
                return [self.sorted_hands[i + j] for j in range(4)]
        pass

    def full_house(self):
        # loop through possible positions for
        # the three of a kind in a full house
        for i in range(5):
            if self.sorted_hands[i] \
                    == self.sorted_hands[i + 1] \
                    == self.sorted_hands[i + 2]:
                # get the three of a kind cards
                trips_card = [self.sorted_hands[i + j] for j in range(3)]
                # loop through the remaining cards to find a pair
                for k in range(6):
                    if self.sorted_hands[k] not in trips_card:
                        if self.sorted_hands[k] == self.sorted_hands[i + 1]:
                            # return the five cards that make up the full house
                            return [self.sorted_hands[k + j]
                                    for j in range(2)].extend(trips_card)
        pass

    def flush(self):
        # loop through possible starting positions for a flush
        for i in range(3):
            # check if all five cards in the same suit
            if self.sorted_hands[i].suit \
              == self.sorted_hands[i + 1].suit \
              == self.sorted_hands[i + 2].suit \
              == self.sorted_hands[i + 3].suit \
              == self.sorted_hands[i + 4].suit:
                # return the five cards that makes up the flush
                return [self.sorted_hands[i + j] for j in range(5)]
        # if no flush is found, return None
        pass

    def straight(self):
        # loop through possible starting positions for a straight
        for i in range(3):
            # check if all five cards have consecutive values
            if self.sorted_hands[i].value_rank \
              == self.sorted_hands[i + 1].value_rank - 1 \
              == self.sorted_hands[i + 2].value_rank - 2 \
              == self.sorted_hands[i + 3].value_rank - 3 \
              == self.sorted_hands[i + 4].value_rank - 4:
                # return the five cards that make up the straight
                return [self.sorted_hands[i + j] for j in range(5)]
        # if no straight is found, return None
        pass

    def three_of_kind(self):
        # loop through possible starting positions for three of a kind
        three_of_kinds = []
        # check if three cards have the same rank
        for i in range(5):
            if self.sorted_hands[i] \
              == self.sorted_hands[i + 1] \
              == self.sorted_hands[i + 2]:
                # add the three cards to the list of three of a kinds
                three_of_kinds.extend(
                    [self.sorted_hands[i + j] for j in range(3)])
        # if there are any three of a kinds, return the top three cards
        if len(three_of_kinds) > 0:
            return sorted(three_of_kinds, reverse=True)[:3]
        # if no three of a kind is found, return None
        pass

    def two_pair(self):
        # loop through possible starting positions for two pairs
        pair = []
        for i in range(6):
            # check if two cards in a row have the same rank
            if self.sorted_hands[i] \
              == self.sorted_hands[i + 1]:
                # add the two cards to the list of pairs
                pair.extend([self.sorted_hands[i + j] for j in range(2)])
        # if there are two pairs, return the top four cards
        if len(pair) == 4:
            return sorted(pair, reverse=True)[:4]
        # if no two pairs are found, return None
        pass

    def pair(self):
        # loop through possible starting positions for a pair
        for i in range(6):
            # check if two cards in a row have the same rank
            if self.sorted_hands[i] \
              == self.sorted_hands[i + 1]:
                # return the two cards that make up the pair
                return [self.sorted_hands[i + j] for j in range(2)]
        # if no pair is found, return None
        pass

    def high_card(self, card=None):
        # if no other hand is provided, return the highest card
        if card:
            return sorted(card, reverse=True)[0]
        return self.sorted_hands[0]
