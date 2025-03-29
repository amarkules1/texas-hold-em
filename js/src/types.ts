export interface Card {
    rank: number;  // 0-12 (2-Ace)
    suit: number;  // 0-3 (Hearts, Diamonds, Clubs, Spades)
}

export interface HandRankDetails {
    expectedWinRate: number;
    expectedTwoPlayerWinRate: number;
    percentile: number;
    idealKellyMax: number;
}

export type PlayerAction = "fold" | "check" | "call" | "raise";
export type HandRank = "high_card" | "pair" | "two_pair" | "three_of_a_kind" | "straight" | "flush" | "full_house" | "four_of_a_kind" | "straight_flush";

export interface PlayerDecision {
    action: PlayerAction;
    amount: number;
}
