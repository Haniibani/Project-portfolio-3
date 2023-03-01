from constants.ranks import ranks

class Poker: #Defining the diffferent hands in the poker game.
    def __init__(self, hand):
        self.sorted_hands = sorted(hand, reverse=True)

    def royal_straight_flush(self):
        if self.sorted_hands[0].value_rank == ranks['A']:
            if self.sorted_hands[4].value_rank == ranks['10']:
                if self.sorted_hands[0].suit == self.sorted_hands[1].suit \
                  == self.sorted_hands[2].suit == self.sorted_hands[3].suit \
                  == self.sorted_hands[4].suit:
                    return self.sorted_hands[:5]
        pass

    def straight_flush(self):
        for i in range(3):
            if self.sorted_hands[i].value_rank \
                  == self.sorted_hands[i + 1].value_rank - 1 \
                  == self.sorted_hands[i + 2].value_rank - 2 \
                  == self.sorted_hands[i + 3].value_rank - 3 \
                  == self.sorted_hands[i + 4].value_rank - 4 \
                  and self.sorted_hands[i].suit \
                  == self.sorted_hands[i + 1].suit \
                  == self.sorted_hands[i + 2].suit \
                  == self.sorted_hands[i + 3].suit \
                  == self.sorted_hands[i + 4].suit:
                return [self.sorted_hands[i + j] for j in range(5)]
        pass

    def four_of_kind(self):
        for i in range(4):
            if self.sorted_hands[i] \
                  == self.sorted_hands[i + 1] \
                  == self.sorted_hands[i + 2] \
                  == self.sorted_hands[i + 3]:
                return [self.sorted_hands[i + j] for j in range(4)]
        pass

    def full_house(self):
        for i in range(5):
            if self.sorted_hands[i] \
               == self.sorted_hands[i + 1] \
               == self.sorted_hands[i + 2]:
                trips_card = [self.sorted_hands[i + j] for j in range(3)]
                for k in range(6):
                    if self.sorted_hands[k] not in trips_card:
                        if self.sorted_hands[k] == self.sorted_hands[i + 1]:
                            return [
                              self.sorted_hands[k + j] for j in range(2)
                            ].extend(trips_card)
        pass

    def flush(self):
        for i in range(3):
            if self.sorted_hands[i].suit \
              == self.sorted_hands[i + 1].suit \
              == self.sorted_hands[i + 2].suit \
              == self.sorted_hands[i + 3].suit \
              == self.sorted_hands[i + 4].suit:
                return [self.sorted_hands[i + j] for j in range(5)]
        pass

    def straight(self):
        for i in range(3):
            if self.sorted_hands[i].value_rank \
              == self.sorted_hands[i + 1].value_rank - 1 \
              == self.sorted_hands[i + 2].value_rank - 2 \
              == self.sorted_hands[i + 3].value_rank - 3 \
              == self.sorted_hands[i + 4].value_rank - 4:
                return [self.sorted_hands[i + j] for j in range(5)]
        pass

    def three_of_kind(self):
        three_of_kinds = []
        for i in range(5):
            if self.sorted_hands[i] \
              == self.sorted_hands[i + 1] \
              == self.sorted_hands[i + 2]:
                three_of_kinds.extend([self.sorted_hands[i + j] for j in range(3)])
        if len(three_of_kinds) > 0:
            return sorted(three_of_kinds, reverse=True)[:3]
        pass

    def two_pair(self):
        pair = []
        for i in range(6):
            if self.sorted_hands[i] \
              == self.sorted_hands[i + 1]:
                pair.extend([self.sorted_hands[i + j] for j in range(2)])
        if len(pair) == 4:
            return sorted(pair, reverse=True)[:4]
        pass

    def pair(self):
        for i in range(6):
            if self.sorted_hands[i] \
              == self.sorted_hands[i + 1]:
                return [self.sorted_hands[i + j] for j in range(2)]
        pass

    def high_card(self, card=None):
        if card:
            return sorted(card, reverse=True)[0]
        return self.sorted_hands[0]
