import { Card } from './types';
export declare class HandOfTwo {
    private cards;
    constructor(cards?: Card[]);
    /**
     * Adds a card to the hand if there are less than 2 cards
     */
    addCard(card: Card): void;
    /**
     * Gets the cards in the hand
     */
    getCards(): Card[];
}
export declare class HandOfFive {
    private handCards;
    private communityCards;
    private handRank;
    private hand;
    /**
     * @param handCards list of 2 cards
     * @param communityCards list of 5 cards
     */
    constructor(handCards: Card[], communityCards: Card[]);
    /**
     * Determines the best hand from the hand and community cards
     * @param handCards list of 2 cards
     * @param communityCards list of 5 cards
     * @returns the 5 cards that make up the best hand, ordered so that the hand is easily compared to other hands
     * Ex: a straight flush would be ordered from highest to lowest card, a full house would be ordered with the three
     * of a kind first, then the pair
     */
    private determineBest;
    /**
     * Gets the name of the hand rank
     */
    getHandRankName(): string;
    /**
     * Gets the full hand rank description
     */
    getFullHandRank(): string;
    /**
     * Compares this hand to another hand
     * @returns true if this hand is better than the other hand
     */
    greaterThan(other: HandOfFive): boolean;
    /**
     * Checks if this hand is equal to another hand
     */
    equals(other: HandOfFive): boolean;
    /**
     * Compares this hand to another hand
     * @returns true if this hand is worse than the other hand
     */
    lessThan(other: HandOfFive): boolean;
}
