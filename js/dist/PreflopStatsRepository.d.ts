export declare class PreflopStatsRepository {
    private allData;
    constructor();
    /**
     * Gets win rate and related info for the given cards and player count
     * @param card1Rank 0-12, 0 is 2, 12 is Ace
     * @param card2Rank 0-12, 0 is 2, 12 is Ace
     * @param suited True if the cards are the same suite, False otherwise
     * @param playerCount number of players in the game
     * @returns Object containing win rate and percentile information
     */
    getWinRate(card1Rank: number, card2Rank: number, suited: boolean, playerCount: number): {
        winRate: number;
        percentile: number;
    };
}
