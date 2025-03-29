export declare class PostflopStatsRepository {
    private allData;
    constructor();
    /**
     * Gets the percentile for the given win rate, player count, and street
     * @param winRate The win rate to get the percentile for
     * @param playerCount Number of players in the game
     * @param street The street ('flop', 'turn', or 'river')
     * @returns The percentile (0-100) for the given parameters
     */
    getPercentile(winRate: number, playerCount: number, street: string): number;
}
