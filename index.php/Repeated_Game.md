---
title: "Repeated Game"
layout: default
permalink: /index.php/Repeated_Game
---

# Repeated Game

{{draft}}

## Repeated Games

### Utility
- the sequence of utility is infinite
- how to write it?
  - average reward
    - $\lim_{k \rightarrow \inf} \sum_{j-1}^{k} \fraq{r_j}{k}$
  - discounted utility
    - players care about future less than about present
    - $\beta$ - discount factor ($0 < \beta < 1$)
    - future discounted reward: $\sum_{j=1}{\inf} \beta ^j r_j$
    - $\beta$ can be seen as an "interest rate"
    - with probability $(1 - \beta)$ game may finish

### Stochastic games
- generalization of repeated games
- informal visualization
  - <img src="<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/legacy/5a33joqeuq1eap2r2sl78811pd.png" alt="Image">" />


### Learning in Repeated Games
- all players learn as they go
- fictitious play (model-based learning)
  - initially - method for computing a NE
  - each player maintains explicit beliefs about the other players
  - algorithm
    - initialize beliefs about opponent's strategy
    - each turn
      - play a BR to the assumed strategy
      - observe actual play and update beliefs
  - consider matching pennies
    - won't converge to a specific value
    - but empirical frequencies will converge to a NA
- No-regret learning
  - regret
    - regret of an agent is experienced at time t for not having played strategy s
    - $R^t(s) = \alpha ^t - \alpha^t (s)$
    - $\alpha ^t$ - payoff player actually gets
    - $\alpha ^t(s)$ - payoff we would have received, if had played s
  - no-regret rule
    - a learning rule exhibits no regret
    - if for any pure strategy of the agent s
    - $Pr[\lim \inf R^t(s)] \leqslant 0) = 1$
    - (if player shows no regret)
  - regret matching
    - look at the regrets you've experienced so far
    - and pick a pure strategy in proportion to this regret
    - $\sigma _i ^{t+ 1} = \freq{ R^t(s) }{ \sum _{ s' \in S_i } R^t (s')$
    - sum in the denominator - sum of all regrets
    - value in the numerator - a particular regret
    - $\sigma_i ^{t + 1}$ - probability that agent $i$ plays $s$ at time $t+1$
    - so it converges to equilibrium

### Equilibrium of Inf. Repeated Games
- pure strategy
  - action on every stage
  - given you remember anything|   |  - history, etc |  - so it's an infinite set
  - example strategies for Prisoner's Dilemma
    - Tit-for-tat
      - start out cooperating
      - if opponent defects, defect next round
      - then go back to cooperation
    - Trigger
      - start out cooperating
      - if opponent defects, defect for ever
- idea
  - we can characterize a set of payoffs that are achievable under equilibrium
  - without having to enumerate the equilibria
  - (the number of equilibria is infinite)
- definitions
  - let $v_i = \min_{s_{-i} \in S_{-i}} \max _{s_i \in S_i}$
  - $v_i$ - minimax value
    - the amount of utility $i$ can get 
    - when $-i$ play a minmax strategy against him
    - so it's the value $i$ will get if others want to hurt him as much as they can
  - enforceability
    - a payoff profile is enforceable if $r_i \geqslant v_i$
    - i.e. if everybody's payoff is at least their minmax value
  - feasibility
    - a payoff profile is feasible if
      - there exists rational non-negative values $\alpha_a$
      - such that for all i we can express r_i as 
      - $\sum_{a \in A} \alpha_a u_i(a)$
      - and $\sum_{a \in A} \alpha_a = 1$
    - so it says that it is possible to have this payoff
- Folk theorem
  - consider any n-player game $G$ and any payoff vector $(r_1, ..., r_n)$
  - first
    - if $r_i$ is the payoff of any NE of $G$, then for player i it's enforceable
    - i.e. greater than or equal to his/her minimax value
  - second
    - if r is both feasible and enforceable
    - then $r$ is the payoff in some NE of $G$
  - so, enforceability and feasibility - things you need to find NE
  - as long as you meet these 2 conditions, you have a NE

### Discounted Repeated Games
- motivation
  - the future is uncertain
  - we are often motivated by what happens today
  - will people punish me if I misbehave today?
    - is it in their interest?
    - do I care about the future?
- discount factor
  - stage game : $(N, A, u)$
  - Discount factor $\beta_1 ... \beta_n, \beta_i \in [0, 1]$
  - $\sum_t = \beta_i^t u_ (a^t)$
- Histories
  - Histories of length t
  - $H^t = \{ h^t : h^t = (a^1, ..., a^t) \in A^t \}$
  - (what everybody did on t period of time)
  - all histories: $H = \bigunion_t H^t$
  - Prisoner's Dilemma
    - $A_i = \{C, D\}$
    - History: (C, C) (C, D) (D, D)
    - a strategy for period 4 would specify what a player would do after seing the history
- Subgame perfection
  - subgame
    - subgame starts at a particular $t'$
    - and contains everything that remains
  - subgame perfection
    - take $t'$
    - play NE
    - and NE will be for ever on
    - i.e. no matter that the history is, playing a NE would lead to a subgame perfection
- Prisoner's Dilemma
  - game
    - C
      - 3,3
      - 0,5
    - D
      - 5,0
      - 1,1
  - consider trigger strategy
  - if cooperate, they will have
    - $3 + 3\beta + 3\beta^2 + ... = \frac{3}{1 - \beta}$
  - if defect
    - $5 + \beta + \beta^2 + ... = 5 + \beta \frac{1}{1 - \beta}$
  - difference (we want to sustain (C,C))
    - $\beta \frac{2}{1 - \beta} - 2 \geqslant 0$
    - $\beta \geqslant 0.5$

## Sources
- [Game Theory (coursera)](Game_Theory_(coursera))

[Category:Game Theory](Category_Game_Theory)