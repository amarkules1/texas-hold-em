from unittest.mock import MagicMock, Mock

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


def test_2_player_simple_full():
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


def test_3_player_simple_full():
    game = Game(3)
    game.players = [SimplePlayer(0), SimplePlayer(1), SimplePlayer(2)]
    game.deal()
    game.get_bets()

    assert game.players[0].round_bet == 20
    assert game.players[1].round_bet == 20
    assert game.players[2].round_bet == 20
    assert game.pot == 60
    assert game.all_day == 20
    assert game.round == 0

    game.flop()
    game.get_bets()

    assert game.players[0].round_bet == 20
    assert game.players[1].round_bet == 20
    assert game.players[2].round_bet == 20
    assert game.pot == 60
    assert game.all_day == 20
    assert game.round == 1

    game.turn()
    game.get_bets()

    assert game.players[0].round_bet == 20
    assert game.players[1].round_bet == 20
    assert game.players[2].round_bet == 20
    assert game.pot == 60
    assert game.all_day == 20
    assert game.round == 2

    game.river()
    game.get_bets()

    assert game.players[0].round_bet == 20
    assert game.players[1].round_bet == 20
    assert game.players[2].round_bet == 20
    assert game.pot == 60
    assert game.all_day == 20
    assert game.round == 3

    winners = game.determine_round_winners()
    assert len(winners) > 0


def test_3_player_game_with_preflop_raise():
    game = Game(3)
    player_3 = SimplePlayer(0)
    player_3.round_bet = 40
    player_3.decide = Mock(return_value=("raise", 40))
    game.players = [player_3, SimplePlayer(1), SimplePlayer(2)]
    game.deal()
    game.get_bets()

    assert game.players[1].round_bet == 10
    assert game.players[2].round_bet == 20
    assert not game.players[1].in_round
    assert not game.players[2].in_round
    assert game.pot == 70
    assert game.all_day == 40


def test_payout_1_winner():
    game = Game(3)
    game.players = [SimplePlayer(0), SimplePlayer(1), SimplePlayer(2)]
    community_cards = [
        Card().from_str("2", "Hearts"),
        Card().from_str("4", "Spades"),
        Card().from_str("6", "Clubs"),
        Card().from_str("8", "Diamonds"),
        Card().from_str("10", "Hearts")
    ]
    game.players[0].hand_of_two = HandOfTwo([
        Card().from_str("A", "Hearts"),
        Card().from_str("A", "Spades")
    ])
    game.players[1].hand_of_two = HandOfTwo([
        Card().from_str("K", "Hearts"),
        Card().from_str("K", "Spades")
    ])
    game.players[2].hand_of_two = HandOfTwo([
        Card().from_str("Q", "Hearts"),
        Card().from_str("Q", "Spades")
    ])
    game.community_cards = community_cards
    game.players[0].round_bet = 20
    game.players[1].round_bet = 20
    game.players[2].round_bet = 20
    game.pot = 60
    game.all_day = 20

    game.pay_out_winners()

    assert game.players[0].chips == 1060
    assert game.players[1].chips == 1000
    assert game.players[2].chips == 1000


def test_payout_even_split():
    game = Game(3)
    game.players = [SimplePlayer(0), SimplePlayer(1), SimplePlayer(2)]
    community_cards = [
        Card().from_str("2", "Hearts"),
        Card().from_str("4", "Spades"),
        Card().from_str("6", "Clubs"),
        Card().from_str("8", "Diamonds"),
        Card().from_str("10", "Hearts")
    ]
    game.players[0].hand_of_two = HandOfTwo([
        Card().from_str("A", "Hearts"),
        Card().from_str("A", "Spades")
    ])
    game.players[1].hand_of_two = HandOfTwo([
        Card().from_str("A", "Clubs"),
        Card().from_str("A", "Diamonds")
    ])
    game.players[2].hand_of_two = HandOfTwo([
        Card().from_str("Q", "Hearts"),
        Card().from_str("Q", "Spades")
    ])
    game.community_cards = community_cards
    game.players[0].round_bet = 20
    game.players[1].round_bet = 20
    game.players[2].round_bet = 20
    game.pot = 60
    game.all_day = 20

    game.pay_out_winners()

    assert game.players[0].chips == 1030
    assert game.players[1].chips == 1030
    assert game.players[2].chips == 1000


def test_payout_uneven_split():
    game = Game(3)
    game.players = [SimplePlayer(0), SimplePlayer(1), SimplePlayer(2)]
    community_cards = [
        Card().from_str("2", "Hearts"),
        Card().from_str("4", "Spades"),
        Card().from_str("6", "Clubs"),
        Card().from_str("8", "Diamonds"),
        Card().from_str("10", "Hearts")
    ]
    game.players[0].hand_of_two = HandOfTwo([
        Card().from_str("A", "Hearts"),
        Card().from_str("A", "Spades")
    ])
    game.players[1].hand_of_two = HandOfTwo([
        Card().from_str("A", "Clubs"),
        Card().from_str("A", "Diamonds")
    ])
    game.players[2].hand_of_two = HandOfTwo([
        Card().from_str("Q", "Hearts"),
        Card().from_str("Q", "Spades")
    ])
    game.community_cards = community_cards
    game.players[0].round_bet = 20
    game.players[1].round_bet = 20
    game.players[2].round_bet = 19
    game.pot = 59
    game.all_day = 20

    game.pay_out_winners()

    assert game.players[0].chips == 1030
    assert game.players[1].chips == 1029
    assert game.players[2].chips == 1000


def test_payout_winner_all_in():
    game = Game(3)
    game.players = [SimplePlayer(0, 0), SimplePlayer(1), SimplePlayer(2)]
    community_cards = [
        Card().from_str("2", "Hearts"),
        Card().from_str("4", "Spades"),
        Card().from_str("6", "Clubs"),
        Card().from_str("8", "Diamonds"),
        Card().from_str("10", "Hearts")
    ]
    game.players[0].hand_of_two = HandOfTwo([
        Card().from_str("A", "Hearts"),
        Card().from_str("A", "Spades")
    ])
    game.players[1].hand_of_two = HandOfTwo([
        Card().from_str("K", "Clubs"),
        Card().from_str("K", "Diamonds")
    ])
    game.players[2].hand_of_two = HandOfTwo([
        Card().from_str("Q", "Hearts"),
        Card().from_str("Q", "Spades")
    ])
    game.community_cards = community_cards
    game.players[0].round_bet = 20
    game.players[1].round_bet = 30
    game.players[2].round_bet = 30
    game.pot = 80
    game.all_day = 30

    game.pay_out_winners()

    assert game.players[0].chips == 60
    assert game.players[1].chips == 1020
    assert game.players[2].chips == 1000
