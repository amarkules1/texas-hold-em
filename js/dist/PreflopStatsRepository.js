"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.PreflopStatsRepository = void 0;
const fs_1 = require("fs");
const path_1 = require("path");
const dataframe_js_1 = require("dataframe-js");
class PreflopStatsRepository {
    constructor() {
        this.allData = null;
        const csvPath = (0, path_1.join)(__dirname, 'data', 'preflop_win_rates.csv');
        this.allData = new dataframe_js_1.DataFrame((0, fs_1.readFileSync)(csvPath, 'utf-8'));
    }
    /**
     * Gets win rate and related info for the given cards and player count
     * @param card1Rank 0-12, 0 is 2, 12 is Ace
     * @param card2Rank 0-12, 0 is 2, 12 is Ace
     * @param suited True if the cards are the same suite, False otherwise
     * @param playerCount number of players in the game
     * @returns Object containing win rate and percentile information
     */
    getWinRate(card1Rank, card2Rank, suited, playerCount) {
        if (!this.allData)
            throw new Error('Data not loaded');
        const filteredData = this.allData.filter((row) => row.get('card1_rank') === card1Rank &&
            row.get('card2_rank') === card2Rank &&
            row.get('suited') === suited &&
            row.get('player_ct') === playerCount);
        if (filteredData.count() === 0) {
            throw new Error('No data found for the given parameters');
        }
        const row = filteredData.toCollection()[0];
        return {
            winRate: row.win_rate,
            percentile: row.percentile
        };
    }
}
exports.PreflopStatsRepository = PreflopStatsRepository;
