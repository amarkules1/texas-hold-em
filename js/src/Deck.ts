import { Card } from './types';

export class Deck {
    private cards: Card[] = [];

    constructor(initialize: boolean = true) {
        if (initialize) {
            this.initialize();
        }
    }

    /**
     * Initializes a standard deck of 52 cards
     */
    private initialize(): void {
        for (let suit = 0; suit < 4; suit++) {
            for (let rank = 0; rank < 13; rank++) {
                this.cards.push({ rank, suit });
            }
        }
    }

    /**
     * Shuffles the deck using the Fisher-Yates algorithm
     */
    public shuffle(): void {
        for (let i = this.cards.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [this.cards[i], this.cards[j]] = [this.cards[j], this.cards[i]];
        }
    }

    /**
     * Draws a card from the top of the deck
     * @returns The drawn card
     * @throws Error if the deck is empty
     */
    public drawCard(): Card {
        if (this.cards.length === 0) {
            throw new Error('No cards left in deck');
        }
        return this.cards.pop()!;
    }

    /**
     * Draws a specified number of cards from the top of the deck
     * @param numCards The number of cards to draw (default is 1)
     * @returns An array of the drawn cards
     * @throws Error if there are not enough cards in the deck
     */
    public draw(numCards: number = 1): Card[] {
        if (numCards > this.cards.length) {
            throw new Error("Not enough cards in deck to draw.");
        }
        // Use splice to remove and return the top numCards cards
        return this.cards.splice(0, numCards);
    }

    /**
     * Gets the number of cards remaining in the deck
     */
    public cardsRemaining(): number {
        return this.cards.length;
    }

    /**
     * Removes specific cards from the deck.
     * @param cardsToRemove An array of Card objects to remove.
     */
    public removeCards(cardsToRemove: Card[]): void {
        const cardSet = new Set(cardsToRemove.map(card => `${card.rank}-${card.suit}`));
        this.cards = this.cards.filter(card => !cardSet.has(`${card.rank}-${card.suit}`));
    }

    /**
     * Creates a deep copy of the deck.
     * @returns A new Deck instance with the same cards.
     */
    public clone(): Deck {
        const clonedDeck = new Deck(false); // Don't initialize with standard 52 cards
        // Perform a deep copy of the cards array
        clonedDeck.cards = this.cards.map(card => ({ ...card }));
        return clonedDeck;
    }

    /**
     * Gets a copy of the cards currently in the deck.
     * @returns An array of Card objects.
     */
    public getCards(): Card[] {
        return [...this.cards]; // Return a copy to prevent external modification
    }
}
