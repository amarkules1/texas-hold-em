import { Card, PlayerDecision } from './types';
export declare class Player {
    protected hand: Card[];
    protected chips: number;
    protected roundBet: number;
    protected inRound: boolean;
    protected position: number;
    constructor(position: number, chips?: number);
    /**
     * Sets the player's hand
     * @param hand Array of two cards
     */
    setHand(hand: Card[]): void;
    /**
     * Bets the given amount if the player has enough chips, otherwise bets all chips
     * @param amount amount the player wants to bet
     * @returns the amount the player actually bets
     */
    bet(amount: number): number;
    /**
     * Gets the player's current chips
     */
    getChips(): number;
    /**
     * Gets whether the player is still in the current round
     */
    isInRound(): boolean;
    /**
     * Gets the player's current bet for the round
     */
    getRoundBet(): number;
    /**
     * Resets the player's round bet to 0
     */
    resetRoundBet(): void;
    /**
     * Gets the player's position at the table
     */
    getPosition(): number;
}
export declare class LimpPlayer extends Player {
    private threshold;
    private preflopStatsRepo;
    private isVariableThreshold;
    constructor(position: number, chips?: number, threshold?: number | number[]);
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
    decide(roundNum: number, pot: number, allDay: number, bigBlind: number, communityCards: Card[], playerCt: number): PlayerDecision;
}
export declare class AllInPreFlopPlayer extends Player {
    private threshold;
    private preflopStatsRepo;
    private inCheckFold;
    constructor(position: number, chips?: number, threshold?: number);
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
    decide(roundNum: number, pot: number, allDay: number, bigBlind: number, communityCards: Card[], playerCt: number): PlayerDecision;
}
