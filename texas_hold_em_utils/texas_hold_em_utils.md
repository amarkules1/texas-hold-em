# Table of Contents

* [.](#.)
* [..card](#..card)
  * [Card](#..card.Card)
    * [from\_ints](#..card.Card.from_ints)
    * [from\_str](#..card.Card.from_str)
    * [is\_higher\_than](#..card.Card.is_higher_than)
    * [is\_lower\_than](#..card.Card.is_lower_than)
* [..deck](#..deck)
  * [Deck](#..deck.Deck)
    * [\_\_init\_\_](#..deck.Deck.__init__)
    * [shuffle](#..deck.Deck.shuffle)
    * [draw](#..deck.Deck.draw)
    * [remove](#..deck.Deck.remove)
* [..game](#..game)
  * [Game](#..game.Game)
    * [\_\_init\_\_](#..game.Game.__init__)
    * [deal](#..game.Game.deal)
    * [flop](#..game.Game.flop)
    * [turn](#..game.Game.turn)
    * [river](#..game.Game.river)
    * [get\_bets](#..game.Game.get_bets)
    * [determine\_round\_winners](#..game.Game.determine_round_winners)
* [..game\_utils](#..game_utils)
  * [get\_card\_counts](#..game_utils.get_card_counts)
  * [get\_suite\_counts](#..game_utils.get_suite_counts)
  * [find\_royal\_flush](#..game_utils.find_royal_flush)
  * [find\_straight\_flush](#..game_utils.find_straight_flush)
  * [find\_four\_of\_a\_kind](#..game_utils.find_four_of_a_kind)
  * [find\_full\_house](#..game_utils.find_full_house)
  * [find\_flush](#..game_utils.find_flush)
  * [find\_straight](#..game_utils.find_straight)
  * [find\_three\_of\_a\_kind](#..game_utils.find_three_of_a_kind)
  * [find\_two\_pair](#..game_utils.find_two_pair)
  * [find\_single\_pair](#..game_utils.find_single_pair)
  * [find\_high\_card](#..game_utils.find_high_card)
* [..hands](#..hands)
  * [HandOfTwo](#..hands.HandOfTwo)
    * [add\_card](#..hands.HandOfTwo.add_card)
  * [HandOfFive](#..hands.HandOfFive)
    * [\_\_init\_\_](#..hands.HandOfFive.__init__)
    * [determine\_best](#..hands.HandOfFive.determine_best)
    * [\_\_gt\_\_](#..hands.HandOfFive.__gt__)
    * [\_\_eq\_\_](#..hands.HandOfFive.__eq__)
    * [\_\_lt\_\_](#..hands.HandOfFive.__lt__)
* [..player](#..player)
  * [Player](#..player.Player)
    * [\_\_init\_\_](#..player.Player.__init__)
    * [bet](#..player.Player.bet)
    * [fold](#..player.Player.fold)
    * [decide](#..player.Player.decide)
  * [SimplePlayer](#..player.SimplePlayer)
    * [decide](#..player.SimplePlayer.decide)
  * [AllInPreFlopPlayer](#..player.AllInPreFlopPlayer)
    * [decide](#..player.AllInPreFlopPlayer.decide)
  * [LimpPlayer](#..player.LimpPlayer)
    * [decide](#..player.LimpPlayer.decide)
* [..preflop\_stats\_repository](#..preflop_stats_repository)
  * [PreflopStatsRepository](#..preflop_stats_repository.PreflopStatsRepository)
    * [\_\_init\_\_](#..preflop_stats_repository.PreflopStatsRepository.__init__)
    * [get\_win\_rate](#..preflop_stats_repository.PreflopStatsRepository.get_win_rate)
* [..relative\_ranking](#..relative_ranking)
  * [rank\_hand](#..relative_ranking.rank_hand)
  * [get\_hand\_stats](#..relative_ranking.get_hand_stats)
* [..sklansky](#..sklansky)
  * [sklansky\_playable\_position](#..sklansky.sklansky_playable_position)
  * [sklansky\_rank](#..sklansky.sklansky_rank)

<a id="."></a>

# .

<a id="..card"></a>

# ..card

<a id="..card.Card"></a>

## Card Objects

```python
class Card()
```

<a id="..card.Card.from_ints"></a>

#### from\_ints

```python
def from_ints(rank: int, suit: int)
```

Set the rank and suit of the card from integers

**Arguments**:

- `rank`: 0 indexed ("2" = 0, "A" = 12) card rank
- `suit`: from 0-3: "Hearts", "Diamonds", "Clubs", "Spades"

<a id="..card.Card.from_str"></a>

#### from\_str

```python
def from_str(rank: str, suit: str)
```

Set the rank and suit of the card from strings

**Arguments**:

- `rank`: single character rank ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
- `suit`: suit ["Hearts", "Diamonds", "Clubs", "Spades"]

<a id="..card.Card.is_higher_than"></a>

#### is\_higher\_than

```python
def is_higher_than(card)
```

Returns True if this card is higher than the card passed in, False otherwise.

**Arguments**:

- `card`: 

<a id="..card.Card.is_lower_than"></a>

#### is\_lower\_than

```python
def is_lower_than(card)
```

Returns True if this card is lower than the card passed in, False otherwise.

**Arguments**:

- `card`: 

<a id="..deck"></a>

# ..deck

<a id="..deck.Deck"></a>

## Deck Objects

```python
class Deck()
```

<a id="..deck.Deck.__init__"></a>

#### \_\_init\_\_

```python
def __init__()
```

Initializes a deck of 52 cards (does not shuffle)

<a id="..deck.Deck.shuffle"></a>

#### shuffle

```python
def shuffle()
```

Shuffles the deck randomly


<a id="..deck.Deck.draw"></a>

#### draw

```python
def draw()
```

Removes a card from the deck and returns it

**Returns**:

the card drawn

<a id="..deck.Deck.remove"></a>

#### remove

```python
def remove(card)
```

Removes a specific card from the deck

**Arguments**:

- `card`: the card to be removed

<a id="..game"></a>

# ..game

<a id="..game.Game"></a>

## Game Objects

```python
class Game()
```

<a id="..game.Game.__init__"></a>

#### \_\_init\_\_

```python
def __init__(num_players, big_blind=20, starting_chips=1000)
```

Initializes a game of Texas Hold 'Em with the given number of players, big blind, and starting chips

**Arguments**:

- `num_players`: the number of players in the game, by default these players are simple players
- `big_blind`: The big blind for the game
- `starting_chips`: The number of chips each player starts with

<a id="..game.Game.deal"></a>

#### deal

```python
def deal()
```

Deals two cards to each player in the game


<a id="..game.Game.flop"></a>

#### flop

```python
def flop()
```

Deals the flop and adds it to the community cards

**Returns**:

an array of the community cards, in this case just the 3 flopped cards

<a id="..game.Game.turn"></a>

#### turn

```python
def turn()
```

Deals the turn and adds it to the community cards

**Returns**:

a list of the community cards, in this case  the 3 flop cards plus the turn card

<a id="..game.Game.river"></a>

#### river

```python
def river()
```

Deals the river and adds it to the community cards

**Returns**:

a list of the community cards, in this case  the 3 flop cards plus the turn card and the river card

<a id="..game.Game.get_bets"></a>

#### get\_bets

```python
def get_bets()
```

Gets the bets from each player in the round, keeping track of the pot and the required bet to stay in the round

**Returns**:

the number of players still in the round

<a id="..game.Game.determine_round_winners"></a>

#### determine\_round\_winners

```python
def determine_round_winners()
```

Determines the winners of the round based on the best hand of five cards from each player

**Returns**:

a list of players who have the best hand (usually just 1 player)

<a id="..game_utils"></a>

# ..game\_utils

<a id="..game_utils.get_card_counts"></a>

#### get\_card\_counts

```python
def get_card_counts(hand, community_cards)
```

Returns a list of the counts of each rank in the hand and community cards

**Arguments**:

- `hand`: list of 2 cards
- `community_cards`: list of 3 to 5 cards

**Returns**:

list of integers representing the counts of each rank 2 to Ace

<a id="..game_utils.get_suite_counts"></a>

#### get\_suite\_counts

```python
def get_suite_counts(hand, community_cards)
```

Returns a list of the counts of each suit in the hand and community cards

**Arguments**:

- `hand`: list of 2 cards
- `community_cards`: list of 3 to 5 cards

**Returns**:

list of integers representing the counts of each suit Hearts, Diamonds, Clubs, Spades

<a id="..game_utils.find_royal_flush"></a>

#### find\_royal\_flush

```python
def find_royal_flush(hand, community_cards)
```

Finds a royal flush in the hand and community cards if it exists

**Arguments**:

- `hand`: list of 2 cards
- `community_cards`: list of 3 to 5 cards

**Returns**:

list of the 5 cards (in order from highest to lowest) that make up the royal flush if it exists,
None otherwise

<a id="..game_utils.find_straight_flush"></a>

#### find\_straight\_flush

```python
def find_straight_flush(hand, community_cards)
```

Finds a straight flush in the hand and community cards if it exists

**Arguments**:

- `hand`: list of 2 cards
- `community_cards`: list of 3 to 5 cards

**Returns**:

list of the 5 cards (in order from highest to lowest) that make up the (best) straight flush if it exists,
None otherwise

<a id="..game_utils.find_four_of_a_kind"></a>

#### find\_four\_of\_a\_kind

```python
def find_four_of_a_kind(hand, community_cards)
```

Finds a four of a kind in the hand and community cards if it exists

**Arguments**:

- `hand`: list of 2 cards
- `community_cards`: list of 3 to 5 cards

**Returns**:

list of the 4 cards that make up the four of a kind and the highest card not in the four of a kind if it
exists, None otherwise

<a id="..game_utils.find_full_house"></a>

#### find\_full\_house

```python
def find_full_house(hand, community_cards)
```

Finds a full house in the hand and community cards if it exists

**Arguments**:

- `hand`: list of 2 cards
- `community_cards`: list of 3 to 5 cards

**Returns**:

list of the best full house if it exists (three of a kind first), None otherwise

<a id="..game_utils.find_flush"></a>

#### find\_flush

```python
def find_flush(hand, community_cards)
```

Finds a flush in the hand and community cards if it exists

**Arguments**:

- `hand`: list of 2 cards
- `community_cards`: list of 3 to 5 cards

**Returns**:

list of the 5 cards that make up the best possible flush if one exists, None otherwise

<a id="..game_utils.find_straight"></a>

#### find\_straight

```python
def find_straight(hand, community_cards)
```

Finds a straight in the hand and community cards if it exists

**Arguments**:

- `hand`: list of 2 cards
- `community_cards`: list of 3 to 5 cards

**Returns**:

list of the 5 cards that make up the best possible straight if one exists, None otherwise

<a id="..game_utils.find_three_of_a_kind"></a>

#### find\_three\_of\_a\_kind

```python
def find_three_of_a_kind(hand, community_cards)
```

Finds a three of a kind in the hand and community cards if it exists

**Arguments**:

- `hand`: list of 2 cards
- `community_cards`: list of 3 to 5 cards

**Returns**:

a list of the three of a kind plus the 2 other highest cards if it exists, None otherwise

<a id="..game_utils.find_two_pair"></a>

#### find\_two\_pair

```python
def find_two_pair(hand, community_cards)
```

Finds two pair in the hand and community cards if it exists

**Arguments**:

- `hand`: list of 2 cards
- `community_cards`: list of 3 to 5 cards

**Returns**:

a list of the 2 pairs (higher one first) and the highest card not in the two pairs if it exists, None
otherwise

<a id="..game_utils.find_single_pair"></a>

#### find\_single\_pair

```python
def find_single_pair(hand, community_cards)
```

Finds a single pair in the hand and community cards if it exists

**Arguments**:

- `hand`: list of 2 cards
- `community_cards`: list of 3 to 5 cards

**Returns**:

the pair and the 3 highest cards not in the pair if it exists, None otherwise

<a id="..game_utils.find_high_card"></a>

#### find\_high\_card

```python
def find_high_card(hand, community_cards)
```

Orders the hand and community cards by rank and returns the 5 highest cards

**Arguments**:

- `hand`: list of 2 cards
- `community_cards`: list of 3 to 5 cards

**Returns**:

list of the 5 highest cards

<a id="..hands"></a>

# ..hands

HAND_FUNCTIONS need to be operated on in the below order BUT ranks are the other way: Royal Flush = 7, and High Card = 0

<a id="..hands.HandOfTwo"></a>

## HandOfTwo Objects

```python
class HandOfTwo()
```

<a id="..hands.HandOfTwo.add_card"></a>

#### add\_card

```python
def add_card(card)
```

Adds a card to the hand if there are less than 2 cards

**Arguments**:

- `card`: 

<a id="..hands.HandOfFive"></a>

## HandOfFive Objects

```python
class HandOfFive()
```

<a id="..hands.HandOfFive.__init__"></a>

#### \_\_init\_\_

```python
def __init__(hand_cards, community_cards)
```

**Arguments**:

- `hand_cards`: list of 2 cards
- `community_cards`: list of 5 cards

<a id="..hands.HandOfFive.determine_best"></a>

#### determine\_best

```python
def determine_best(hand_cards, community_cards)
```

Determines the best hand from the hand and community cards

**Arguments**:

- `hand_cards`: list of 2 cards
- `community_cards`: list of 5 cards

**Returns**:

the 5 cards that make up the best hand, ordered so that the hand is easily compared to other hands
Ex: a straight flush would be ordered from highest to lowest card, a full house would be ordered with the three
of a kind first, then the pair

<a id="..hands.HandOfFive.__gt__"></a>

#### \_\_gt\_\_

```python
def __gt__(other)
```

Compares two hands to see if the first hand is better than the second

**Arguments**:

- `other`: the other hand to compare to

**Returns**:

True if this hand is better than the other, False otherwise (including when they are equal)

<a id="..hands.HandOfFive.__eq__"></a>

#### \_\_eq\_\_

```python
def __eq__(other)
```

Compares two hands to see if they are equal

**Arguments**:

- `other`: the other hand to compare to

**Returns**:

True if the hands are equal, False otherwise

<a id="..hands.HandOfFive.__lt__"></a>

#### \_\_lt\_\_

```python
def __lt__(other)
```

Compares two hands to see if the first hand is worse than the second

**Arguments**:

- `other`: the other hand to compare to

**Returns**:

True if this hand is worse than the other, False otherwise (including when they are equal)

<a id="..player"></a>

# ..player

<a id="..player.Player"></a>

## Player Objects

```python
class Player()
```

<a id="..player.Player.__init__"></a>

#### \_\_init\_\_

```python
def __init__(position, chips=1000)
```

Initializes a player with a position (0 to n-1) and chips

**Arguments**:

- `position`: int from 0 to n-1
- `chips`: int representing the number of chips the player starts with (default 1000)

<a id="..player.Player.bet"></a>

#### bet

```python
def bet(amount)
```

Bets the given amount if the player has enough chips, otherwise bets all chips

**Arguments**:

- `amount`: amount the player wants to bet

**Returns**:

the amount the player actually bets

<a id="..player.Player.fold"></a>

#### fold

```python
def fold()
```

Folds the player's hand and marks them as out of the round

**Returns**:

the player's round bet (0)

<a id="..player.Player.decide"></a>

#### decide

```python
def decide(round_num, pot, all_day, big_blind, community_cards, player_ct)
```

Abstract method for deciding what to do in a round

**Arguments**:

- `round_num`: 0 for pre-flop, 1 for flop, 2 for turn, 3 for river
- `pot`: the current pot
- `all_day`: the current highest bet (including all rounds)
- `big_blind`: the big blind for the game
- `community_cards`: the community cards (list of 0 to 5 cards)
- `player_ct`: number of players in the game

**Returns**:

a tuple of the action ("fold", "check", "call", "raise") and the amount to bet

<a id="..player.SimplePlayer"></a>

## SimplePlayer Objects

```python
class SimplePlayer(Player)
```

<a id="..player.SimplePlayer.decide"></a>

#### decide

```python
def decide(round_num, pot, all_day, big_blind, community_cards, player_ct)
```

Simple player calls big blind, then checks, folds to any bet past BB

**Arguments**:

- `round_num`: 0 for pre-flop, 1 for flop, 2 for turn, 3 for river
- `pot`: the current pot
- `all_day`: the current highest bet (including all rounds)
- `big_blind`: the big blind for the game
- `community_cards`: the community cards (list of 0 to 5 cards)
- `player_ct`: number of players in the game

**Returns**:

a tuple of the action ("fold", "check", "call", "raise") and the amount to bet

<a id="..player.AllInPreFlopPlayer"></a>

## AllInPreFlopPlayer Objects

```python
class AllInPreFlopPlayer(Player)
```

<a id="..player.AllInPreFlopPlayer.decide"></a>

#### decide

```python
def decide(round_num, pot, all_day, big_blind, community_cards, player_ct)
```

Goes all in preflop if win rate is above threshold, otherwise check/folds

**Arguments**:

- `round_num`: 0 for pre-flop, 1 for flop, 2 for turn, 3 for river
- `pot`: the current pot
- `all_day`: the current highest bet (including all rounds)
- `big_blind`: the big blind for the game
- `community_cards`: the community cards (list of 0 to 5 cards)
- `player_ct`: number of players in the game

**Returns**:

a tuple of the action ("fold", "check", "call", "raise") and the amount to bet

<a id="..player.LimpPlayer"></a>

## LimpPlayer Objects

```python
class LimpPlayer(Player)
```

<a id="..player.LimpPlayer.decide"></a>

#### decide

```python
def decide(round_num, pot, all_day, big_blind, community_cards, player_ct)
```

Calls if win rate is above threshold, otherwise check/folds

**Arguments**:

- `round_num`: 0 for pre-flop, 1 for flop, 2 for turn, 3 for river
- `pot`: the current pot
- `all_day`: the current highest bet (including all rounds)
- `big_blind`: the big blind for the game
- `community_cards`: the community cards (list of 0 to 5 cards)
- `player_ct`: number of players in the game

**Returns**:

a tuple of the action ("fold", "check", "call", "raise") and the amount to bet

<a id="..preflop_stats_repository"></a>

# ..preflop\_stats\_repository

<a id="..preflop_stats_repository.PreflopStatsRepository"></a>

## PreflopStatsRepository Objects

```python
class PreflopStatsRepository()
```

<a id="..preflop_stats_repository.PreflopStatsRepository.__init__"></a>

#### \_\_init\_\_

```python
def __init__(use_database=False)
```

Constructor for the PreflopStatsRepository

**Arguments**:

- `use_database`: Default False. gets the data from the database if True and DATABASE_CONN_STRING env variable is set,
otherwise gets the data from the csv file. If you don't know what to set this to, leave it as False.

<a id="..preflop_stats_repository.PreflopStatsRepository.get_win_rate"></a>

#### get\_win\_rate

```python
def get_win_rate(card1_rank, card2_rank, suited, player_count)
```

Gets win rate and related info for the given cards and player count

**Arguments**:

- `card1_rank`: 0-12, 0 is 2, 12 is Ace
- `card2_rank`: 0-12, 0 is 2, 12 is Ace
- `suited`: True if the cards are the same suite, False otherwise
- `player_count`: number of players in the game

**Returns**:

a dict with the following values: card_1_rank, card_2_rank, suited, win_rate, rank, percentile,
player_count, sklansky, sklansky_position, modified_sklansky, modified_sklansky_position

<a id="..relative_ranking"></a>

# ..relative\_ranking

<a id="..relative_ranking.rank_hand"></a>

#### rank\_hand

```python
def rank_hand(hand, community_cards)
```

*Post Flop*

Ranks a hand of two cards and 3-5 five community cards relative to all other possible hands, based only on known cards
Known issue: odds assume no additional community cards. Works best for after the river, does an ok approx before then

**Arguments**:

- `hand`: a list of 2 cards (Card objects)
- `community_cards`: a list of 3-5 cards (Card objects)

**Returns**:

a tuple of the number of wins, losses, and ties for the given hand

<a id="..relative_ranking.get_hand_stats"></a>

#### get\_hand\_stats

```python
def get_hand_stats(hand, community_cards, player_count)
```

*Post Flop*

Provides expected outcome information for a given hand based on the number of players
Known issue: odds assume no additional community cards. Works best for after the river, does an ok approx before then

**Arguments**:

- `hand`: 2 cards
- `community_cards`: a list of 3-5 cards
- `player_count`: 2+

**Returns**:

dict with keys: "two_player_effective_win_rate", "percentile", "win_rate"

<a id="..sklansky"></a>

# ..sklansky

<a id="..sklansky.sklansky_playable_position"></a>

#### sklansky\_playable\_position

```python
def sklansky_playable_position(position: int)
```

Returns the playable positions for a given Sklansky rank

https://en.wikipedia.org/wiki/Texas_hold_%27em_starting_hands#Sklansky_hand_groups

**Arguments**:

- `position`: int from 1 to 9

**Returns**:

the positions and situations where the hand is playable

<a id="..sklansky.sklansky_rank"></a>

#### sklansky\_rank

```python
def sklansky_rank(card1, card2)
```

Returns the Sklansky rank of the two hole cards passed in

https://en.wikipedia.org/wiki/Texas_hold_%27em_starting_hands#Sklansky_hand_groups

**Arguments**:

- `card1`: a Card object
- `card2`: a (different) Card object

**Returns**:

an int from 1 to 9, 1 being the best hand and 9 being the worst

