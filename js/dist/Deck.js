"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Deck = void 0;
class Deck {
    constructor() {
        this.cards = [];
        this.initialize();
    }
    /**
     * Initializes a standard deck of 52 cards
     */
    initialize() {
        for (let suit = 0; suit < 4; suit++) {
            for (let rank = 0; rank < 13; rank++) {
                this.cards.push({ rank, suit });
            }
        }
    }
    /**
     * Shuffles the deck using the Fisher-Yates algorithm
     */
    shuffle() {
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
    drawCard() {
        if (this.cards.length === 0) {
            throw new Error('No cards left in deck');
        }
        return this.cards.pop();
    }
    /**
     * Gets the number of cards remaining in the deck
     */
    cardsRemaining() {
        return this.cards.length;
    }
}
exports.Deck = Deck;
