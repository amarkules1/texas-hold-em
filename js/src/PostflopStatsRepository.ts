import * as dataForge from 'data-forge';
import * as path from 'path';
import { readFileSync } from 'fs';

const EPSILON = 1e-9; // Tolerance for float comparison

export class PostflopStatsRepository {
    private percentileData: dataForge.IDataFrame<number, any>;
    private readonly validStreets = ['flop', 'turn', 'river'];

    constructor() {
        const dataPath = path.resolve(__dirname, 'data', 'post_flop_win_rate_distribution.csv');
            const csvContent = readFileSync(dataPath, 'utf-8');
            this.percentileData = dataForge.fromCSV(csvContent);
            this.percentileData = this.percentileData.parseFloats(['win_rate']);
    }

    /**
     * Gets the percentile for the given win rate, player count, and street
     * @param winRate The win rate to get the percentile for (0-1)
     * @param playerCount Number of players in the game (3-6)
     * @param street The street ('flop', 'turn', or 'river')
     * @returns The percentile (0-100) for the given parameters
     * @throws Error if parameters are invalid
     */
    public getPercentile(winRate: number, playerCount: number, street: string): number {
        // Validate parameters
        if (winRate < 0 || winRate > 1) {
            throw new Error('Win rate must be between 0 and 1');
        }
        if (playerCount < 3 || playerCount > 6) {
            throw new Error('Player count must be between 3 and 6');
        }
        const lowerCaseStreet = street.toLowerCase();
        if (!this.validStreets.includes(lowerCaseStreet)) {
            throw new Error(`Street must be one of: ${this.validStreets.join(', ')}`);
        }

        // Find rows matching player count and street, with win_rate <= input winRate
        const rowsBelowOrEqual = this.percentileData
            .where(row => 
                row.player_count === playerCount && 
                row.street === lowerCaseStreet && 
                (row.win_rate <= winRate || Math.abs(row.win_rate - winRate) < EPSILON) // Check within epsilon
            )
            .orderByDescending(row => row.win_rate); // Order to get the max easily

        const resultRow = rowsBelowOrEqual.first(); // Get the row with the highest win_rate <= input

        if (!resultRow) {
            // Log specifically for the problematic test case if needed
            if (playerCount === 3 && street === 'flop') {
                 console.log(`[Postflop Debug] No row found for winRate <= ${winRate}, pc=3, street=flop`);
            }
            return 0.0; // If no win rate is <= input, return 0 percentile
        }

        // Log specifically for the problematic test case if needed
        if (playerCount === 3 && street === 'flop') {
            console.log(`[Postflop Debug] Found matching row for pc=3, street=flop:`, resultRow);
        }
        return resultRow.percentile;
    }
}
