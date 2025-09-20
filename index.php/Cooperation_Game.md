---
layout: default
permalink: /index.php/Cooperation_Game
tags:
- game-theory
title: Cooperation Game
---
## Cooperation Games
Unlike [Pure Competition Game](Pure_Competition_Game)s where players have opposite interests, here players have the same interests 
- $\forall a \in A, \forall i, j: u_i(a) = u_j(a)$


## Coordination Game
Which side of the road you drive on?
- suppose two players meet at a passage 
- they want to get through 
- both need to choose either to go left or right
- win-win situation only when they both pick the same side 
- otherwise both lose 

|    |  Left  |  Right  |   Left    |  (1, 1)  |  (0, 0) ||   Right   |  (0, 0)  |  (1, 1) |

## Battle of the Sexes
This is not only a cooperation game, but also a [Pure Competition Game](Pure_Competition_Game)

Description:
- 2 players - a husband and a wife
- 2 options - ballet and football
- they want to go together
- but Husband prefers to go to football, and wife wants to see the ballet

|   wife $\to$ <br> husband $\downarrow$  |  $B$  |  $F$  |   $B$   |  <font color="blue">(2, 1)</font>  |  <font color="grey">(0, 0)</font> ||   $F$   |  <font color="grey">(0, 0)</font>  |  <font color="blue">(1, 2)</font> |
There are two [Nash Equilibria](Nash_Equilibrium):
- $(B, B)$ and $(F, F)$
- in both these cases nobody wants to deviate as they would get worse payoff
- consider $(B, F)$ - in this case both want to deviate 


## Sources
- [Game Theory (coursera)](Game_Theory_(coursera))
