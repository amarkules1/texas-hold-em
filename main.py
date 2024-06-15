from texas_hold_em_utils import Card
from texas_hold_em_utils.sklansky import sklansky_playable_position, sklansky_rank


def main():
    while True:
        print("Enter the value of the first card: ")
        value1 = str(input())
        if value1 not in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]:
            break
        print("Enter the suit of the first card: ")
        suit1 = str(input())
        if suit1 not in ["H", "D", "C", "S"]:
            break
        print("Enter the value of the second card: ")
        value2 = str(input())
        if value2 not in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]:
            break
        print("Enter the suit of the second card: ")
        suit2 = str(input())
        if suit2 not in ["H", "D", "C", "S"]:
            break
        card1 = Card().from_str(value1, suite_lookup(suit1))
        card2 = Card().from_str(value2, suite_lookup(suit2))
        print(f"Your cards are {card1.name()} and {card2.name()}")
        rank = sklansky_rank(card1, card2)
        print(f"Your rank is {rank}")
        print(f"Your position is {sklansky_playable_position(rank)}")


def suite_lookup(suit):
    if suit == "H":
        return "Hearts"
    if suit == "D":
        return "Diamonds"
    if suit == "C":
        return "Clubs"
    if suit == "S":
        return "Spades"
    return "Invalid suit"


if __name__ == "__main__":
    main()
