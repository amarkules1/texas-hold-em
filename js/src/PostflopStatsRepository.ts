import * as dataForge from 'data-forge';
import * as path from 'path';
import { readFileSync } from 'fs';

const EPSILON = 1e-9; // Tolerance for float comparison

export class PostflopStatsRepository {
    private percentileData: dataForge.IDataFrame<number, any>;
    private readonly validStreets = ['flop', 'turn', 'river'];

    constructor() {
        const dataPath = path.resolve(__dirname, 'data', 'post_flop_win_rate_distribution.json');
        const jsonContent = readFileSync(dataPath, 'utf-8');
        this.percentileData = dataForge.fromJSON(jsonContent);
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
        const rowsForPlayerCtAndStreet = this.percentileData
            .filter(row => 
                row.player_ct === playerCount && 
                row.street === lowerCaseStreet
            )
        const total = rowsForPlayerCtAndStreet.toArray().length;
        const below = rowsForPlayerCtAndStreet.filter(row => row.win_rate < winRate).toArray().length;

        return 100 * (below / total);
    }
}
