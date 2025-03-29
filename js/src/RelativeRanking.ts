import { Deck } from "./Deck";
import { Card, HandRankDetails } from "./types";
import { HandOfTwo, HandOfFive } from "./Hand";
import { PreflopStatsRepository } from "./PreflopStatsRepository";
import { PostflopStatsRepository } from "./PostflopStatsRepository";

// Placeholder for normalCDF function - Replace with actual implementation
function normalCDF(x: number, mean: number, stdDev: number): number {
    // Very basic placeholder, replace with actual implementation
    console.warn("Warning: Using placeholder normalCDF function.");
    if (stdDev <= 0) return x < mean ? 0 : 1; // Handle non-positive std dev
    // Simple approximation or fixed value
    return 0.5;
}

export class RelativeRanking {
    private preflopStatsRepository: PreflopStatsRepository;
    private postflopStatsRepository: PostflopStatsRepository;

    constructor() {
        this.preflopStatsRepository = new PreflopStatsRepository();
        this.postflopStatsRepository = new PostflopStatsRepository();
    }

    /**
     * Calculates win rate and percentile for a given hand at any point in the game
     * @param hand Array of 2 cards
     * @param communityCards Array of 3-5 cards or null/empty for pre-flop (default null)
     * @param playerCount Number of players in the game (default 2)
     * @param sampleSize Number of simulation runs for sample based win rates (post-flop, post-turn) (default 1000)
     * @returns An object containing win rates, percentile, and ideal Kelly max.
     */
    getHandRankDetails(
        hand: HandOfTwo,
        communityCards: Card[] | null = null,
        playerCount: number = 2,
        sampleSize: number = 1000
    ): HandRankDetails {
        let expectedWinRate = 0.0;
        let expectedTwoPlayerWinRate = 0.0;
        let percentile = 0.0;
        const currentCommunityCards = communityCards || [];

        // Validate params
        if (hand.getCards().length !== 2) {
            throw new Error("Hand must contain exactly 2 cards");
        }
        if (currentCommunityCards.length > 5) {
            throw new Error("There can only be up to 5 community cards in Texas Hold'em");
        }
        if (playerCount < 2) {
            throw new Error("Player count must be at least 2");
        }

        const isSuited = hand.getCards()[0].suit === hand.getCards()[1].suit;
        const rank1 = hand.getCards()[0].rank;
        const rank2 = hand.getCards()[1].rank;

        // Preflop
        if (currentCommunityCards.length < 3) {
            const nPlayerData = this.preflopStatsRepository.getWinRate(rank1, rank2, isSuited, playerCount);
            let twoPlayerData = nPlayerData;
            if (playerCount > 2) {
                twoPlayerData = this.preflopStatsRepository.getWinRate(rank1, rank2, isSuited, 2);
            }
            expectedWinRate = nPlayerData.winRate;
            expectedTwoPlayerWinRate = twoPlayerData.winRate;
            percentile = nPlayerData.percentile;
        }
        // Flop
        else if (currentCommunityCards.length === 3) {
            expectedTwoPlayerWinRate = this.rankHandPostFlop(hand, currentCommunityCards, 1, sampleSize);
            if (playerCount > 2) {
                expectedWinRate = this.rankHandPostFlop(hand, currentCommunityCards, playerCount - 1, sampleSize);
                percentile = this.postflopStatsRepository.getPercentile(expectedWinRate, playerCount, 'flop');
            } else {
                expectedWinRate = expectedTwoPlayerWinRate;
                percentile = this.expectedPercentile(expectedTwoPlayerWinRate, 0.5, 0.20277154473723782);
            }
        }
        // Turn
        else if (currentCommunityCards.length === 4) {
            expectedTwoPlayerWinRate = this.rankHandPostTurn(hand, currentCommunityCards, 1, sampleSize);
            if (playerCount > 2) {
                expectedWinRate = this.rankHandPostTurn(hand, currentCommunityCards, playerCount - 1, sampleSize);
                percentile = this.postflopStatsRepository.getPercentile(expectedWinRate, playerCount, 'turn');
            } else {
                expectedWinRate = expectedTwoPlayerWinRate;
                percentile = this.expectedPercentile(expectedTwoPlayerWinRate, 0.5, 0.23895325562434003);
            }
        }
        // River
        else if (currentCommunityCards.length === 5) {
            expectedTwoPlayerWinRate = this.rankHandPostRiver(hand, currentCommunityCards, playerCount);
            expectedWinRate = Math.pow(expectedTwoPlayerWinRate, playerCount - 1);
            if (playerCount > 2) {
                percentile = this.postflopStatsRepository.getPercentile(expectedWinRate, playerCount, 'river');
            } else {
                percentile = this.expectedPercentile(expectedTwoPlayerWinRate, 0.5, 0.29411125409761246);
            }
        }

        const kellyMax = this.computeKellyMax(expectedWinRate, playerCount);

        return {
            expectedWinRate,
            expectedTwoPlayerWinRate,
            percentile,
            idealKellyMax: kellyMax
        };
    }

    /**
     * Calculate the relative rank of a hand post river
     *
     * @param hand The two card hand
     * @param communityCards The five community cards
     * @param numPlayers The number of players
     * @param numSimulations The number of simulations to run
     * @returns The win rate of the hand
     */
    public rankHandPostRiver(hand: HandOfTwo, communityCards: Card[], numPlayers: number, numSimulations: number = 1000): number {
        if (!communityCards || communityCards.length !== 5) {
            throw new Error("Post-river requires exactly 5 community cards.");
        }

        let wins = 0;
        const knownCards = [...hand.getCards(), ...communityCards];

        for (let i = 0; i < numSimulations; i++) {
            const deck = new Deck();
            deck.removeCards(knownCards);
            deck.shuffle();

            const opponentHands: HandOfTwo[] = [];
            for (let p = 0; p < numPlayers - 1; p++) {
                if (deck.cardsRemaining() < 2) {
                    console.warn("Not enough cards to deal opponent hands in simulation.");
                    break; // Not enough cards
                }
                const cards = deck.draw(2); // Use the new draw method
                opponentHands.push(new HandOfTwo(cards));
            }

            if (opponentHands.length < numPlayers - 1) continue; // Skip simulation if couldn't deal hands

            // --- Hand Evaluation Logic using HandOfFive --- 
            const playerBestHand = new HandOfFive(hand.getCards(), communityCards);
            const opponentBestHands = opponentHands.map(oppHand => new HandOfFive(oppHand.getCards(), communityCards));
            
            let bestHandRank = playerBestHand; // Track the current best hand rank found
            let winners: (HandOfTwo | null)[] = [hand]; // Start with the player potentially winning

            for (let j = 0; j < opponentBestHands.length; j++) {
                const opponentHand = opponentBestHands[j];
                const opponentCards = opponentHands[j]; // Keep track of the HandOfTwo object

                if (opponentHand.greaterThan(bestHandRank)) {
                    // Opponent has a better hand than the current best (player or previous opponent)
                    bestHandRank = opponentHand;
                    winners = [opponentCards]; // This opponent is the new sole winner
                } else if (opponentHand.equals(bestHandRank)) {
                    // Opponent ties with the current best hand
                    winners.push(opponentCards);
                } 
                // If opponent hand is worse than bestHandRank, do nothing
            }

            // Check if the player is among the winners
            const playerIsWinner = winners.includes(hand);

            if (playerIsWinner) {
                wins += (1.0 / winners.length); // Add the fraction of the pot won
            }
            // --- End Hand Evaluation Logic ---
        }

        return wins / numSimulations;
    }

    /**
     * Calculate the relative rank of a hand post turn
     *
     * @param hand The two card hand
     * @param communityCards The four community cards
     * @param numPlayers The number of players
     * @param numSimulations The number of simulations to run
     * @returns The win rate of the hand
     */
    public rankHandPostTurn(hand: HandOfTwo, communityCards: Card[] | undefined, numPlayers: number, numSimulations: number = 1000): number {
        if (!communityCards || communityCards.length !== 4) {
            throw new Error("Post-turn requires exactly 4 community cards.");
        }

        let wins = 0;
        const knownCards = communityCards ? [...hand.getCards(), ...communityCards] : [...hand.getCards()];
        const cardsToDraw = 1; // Draw the river card

        for (let i = 0; i < numSimulations; i++) {
            const deck = new Deck();
            deck.removeCards(knownCards);
            deck.shuffle();

            // Deal opponent hands
            const opponentHands: HandOfTwo[] = [];
            for (let p = 0; p < numPlayers - 1; p++) {
                if (deck.cardsRemaining() < 2) {
                    console.warn("Not enough cards to deal opponent hands in simulation.");
                    break;
                }
                const cards = deck.draw(2); // Use the new draw method
                opponentHands.push(new HandOfTwo(cards));
            }

            if (opponentHands.length < numPlayers - 1) continue; // Skip simulation if couldn't deal hands

            // Draw the river card
            if (deck.cardsRemaining() < 1) {
                console.warn("Not enough cards to draw river card in simulation.");
                continue;
            }
            const riverCard = deck.draw(1)[0]; // Draw one card
            const finalCommunityCards = [...communityCards, riverCard];

            // --- Hand Evaluation Logic using HandOfFive --- 
            const playerBestHand = new HandOfFive(hand.getCards(), finalCommunityCards);
            const opponentBestHands = opponentHands.map(oppHand => new HandOfFive(oppHand.getCards(), finalCommunityCards));

            let bestHandRank = playerBestHand;
            let winners: (HandOfTwo | null)[] = [hand];

            for (let j = 0; j < opponentBestHands.length; j++) {
                const opponentHand = opponentBestHands[j];
                const opponentCards = opponentHands[j];

                if (opponentHand.greaterThan(bestHandRank)) {
                    bestHandRank = opponentHand;
                    winners = [opponentCards];
                } else if (opponentHand.equals(bestHandRank)) {
                    winners.push(opponentCards);
                }
            }

            const playerIsWinner = winners.includes(hand);
            if (playerIsWinner) {
                wins += (1.0 / winners.length);
            }
            // --- End Hand Evaluation Logic ---
        }

        return wins / numSimulations;
    }

    /**
     * Calculate the relative rank of a hand post flop
     *
     * @param hand The two card hand
     * @param communityCards The three community cards
     * @param numPlayers The number of players
     * @param numSimulations The number of simulations to run
     * @returns The win rate of the hand
     */
    public rankHandPostFlop(hand: HandOfTwo, communityCards: Card[] | undefined, numPlayers: number, numSimulations: number = 1000): number {
        if (!communityCards || communityCards.length !== 3) {
            throw new Error("Post-flop requires exactly 3 community cards.");
        }

        let wins = 0;
        const knownCards = communityCards ? [...hand.getCards(), ...communityCards] : [...hand.getCards()];
        const cardsToDraw = 2; // Draw turn and river cards

        for (let i = 0; i < numSimulations; i++) {
            const deck = new Deck();
            deck.removeCards(knownCards);
            deck.shuffle();

            // Deal opponent hands
            const opponentHands: HandOfTwo[] = [];
            for (let p = 0; p < numPlayers - 1; p++) {
                if (deck.cardsRemaining() < 2) {
                    console.warn("Not enough cards to deal opponent hands in simulation.");
                    break;
                }
                const cards = deck.draw(2); // Use the new draw method
                opponentHands.push(new HandOfTwo(cards));
            }

            if (opponentHands.length < numPlayers - 1) continue; // Skip simulation if couldn't deal hands

            // Draw turn and river cards
            if (deck.cardsRemaining() < 2) {
                console.warn("Not enough cards to draw turn/river cards in simulation.");
                continue;
            }
            const turnRiverCards = deck.draw(2); // Draw two cards
            const finalCommunityCards = [...communityCards, ...turnRiverCards];

            // --- Hand Evaluation Logic using HandOfFive --- 
            const playerBestHand = new HandOfFive(hand.getCards(), finalCommunityCards);
            const opponentBestHands = opponentHands.map(oppHand => new HandOfFive(oppHand.getCards(), finalCommunityCards));

            let bestHandRank = playerBestHand;
            let winners: (HandOfTwo | null)[] = [hand];

            for (let j = 0; j < opponentBestHands.length; j++) {
                const opponentHand = opponentBestHands[j];
                const opponentCards = opponentHands[j];

                if (opponentHand.greaterThan(bestHandRank)) {
                    bestHandRank = opponentHand;
                    winners = [opponentCards];
                } else if (opponentHand.equals(bestHandRank)) {
                    winners.push(opponentCards);
                }
            }

            const playerIsWinner = winners.includes(hand);
            if (playerIsWinner) {
                wins += (1.0 / winners.length);
            }
            // --- End Hand Evaluation Logic ---
        }

        return wins / numSimulations;
    }

    /**
     * Calculates the expected percentile for a given win rate based on a normal distribution.
     */
    expectedPercentile(winRate: number, mean: number, stdDev: number): number {
        // Using the placeholder normalCDF. Replace with a proper implementation.
        return normalCDF(winRate, mean, stdDev) * 100;
    }

    /**
     * Computes the Kelly criterion max bet proportion.
     */
    computeKellyMax(winRate: number, playerCount: number): number {
        if (playerCount < 2) return -1; // Or throw error
        const pLoss = 1.0 - winRate;
        const b = playerCount - 1; // Odds multiplier (bet $1 to win $b)
        if (b <= 0) return winRate > 0 ? 1 : -1; // Avoid division by zero if only 1 opponent and they fold implicitly? Or handle game logic elsewhere. Usually b >= 1.
        return winRate - (pLoss / b);
    }

    /**
     * Compares multiple hands to determine win rates against each other.
     * @param hands Array of hands (each an array of 2 cards)
     * @param communityCards Optional array of 3-5 community cards
     * @param sampleSize Samples for simulation if needed (pre-river)
     * @returns Array of win rates corresponding to the input hands array.
     */
    compareHands(
        hands: HandOfTwo[],
        communityCards: Card[] | null = null,
        sampleSize: number = 1000
    ): number[] {
        // Validate
        if (hands.length < 2 || hands.length > 12) { // Adjusted max players based on typical tables
            throw new Error(`Please provide between 2 and 12 hands, got ${hands.length}`);
        }
        hands.forEach((hand, i) => {
            if (hand.getCards().length !== 2) {
                throw new Error(`Hand at index ${i} must have exactly 2 cards`);
            }
        });
        const currentCommunityCards = communityCards || [];
        if (currentCommunityCards.length > 0 && (currentCommunityCards.length < 3 || currentCommunityCards.length > 5)) {
            throw new Error(`Community cards must be null/empty or a list of 3-5 cards, found ${currentCommunityCards.length}`);
        }

        // River - deterministic outcome
        if (currentCommunityCards.length === 5) {
            let winnerIndices: number[] = [];
            let bestHand: HandOfFive | null = null;

            for (let i = 0; i < hands.length; i++) {
                const currentHandObj = new HandOfFive(hands[i].getCards(), currentCommunityCards);
                if (!bestHand || currentHandObj.greaterThan(bestHand)) {
                    bestHand = currentHandObj;
                    winnerIndices = [i];
                } else if (currentHandObj.equals(bestHand)) {
                    winnerIndices.push(i);
                }
            }
            const winRateShare = winnerIndices.length > 0 ? 1.0 / winnerIndices.length : 0;
            return hands.map((_, i) => (winnerIndices.includes(i) ? winRateShare : 0.0));
        }

        // Pre-River Simulation
        const wins = Array(hands.length).fill(0.0);
        const baseDeck = new Deck();
        const allPocketCards = hands.flatMap(hand => hand.getCards());
        // Combine pocket cards and existing community cards for removal
        const cardsToRemove = [...allPocketCards, ...(communityCards || [])];
        baseDeck.removeCards(cardsToRemove);

        for (let s = 0; s < sampleSize; s++) {
            const sampleDeck = baseDeck.clone();
            sampleDeck.shuffle();
            // Start with existing community cards or empty array
            const currentCommunityCards = [...(communityCards || [])];

            // Draw remaining community cards needed (up to 5)
            while (currentCommunityCards.length < 5) {
                if (sampleDeck.cardsRemaining() === 0) {
                    console.warn("Deck ran out of cards during community card draw in simulation.");
                    break; // Exit if no more cards
                }
                const card = sampleDeck.draw(1)[0]; // Use draw method
                currentCommunityCards.push(card);
            }

            if (currentCommunityCards.length < 5) continue; // Skip if couldn't complete board

            // --- Hand Evaluation Logic using HandOfFive --- 
            const handObjects = hands.map(h => new HandOfFive(h.getCards(), currentCommunityCards));

            let bestHand: HandOfFive | null = null;
            let winnerIndices: number[] = [];

            for (let i = 0; i < handObjects.length; i++) {
                const currentHandObj = handObjects[i];
                if (!bestHand || currentHandObj.greaterThan(bestHand)) {
                    bestHand = currentHandObj;
                    winnerIndices = [i]; // New best hand found
                } else if (currentHandObj.equals(bestHand)) {
                    winnerIndices.push(i); // Tied with the current best
                }
            }

            // Distribute win shares for this simulation round
            if (winnerIndices.length > 0) {
                const winShare = 1.0 / winnerIndices.length;
                winnerIndices.forEach(index => {
                    wins[index] += winShare;
                });
            }
            // --- End Hand Evaluation Logic ---
        }

        return wins.map(w => w / sampleSize);
    }
}
