from src.texas_hold_em_utils.card import Card


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
    suite_counts = get_suite_counts(hand, community_cards)
    for i in range(4):
        if suite_counts[i] >= 5:
            suite_ranks = [card.rank for card in hand + community_cards if card.suit == i]
            if 8 in suite_ranks and 9 in suite_ranks and 10 in suite_ranks and 11 in suite_ranks and 12 in suite_ranks:
                # royal flush found
                return [Card().from_ints(12, i), Card().from_ints(11, i), Card().from_ints(10, i),
                        Card().from_ints(9, i), Card().from_ints(8, i)]
    return None


def find_straight_flush(hand, community_cards):
    suite_counts = get_suite_counts(hand, community_cards)
    for i in range(4):
        if suite_counts[i] >= 5:
            suite_ranks = [card.rank for card in hand + community_cards if card.suit == i]
            suite_ranks.sort(reverse=True)
            for j in range(0, 8):
                if (j in suite_ranks and j + 1 in suite_ranks and j + 2 in suite_ranks and j + 3 in suite_ranks
                        and j + 4 in suite_ranks):
                    # straight flush found
                    return [Card().from_ints(j + 4, i), Card().from_ints(j + 3, i), Card().from_ints(j + 2, i),
                            Card().from_ints(j + 1, i), Card().from_ints(j, i)]
    return None


def find_four_of_a_kind(hand, community_cards):
    card_counts = get_card_counts(hand, community_cards)
    for i in range(0, 13):
        if card_counts[i] == 4:
            # four of a kind found
            four = [Card().from_ints(i, 0), Card().from_ints(i, 1), Card().from_ints(i, 2), Card().from_ints(i, 3)]
            last_card = None
            for card in hand + community_cards:
                if card.rank != i and (last_card is None or card.rank > last_card.rank):
                    last_card = card
            return four + [last_card]

    return None


def find_full_house(hand, community_cards):
    card_counts = get_card_counts(hand, community_cards)
    highest_three_of_a_kind = -1
    highest_pair_not_highest_3 = -1
    for i in range(0, 13):
        if card_counts[i] == 3:
            if highest_three_of_a_kind > highest_pair_not_highest_3:
                highest_pair_not_highest_3 = highest_three_of_a_kind
            highest_three_of_a_kind = i
        elif card_counts[i] == 2:
            highest_pair_not_highest_3 = i
    if highest_three_of_a_kind != -1 and highest_pair_not_highest_3 != -1:
        # full house found
        hand_five = [card for card in hand + community_cards if card.rank == highest_three_of_a_kind]
        hand_five += [card for card in hand + community_cards if card.rank == highest_pair_not_highest_3][:2]
        return hand_five
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
    # count high_to_low straights
    for i in range(8, -1, -1):
        if card_counts[i] > 0 and card_counts[i + 1] > 0 and card_counts[i + 2] > 0 and card_counts[i + 3] > 0 and \
                card_counts[i + 4] > 0:
            # straight found
            cards = [card for card in hand + community_cards if card.rank in [i, i + 1, i + 2, i + 3, i + 4]]
            # remove dupes by rank
            final_cards = []
            for card in cards:
                if card.rank not in [c.rank for c in final_cards]:
                    final_cards.append(card)
            cards.sort(key=lambda x: x.rank, reverse=True)
            return cards[:5]

    return None


def find_three_of_a_kind(hand, community_cards):
    card_counts = get_card_counts(hand, community_cards)
    for i in range(12, -1, -1):
        if card_counts[i] == 3:
            # three of a kind found
            three = [card for card in hand + community_cards if card.rank == i]
            sorted_cards = sorted([card for card in hand + community_cards if card.rank != i], key=lambda x: x.rank,
                                  reverse=True)
            three += [card for card in sorted_cards if card.rank != i][:2]
            return three
    return None


def find_two_pair(hand, community_cards):
    card_counts = get_card_counts(hand, community_cards)
    pairs = []
    for i in range(12, -1, -1):
        if card_counts[i] == 2:
            pairs.append(i)
        if len(pairs) == 2:
            break
    if len(pairs) == 2:
        # at least two pair found
        hand_of_5 = [card for card in hand + community_cards if card.rank in pairs]
        hand_of_5.sort(key=lambda x: x.rank, reverse=True)
        remaining_cards = [card for card in hand + community_cards if card.rank not in pairs]
        remaining_cards.sort(key=lambda x: x.rank, reverse=True)
        return hand_of_5 + [remaining_cards[0]]
    return None


def find_single_pair(hand, community_cards):
    card_counts = get_card_counts(hand, community_cards)
    for i in range(12, -1, -1):
        if card_counts[i] == 2:
            # pair found
            hand_of_5 = [card for card in hand + community_cards if card.rank == i]
            remaining = [card for card in hand + community_cards if card.rank != i]
            remaining.sort(key=lambda x: x.rank, reverse=True)
            hand_of_5 += remaining[:3]
            return hand_of_5
    return None


def find_high_card(hand, community_cards):
    sorted_cards = hand + community_cards
    sorted_cards.sort(key=lambda x: x.rank, reverse=True)
    return sorted_cards[:5]
