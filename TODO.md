- [x] implement pot splitting
- [x] way to pull in data from pre-flop odds database 
- [x] function to determine hand ranks based on community cards
  - Simple version that just checks every hand to calculate ranks
  - Version that samples hands for efficiency
- [ ] write some semi-intelligent players based on those odds:
  - [x] AllInPlayer - goes all in pre-flop above a certain threshold, otherwise check/folds.
  Needs a copy of the pre-flop odds and a threshold parameter.
  - [x] LimpPlayer - calls above a certain threshold (constant or based on point in game), otherwise check/folds. 
  Needs the same params as AllInPLayer.
  - [x] KellyMaxProportionPlayer - makes betting decisions based on the kelly criterion and round proportion
  - [ ] UserInputPlayer - allows for decisions based on user input (requires adjustments to game object)
- [ ] write gym environment for the game
- [ ] train a NN to play the game