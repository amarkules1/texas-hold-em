import { describe, it, expect, beforeAll } from '@jest/globals';
import { RelativeRanking } from '../RelativeRanking';
import { Card } from '../types';
import { PreflopStatsRepository } from '../PreflopStatsRepository';
import { PostflopStatsRepository } from '../PostflopStatsRepository';
import { HandOfTwo } from '../Hand'; // Import HandOfTwo
import { Deck } from '../Deck';

// Mock data for repositories (replace with actual paths or setup)
const mockPreflopDataPath = 'path/to/your/preflop_stats.json'; // Adjust path
const mockPostflopDataPath = 'path/to/your/postflop_stats.json'; // Adjust path

// Helper to create a HandOfTwo object
const createHand = (cards: Card[]): HandOfTwo => {
    if (cards.length !== 2) throw new Error('Hand must have exactly 2 cards');
    return new HandOfTwo(cards);
}

describe('RelativeRanking', () => {
    let relativeRanker: RelativeRanking;
    let preflopRepo: PreflopStatsRepository;
    let postflopRepo: PostflopStatsRepository;

    // Mock the repositories - adjust implementation as needed
    // This is a very basic mock. You might need a more sophisticated setup.
    beforeAll(() => {
        relativeRanker = new RelativeRanking();
    });

    describe('getHandRankDetails - Preflop', () => {
        it('should return correct details for AA vs 2 players', () => {
            const hand = createHand([{ rank: 12, suit: 0 }, { rank: 12, suit: 1 }]); // AA
            const details = relativeRanker.getHandRankDetails(hand, null, 2);
            expect(details.expectedWinRate).toBeCloseTo(0.85); 
            expect(details.percentile).toBeCloseTo(100, 2);
        });

        it('should return correct details for 72o vs 6 players', () => {
            const hand = createHand([{ rank: 5, suit: 0 }, { rank: 0, suit: 1 }]); // 72o
            const details = relativeRanker.getHandRankDetails(hand, null, 6);
            expect(details.expectedWinRate).toBeCloseTo(0.075);
            expect(details.percentile).toBeGreaterThan(0);
            expect(details.percentile).toBeLessThan(10);
        });

        it('should throw error for invalid player count', () => {
            const hand = createHand([{ rank: 12, suit: 0 }, { rank: 12, suit: 1 }]);
            expect(() => relativeRanker.getHandRankDetails(hand, null, 1)).toThrow("Player count must be at least 2");
        });
    });

    describe('rankHandPostRiver', () => {
        it('should calculate win rate correctly post-river (AA vs KK on low board)', () => {
            const hand = createHand([{ rank: 12, suit: 0 }, { rank: 12, suit: 1 }]); // AA
            const communityCards: Card[] = [
                { rank: 2, suit: 0 }, { rank: 3, suit: 1 }, { rank: 4, suit: 2 }, // Flop
                { rank: 7, suit: 0 }, // Turn
                { rank: 8, suit: 1 }  // River
            ];
            // For deterministic post-river, simulation isn't strictly needed if we compare vs all hands
            // But the current implementation uses simulation, so we test that.
            // We expect AA to win almost always here unless opponent got lucky runner-runner.
            // Let's mock the Deck behavior or run enough simulations.
            const winRate = relativeRanker.rankHandPostRiver(hand, communityCards, 2, 5000); // More sims for accuracy
            // AA has the best possible hand (Ace high) on this board
            expect(winRate).toBeGreaterThan(0.8); // Should win most unless opponent had runner-runner straight/flush unlikely
        });

        it('should calculate win rate for a dominated hand (KK vs AA on low board)', () => {
             const hand = createHand([{ rank: 11, suit: 0 }, { rank: 11, suit: 1 }]); // KK
             const communityCards: Card[] = [
                { rank: 2, suit: 0 }, { rank: 3, suit: 1 }, { rank: 4, suit: 2 },
                { rank: 7, suit: 0 }, 
                { rank: 8, suit: 1 }
             ];
             const winRate = relativeRanker.rankHandPostRiver(hand, communityCards, 2, 5000); // Player count 2
             // KK loses to AA, might chop with another KK, beats everything else.
             // Win rate depends heavily on whether the single opponent could have AA.
             // Given AA exists, winrate < 1. Let's expect it to win against most random hands.
             expect(winRate).toBeGreaterThan(0.8);
        });

        it('should handle ties correctly (e.g., same straight)', () => {
            const hand1 = createHand([{ rank: 11, suit: 0 }, { rank: 2, suit: 1 }]); // T9 for J high straight
            const communityCards: Card[] = [
                { rank: 7, suit: 0 }, { rank: 6, suit: 1 }, { rank: 5, suit: 2 }, // J, 7, 6
                { rank: 4, suit: 3 }, 
                { rank: 3, suit: 0 }
            ];
             const hand2 = createHand([{ rank: 8, suit: 0 }, { rank: 9, suit: 1 }]);
             // Vs 1 opponent. If opponent has 98 too => tie. If opponent has 7x => player wins. etc.
             const winRate = relativeRanker.rankHandPostRiver(hand1, communityCards, 2, 10000);
             expect(winRate).toBeGreaterThan(0.4); 
             expect(winRate).toBeLessThan(0.6); // Should tie sometimes
        });
    });

    describe('rankHandPostTurn', () => {
        it('should estimate win rate correctly post-turn (set vs flush draw)', () => {
            const hand = createHand([{ rank: 10, suit: 0 }, { rank: 10, suit: 1 }]); // JJ set
            const communityCards: Card[] = [
                { rank: 10, suit: 2 }, { rank: 2, suit: 0 }, { rank: 7, suit: 0 }, // Flop Jc 2h 7h
                { rank: 8, suit: 0 }  // Turn 8h (flush draw possible)
            ];
            const winRate = relativeRanker.rankHandPostTurn(hand, communityCards, 2, 5000);
            expect(winRate).toBeGreaterThan(0.85); 
        });
    });

    describe('rankHandPostFlop', () => {
        it('should estimate win rate correctly post-flop (top pair vs gutshot)', () => {
            const hand = createHand([{ rank: 12, suit: 0 }, { rank: 8, suit: 1 }]); // AT on T high flop
            const communityCards: Card[] = [
                { rank: 8, suit: 2 }, { rank: 2, suit: 0 }, { rank: 1, suit: 1 } // Td 3s 2c
            ];
            const winRate = relativeRanker.rankHandPostFlop(hand, communityCards, 2, 5000);
            // Player has top pair (Tens). Opponent might have draws (e.g., gutshot with 4x needs a 5) or better pair.
            // Win rate should be decent.
            expect(winRate).toBeGreaterThan(0.6); 
            expect(winRate).toBeLessThan(0.9); 
        });
    });

    describe('compareHands - River', () => {
        // Test deterministic comparison on the river
        const community: Card[] = [
            { rank: 12, suit: 0 }, { rank: 11, suit: 0 }, { rank: 2, suit: 1 }, // Ah Kh Dc
            { rank: 3, suit: 1 }, { rank: 10, suit: 2 }  // Dd 4c
        ];
        const hand1 = createHand([{ rank: 10, suit: 0 }, { rank: 9, suit: 0 }]); // Qh Jh -> Ah Kh Qh Jh T (Royal Flush is board)
        const hand2 = createHand([{ rank: 7, suit: 1 }, { rank: 8, suit: 1 }]); // 7d 8d -> Ah Kh Flush
        const hand3 = createHand([{ rank: 4, suit: 0 }, { rank: 4, suit: 1 }]); // 4h 4d -> Three 4s

        it('should correctly identify winners and ties on the river', () => {
            const results = relativeRanker.compareHands([hand1, hand2, hand3], community);
            // Hand1 (Royal Flush uses board) vs Hand2 (Ace high flush uses board) vs Hand3 (Set of 4s)
            // Everyone plays the board A K high flush essentially. It's a chop.
            // Let's adjust community to make hands distinct
            const community2: Card[] = [
                 { rank: 9, suit: 0 }, { rank: 10, suit: 0 }, { rank: 11, suit: 0 }, // T H J H Q H
                 { rank: 2, suit: 1 }, { rank: 3, suit: 2 }  // 2 D 3 C
            ];
            const h1 = createHand([{ rank: 12, suit: 0 }, { rank: 8, suit: 0 }]); // A H 9 H -> K high Straight Flush (A K Q J T)
            const h2 = createHand([{ rank: 7, suit: 0 }, { rank: 6, suit: 0 }]); // 8 H 7 H -> J high Straight Flush
            const h3 = createHand([{ rank: 2, suit: 0 }, { rank: 2, suit: 2 }]); // Pair of 2s

            const results2 = relativeRanker.compareHands([h1, h2, h3], community2);
            // Expected: h1 wins (1.0), h2 loses (0.0), h3 loses (0.0)
            expect(results2[0]).toBeCloseTo(1.0); 
            expect(results2[1]).toBeCloseTo(0.0);
            expect(results2[2]).toBeCloseTo(0.0);
        });

         it('should handle ties correctly on the river', () => {
             const community3: Card[] = [
                 { rank: 0, suit: 0 }, { rank: 1, suit: 0 }, { rank: 2, suit: 0 }, // 2H 3H 4H
                 { rank: 3, suit: 0 }, { rank: 10, suit: 1 } // 5H JD
             ];
             const h_tie1 = createHand([{ rank: 4, suit: 2 }, { rank: 5, suit: 2 }]); // 6H 7H -> 7 high Straight Flush
             const h_tie2 = createHand([{ rank: 4, suit: 1 }, { rank: 5, suit: 2 }]); // 6D 7H -> 7 high Straight Flush
             const h_lose = createHand([{ rank: 11, suit: 1 }, { rank: 11, suit: 2 }]); // Ks Kc -> Pair Kings

             const results3 = relativeRanker.compareHands([h_tie1, h_tie2, h_lose], community3);
             // Expected: h_tie1 ties (0.5), h_tie2 ties (0.5), h_lose loses (0.0)
             expect(results3[0]).toBeCloseTo(0.5);
             expect(results3[1]).toBeCloseTo(0.5);
             expect(results3[2]).toBeCloseTo(0.0);
         });
    });

    describe('compareHands - Pre-River Simulation', () => {
        it('should simulate win rates correctly pre-flop (AA vs KK)', () => {
            const handAA = createHand([{ rank: 12, suit: 0 }, { rank: 12, suit: 1 }]);
            const handKK = createHand([{ rank: 11, suit: 0 }, { rank: 11, suit: 1 }]);
            const results = relativeRanker.compareHands([handAA, handKK], null, 10000); // Preflop (null community), more sims
            // AA is a big favorite over KK (~82% equity)
            expect(results[0]).toBeGreaterThan(0.80);
            expect(results[0]).toBeLessThan(0.85);
            expect(results[1]).toBeGreaterThan(0.15);
            expect(results[1]).toBeLessThan(0.20);
            expect(results[0] + results[1]).toBeCloseTo(1.0); // Should sum to 1 (ignoring tiny tie %)
        });

        it('should simulate win rates correctly on the flop (Set vs Flush Draw)', () => {
            const handSet = createHand([{ rank: 7, suit: 0 }, { rank: 7, suit: 1 }]); // 88
            const handFlushDraw = createHand([{ rank: 12, suit: 2 }, { rank: 11, suit: 2 }]); // Ac Kc
            const community: Card[] = [
                { rank: 7, suit: 2 }, { rank: 2, suit: 2 }, { rank: 5, suit: 0 } // 8c 3c 6h
            ]; // Set of 8s vs Nut Flush Draw
            const results = relativeRanker.compareHands([handSet, handFlushDraw], community, 10000);
            // Equity is roughly 65-70% for the set vs NFD on flop
            expect(results[0]).toBeGreaterThan(0.60);
            expect(results[0]).toBeLessThan(0.8);
            expect(results[1]).toBeGreaterThan(0.2);
            expect(results[1]).toBeLessThan(0.40);
            expect(results[0] + results[1]).toBeCloseTo(1.0);
        });

        it('should simulate 3-way pot correctly', () => {
            const handAA = createHand([{ rank: 12, suit: 0 }, { rank: 12, suit: 1 }]);
            const handKK = createHand([{ rank: 11, suit: 0 }, { rank: 11, suit: 1 }]);
            const handQQ = createHand([{ rank: 10, suit: 0 }, { rank: 10, suit: 1 }]);
            const results = relativeRanker.compareHands([handAA, handKK, handQQ], null, 10000); // Preflop 3-way
            // Equities roughly: AA ~65%, KK ~20%, QQ ~15%
            expect(results[0]).toBeGreaterThan(0.60); 
            expect(results[1]).toBeGreaterThan(0.15); 
            expect(results[2]).toBeGreaterThan(0.10);
            expect(results[0] + results[1] + results[2]).toBeCloseTo(1.0); 
        });
    });

    // Add tests for expectedPercentile and computeKellyMax if they become complex
    // For now, expectedPercentile uses normalCDF (mocked/placeholder) and computeKellyMax is simple math
});
