from constants.ranks import ranks


class Card:
    """
    A class representing a standard playing card.

    Attributes:
        rank (str): The rank of the card, from 2 to A.
        suit (str): The suit of the card, one of 'C', 'D', 'H', or 'S'.
        value_rank (int): The numeric value of the rank, used for comparison.

    Methods:
        __str__(): Returns a string representation of the card.
        __eq__(other): Returns True if the rank of this card is equal to the
            rank of another card.
        __ne__(other): Returns True if the rank of this card is not equal to
            the rank of another card.
        __lt__(other): Returns True if the rank of this card is less than the
            rank of another card.
        __gt__(other): Returns True if the rank of this card is greater than
            the rank of another card.
    """

    def __init__(self, rank, suit):
        """Initialize a Card object with the given rank and suit."""
        self.rank = rank
        self.suit = suit
        self.value_rank = ranks[self.rank]

    def __str__(self):
        """Return a string representation of the card."""
        return f'{self.suit}{self.rank}'

    def __eq__(self, other):
        """Return True if the rank of this card is equal to the rank of
            another card."""
        return self.rank == other.rank

    def __ne__(self, other):
        """Return True if the rank of this card is not equal to the
            rank of another card."""
        return self.rank != other.rank

    def __lt__(self, other):
        """Return True if the rank of this card is less than
            the rank of another card."""
        return self.value_rank < other.value_rank

    def __gt__(self, other):
        """Return True if the rank of this card is greater than
            the rank of another card."""
        return self.value_rank > other.value_rank
