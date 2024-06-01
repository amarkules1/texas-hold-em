from texas_hold_em.card import Card
from texas_hold_em.hands import HandOfTwo
from texas_hold_em.player import Player
from texas_hold_em.game import Game


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
