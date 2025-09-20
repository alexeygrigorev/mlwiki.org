---
layout: default
permalink: /index.php/Mixed-Strategy_Game
tags:
- game-theory
title: Mixed-Strategy Game
---
{{draft}}

## Mixed-Strategy

### Randomization
- Not a good idea to play deterministic game
- so another player will always want to choose better results
- Idea: confuse them by playing randomly
- Consider the matching pennies: randomly picking actions is better

### Pure vs mixed
- Pure strategy: only one action is played with positive probability
- Mixed strategy: more than one action is player with positive probability
- these actions are called the support of the mixed strategy

### Expected payoff
- $u_i(s) = \sum_{a \in A} u_i(a) Pr(a |  s)$ - sum over all cells of the game with each payoff multiplied by probability it happens  |- $Pr(a |  s) = \prod_{j \in N} s_j(a_j)$: probability it happens - product of each player's probability to select this cell |

### Best Response
- $s^*_i \in BR(s_{-i}) \iff \forall s_i \in S_i, u_i(s^*_i, s_{-i}) \geqslant u_i(s_i, s_{-i})$: $s^*_i$ is a BR if it's as good as others or better
- $s = \{s_1, ..., s_n\}$ is a Nash Equilibrium if $\forall i, s_i \in BR(s_{-i})$


### Theorem (Nash)
- Every finite gave has a Hash Equilibrium
- Matching pennies - NE is to play randomly 50/50 
- Coordinating game - NE is to play randomly 50/50
- Prisoners' dilemma - only a pure strategy NE, no mixed one

### Computing
- hard to compute
- easier when you can guess the support (pure strategies with positive probability)
- Indifference
  - if P1 best-responds with a mixed strategy
  - P2 must make him indifferent
  - He himself plays mixed strategy, so it's the best response
  - if he's not indifferent, he will play the same strategy, and over time his opponent will use it
  - $u_1(A) = u_1(B)$
utility when P1 plays A = P1 plays B
- Battle of the Sexes
  - $2p+0(1-p) = 0p + 1(1-p)$; $p = 1/3$
  - $q+0(1-q) = 0q+2(1-q)$; $q = 2/3$
  - Thus, the mixed strategies $(2/3, 1/3)$ and $(1/3, 2/3)$ are NE

### Interpreting
- What does it mean to play a mixed strategy?
- Randomize to confuse your opponent
  - consider the matching pennies
- Randomize what uncertain about the others' actions
  - consider the battle of the sexes

### Examples
- Predator vs Prey
  - a competition between 2 animals
  - possible strategies for each: be active or passive
  - predator\prey
    - prob
      - 
      - p
      - 1-p
    - Active
      - 2, -5
      - 3, -6
      - q
    - Passive
      - -1, 0
      - 3, -2
      - 1-q
  - what p and q are the mixed strategy equilibrium?
  - predator plays active with q (rows, 1rd), 
prey plays active with p (cols, 2nd)
  - 

predator:

 {when plays active} 
 p {prey is active} * 2 {possible payoff}
 +
 (1 - p) {prey is passive} * 3 {possible payoff} 
 = 
 {when plays passive}
 p {prey is active} * 3 {possible payoff}
 +
 (1 - p) {prey is passive} * (-1) {possible payoff} 

=>

 prey plays active with p = 4/5

  - prey: $-5q-2(1-q) = -6q $=> $q = 2/3$
- Kicker vs Goalie
  - Soccer penalty kicks 
  - usual
    - kicker\goalie
      - prob
        - 
        - 1/2
        - 1/2
      - Left
        - 0, 1
        - 1, 0
        - 1/2
      - Right
        - 0, 1
        - 1, 0
        - 1/2
    - equlibrium is to play 1/2
  - kicker is weak on right
    - a kicker misses right every 4th time
    - kicker\goalie
      - prob
        - 
        - p
        - 1-p
      - Left
        - 0, 1
        - 1, 0
        - q
      - Right
        - 0, 1
        - .75, .25
        - 1-q
    - K plays L with q, G plays L with p
    - {L} $G: 0p+1(1-p) = 0.75p+0(1-p)$ {R}, $p = 4/7$
    - {L} $K: q+0.25(1-q)  = 1-q;$ {R}, $q = 3/7$ 
    - result: Kicker kicks more to the Right|   |    - because G has adjusted |
## Sources
- [Game Theory (coursera)](Game_Theory_(coursera))
