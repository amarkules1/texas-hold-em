class Card:
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

    rank: int = 0
    suit: int = 0

    def __init__(self):
        self.rank = 0
        self.suit = 0

    def from_ints(self, rank: int, suit: int):
        """
        Set the rank and suit of the card from integers
        :param rank: 0 indexed ("2" = 0, "A" = 12) card rank
        :param suit: from 0-3: "Hearts", "Diamonds", "Clubs", "Spades"
        """
        self.rank = rank
        self.suit = suit
        return self

    def from_str(self, rank: str, suit: str):
        """
        Set the rank and suit of the card from strings
        :param rank: single character rank ["2", "3", "4", "5", "6", "7", "8", "9", "10"/"T", "J", "Q", "K", "A"]
        :param suit: suit ["Hearts", "Diamonds", "Clubs", "Spades"] (first letter of suit also works)
        :return: self
        """
        if len(suit) > 1:
            self.suit = self.suits.index(suit)
        else:
            suit = suit.upper()
            self.suit = next(i for i, v in enumerate(self.suits) if v.startswith(suit))

        rank = rank if rank != "T" else "10"
        self.rank = self.ranks.index(rank)
        return self

    def name(self):
        return f"{self.ranks[self.rank]} of {self.suits[self.suit]}"

    def from_name(self, name: str):
        rank, suit = name.split(" of ")
        self.rank = self.ranks.index(rank)
        self.suit = self.suits.index(suit)
        return self

    def is_higher_than(self, card):
        """
        Returns True if this card is higher than the card passed in, False otherwise.
        :param card:
        :return:
        """
        return self.rank > card.rank

    def is_lower_than(self, card):
        """
        Returns True if this card is lower than the card passed in, False otherwise.
        :param card:
        :return:
        """
        return self.rank < card.rank

    def is_same_suit(self, card):
        return self.suit == card.suit

    def get_rank_str(self):
        """
        :return: the rank of the card as a string (2-10, J, Q, K, A)
        """
        return self.ranks[self.rank]

    def get_suit_str(self):
        """
        :return: the suit of the card as a string
        """
        return self.suits[self.suit]

    def __gt__(self, other):
        return self.rank > other.rank

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __str__(self):
        return self.name()
