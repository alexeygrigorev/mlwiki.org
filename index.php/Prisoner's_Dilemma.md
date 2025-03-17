---
title: "Prisoner's Dilemma"
layout: default
permalink: /index.php/Prisoner's_Dilemma
---

# Prisoner's Dilemma

## Prisoner's Dilemma
This is a game of [Game Theory](Game_Theory)

The set up:
- There are two players $p_1$ and $p_2$
- both have committed a crime 
- they are caught by the police and kept in separate rooms - so they cannot communicate with each other
- they have two options: cooperate with the police and confess ($C$), or don't cooperate ($N$)
- for not cooperating: 1 year in prison
- for cooperating: the other goes to jail on 10 years and you are set free 
- but if both cooperate, each gets 5 years in prison

This can be depicted by a matrix: 

|    |  $N$  |  $C$  |   $N$   |  (-1, -1)  |  (-10, 0) ||   $C$   |  (0, -10)  |  (-5, -5) |
The best strategy - the [Nash Equilibria](Nash_Equilibrium) is:
- for $p_2$: $C$ is always better: (0 > -5)
- for $p_1$: the same 
- so both choose to play $(C, C)$ - the strictly dominating strategy
- but this strategy clearly is not better than $(N, N)$ - but the [Dominance](Dominance) principle misses it
- which is why it's called a [Game Theory](Game_Theory) paradox 


## Variations
### TCP blackoff
Set up
- when TCP correctly implemented, it has "backoff mechanism"
- if data flow causes congestion, sender reduces speed, until a jam subsides
- defective implementation doesn't backoff

There are two strategies
- $C$ to use correct implementation
- $D$ to use defective one
- if both players use $C$, delay is 1
- if $p_1$ uses $D$, and $p_2$ uses $C$, then $p_1$ has no delays, but $p_2$ has 4ms of delays
- both players want to minimize the delay time

|    |  $C$  |  $D$   |   $C$   |  (-1, -1)  |  (0, -4) ||   $D$   |  (-4, 0)  |  (-3, -3) |
For both players the dominating strategy is $D$


### Tickets Price
- Suppose we have two airline companies $P_1$ and $P_2$
- They are both thinking about about opening a new destination 
- Both consider two options: either make tickets cheap or make them expensive 
- Clearly if $p_1$ decides to sell cheap tickets while $p_2$ - to sell expensive tickets, everybody will buy from $p_1$

So we can depict it with the following pay-off matrix
- a cell represents consequences of the decision that both players take

|   $p_2 \to$ <br/> $p_1 \downarrow$  |  200  |  500   |   200   |  (50, 100)  |  (-100, 200) ||   500   |  (150, -200)  |  (-10, -10) |
We see that:
- if both agree on cheap tickets - both will have profits
- if $p_2$ sells expensive tickets and $p_1$ cheap ones, all go to $p_1$ and $p_2$ will have losses
- the same with $p_1$ and $p_1$
- if both decide on expensive tickets - nobody will buy them and they both will experience losses


The profile (500, 500) is the Nash Equilibria



## Sources
- [Decision Engineering (ULB)](Decision_Engineering_(ULB))
- [Game Theory (coursera)](Game_Theory_(coursera))

[Category:Game Theory](Category_Game_Theory)