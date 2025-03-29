import { Card } from './types';
export declare class Game {
    private deck;
    private hands;
    private communityCards;
    private players;
    private dealerPosition;
    private bigBlind;
    private startingChips;
    private pot;
    private allDay;
    private round;
    private playerCount;
    /**
     * Initializes a game of Texas Hold 'Em with the given number of players, big blind, and starting chips
     * @param numPlayers the number of players in the game, by default these players are simple players
     * @param bigBlind The big blind for the game
     * @param startingChips The number of chips each player starts with
     */
    constructor(numPlayers: number, bigBlind?: number, startingChips?: number);
    /**
     * Deals cards to all players and resets the game state for a new hand
     */
    dealNewHand(): void;
    /**
     * Deals the flop
     */
    dealFlop(): void;
    /**
     * Deals the turn
     */
    dealTurn(): void;
    /**
     * Deals the river
     */
    dealRiver(): void;
    /**
     * Gets the current pot size
     */
    getPot(): number;
    /**
     * Gets the current community cards
     */
    getCommunityCards(): Card[];
    /**
     * Gets the current round number (0=preflop, 1=flop, 2=turn, 3=river)
     */
    getRound(): number;
}
