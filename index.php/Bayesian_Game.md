---
title: Bayesian Game
layout: default
permalink: /index.php/Bayesian_Game
---

# Bayesian Game

{{draft}}

## Bayesian Games
### Motivation
- auctions
  - I'm not quite sure what are the utilities of other players
- usually everyone knows
  - the number of players 
  - the actions available to each player
  - payoff associated with each action vector

### Assumptions
- there are some games (not only one)
  - all games have the same number of agents
  - the same strategy space for each agent
  - the only difference is in the payoff
- agents' beliefs are posterior
  - obtained by conditioning a common prior on individual private signals
  - common prior - what's possible
  - individual private signals - beliefs that agents have

### Bayesian game
- Definition 1: based on Information set
  - Intuition
    - BG - a set of games that differ only in their payoffs
    - plus a common prior is defined over them
    - and a partition structure is defined over the games for each agent
  - A BG is a tuple $(N, G, P, I)$ where
    - $N$ - a set of agents
    - G$$ set of games with N agents for each
      - if $g$ and $g' \in G$ for each agent $i \in N$
      - the strategy space in $g$ is identical to the strategy space in $g'$
      - (so games differ only in their utility functions)
    - $P \in \Pi (G)$ - a common prior over games
      - $\Pi(G)$ set of probability distribution over $G$
      - (how likely each of these games is)
    - $I = (I_1, I_2, ..., I_N)$ is a set of partitions of $G$, one for each agent
      - set of equivalence classes: some games are indistinguishable
  - Example
    - 4 games
      - Matching Pennies
      - Prisoner's Dilemma
      - Coordination game
      - The Battle of the Sexes
    - equivalence classes
      - Player I
        - MP and PD
        - Coord and BoS
      - Player II
        - MP and Coord
        - PD and BoS
    - when playing, players don't know what game they're playing
    - only the equivalence class
- Definition 2: based on epistemic types
  - directly represents uncertainly over utility function using the notion of epistemic type
  - epistemic type - private information of an agent
  - A BG is a tuple $(N, A, \Theta, p, u)$ where
    - $N$ - a set of agents
    - $A = (A_1, A_2, ..., A_n)$
      - $A_i$ - set of actions available to $i$
    - $\Theta = (\theta_1, ..., \theta_n)$
      - $\theta_i$ - type space of player $i$
    - $p: \theta \mapsto [0, 1]$
      - the common prior over types
    - $u = (u_1, ..., u_n)$
      - where $u_i = A * \theta \mapsto \mathbb{R}$

### Analysing Bayesian Games
- Bayesian (Nash) Equilibrium
  - a plan of actions for each player as a function that maximizes each type's expected utility
  - so it should be a best reply
  - If I observe a certain type, what am I going to do?
  - expecting over the actions of other players
    - what are the expected action distributions we're going to face
  - expecting over the types of ther players
- Strategies
  - given a Bayesian finite game $(N, A, \Theta, p, u)$
  - pure strategy
    - $s_i : \theta_i \mapsto A_i$
      - for a type, what action you'll take?
    - a choice of a pure strategy for player i as a function of her type
  - mixed strategy
    - $s_i : \theta_i \mapsto \Pi(A_i)$
      - $\Pi(A_i)$ - probability distribution over actions of your type
    - a choice of x mixed action for player i as a function of his type
    - distribution over actions
      - $s_i(a_i |  \Theta_i)$ |      - [what's the probability that action a_i will be chosen if they happen to be of type $\Theta_i$]
      - the probability under mixed strategy $s_i$ that agent $i$ plays action $a_i$, given that type is $\Theta_i$
- types
  - ex-ante
    - the agent knows nothing about anyone's actual type
  - interim
    - agents know their own types, but don't know the types of each other
    - for player i with respect to type \theta_i and mixed strategy profile s
    - expected utility
      - $EU_i(s |  \Theta_i) = \sum_{\theta_{-i} \in \Theta_{-i}} p (\theta_{-i} | \theta{i}) * \sum_{a \in A}(\prod_{j \in N} s_i(a_i | \theta_i) * u_i(a, \Theta_i, \Theta_{-i}))$ |      - $u_i(a, \Theta_i, \Theta_{-i})$ - utilities evaluated with respect to their types
      - $\prod_{j \in N} s_i(a_i |  \theta_i)$  - what other players will be doing |      - $\sum_{\theta_{-i) \in \Theta_{-i}} p (\theta_{-i} |  \theta{i})$ - sum across all probabilities of types for others |      - $EU_i(s |  \Theta_i)$ - what can i expect of he of type \Theta_i and follows s |  - ex-post
    - averybody knows everything
    - expected utility
      - $EU_i (s) = \sum_{\theta_i \in \Theta_i} p(\theta_i) EU_i(s |  \theta_i)$ |- Bayesian Equilibrium
  - a mixed strategy profile s that satisfies
  - $s_i \in \arg \max_{s'_i} EU_i(s'_i, s_{-i} |  \Theta_i)$ |  - each individual should choose the best response, maximizing the expected utility
  - for each $i$ and $\theta_i \in \Theta_i$
  - summary
    - it explicitly models behavior in uncertain environment
    - players choose strategies to maximize their payoffs in response to others
    - accounting for
      - strategic uncertainty about how others will play
      - payoff uncertainty about the value of their actions
- A Sherif's Dilemma
  - a sheriff faces an armed suspect and they each must (simultaneously) decide whether to shot or not
  - a suspect is criminal with probability p and not a criminal with probability 1 - p
  - the sheriff would rather shoot if suspect shoots, and not shoot otherwise
  - the criminal would rather shoot even if the sheriff doesn't - he doesn't want to be caught
  - the innocent would rather not shoot even if the sheriff does
  - ==> sheriff's best reply to shoot if $p > 1/3$


## Sources
- [Game Theory (coursera)](Game_Theory_(coursera))

[Category:Game Theory](Category_Game_Theory)