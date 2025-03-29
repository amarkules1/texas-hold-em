"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.HAND_FUNCTIONS = exports.HAND_TYPE_NAMES = void 0;
exports.getCardCounts = getCardCounts;
exports.getSuitCounts = getSuitCounts;
exports.createCard = createCard;
exports.findRoyalFlush = findRoyalFlush;
exports.findStraightFlush = findStraightFlush;
exports.findFourOfAKind = findFourOfAKind;
exports.findFullHouse = findFullHouse;
exports.findFlush = findFlush;
exports.findStraight = findStraight;
exports.findThreeOfAKind = findThreeOfAKind;
exports.findTwoPair = findTwoPair;
exports.findSinglePair = findSinglePair;
exports.findHighCard = findHighCard;
exports.HAND_TYPE_NAMES = [
    "High Card", "Pair", "Two Pair", "Three of a Kind", "Straight",
    "Flush", "Full House", "Four of a Kind", "Straight Flush", "Royal Flush"
];
/**
 * Returns a list of the counts of each rank in the hand and community cards
 */
function getCardCounts(hand, communityCards) {
    const rankCounts = new Array(13).fill(0);
    [...hand, ...communityCards].forEach(card => {
        rankCounts[card.rank]++;
    });
    return rankCounts;
}
/**
 * Returns a list of the counts of each suit in the hand and community cards
 */
function getSuitCounts(hand, communityCards) {
    const suitCounts = new Array(4).fill(0);
    [...hand, ...communityCards].forEach(card => {
        suitCounts[card.suit]++;
    });
    return suitCounts;
}
/**
 * Creates a card with the given rank and suit
 */
function createCard(rank, suit) {
    return { rank, suit };
}
/**
 * Finds a royal flush in the hand and community cards if it exists
 */
function findRoyalFlush(hand, communityCards) {
    const suitCounts = getSuitCounts(hand, communityCards);
    for (let i = 0; i < 4; i++) {
        if (suitCounts[i] >= 5) {
            const suitRanks = [...hand, ...communityCards]
                .filter(card => card.suit === i)
                .map(card => card.rank);
            if ([8, 9, 10, 11, 12].every(rank => suitRanks.includes(rank))) {
                return [8, 9, 10, 11, 12].map(rank => createCard(rank, i)).reverse();
            }
        }
    }
    return null;
}
/**
 * Finds a straight flush in the hand and community cards if it exists
 */
function findStraightFlush(hand, communityCards) {
    const suitCounts = getSuitCounts(hand, communityCards);
    for (let i = 0; i < 4; i++) {
        if (suitCounts[i] >= 5) {
            const suitRanks = [...hand, ...communityCards]
                .filter(card => card.suit === i)
                .map(card => card.rank)
                .sort((a, b) => b - a);
            for (let j = 0; j < 9; j++) {
                if ([j, j + 1, j + 2, j + 3, j + 4].every(rank => suitRanks.includes(rank))) {
                    return [j, j + 1, j + 2, j + 3, j + 4].map(rank => createCard(rank, i)).reverse();
                }
            }
        }
    }
    return null;
}
/**
 * Finds a four of a kind in the hand and community cards if it exists
 */
function findFourOfAKind(hand, communityCards) {
    const cardCounts = getCardCounts(hand, communityCards);
    const allCards = [...hand, ...communityCards];
    for (let i = 12; i >= 0; i--) {
        if (cardCounts[i] === 4) {
            const four = [0, 1, 2, 3].map(suit => createCard(i, suit));
            const kicker = allCards
                .filter(card => card.rank !== i)
                .sort((a, b) => b.rank - a.rank)[0];
            return [...four, kicker];
        }
    }
    return null;
}
/**
 * Finds a full house in the hand and community cards if it exists
 */
function findFullHouse(hand, communityCards) {
    const cardCounts = getCardCounts(hand, communityCards);
    const allCards = [...hand, ...communityCards];
    let highestThreeOfAKind = -1;
    let highestPairNotHighest3 = -1;
    for (let i = 12; i >= 0; i--) {
        if (cardCounts[i] === 3) {
            if (highestThreeOfAKind > highestPairNotHighest3) {
                highestPairNotHighest3 = highestThreeOfAKind;
            }
            highestThreeOfAKind = i;
        }
        else if (cardCounts[i] === 2) {
            highestPairNotHighest3 = i;
        }
    }
    if (highestThreeOfAKind !== -1 && highestPairNotHighest3 !== -1) {
        const three = allCards.filter(card => card.rank === highestThreeOfAKind);
        const pair = allCards.filter(card => card.rank === highestPairNotHighest3).slice(0, 2);
        return [...three, ...pair];
    }
    return null;
}
/**
 * Finds a flush in the hand and community cards if it exists
 */
function findFlush(hand, communityCards) {
    const suitCounts = getSuitCounts(hand, communityCards);
    const allCards = [...hand, ...communityCards];
    for (let i = 0; i < 4; i++) {
        if (suitCounts[i] >= 5) {
            const flushCards = allCards
                .filter(card => card.suit === i)
                .sort((a, b) => b.rank - a.rank)
                .slice(0, 5);
            return flushCards;
        }
    }
    return null;
}
/**
 * Finds a straight in the hand and community cards if it exists
 */
function findStraight(hand, communityCards) {
    const cardCounts = getCardCounts(hand, communityCards);
    const allCards = [...hand, ...communityCards];
    for (let i = 8; i >= 0; i--) {
        if ([i, i + 1, i + 2, i + 3, i + 4].every(rank => cardCounts[rank] > 0)) {
            const straightCards = [i, i + 1, i + 2, i + 3, i + 4].map(rank => {
                return allCards.find(card => card.rank === rank);
            });
            return straightCards.sort((a, b) => b.rank - a.rank);
        }
    }
    return null;
}
/**
 * Finds a three of a kind in the hand and community cards if it exists
 */
function findThreeOfAKind(hand, communityCards) {
    const cardCounts = getCardCounts(hand, communityCards);
    const allCards = [...hand, ...communityCards];
    for (let i = 12; i >= 0; i--) {
        if (cardCounts[i] === 3) {
            const three = allCards.filter(card => card.rank === i);
            const kickers = allCards
                .filter(card => card.rank !== i)
                .sort((a, b) => b.rank - a.rank)
                .slice(0, 2);
            return [...three, ...kickers];
        }
    }
    return null;
}
/**
 * Finds two pair in the hand and community cards if it exists
 */
function findTwoPair(hand, communityCards) {
    const cardCounts = getCardCounts(hand, communityCards);
    const allCards = [...hand, ...communityCards];
    const pairs = [];
    for (let i = 12; i >= 0; i--) {
        if (cardCounts[i] === 2) {
            pairs.push(i);
        }
        if (pairs.length === 2)
            break;
    }
    if (pairs.length === 2) {
        const pairCards = allCards
            .filter(card => pairs.includes(card.rank))
            .sort((a, b) => b.rank - a.rank);
        const kicker = allCards
            .filter(card => !pairs.includes(card.rank))
            .sort((a, b) => b.rank - a.rank)[0];
        return [...pairCards, kicker];
    }
    return null;
}
/**
 * Finds a single pair in the hand and community cards if it exists
 */
function findSinglePair(hand, communityCards) {
    const cardCounts = getCardCounts(hand, communityCards);
    const allCards = [...hand, ...communityCards];
    for (let i = 12; i >= 0; i--) {
        if (cardCounts[i] === 2) {
            const pair = allCards.filter(card => card.rank === i);
            const kickers = allCards
                .filter(card => card.rank !== i)
                .sort((a, b) => b.rank - a.rank)
                .slice(0, 3);
            return [...pair, ...kickers];
        }
    }
    return null;
}
/**
 * Orders the hand and community cards by rank and returns the 5 highest cards
 */
function findHighCard(hand, communityCards) {
    return [...hand, ...communityCards]
        .sort((a, b) => b.rank - a.rank)
        .slice(0, 5);
}
exports.HAND_FUNCTIONS = [
    findRoyalFlush,
    findStraightFlush,
    findFourOfAKind,
    findFullHouse,
    findFlush,
    findStraight,
    findThreeOfAKind,
    findTwoPair,
    findSinglePair,
    findHighCard
];
