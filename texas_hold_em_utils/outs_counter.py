from texas_hold_em_utils.deck import Deck
from texas_hold_em_utils.hands import HandOfFive


def count_outs(hands, community_cards=None, sample_size=1000):
    pass

def get_one_card_outs(hands, community_cards=None):
    outs = [[] for i in range(len(hands))]
    if community_cards is None or len(community_cards) < 4:
        return outs
    deck = Deck()
    for hand in hands:
        for card in hand:
            deck.remove(card)

    for card in community_cards:
        deck.remove(card)

    for card in deck.cards:
        final_hands = []
        winner = None
        winner_index = 0
        is_split = False
        for i in range(len(hands)):
            hand = HandOfFive(hands[i], community_cards + [card])
            final_hands.append(hand)
            if winner is None or hand > winner:
                winner = hand
                winner_index = i
                is_split = False
            elif hand == winner and i != winner_index:
                is_split = True

        if not is_split:
            outs[winner_index].append(card)

    return outs

def get_two_card_outs(hands, community_cards=None):
    pass
