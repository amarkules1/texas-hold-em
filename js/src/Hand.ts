import { Card } from './types';
import { HAND_FUNCTIONS, HAND_TYPE_NAMES } from './HandUtils';

export class HandOfTwo {
    private cards: Card[] = [];

    constructor(cards: Card[] = []) {
        this.cards = cards;
    }

    /**
     * Adds a card to the hand if there are less than 2 cards
     */
    public addCard(card: Card): void {
        if (this.cards.length < 2) {
            this.cards.push(card);
        } else {
            throw new Error("Hand already has 2 cards");
        }
    }

    /**
     * Gets the cards in the hand
     */
    public getCards(): Card[] {
        return [...this.cards];
    }
}

export class HandOfFive {
    private handCards: Card[];
    private communityCards: Card[];
    private handRank: number | null = null;
    private hand: Card[] = [];

    /**
     * @param handCards list of 2 cards
     * @param communityCards list of 5 cards
     */
    constructor(handCards: Card[], communityCards: Card[]) {
        this.handCards = handCards;
        this.communityCards = communityCards;
        this.determineBest(handCards, communityCards);
    }

    /**
     * Determines the best hand from the hand and community cards
     * @param handCards list of 2 cards
     * @param communityCards list of 5 cards
     * @returns the 5 cards that make up the best hand, ordered so that the hand is easily compared to other hands
     * Ex: a straight flush would be ordered from highest to lowest card, a full house would be ordered with the three
     * of a kind first, then the pair
     */
    private determineBest(handCards: Card[], communityCards: Card[]): void {
        for (let i = 0; i < HAND_FUNCTIONS.length; i++) {
            const result = HAND_FUNCTIONS[i](handCards, communityCards);
            if (result !== null) {
                this.hand = result;
                this.handRank = 9 - i;
                break;
            }
        }
    }

    /**
     * Gets the name of the hand rank
     */
    public getHandRankName(): string {
        return this.handRank !== null ? HAND_TYPE_NAMES[this.handRank] : "Invalid Hand";
    }

    /**
     * Gets the full hand rank description
     */
    public getFullHandRank(): string {
        if (this.handRank === null) return "Invalid Hand";
        const cardNames = this.hand.map(card => 
            `${["2","3","4","5","6","7","8","9","10","J","Q","K","A"][card.rank]}${["♥","♦","♣","♠"][card.suit]}`
        );
        return `${HAND_TYPE_NAMES[this.handRank]} [${cardNames.join(",")}]`;
    }

    /**
     * Compares this hand to another hand
     * @returns true if this hand is better than the other hand
     */
    public greaterThan(other: HandOfFive): boolean {
        if (this.handRank === null || other.handRank === null) return false;
        if (this.handRank > other.handRank) return true;
        if (this.handRank < other.handRank) return false;
        
        for (let i = 0; i < 5; i++) {
            if (this.hand[i].rank > other.hand[i].rank) return true;
            if (this.hand[i].rank < other.hand[i].rank) return false;
        }
        return false;
    }

    /**
     * Checks if this hand is equal to another hand
     */
    public equals(other: HandOfFive): boolean {
        if (this.handRank === null || other.handRank === null) return false;
        if (this.handRank !== other.handRank) return false;
        
        for (let i = 0; i < 5; i++) {
            if (this.hand[i].rank !== other.hand[i].rank) return false;
        }
        return true;
    }

    /**
     * Compares this hand to another hand
     * @returns true if this hand is worse than the other hand
     */
    public lessThan(other: HandOfFive): boolean {
        return !this.greaterThan(other) && !this.equals(other);
    }
}
