---
layout: default
permalink: /index.php/Pure_Competition_Game
tags:
- game-theory
title: Pure Competition Game
---
## Pure Competition Game
This is a type of game is the [Game Theory](Game_Theory) where players have exactly opposite interests 
- In such games there should be precisely two players (otherwise they couldn't have the opposite interests)

So a pure competition game is where
- $a \in A, u_1(a) + u_2(a) = c$
- means that if somebody wins, another player loses exactly the amount the first player wins
- this is also called  constant sum game
- if $c$ = 0, a game is called a ''zero sum game'' 


## Zero Sum Games
### Matching Pennies
This is a zero-sum game

Rules:
- $p_1$ wants to match, $p_2$ - to mismatch
- each player tosses a coin and record what they have: heads or tails
- if both have the same, $p_1$ wins, $p_2$ looses
- if both have different, $p_1$ looses, $p_2$ wins

Payoff matrix:

|    |  Head  |  Tail  |   Head   |  (1, -1)  |  (-1, 1)  ||   Tail   |  (-1, 1)  |  (1, -1) |

In this game there's no [Nash Equilibrium](Nash_Equilibrium):
- if $p_2$ knows that $p_1$ plays $H$ he will play $H$
- then if $p_1$ knows that $p_2$ plays $H$, he will play $T$
- so there's always an incentive to deviate to other alternative



### Rock Paper Scissors
Is a generalization of Matching Pennies to 3 alternatives

|    |  Rock  |  Paper  |  Scissors  |   Rock       |  (0, 0)  |  (-1, 1)  |  (1, -1)  ||   Paper      |  (1, -1)  |  (0, 0)  |  (-1, 1)  ||   Scissors   |  (-1, 1)  |  (1, -1)  |  (0, 0)  |

## See also
- [Cooperation Game](Cooperation_Game)

## Sources
- [Game Theory (coursera)](Game_Theory_(coursera))
- [Decision Engineering (ULB)](Decision_Engineering_(ULB))
