"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.PostflopStatsRepository = void 0;
const fs_1 = require("fs");
const path_1 = require("path");
const dataframe_js_1 = require("dataframe-js");
class PostflopStatsRepository {
    constructor() {
        this.allData = null;
        const csvPath = (0, path_1.join)(__dirname, 'data', 'post_flop_win_rate_distribution.csv');
        this.allData = new dataframe_js_1.DataFrame((0, fs_1.readFileSync)(csvPath, 'utf-8'));
    }
    /**
     * Gets the percentile for the given win rate, player count, and street
     * @param winRate The win rate to get the percentile for
     * @param playerCount Number of players in the game
     * @param street The street ('flop', 'turn', or 'river')
     * @returns The percentile (0-100) for the given parameters
     */
    getPercentile(winRate, playerCount, street) {
        if (!this.allData)
            throw new Error('Data not loaded');
        const filteredData = this.allData.filter((row) => row.get('player_ct') === playerCount &&
            row.get('street') === street);
        const belowWinRate = filteredData.filter((row) => row.get('win_rate') < winRate);
        const count = belowWinRate.count();
        const total = filteredData.count();
        return 100 * (count / total);
    }
}
exports.PostflopStatsRepository = PostflopStatsRepository;
