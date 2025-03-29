import { describe, expect, it, beforeEach } from '@jest/globals';
import { PostflopStatsRepository } from '../PostflopStatsRepository';

describe('PostflopStatsRepository', () => {
    let repo: PostflopStatsRepository;

    beforeEach(() => {
        repo = new PostflopStatsRepository();
    });

    describe('getPercentile', () => {
        it('should return valid percentile for flop with 3 players', () => {
            const percentile = repo.getPercentile(0.4806666666666667, 3, 'flop');
            expect(typeof percentile).toBe('number');
            expect(percentile).toBeGreaterThanOrEqual(0);
            expect(percentile).toBeLessThanOrEqual(100);
        });

        it('should return valid percentile for turn with 4 players', () => {
            const percentile = repo.getPercentile(0.5, 4, 'turn');
            expect(typeof percentile).toBe('number');
            expect(percentile).toBeGreaterThanOrEqual(0);
            expect(percentile).toBeLessThanOrEqual(100);
        });

        it('should handle edge cases correctly', () => {
            // Test with minimum win rate
            const minPercentile = repo.getPercentile(0.0, 3, 'flop');
            expect(typeof minPercentile).toBe('number');
            expect(minPercentile).toBe(0.0);

            // Test with maximum win rate
            const maxPercentile = repo.getPercentile(1.0, 3, 'flop');
            expect(typeof maxPercentile).toBe('number');
            expect(maxPercentile).toBeGreaterThanOrEqual(99.9);
            expect(maxPercentile).toBeLessThanOrEqual(100);
        });

        it('should work with different player counts', () => {
            const playerCounts = [3, 4, 5, 6];
            playerCounts.forEach(playerCount => {
                const percentile = repo.getPercentile(0.5, playerCount, 'flop');
                expect(typeof percentile).toBe('number');
                expect(percentile).toBeGreaterThanOrEqual(0);
                expect(percentile).toBeLessThanOrEqual(100);
            });
        });

        it('should work with all street types', () => {
            const streets = ['flop', 'turn', 'river'];
            streets.forEach(street => {
                const percentile = repo.getPercentile(0.5, 3, street);
                expect(typeof percentile).toBe('number');
                expect(percentile).toBeGreaterThanOrEqual(0);
                expect(percentile).toBeLessThanOrEqual(100);
            });
        });

        it('should throw error for invalid parameters', () => {
            expect(() => repo.getPercentile(-0.1, 3, 'flop')).toThrow(); // Invalid win rate
            expect(() => repo.getPercentile(1.1, 3, 'flop')).toThrow(); // Invalid win rate
            expect(() => repo.getPercentile(0.5, 2, 'flop')).toThrow(); // Invalid player count
            expect(() => repo.getPercentile(0.5, 3, 'preflop')).toThrow(); // Invalid street
        });
    });
});
