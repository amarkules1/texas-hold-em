import { Card, PlayerAction, PlayerDecision } from './types';
import { PreflopStatsRepository } from './PreflopStatsRepository';

export class Player {
    protected hand: Card[] = [];
    protected chips: number;
    protected roundBet: number = 0;
    protected inRound: boolean = true;
    protected position: number;

    constructor(position: number, chips: number = 1000) {
        this.position = position;
        this.chips = chips;
    }

    /**
     * Sets the player's hand
     * @param hand Array of two cards
     */
    public setHand(hand: Card[]): void {
        if (hand.length !== 2) throw new Error('Hand must contain exactly 2 cards');
        this.hand = [...hand];
    }

    /**
     * Bets the given amount if the player has enough chips, otherwise bets all chips
     * @param amount amount the player wants to bet
     * @returns the amount the player actually bets
     */
    public bet(amount: number): number {
        const actualBet = Math.min(amount, this.chips);
        this.chips -= actualBet;
        this.roundBet += actualBet;
        return actualBet;
    }

    /**
     * Gets the player's current chips
     */
    public getChips(): number {
        return this.chips;
    }

    /**
     * Gets whether the player is still in the current round
     */
    public isInRound(): boolean {
        return this.inRound;
    }

    /**
     * Gets the player's current bet for the round
     */
    public getRoundBet(): number {
        return this.roundBet;
    }

    /**
     * Resets the player's round bet to 0
     */
    public resetRoundBet(): void {
        this.roundBet = 0;
    }

    /**
     * Gets the player's position at the table
     */
    public getPosition(): number {
        return this.position;
    }
}

export class LimpPlayer extends Player {
    private threshold: number | number[];
    private preflopStatsRepo: PreflopStatsRepository;
    private isVariableThreshold: boolean;

    constructor(position: number, chips: number = 1000, threshold: number | number[] = 0.5) {
        super(position, chips);
        this.threshold = threshold;
        this.preflopStatsRepo = new PreflopStatsRepository();
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
    public decide(
        roundNum: number,
        pot: number,
        allDay: number,
        bigBlind: number,
        communityCards: Card[],
        playerCt: number
    ): PlayerDecision {
        if (roundNum === 0) {
            const currentThreshold = this.isVariableThreshold 
                ? (this.threshold as number[])[this.position] 
                : this.threshold as number;

            const stats = this.preflopStatsRepo.getWinRate(
                this.hand[0].rank,
                this.hand[1].rank,
                this.hand[0].suit === this.hand[1].suit,
                playerCt
            );

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

export class AllInPreFlopPlayer extends Player {
    private threshold: number;
    private preflopStatsRepo: PreflopStatsRepository;
    private inCheckFold: boolean = false;

    constructor(position: number, chips: number = 1000, threshold: number = 0.5) {
        super(position, chips);
        this.threshold = threshold;
        this.preflopStatsRepo = new PreflopStatsRepository();
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
    public decide(
        roundNum: number,
        pot: number,
        allDay: number,
        bigBlind: number,
        communityCards: Card[],
        playerCt: number
    ): PlayerDecision {
        if (roundNum === 0 && !this.inCheckFold) {
            const stats = this.preflopStatsRepo.getWinRate(
                this.hand[0].rank,
                this.hand[1].rank,
                this.hand[0].suit === this.hand[1].suit,
                playerCt
            );

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
