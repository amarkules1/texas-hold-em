# texas-hold-em-utils

A TypeScript/JavaScript library containing logic for Texas Hold 'Em poker game and related utilities.

## Installation

```bash
npm install texas-hold-em-utils
```

## Features

- Pre-flop statistics and win rate calculations
- Post-flop statistics and win rate calculations
- Hand ranking and comparison
- Game simulation
- Various player strategies (Limp, All-In, Kelly Criterion)
- Sklansky hand groups support

## Usage

```typescript
import { Game, Player, Card } from 'texas-hold-em-utils';

// Create a new game with 4 players
const game = new Game(4);

// Get pre-flop statistics
const stats = game.getPreflopStats();

// More examples coming soon...
```

## Documentation

Full documentation and API reference coming soon.

## License

MIT
