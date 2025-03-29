import * as dataForge from 'data-forge';
import * as path from 'path';
import { readFileSync } from 'fs';

export class PreflopStatsRepository {
    private winRates: dataForge.IDataFrame<number, any>;

    constructor() {
        const dataPath = path.resolve(__dirname, 'data', 'preflop_win_rates.json');
        const jsonContent = readFileSync(dataPath, 'utf-8');
        this.winRates = dataForge.fromJSON(jsonContent);
    }

    /**
     * Gets win rate and related info for the given cards and player count
     * @param card1Rank 0-12, 0 is 2, 12 is Ace
     * @param card2Rank 0-12, 0 is 2, 12 is Ace
     * @param suited True if the cards are the same suite, False otherwise
     * @param playerCount number of players in the game
     * @returns Object containing win rate and percentile information
     * @throws Error if parameters are invalid
     */
    public getWinRate(card1Rank: number, card2Rank: number, suited: boolean, playerCount: number): { winRate: number; percentile: number } {
        // Validate input parameters
        if (card1Rank < 0 || card1Rank > 12 || card2Rank < 0 || card2Rank > 12) {
            throw new Error('Card ranks must be between 0 and 12');
        }

        if (playerCount < 2 || playerCount > 6) {
            throw new Error('Player count must be between 2 and 6');
        }

        // Ensure card1Rank is higher or equal to card2Rank
        if (card2Rank > card1Rank) {
            [card1Rank, card2Rank] = [card2Rank, card1Rank];
        }

        const result = this.winRates.where(row => 
            row.card_1_rank === card1Rank &&
            row.card_2_rank === card2Rank &&
            row.suited === suited &&
            row.player_count === playerCount
        ).first(); // Get the first matching row

        if (!result) {
            console.error(`[Preflop] No preflop data found for ${card1Rank}, ${card2Rank}, ${suited}, ${playerCount}`);
            throw new Error(`No preflop data found for ${card1Rank}, ${card2Rank}, ${suited}, ${playerCount}`);
        }

        return {
            winRate: result.win_rate,
            percentile: result.percentile
        };
    }
}
