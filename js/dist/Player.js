"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.AllInPreFlopPlayer = exports.LimpPlayer = exports.Player = void 0;
const PreflopStatsRepository_1 = require("./PreflopStatsRepository");
class Player {
    constructor(position, chips = 1000) {
        this.hand = [];
        this.roundBet = 0;
        this.inRound = true;
        this.position = position;
        this.chips = chips;
    }
    /**
     * Sets the player's hand
     * @param hand Array of two cards
     */
    setHand(hand) {
        if (hand.length !== 2)
            throw new Error('Hand must contain exactly 2 cards');
        this.hand = [...hand];
    }
    /**
     * Bets the given amount if the player has enough chips, otherwise bets all chips
     * @param amount amount the player wants to bet
     * @returns the amount the player actually bets
     */
    bet(amount) {
        const actualBet = Math.min(amount, this.chips);
        this.chips -= actualBet;
        this.roundBet += actualBet;
        return actualBet;
    }
    /**
     * Gets the player's current chips
     */
    getChips() {
        return this.chips;
    }
    /**
     * Gets whether the player is still in the current round
     */
    isInRound() {
        return this.inRound;
    }
    /**
     * Gets the player's current bet for the round
     */
    getRoundBet() {
        return this.roundBet;
    }
    /**
     * Resets the player's round bet to 0
     */
    resetRoundBet() {
        this.roundBet = 0;
    }
    /**
     * Gets the player's position at the table
     */
    getPosition() {
        return this.position;
    }
}
exports.Player = Player;
class LimpPlayer extends Player {
    constructor(position, chips = 1000, threshold = 0.5) {
        super(position, chips);
        this.threshold = threshold;
        this.preflopStatsRepo = new PreflopStatsRepository_1.PreflopStatsRepository();
        this.isVariableThreshold = Array.isArray(threshold);
    }
    /**
     * Calls if win rate is above threshold, otherwise check/folds
     * @param roundNum 0 for pre-flop, 1 for flop, 2 for turn, 3 for river
     * @param pot the current pot
     * @param allDay the current highest bet (including all rounds)
     * @param bigBlind the big blind for the game
     * @param communityCards the community cards (list of 0 to 5 cards)
     * @param playerCt number of players in the game
     * @returns a tuple of the action ("fold", "check", "call", "raise") and the amount to bet
     */
    decide(roundNum, pot, allDay, bigBlind, communityCards, playerCt) {
        if (roundNum === 0) {
            const currentThreshold = this.isVariableThreshold
                ? this.threshold[this.position]
                : this.threshold;
            const stats = this.preflopStatsRepo.getWinRate(this.hand[0].rank, this.hand[1].rank, this.hand[0].suit === this.hand[1].suit, playerCt);
            if (stats.winRate > currentThreshold) {
                const toCall = allDay - this.roundBet;
                return { action: "call", amount: toCall };
            }
        }
        const toCall = allDay - this.roundBet;
        return toCall === 0
            ? { action: "check", amount: 0 }
            : { action: "fold", amount: 0 };
    }
}
exports.LimpPlayer = LimpPlayer;
class AllInPreFlopPlayer extends Player {
    constructor(position, chips = 1000, threshold = 0.5) {
        super(position, chips);
        this.inCheckFold = false;
        this.threshold = threshold;
        this.preflopStatsRepo = new PreflopStatsRepository_1.PreflopStatsRepository();
    }
    /**
     * Goes all in preflop if win rate is above threshold, otherwise check/folds
     * @param roundNum 0 for pre-flop, 1 for flop, 2 for turn, 3 for river
     * @param pot the current pot
     * @param allDay the current highest bet (including all rounds)
     * @param bigBlind the big blind for the game
     * @param communityCards the community cards (list of 0 to 5 cards)
     * @param playerCt number of players in the game
     * @returns a tuple of the action ("fold", "check", "call", "raise") and the amount to bet
     */
    decide(roundNum, pot, allDay, bigBlind, communityCards, playerCt) {
        if (roundNum === 0 && !this.inCheckFold) {
            const stats = this.preflopStatsRepo.getWinRate(this.hand[0].rank, this.hand[1].rank, this.hand[0].suit === this.hand[1].suit, playerCt);
            if (stats.winRate > this.threshold) {
                return { action: "raise", amount: this.chips };
            }
            this.inCheckFold = true;
        }
        const toCall = allDay - this.roundBet;
        return toCall === 0
            ? { action: "check", amount: 0 }
            : { action: "fold", amount: 0 };
    }
}
exports.AllInPreFlopPlayer = AllInPreFlopPlayer;
