import { Card } from './types';
export declare const HAND_TYPE_NAMES: string[];
/**
 * Returns a list of the counts of each rank in the hand and community cards
 */
export declare function getCardCounts(hand: Card[], communityCards: Card[]): number[];
/**
 * Returns a list of the counts of each suit in the hand and community cards
 */
export declare function getSuitCounts(hand: Card[], communityCards: Card[]): number[];
/**
 * Creates a card with the given rank and suit
 */
export declare function createCard(rank: number, suit: number): Card;
/**
 * Finds a royal flush in the hand and community cards if it exists
 */
export declare function findRoyalFlush(hand: Card[], communityCards: Card[]): Card[] | null;
/**
 * Finds a straight flush in the hand and community cards if it exists
 */
export declare function findStraightFlush(hand: Card[], communityCards: Card[]): Card[] | null;
/**
 * Finds a four of a kind in the hand and community cards if it exists
 */
export declare function findFourOfAKind(hand: Card[], communityCards: Card[]): Card[] | null;
/**
 * Finds a full house in the hand and community cards if it exists
 */
export declare function findFullHouse(hand: Card[], communityCards: Card[]): Card[] | null;
/**
 * Finds a flush in the hand and community cards if it exists
 */
export declare function findFlush(hand: Card[], communityCards: Card[]): Card[] | null;
/**
 * Finds a straight in the hand and community cards if it exists
 */
export declare function findStraight(hand: Card[], communityCards: Card[]): Card[] | null;
/**
 * Finds a three of a kind in the hand and community cards if it exists
 */
export declare function findThreeOfAKind(hand: Card[], communityCards: Card[]): Card[] | null;
/**
 * Finds two pair in the hand and community cards if it exists
 */
export declare function findTwoPair(hand: Card[], communityCards: Card[]): Card[] | null;
/**
 * Finds a single pair in the hand and community cards if it exists
 */
export declare function findSinglePair(hand: Card[], communityCards: Card[]): Card[] | null;
/**
 * Orders the hand and community cards by rank and returns the 5 highest cards
 */
export declare function findHighCard(hand: Card[], communityCards: Card[]): Card[];
export declare const HAND_FUNCTIONS: (typeof findRoyalFlush)[];
