from .Poker import Poker


class Players(Poker):
    def __init__(self, hand):
        super().__init__(hand)

    def best_hand(self):
        royal_straight_flush = self.royal_straight_flush()
        if royal_straight_flush:
            return {
                "hand": royal_straight_flush,
                "rank": 10,
                "hand_str": "Royal straight flush",
                "highest_rank":
                self.high_card(royal_straight_flush).value_rank
            }

        straight_flush = self.straight_flush()
        if straight_flush:
            return {
                "hand": straight_flush,
                "rank": 9,
                "hand_str": "Straight flush",
                "highest_rank": self.high_card(straight_flush).value_rank
            }

        four_of_kind = self.four_of_kind()
        if four_of_kind:
            return {
                "hand": four_of_kind,
                "rank": 8,
                "hand_str": "Four of a kind",
                "highest_rank": self.high_card(four_of_kind).value_rank
            }

        full_house = self.full_house()
        if full_house:
            return {
                "hand": full_house,
                "rank": 7,
                "hand_str": "Full house",
                "highest_rank": self.high_card(full_house).value_rank
            }

        flush = self.flush()
        if flush:
            return {
                "hand": flush,
                "rank": 6,
                "hand_str": "Flush",
                "highest_rank": self.high_card(flush).value_rank
            }

        straight = self.straight()
        if straight:
            return {
                "hand": straight,
                "rank": 5,
                "hand_str": "Straight",
                "highest_rank": self.high_card(straight).value_rank
            }

        three_of_kind = self.three_of_kind()
        if three_of_kind:
            return {
                "hand": three_of_kind,
                "rank": 4,
                "hand_str": "Three of a kind",
                "highest_rank": self.high_card(three_of_kind).value_rank
            }

        two_pair = self.two_pair()
        if two_pair:
            return {
                "hand": two_pair,
                "rank": 3,
                "hand_str": "Two pair",
                "highest_rank": self.high_card(two_pair).value_rank
            }

        pair = self.pair()
        if pair:
            return {
                "hand": pair,
                "rank": 2,
                "hand_str": "Pair",
                "highest_rank": self.high_card(pair).value_rank
            }

        high_card = self.high_card()
        if high_card:
            return {
              "hand": [high_card],
              "rank": 1,
              "hand_str": "High card",
              "highest_rank": high_card.value_rank
            }
