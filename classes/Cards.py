from constants.ranks import ranks


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value_rank = ranks[self.rank]

    def __str__(self):
        return f'{self.suit}{self.rank}'

    def __eq__(self, other):
        return self.rank == other.rank

    def __ne__(self, other):
        return self.rank != other.rank

    def __lt__(self, other):
        return self.value_rank < other.value_rank

    def __gt__(self, other):
        return self.value_rank > other.value_rank
