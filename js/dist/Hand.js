"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.HandOfFive = exports.HandOfTwo = void 0;
const HandUtils_1 = require("./HandUtils");
class HandOfTwo {
    constructor(cards = []) {
        this.cards = [];
        this.cards = cards;
    }
    /**
     * Adds a card to the hand if there are less than 2 cards
     */
    addCard(card) {
        if (this.cards.length < 2) {
            this.cards.push(card);
        }
        else {
            throw new Error("Hand already has 2 cards");
        }
    }
    /**
     * Gets the cards in the hand
     */
    getCards() {
        return [...this.cards];
    }
}
exports.HandOfTwo = HandOfTwo;
class HandOfFive {
    /**
     * @param handCards list of 2 cards
     * @param communityCards list of 5 cards
     */
    constructor(handCards, communityCards) {
        this.handRank = null;
        this.hand = [];
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
    determineBest(handCards, communityCards) {
        for (let i = 0; i < HandUtils_1.HAND_FUNCTIONS.length; i++) {
            const result = HandUtils_1.HAND_FUNCTIONS[i](handCards, communityCards);
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
    getHandRankName() {
        return this.handRank !== null ? HandUtils_1.HAND_TYPE_NAMES[this.handRank] : "Invalid Hand";
    }
    /**
     * Gets the full hand rank description
     */
    getFullHandRank() {
        if (this.handRank === null)
            return "Invalid Hand";
        const cardNames = this.hand.map(card => `${["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"][card.rank]}${["♥", "♦", "♣", "♠"][card.suit]}`);
        return `${HandUtils_1.HAND_TYPE_NAMES[this.handRank]} [${cardNames.join(",")}]`;
    }
    /**
     * Compares this hand to another hand
     * @returns true if this hand is better than the other hand
     */
    greaterThan(other) {
        if (this.handRank === null || other.handRank === null)
            return false;
        if (this.handRank > other.handRank)
            return true;
        if (this.handRank < other.handRank)
            return false;
        for (let i = 0; i < 5; i++) {
            if (this.hand[i].rank > other.hand[i].rank)
                return true;
            if (this.hand[i].rank < other.hand[i].rank)
                return false;
        }
        return false;
    }
    /**
     * Checks if this hand is equal to another hand
     */
    equals(other) {
        if (this.handRank === null || other.handRank === null)
            return false;
        if (this.handRank !== other.handRank)
            return false;
        for (let i = 0; i < 5; i++) {
            if (this.hand[i].rank !== other.hand[i].rank)
                return false;
        }
        return true;
    }
    /**
     * Compares this hand to another hand
     * @returns true if this hand is worse than the other hand
     */
    lessThan(other) {
        return !this.greaterThan(other) && !this.equals(other);
    }
}
exports.HandOfFive = HandOfFive;
