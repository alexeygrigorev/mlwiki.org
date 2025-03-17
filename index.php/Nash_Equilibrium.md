---
title: Nash Equilibrium
layout: default
permalink: /index.php/Nash_Equilibrium
---

# Nash Equilibrium

## Nash Equilibrium
This is an important concept of the [Game Theory](Game_Theory)
- It assumes that the agents act rationally
- That it, he always wants to maximize the consequences
- and he will never take an action if there exists another action that has better consequences (for him)


### Example
Consider a Beauty Context Game;
- each player says a number form 1 to 100
- the player who says the number that is closest to 2/3 of the average wins the prise
- ties are broken randomly
- Nash Equilibrium in this case is 1

Strategic reasoning:
- what will other players do?
- What should I do in response?
- Each player best responds to the others?

### Main Ideas
- each player wants to maximize their payoff 
- so by the best reasoning, knowing what the others may take, they pick up an action that should be the best 
- The actions taken by all players form an ''action profile''

An action profile is a Nash Equilibrium if
- it is stable: nobody has an incentive to deviate from their action 


## [Normal Form Game](Normal_Form_Game)s
In a Normal Form Game a profile $a^* \in A$ is a Nash Equilibria if
- $ \forall a_i \in A: (a^*_{-i}, a^*_i) \ S_i \ (a^*{-i}, a_i):$
- $S_i$ is a preference relation of a player $i$
- $a_{-i}$ - all components except $i$

This needs to hold for all the players 


## Examples
### [Prisoner's Dilemma](Prisoner's_Dilemma)

|    |  $C$  |  $D$  |   $C$   |  (-1, -1)  |  (0, -4) ||   $D$   |  (-4, 0)  |  (-3, -3) |
Both prisoners choose $D$: 
- the $(D, D)$ is the Nash Equilibrium
- it is stable: nobody wants to deviate 

Consider the profile $(C, C)$
- it's not stable: $p_1$ wants to change his mind and choose $D$
- $p_2$ wants to do the same
- so they wind up in $(D, D)$
- if they never stabilize at some profile - there is no Nash Equilibria


### [Matching Pennies](Matching_Pennies)

|    |  Head  |  Tail  |   Head   |  (1, -1)  |  (-1, 1)  ||   Tail   |  (-1, 1)  |  (1, -1) |

In this game there's no [Nash Equilibrium](Nash_Equilibrium):
- if $p_2$ knows that $p_1$ plays $H$ he will play $H$
- then if $p_1$ knows that $p_2$ plays $H$, he will play $T$
- so there's always an incentive to deviate to other alternative


### The [Battle of the Sexes](Battle_of_the_Sexes)
In this case there are two equilibrium: $(B, B)$ and $(F, F)$

|   wife $\to$ <br> husband $\downarrow$  |  $B$  |  $F$  |   $B$   |  <font color="blue">(2, 1)</font>  |  <font color="grey">(0, 0)</font> ||   $F$   |  <font color="grey">(0, 0)</font>  |  <font color="blue">(1, 2)</font> |


## Correlated Equilibria
- consider a traffic game
  - 2 cars are on crossing
  - they can go or yield another car
  - P1 rows, P2 cols
    - go
      - -10 -10
      - 1 0
    - wait
      - -1 -1
      - 0 1
  - not stable, players may miscoordinate
  - we place a traffic light
  - so by putting a fair randomizing device that
tells players whether to go or wait
- the same can be applied to Battle of the Sexes
- benefits
  - we avoid negative outcomes
  - fairness is achieved
  - the total sum can exceed the NE
- correlated equilibrium
  - a randomized assignment of action recommendation to agents, such as nobody wants to deviate



## Sources
- [Decision Engineering (ULB)](Decision_Engineering_(ULB))
- [Game Theory (coursera)](Game_Theory_(coursera))

[Category:Game Theory](Category_Game_Theory)