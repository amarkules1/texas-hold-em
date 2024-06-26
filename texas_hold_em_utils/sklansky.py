def sklansky_playable_position(position: int):
    """
    Returns the playable positions for a given Sklansky rank
    https://en.wikipedia.org/wiki/Texas_hold_%27em_starting_hands#Sklansky_hand_groups
    :param position: int from 1 to 9
    :return: the positions and situations where the hand is playable
    """
    if position < 5:
        return "Early, Middle, Late"
    if position == 5:
        return "Early (loose/passive), Middle, Late"
    if position == 6:
        return "Middle (loose/passive), Late"
    if position == 7:
        return "Late if no bettors"
    if position == 8:
        return "Call if late and no bettors"
    return "Not playable"


def sklansky_rank(card1, card2):
    """
    Returns the Sklansky rank of the two hole cards passed in
    https://en.wikipedia.org/wiki/Texas_hold_%27em_starting_hands#Sklansky_hand_groups
    :param card1: a Card object
    :param card2: a (different) Card object
    :return: an int from 1 to 9, 1 being the best hand and 9 being the worst
    """
    higher_card = card1 if card1.rank > card2.rank else card2
    lower_card = card1 if card1.rank < card2.rank else card2
    if is_rank_1(higher_card, lower_card):
        return 1
    if is_rank_2(higher_card, lower_card):
        return 2
    if is_rank_3(higher_card, lower_card):
        return 3
    if is_rank_4(higher_card, lower_card):
        return 4
    if is_rank_5(higher_card, lower_card):
        return 5
    if is_rank_6(higher_card, lower_card):
        return 6
    if is_rank_7(higher_card, lower_card):
        return 7
    if is_rank_8(higher_card, lower_card):
        return 8
    return 9
    

def is_rank_1(higher_card, lower_card):
    if higher_card.rank == lower_card.rank and higher_card.rank >= 9:
        return True
    # ace king suited
    if (higher_card.suit == lower_card.suit) and (higher_card.rank == 12 and lower_card.rank == 11):
        return True
    return False
    

def is_rank_2(higher_card, lower_card):
    # ace king offsuit
    if higher_card.rank == 12 and lower_card.rank == 11:
        return True
    # ace queen/jack suited
    if (higher_card.suit == lower_card.suit) and (higher_card.rank == 12 and lower_card.rank >= 9):
        return True
    # king queen suited
    if (higher_card.suit == lower_card.suit) and (higher_card.rank == 11 and lower_card.rank == 10):
        return True
    # tens
    if higher_card.rank == 8 and lower_card.rank == 8:
        return True
    return False


def is_rank_3(higher_card, lower_card):
    # ace queen offsuit
    if higher_card.rank == 12 and lower_card.rank == 10:
        return True
    # jack king/queen suited
    if (higher_card.suit == lower_card.suit) and (higher_card.rank >= 10 and lower_card.rank == 9):
        return True
    # ace/jack ten suited
    if (higher_card.suit == lower_card.suit) and (higher_card.rank in [12, 9] and lower_card.rank == 8):
        return True
    # nines
    if higher_card.rank == 7 and lower_card.rank == 7:
        return True

    return False


def is_rank_4(higher_card, lower_card):
    # ace jack offsuit
    if higher_card.rank == 12 and lower_card.rank == 9:
        return True
    # king queen offsuit
    if higher_card.rank == 11 and lower_card.rank == 10:
        return True
    # ten king/queen suited
    if (higher_card.suit == lower_card.suit) and (higher_card.rank >= 10 and lower_card.rank == 8):
        return True
    # nine ten/jack suited
    if (higher_card.suit == lower_card.suit) and (higher_card.rank in [9, 8] and lower_card.rank >= 7):
        return True
    # nine eight suited
    if (higher_card.suit == lower_card.suit) and (higher_card.rank == 7 and lower_card.rank == 6):
        return True
    # eights
    if higher_card.rank == 6 and lower_card.rank == 6:
        return True
    
    return False


def is_rank_5(higher_card, lower_card):
    # jack king/queen offsuit
    if higher_card.rank >= 10 and lower_card.rank == 9:
        return True
    # jack ten offsuit
    if higher_card.rank == 9 and lower_card.rank == 8:
        return True
    # ace any suited
    if higher_card.suit == lower_card.suit and higher_card.rank == 12:
        return True
    # queen nine suited
    if higher_card.suit == lower_card.suit and higher_card.rank == 10 and lower_card.rank == 7:
        return True
    # ten eight suited
    if higher_card.suit == lower_card.suit and higher_card.rank == 8 and lower_card.rank == 6:
        return True
    # seven eight/nine suited
    if higher_card.suit == lower_card.suit and higher_card.rank in [6, 7] and lower_card.rank == 5:
        return True
    # sevens
    if higher_card.rank == 5 and lower_card.rank == 5:
        return True
    # seven six suited
    if higher_card.suit == lower_card.suit and higher_card.rank == 5 and lower_card.rank == 4:
        return True

    return False


def is_rank_6(higher_card, lower_card):
    # ace/king/queen ten offsuit
    if higher_card.rank >= 10 and lower_card.rank == 8:
        return True
    # king nine suited
    if higher_card.suit == lower_card.suit and higher_card.rank == 11 and lower_card.rank == 7:
        return True
    # jack eight suited
    if higher_card.suit == lower_card.suit and higher_card.rank == 9 and lower_card.rank == 6:
        return True
    # eight six suited
    if higher_card.suit == lower_card.suit and higher_card.rank == 6 and lower_card.rank == 4:
        return True
    # sixes
    if higher_card.rank == 4 and lower_card.rank == 4:
        return True
    # seven five suited
    if higher_card.suit == lower_card.suit and higher_card.rank == 5 and lower_card.rank == 3:
        return True
    # fives
    if higher_card.rank == 3 and lower_card.rank == 3:
        return True
    # five four suited
    if higher_card.suit == lower_card.suit and higher_card.rank == 3 and lower_card.rank == 2:
        return True

    return False


def is_rank_7(higher_card, lower_card):
    # king any suited
    if higher_card.suit == lower_card.suit and higher_card.rank == 11:
        return True
    # queen eight suited
    if higher_card.suit == lower_card.suit and higher_card.rank == 10 and lower_card.rank == 6:
        return True
    # ten seven suited
    if higher_card.suit == lower_card.suit and higher_card.rank == 8 and lower_card.rank == 5:
        return True
    # jack/ten nine offsuit
    if higher_card.rank in [9, 8] and lower_card.rank == 7:
        return True
    # nine eight offsuit
    if higher_card.rank == 7 and lower_card.rank == 6:
        return True
    # six five/four suited
    if higher_card.suit == lower_card.suit and higher_card.rank == 4 and lower_card.rank in [3, 2]:
        return True
    # five/four three suited
    if higher_card.suit == lower_card.suit and higher_card.rank in [3, 2] and lower_card.rank == 1:
        return True
    # any pair
    if higher_card.rank == lower_card.rank:
        return True

    return False


def is_rank_8(higher_card, lower_card):
    # ace/king/queen nine offsuit
    if higher_card.rank >= 10 and lower_card.rank == 7:
        return True
    # jack/ten eight offsuit
    if higher_card.rank in [9, 8] and lower_card.rank == 6:
        return True
    # jack seven suited
    if higher_card.suit == lower_card.suit and higher_card.rank == 9 and lower_card.rank == 5:
        return True
    # nine six suited
    if higher_card.suit == lower_card.suit and higher_card.rank == 7 and lower_card.rank == 4:
        return True
    # eight five suited
    if higher_card.suit == lower_card.suit and higher_card.rank == 6 and lower_card.rank == 3:
        return True
    # seven four suited
    if higher_card.suit == lower_card.suit and higher_card.rank == 5 and lower_card.rank == 2:
        return True
    # four/three two suited
    if higher_card.suit == lower_card.suit and higher_card.rank in [2, 1] and lower_card.rank == 0:
        return True
    # eight seven offsuit
    if higher_card.rank == 6 and lower_card.rank == 5:
        return True
    # seven six offsuit
    if higher_card.rank == 5 and lower_card.rank == 4:
        return True
    # six five offsuit
    if higher_card.rank == 4 and lower_card.rank == 3:
        return True
    # five four offsuit
    if higher_card.rank == 3 and lower_card.rank == 2:
        return True

    return False


    