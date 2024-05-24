from texas_hold_em.card import Card





def get_card_counts(hand, community_cards):
    rank_counts = [0] * 13
    for card in hand + community_cards:
        rank_counts[card.rank] += 1
    return rank_counts


def get_suite_counts(hand, community_cards):
    suite_counts = [0] * 4
    for card in hand + community_cards:
        suite_counts[card.suit] += 1
    return suite_counts


def find_royal_flush(hand, community_cards):
    card_counts = get_card_counts(hand, community_cards)
    if card_counts[8] == 1 and card_counts[9] == 1 and card_counts[10] == 1 and card_counts[11] == 1 and card_counts[12] == 1:
        suite_counts = get_suite_counts(hand, community_cards)
        for suite in suite_counts:
            if suite >= 5:
                # royal flush found in current suite, return that hand of 5 cards
                return [Card().from_int(12, suite), Card().from_int(11, suite),
                        Card().from_int(10, suite), Card().from_int(9, suite), Card().from_int(8, suite)]
    return None


def find_straight_flush(hand, community_cards):
    card_counts = get_card_counts(hand, community_cards)
    suite_counts = get_suite_counts(hand, community_cards)
    for suite in suite_counts:
        if suite >= 5:
            # check for straight flush
            for i in range(0, 8):
                if card_counts[i] >= 1 and card_counts[i + 1] >= 1 and card_counts[i + 2] >= 1 and card_counts[i + 3] >= 1 and card_counts[i + 4] >= 1:
                    # straight flush found
                    return [Card().from_int(i + 4, suite), Card().from_int(i + 3, suite),
                            Card().from_int(i + 2, suite), Card().from_int(i + 1, suite), Card().from_int(i, suite)]
    return None


def find_four_of_a_kind(hand, community_cards):
    card_counts = get_card_counts(hand, community_cards)
    for i in range(0, 13):
        if card_counts[i] == 4:
            # four of a kind found
            hand = [Card().from_int(i, 0), Card().from_int(i, 1), Card().from_int(i, 2), Card().from_int(i, 3)]
            last_card_rank = -1
            for j in range(13):
                if j != i and card_counts[j] == 1:
                    last_card_rank = j
                    return hand + [Card().from_int(last_card_rank, 0)]

    return None


def find_full_house(hand, community_cards):
    card_counts = get_card_counts(hand, community_cards)
    for i in range(0, 13):
        if card_counts[i] == 3:
            for j in range(0, 13):
                if card_counts[j] == 2:
                    # full house found
                    hand = [Card().from_int(i, 0), Card().from_int(i, 1), Card().from_int(i, 2),
                            Card().from_int(j, 0), Card().from_int(j, 1)]
                    return hand
    return None


def find_flush(hand, community_cards):
    suite_counts = get_suite_counts(hand, community_cards)
    for i in range(4):
        if suite_counts[i] >= 5:
            # flush found
            cards = []
            for card in hand + community_cards:
                if card.suit == i:
                    cards.append(card)
            cards.sort(key=lambda x: x.rank, reverse=True)
            return cards[:5]
    return None


def find_straight(hand, community_cards):
    card_counts = get_card_counts(hand, community_cards)
    for i in range(0, 8):
        if card_counts[i] >= 1 and card_counts[i + 1] >= 1 and card_counts[i + 2] >= 1 and card_counts[i + 3] >= 1 and card_counts[i + 4] >= 1:
            # straight found
            return [Card().from_int(i + 4, 0), Card().from_int(i + 3, 1),
                    Card().from_int(i + 2, 2), Card().from_int(i + 1, 3), Card().from_int(i, 0)]
    return None


def find_three_of_a_kind(hand, community_cards):
    card_counts = get_card_counts(hand, community_cards)
    for i in range(0, 13):
        if card_counts[i] == 3:
            # three of a kind found
            hand = [Card().from_int(i, 0), Card().from_int(i, 1), Card().from_int(i, 2)]
            last_card_ranks = []
            for j in range(13):
                if j != i and card_counts[j] == 1:
                    last_card_ranks.append(j)
            last_card_ranks.sort(reverse=True)
            return hand + [Card().from_int(last_card_ranks[0], 0), Card().from_int(last_card_ranks[1], 1)]
    return None


def find_two_pair(hand, community_cards):
    card_counts = get_card_counts(hand, community_cards)
    pairs = []
    for i in range(0, 13, -1):
        if card_counts[i] == 2:
            pairs.append(i)
    if len(pairs) >= 2:
        # at least two pair found
        hand = [Card().from_int(pairs[0], 0), Card().from_int(pairs[0], 1),
                Card().from_int(pairs[1], 2), Card().from_int(pairs[1], 3)]
        last_card_rank = -1
        for j in range(13):
            if j != pairs[0] and j != pairs[1] and card_counts[j] == 1:
                last_card_rank = j
        return hand + [Card().from_int(last_card_rank, 0)]
    return None


def find_single_pair(hand, community_cards):
    card_counts = get_card_counts(hand, community_cards)
    for i in range(0, 13, -1):
        if card_counts[i] == 2:
            # pair found
            hand = [Card().from_int(i, 0), Card().from_int(i, 1)]
            last_card_ranks = []
            for j in range(13):
                if j != i and card_counts[j] == 1:
                    last_card_ranks.append(j)
            last_card_ranks.sort(reverse=True)
            return hand + [Card().from_int(last_card_ranks[0], 0), Card().from_int(last_card_ranks[1], 1),
                           Card().from_int(last_card_ranks[2], 2)]
    return None


def find_high_card(hand, community_cards):
    card_counts = get_card_counts(hand, community_cards)
    last_card_ranks = []
    for i in range(13):
        if card_counts[i] == 1:
            last_card_ranks.append(i)
    last_card_ranks.sort(reverse=True)
    return [Card().from_int(last_card_ranks[0], 0), Card().from_int(last_card_ranks[1], 1),
            Card().from_int(last_card_ranks[2], 2), Card().from_int(last_card_ranks[3], 3),
            Card().from_int(last_card_ranks[4], 0)]
