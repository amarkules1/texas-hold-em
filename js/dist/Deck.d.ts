import { Card } from './types';
export declare class Deck {
    private cards;
    constructor();
    /**
     * Initializes a standard deck of 52 cards
     */
    private initialize;
    /**
     * Shuffles the deck using the Fisher-Yates algorithm
     */
    shuffle(): void;
    /**
     * Draws a card from the top of the deck
     * @returns The drawn card
     * @throws Error if the deck is empty
     */
    drawCard(): Card;
    /**
     * Gets the number of cards remaining in the deck
     */
    cardsRemaining(): number;
}
