- [x] implement pot splitting
- [ ] way to pull in data from pre-flop odds database 
- [ ] function to determine hand ranks based on community cards
  - Simple version that just checks every hand to calculate ranks
  - Version that samples hands for efficiency
- [ ] write some semi-intelligent players based on those odds:
  - [ ] AllInPlayer - goes all in pre-flop above a certain threshold, otherwise check/folds.
  Needs a copy of the pre-flop odds and a threshold parameter.
  - [ ] LimpPlayer - calls above a certain threshold (constant or based on point in game), otherwise check/folds. 
  Needs the same params as AllInPLayer.
  - [ ] DiscreteBetPlayer - Takes as a parameter multiple thresholds for different bet sizes and points in the game.
  Bets according to those thresholds.
  - [ ] VariablePlayer - Takes as a parameter a function that returns a bet size based on the current game state.
    - Gonna want multiple functions to try out
- [ ] do this locally https://www.youtube.com/watch?v=cO5g5qLrLSo
- [ ] adapt the tutorial to work for poker
- [ ] playable game back end