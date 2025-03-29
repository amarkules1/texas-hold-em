import { Card } from './types';

export class Deck {
    private cards: Card[] = [];

    constructor() {
        this.initialize();
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
     * Gets the number of cards remaining in the deck
     */
    public cardsRemaining(): number {
        return this.cards.length;
    }
}
