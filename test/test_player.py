from texas_hold_em_utils.card import Card
from texas_hold_em_utils.player import AllInPreFlopPlayer, LimpPlayer


def test_all_in_preflop_good_hand():
    player = AllInPreFlopPlayer(0, 1000, 0.5)
    # pocket aces should be above 50% win rate in a 2 player game
    player.hand_of_two.add_card(Card().from_ints(12, 0))
    player.hand_of_two.add_card(Card().from_ints(12, 1))

    action = player.decide(0, 0, 20, 20, [], 2)

    assert action[0] == "raise"
    assert action[1] == 1000


def test_all_in_preflop_bad_hand():
    player = AllInPreFlopPlayer(0, 1000, 0.5)
    # 2 7 off should be below 50% win rate in a 2 player game
    player.hand_of_two.add_card(Card().from_ints(0, 0))
    player.hand_of_two.add_card(Card().from_ints(5, 1))

    action = player.decide(0, 0, 20, 20, [], 2)

    assert action[0] == "fold"
    assert action[1] == 0


def test_all_in_preflop_bad_hand_big_blind():
    player = AllInPreFlopPlayer(0, 1000, 0.5)
    # 2 7 off should be below 50% win rate in a 2 player game
    player.hand_of_two.add_card(Card().from_ints(0, 0))
    player.hand_of_two.add_card(Card().from_ints(5, 1))
    player.round_bet = 20

    action = player.decide(0, 40, 20, 20, [], 2)

    assert action[0] == "check"
    assert action[1] == 0


def test_all_in_preflop_but_its_post_flop():
    player = AllInPreFlopPlayer(0, 1000, 0.5)
    # 2 7 off should be below 50% win rate in a 2 player game
    player.hand_of_two.add_card(Card().from_ints(0, 0))
    player.hand_of_two.add_card(Card().from_ints(5, 1))

    action = player.decide(1, 0, 20, 20, [], 2)

    assert action[0] == "check"
    assert action[1] == 0


def test_limper_no_bet():
    player = LimpPlayer(0, 1000, 0.5)
    player.round_bet = 20

    action = player.decide(0, 0, 20, 20, [], 2)

    assert action[0] == "check"
    assert action[1] == 0


def test_limper_already_all_in():
    player = LimpPlayer(0, 1000, 0.5)
    player.round_bet = 1000
    player.chips = 0

    action = player.decide(0, 0, 1000, 1000, [], 2)

    assert action[0] == "check"
    assert action[1] == 0


def test_limper_good_hand_preflop():
    player = LimpPlayer(0, 1000, 0.5)
    # pocket aces should be above 50% win rate in a 2 player game
    player.hand_of_two.add_card(Card().from_ints(12, 0))
    player.hand_of_two.add_card(Card().from_ints(12, 1))

    action = player.decide(0, 0, 20, 20, [], 2)

    assert action[0] == "call"
    assert action[1] == 20


def test_limper_good_hand_postflop():
    player = LimpPlayer(0, 1000, 0.5)
    player.hand_of_two.add_card(Card().from_ints(12, 0))
    player.hand_of_two.add_card(Card().from_ints(12, 1))
    player.round_bet = 20
    # pocket aces with some random unsuited community cards should win against most hands
    community = [Card().from_ints(0, 0), Card().from_ints(8, 1), Card().from_ints(4, 2)]

    action = player.decide(1, 60, 40, 20, community, 2)

    assert action[0] == "call"
    assert action[1] == 20


def test_limper_bad_hand_postflop():
    player = LimpPlayer(0, 1000, 0.5)
    player.hand_of_two.add_card(Card().from_ints(1, 0))
    player.hand_of_two.add_card(Card().from_ints(5, 1))
    player.round_bet = 20
    # pocket aces with some random unsuited community cards should win against most hands
    community = [Card().from_ints(0, 0), Card().from_ints(8, 1), Card().from_ints(4, 2)]

    action = player.decide(1, 60, 40, 20, community, 2)

    assert action[0] == "fold"
    assert action[1] == 0


def test_limper_bad_hand_preflop():
    player = LimpPlayer(0, 1000, 0.5)
    # 2 7 off should be below 50% win rate in a 2 player game
    player.hand_of_two.add_card(Card().from_ints(0, 0))
    player.hand_of_two.add_card(Card().from_ints(5, 1))

    action = player.decide(0, 0, 20, 20, [], 2)

    assert action[0] == "fold"
    assert action[1] == 0


def test_limper_good_hand_preflop_variable():
    player = LimpPlayer(0, 1000, [0.5, 1.0, 1.0, 1.0])
    # pocket aces should be above 50% win rate in a 2 player game
    player.hand_of_two.add_card(Card().from_ints(12, 0))
    player.hand_of_two.add_card(Card().from_ints(12, 1))

    action = player.decide(0, 0, 20, 20, [], 2)

    assert action[0] == "call"
    assert action[1] == 20


def test_limper_good_hand_postflop_variable():
    player = LimpPlayer(0, 1000, [1.0, 0.5, 1.0, 1.0])
    player.hand_of_two.add_card(Card().from_ints(12, 0))
    player.hand_of_two.add_card(Card().from_ints(12, 1))
    player.round_bet = 20
    # pocket aces with some random unsuited community cards should win against most hands
    community = [Card().from_ints(0, 0), Card().from_ints(8, 1), Card().from_ints(4, 2)]

    action = player.decide(1, 60, 40, 20, community, 2)

    assert action[0] == "call"
    assert action[1] == 20


def test_limper_bad_hand_postflop_variable():
    player = LimpPlayer(0, 1000, [0.0, 0.5, 0.0, 0.0])
    player.hand_of_two.add_card(Card().from_ints(1, 0))
    player.hand_of_two.add_card(Card().from_ints(5, 1))
    player.round_bet = 20
    # pocket aces with some random unsuited community cards should win against most hands
    community = [Card().from_ints(0, 0), Card().from_ints(8, 1), Card().from_ints(4, 2)]

    action = player.decide(1, 60, 40, 20, community, 2)

    assert action[0] == "fold"
    assert action[1] == 0


def test_limper_bad_hand_preflop_variable():
    player = LimpPlayer(0, 1000, [0.5, 0.0, 0.0, 0.0])
    # 2 7 off should be below 50% win rate in a 2 player game
    player.hand_of_two.add_card(Card().from_ints(0, 0))
    player.hand_of_two.add_card(Card().from_ints(5, 1))

    action = player.decide(0, 0, 20, 20, [], 2)

    assert action[0] == "fold"
    assert action[1] == 0
