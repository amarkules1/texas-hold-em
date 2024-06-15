from texas_hold_em_utils.card import Card
from texas_hold_em_utils.hands import HandOfTwo
from texas_hold_em_utils.player import Player, SimplePlayer
from texas_hold_em_utils.game import Game


def test_determine_round_winners_all_in_one_winner():
    community_cards = [
        Card().from_str("A", "Hearts"),
        Card().from_str("A", "Spades"),
        Card().from_str("4", "Clubs"),
        Card().from_str("6", "Diamonds"),
        Card().from_str("9", "Hearts")
    ]
    # 2 pair
    player1 = Player(0)
    player1.hand_of_two = HandOfTwo([
        Card().from_str("K", "Hearts"),
        Card().from_str("K", "Spades")
    ])
    # 2 pair
    player2 = Player(1)
    player2.hand_of_two = HandOfTwo([
        Card().from_str("Q", "Hearts"),
        Card().from_str("Q", "Spades")
    ])
    # 2 pair
    player3 = Player(2)
    player3.hand_of_two = HandOfTwo([
        Card().from_str("J", "Hearts"),
        Card().from_str("10", "Hearts")
    ])
    # aces full of 9s
    player4 = Player(3)
    player4.hand_of_two = HandOfTwo([
        Card().from_str("9", "Spades"),
        Card().from_str("A", "Diamonds")
    ])
    # aces full of 4s
    player5 = Player(4)
    player5.hand_of_two = HandOfTwo([
        Card().from_str("A", "Clubs"),
        Card().from_str("4", "Hearts")
    ])

    game = Game(5)
    game.players = [player1, player2, player3, player4, player5]
    game.community_cards = community_cards

    winners = game.determine_round_winners()

    assert len(winners) == 1
    assert winners[0].position == 3


def test_determine_round_winners_all_in_two_winner():
    community_cards = [
        Card().from_str("A", "Hearts"),
        Card().from_str("A", "Spades"),
        Card().from_str("4", "Clubs"),
        Card().from_str("6", "Diamonds"),
        Card().from_str("9", "Hearts")
    ]
    # 2 pair
    player1 = Player(0)
    player1.hand_of_two = HandOfTwo([
        Card().from_str("K", "Hearts"),
        Card().from_str("K", "Spades")
    ])
    # 2 pair
    player2 = Player(1)
    player2.hand_of_two = HandOfTwo([
        Card().from_str("Q", "Hearts"),
        Card().from_str("Q", "Spades")
    ])
    # 2 pair
    player3 = Player(2)
    player3.hand_of_two = HandOfTwo([
        Card().from_str("J", "Hearts"),
        Card().from_str("10", "Hearts")
    ])
    # aces full of 4s
    player4 = Player(3)
    player4.hand_of_two = HandOfTwo([
        Card().from_str("4", "Spades"),
        Card().from_str("A", "Diamonds")
    ])
    # aces full of 4s
    player5 = Player(4)
    player5.hand_of_two = HandOfTwo([
        Card().from_str("A", "Clubs"),
        Card().from_str("4", "Hearts")
    ])

    game = Game(5)
    game.players = [player4, player5]
    game.community_cards = community_cards

    winners = game.determine_round_winners()

    assert len(winners) == 2
    assert winners[0].position == 3
    assert winners[1].position == 4


def test_determine_round_winners_best_folded():
    community_cards = [
        Card().from_str("A", "Hearts"),
        Card().from_str("A", "Spades"),
        Card().from_str("4", "Clubs"),
        Card().from_str("6", "Diamonds"),
        Card().from_str("9", "Hearts")
    ]
    # 2 pair
    player1 = Player(0)
    player1.hand_of_two = HandOfTwo([
        Card().from_str("K", "Hearts"),
        Card().from_str("K", "Spades")
    ])
    # 2 pair
    player2 = Player(1)
    player2.hand_of_two = HandOfTwo([
        Card().from_str("Q", "Hearts"),
        Card().from_str("Q", "Spades")
    ])
    # 2 pair
    player3 = Player(2)
    player3.hand_of_two = HandOfTwo([
        Card().from_str("J", "Hearts"),
        Card().from_str("10", "Hearts")
    ])
    # aces full of 9s
    player4 = Player(3)
    player4.hand_of_two = HandOfTwo([
        Card().from_str("9", "Spades"),
        Card().from_str("A", "Diamonds")
    ])
    player4.in_round = False
    # aces full of 4s
    player5 = Player(4)
    player5.hand_of_two = HandOfTwo([
        Card().from_str("A", "Clubs"),
        Card().from_str("4", "Hearts")
    ])

    game = Game(5)
    game.players = [player1, player2, player3, player4, player5]
    game.community_cards = community_cards

    winners = game.determine_round_winners()

    assert len(winners) == 1
    assert winners[0].position == 4


def test_2_player_simple_pre_flop():
    game = Game(2)
    game.players = [SimplePlayer(0), SimplePlayer(1)]
    game.deal()
    game.get_bets()

    assert game.players[0].round_bet == 20
    assert game.players[1].round_bet == 20
    assert game.pot == 40
    assert game.all_day == 20


def test_2_player_simple_through_flop():
    game = Game(2)
    game.players = [SimplePlayer(0), SimplePlayer(1)]
    game.deal()
    game.get_bets()

    assert game.players[0].round_bet == 20
    assert game.players[1].round_bet == 20
    assert game.pot == 40
    assert game.all_day == 20
    assert game.round == 0

    game.flop()
    game.get_bets()

    assert game.players[0].round_bet == 20
    assert game.players[1].round_bet == 20
    assert game.pot == 40
    assert game.all_day == 20
    assert game.round == 1

    game.turn()
    game.get_bets()

    assert game.players[0].round_bet == 20
    assert game.players[1].round_bet == 20
    assert game.pot == 40
    assert game.all_day == 20
    assert game.round == 2

    game.river()
    game.get_bets()

    assert game.players[0].round_bet == 20
    assert game.players[1].round_bet == 20
    assert game.pot == 40
    assert game.all_day == 20
    assert game.round == 3

    winners = game.determine_round_winners()
    assert len(winners) > 0



