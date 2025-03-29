"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Game = void 0;
const Player_1 = require("./Player");
const Deck_1 = require("./Deck");
class Game {
    /**
     * Initializes a game of Texas Hold 'Em with the given number of players, big blind, and starting chips
     * @param numPlayers the number of players in the game, by default these players are simple players
     * @param bigBlind The big blind for the game
     * @param startingChips The number of chips each player starts with
     */
    constructor(numPlayers, bigBlind = 20, startingChips = 1000) {
        this.hands = [];
        this.communityCards = [];
        this.players = [];
        this.dealerPosition = 0;
        this.pot = 0;
        this.allDay = 0;
        this.round = 0;
        this.playerCount = numPlayers;
        this.bigBlind = bigBlind;
        this.startingChips = startingChips;
        this.deck = new Deck_1.Deck();
        this.deck.shuffle();
        // Initialize players
        for (let i = 0; i < numPlayers; i++) {
            this.players.push(new Player_1.Player(i, startingChips));
        }
    }
    /**
     * Deals cards to all players and resets the game state for a new hand
     */
    dealNewHand() {
        this.deck.shuffle();
        this.communityCards = [];
        this.hands = [];
        this.pot = 0;
        this.allDay = 0;
        this.round = 0;
        // Deal two cards to each player
        for (let i = 0; i < this.playerCount; i++) {
            const hand = [this.deck.drawCard(), this.deck.drawCard()];
            this.hands.push(hand);
            this.players[i].setHand(hand);
        }
        // Post blinds
        const sbPos = (this.dealerPosition + 1) % this.playerCount;
        const bbPos = (this.dealerPosition + 2) % this.playerCount;
        this.players[sbPos].bet(this.bigBlind / 2);
        this.players[bbPos].bet(this.bigBlind);
        this.pot = this.bigBlind * 1.5;
        this.allDay = this.bigBlind;
    }
    /**
     * Deals the flop
     */
    dealFlop() {
        if (this.round !== 0)
            throw new Error('Cannot deal flop - wrong round');
        this.communityCards = [
            this.deck.drawCard(),
            this.deck.drawCard(),
            this.deck.drawCard()
        ];
        this.round = 1;
    }
    /**
     * Deals the turn
     */
    dealTurn() {
        if (this.round !== 1)
            throw new Error('Cannot deal turn - wrong round');
        this.communityCards.push(this.deck.drawCard());
        this.round = 2;
    }
    /**
     * Deals the river
     */
    dealRiver() {
        if (this.round !== 2)
            throw new Error('Cannot deal river - wrong round');
        this.communityCards.push(this.deck.drawCard());
        this.round = 3;
    }
    /**
     * Gets the current pot size
     */
    getPot() {
        return this.pot;
    }
    /**
     * Gets the current community cards
     */
    getCommunityCards() {
        return [...this.communityCards];
    }
    /**
     * Gets the current round number (0=preflop, 1=flop, 2=turn, 3=river)
     */
    getRound() {
        return this.round;
    }
}
exports.Game = Game;
