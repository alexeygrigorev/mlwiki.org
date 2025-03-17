---
title: Normal Form Game
layout: default
permalink: /index.php/Normal_Form_Game
---

# Normal Form Game

## Normal Form Game
A ''Normal Form Game'' (also ''Matrix Form Game'' or ''Strategic Game'') if a type of games from the [Game Theory](Game_Theory)
- main idea: the players move simultaneously
- compare to [Extensive Form Game](Extensive_Form_Game)s where players move sequentially 


In these games:
- There is a finite number $n$ of [rational](Rational_Behavior) players: $N = \{ 1, 2, ..., n \}$
- Each player $i$ has a finite set of actions $A_i$
- Also each player $i$ has a set of possible consequences $C$, in this case it's $C \equiv \mathbb{R}$
- The chosen alternatives form an ''action profile'' (or ''strategy profile'') $A: A_1 \times ... \times A_n$
- There's a consequence function $g_i: A \mapsto C$ that associates each alternative $a \in A_i$ with some consequence 
- The preferences of agents are modeled with an utility function $u_i: A \mapsto \mathbb{R}$


'''def:''' So a ''normal form game'' (or a ''strategic game'') is
- a tuple $\langle N, A, u \rangle$ where
- $N = \{ 1, 2, ..., n \}$ - set of all players 
- $A = \{A_1, ..., A_n\}$ - set of each players' actions 
- $u = \{u_1, ..., u_n\}$ - set of utility functions that expresses preferences

Utility Function (of payoff function) $u_i$
- $u_i: A_i \mapsto \mathbb{R}$
- each agent has a preference relation $S_i$ 
- agents are rational: therefore $\forall a,b \in A_i: u_i(a) \geqslant u_i(b) \Rightarrow a \ S_i \ b$
- in other words, if alternative $a$ gives a better payoff than $b$, $i$ will always prefer $a$ over $b$



### Representation
These games are typically represented with a pay-off matrix
- columns/rows represent actions that players can take 
- each cell shows the outcome of game: it lists utilities that all players will receive 

For example, 
- consider this 2-player game, with two players $p_1$ and $p_2$
- each has two strategies: $A_1 = \{a, b\}, A_2 = \{x, y\}$
- the payoffs are shown in the cells of the matrix
|   $p_2 \to$ <br> $p_1 \downarrow$  |  $x$  |  $y$  |   $a$   |  $[u_1(a,x), u_2(a,x)]$  |  $[u_1(a,y), u_2(a,y)]$  ||   $b$   |  $[u_1(b,x), u_2(b,x)]$  |  $[u_1(a,y), u_2(a,y)]$ |
Another example
- 2 players, 3 strategies 
|   $p_2 \to$ <br> $p_1 \downarrow$   |  $L$  |  $C$  |  $R$   |   $T$   |  (1,0)  |  (1,3)  |  (3,0) ||   $M$   |  (0,2)  |  (0,1)  |  (3,0) ||   $B$   |  (0,2)  |  (2,4)  |  (5,3) |
- This game can be solved by [Iterative Removal](Iterative_Removal)
- At the end the profile $(C, B)$ will be chosen


## Types
There are several types of normal form games:
- [Pure Competition Game](Pure_Competition_Game)s
  - [Matching Pennies](Matching_Pennies)
- [Cooperation Game](Cooperation_Game)s
  - [Coordination Game](Coordination_Game)
  - [Battle of the Sexes](Battle_of_the_Sexes)

## Sources
- [Game Theory (coursera)](Game_Theory_(coursera))
- [Decision Engineering (ULB)](Decision_Engineering_(ULB))

[Category:Game Theory](Category_Game_Theory)