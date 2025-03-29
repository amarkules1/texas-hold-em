import { HandOfTwo, HandOfFive } from '../Hand';
import { Card } from '../types';

describe('HandOfTwo', () => {
    it('should allow adding up to 2 cards', () => {
        const hand = new HandOfTwo();
        const card1: Card = { rank: 0, suit: 0 };
        const card2: Card = { rank: 1, suit: 1 };
        
        hand.addCard(card1);
        hand.addCard(card2);
        
        expect(hand.getCards()).toHaveLength(2);
        expect(() => hand.addCard(card1)).toThrow();
    });
});

describe('HandOfFive', () => {
    it('should correctly identify a royal flush', () => {
        const hand: Card[] = [
            { rank: 12, suit: 0 },
            { rank: 11, suit: 0 }
        ];
        const community: Card[] = [
            { rank: 10, suit: 0 },
            { rank: 9, suit: 0 },
            { rank: 8, suit: 0 }
        ];
        
        const handOfFive = new HandOfFive(hand, community);
        expect(handOfFive.getHandRankName()).toBe('Royal Flush');
    });
    
    it('should correctly compare hands', () => {
        const hand1 = new HandOfFive(
            [{ rank: 12, suit: 0 }, { rank: 12, suit: 1 }],
            [{ rank: 12, suit: 2 }, { rank: 12, suit: 3 }, { rank: 0, suit: 0 }]
        );
        
        const hand2 = new HandOfFive(
            [{ rank: 11, suit: 0 }, { rank: 11, suit: 1 }],
            [{ rank: 11, suit: 2 }, { rank: 11, suit: 3 }, { rank: 0, suit: 0 }]
        );
        
        expect(hand1.greaterThan(hand2)).toBe(true);
        expect(hand2.lessThan(hand1)).toBe(true);
    });
});
