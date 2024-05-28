class Card:
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

    rank: int = 0
    suit: int = 0

    def __init__ (self):
        self.rank = 0
        self.suit = 0

    def from_ints(self, rank: int, suit: int):
        """
        :param rank: 0 indexed ("2" = 0, "A" = 12) card rank
        :param suit: from 0-3: "Hearts", "Diamonds", "Clubs", "Spades"
        """
        self.rank = rank
        self.suit = suit
        return self

    def from_str(self, rank: str, suit: str):
        self.rank = self.ranks.index(rank)
        self.suit = self.suits.index(suit)
        return self

    def name(self):
        return f"{self.ranks[self.rank]} of {self.suits[self.suit]}"

    def is_higher_than(self, card):
        return self.rank > card.rank

    def is_lower_than(self, card):
        return self.rank < card.rank

    def is_same_suit(self, card):
        return self.suit == card.suit

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit
