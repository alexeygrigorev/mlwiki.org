---
title: "Coalitional Game"
layout: default
permalink: /index.php/Coalitional_Game
---

# Coalitional Game

{{draft}}

## Coalitional Games

### Coalitional Game Theory
- Applications
  - politics, political parties
  - companies
  - marriage, building a house
  - etc
- basic unit - a team
  - the focus is on the group rather than on individuals
- Transferable utility
  - we assign payoff to the whole coalition
  - and player decide on themselves how to distribute it
- Coalitional Game with Transferable Utility
  - a pair $(N, v)$ where
  - $N$ - finite set of players
  - $v: 2^N \mapsto R$
    - utility function
    - associates with coalition rather with an individual
- questions
  - which coalitions will form?
  - how a coalition would divide payoffs among its members?
- Superadditive Coalitional Game
  - a game $G = (N, v)$
  - if
    - for all pairs $(S, T) \subset N$
    - $S \cap T = \emptyset$ (intersection) 
  - then $v(S \cup T) \geqslant v(S) + v(T)$
  - if we form a coalition of $S$ and $T$,
  - then its payoff is at least as good as sum of their payoffs separately
  - eg
    - $N = 3$
    - $v(1) = v(2) = v(3) = 1$
    - $v(1, 2) = 3$, $v(1, 3) = 4$, $v(2, 3) = 5$
    - $v(1, 2, 3) = 7$ - greater than if acted on their own

### The Shapley Value
- what if a "fair" way for a coalition to divide its payoff?
- how we define "fairness"?
- Shapley's idea: members receive payoffs proportional to their marginal contribution
- axioms of fairness
  - symmetry
    - if 2 agents i and j, when contributed, give the same amount of payoff
    - give them the same amount of payoff
    - for each S which contains neither i not j
    - $v(S \cup \{i\}) = v(S \cup \{j\})$
      - if we add $i$ or $j$
      - we will get the same payoff
    - so they should receive the same amount of payment
  - dummy player
    - $i$ is a dummy player if
    - for all $S: v(S \cup {i}) = v(S)$
    - i.e. $i$ doesn't bring anything
    - therefore $i$ shouldn't receive anything
  - additivity
    - if we can separate a game into 2 parts
    - we should be able to decompose payments  
    - $v = v_1 + v_2$
- the Shapley value
  - with all these axioms
  - for game $G(N, v)$
  - the Shapley value is
  - $\phi_i(N, v) = \frac{1}{N|  } \sum_{S \in N\{i}} |S|! (|N| - |S| - 1)! [v(S \cup {i}] - v(S)] $ |  - explanation |    - $\frac{1}{N|  }$ - we average over all combinations |    - sum over all subsets without $i$ |    - $| S |   (|N| - |S| - 1)!$ - weighted by how many different ways we could come up with this calculation |      - $|S |  $ - ways the set S could be formed before i's addition |      - $(|N| - |S| - 1)| $ - ways the remaining players could be added |    - $[v(S \cup {i}] - v(S)]$  - how much $i$ brings if added to the coalition |- theorem
  - given a coalition game $(N, v)$
  - there is a unique payoff division
  - $x(v) = \phi(N, v)$
  - that divides that payoff and satisfies 3 axioms
  - it's the Shapley value

### The Core
- voting game
  - a parliament is made of 4 parties: A, B, C, D
  - each has 45, 25, 15, 15 representatives
  - they are to vote
  - 51 should vote for a law to pass, otherwise all get nothing
  - Shapley Value: (50, 16.67, 16.67, 16.67)
  - But A and B can form a coalition and get more|   (75, 25) |  - so they have incentive to defect |- motivation
  - The Shapley Value - how to divide in a fair way
  - but it ignores the question of stability
  - i.e. would agents be willing to form the grand coalition?
  - or they would prefer to have smaller? (sometimes smaller is more attractive)
  - Under what payment division would the agents want to form the grand coalition?
- core
  - a payoff vector x is in the core of a coalition game $G = (N, v)$ iff
  - $\forall S \subset N, \sum_{i \in S} x_i \geqslant v(S)$
    - for every coalition they could form
    - the value they would get if form a grand coalition
    - $v(S)$ - if they deviate and don't form a GC
  - the sum of payoffs to the agents in many subcoalition S
  - is at least as good as the one they could earn on their own
  - core may be empty and sometimes may not exist
  - and it's not always unique
- Theorem
  - simple game
    - a game $G = (N, v)$ is simple if
    - $\forall S \subset N, v(S) \in \{0, 1\}$
    - for all coalitions they gain either 0 or 1
    - vote game is a simple game: they either get money (1) or no (0)
  - veto player
    - a player $i$ is a veto player if 
    - $v(N - \{i\}) = 9$
    - it's participation is needed if a coalition wants to produce any value
  - in a simple game the core is empty if
  - there is no veto player
- Convex game
  - a game $G=(N, v)$ is convex if
  - for all $(S, T) \subset N, v(S \cup T) \geqslant v(S) + v(T) - v(S \cap T)$
  - for all coalitions in $N$, if they form a bigger coalition, they will achieve
- Airport game
  - several cities want an airport
  - options: 
  - big regional airport and share costs vs own airports
  - $N$ - set of cities
  - sum of costs of building runways for each city in $S$ vs
  - vs cost of the largest runway required by the cities in $S$
  - a convex game
- Theorems
  - every convex game has a non-empty core
  - in every convex game, the Shapley value is in the core
  - (possible to do both stable and fair division)


## Sources
- [Game Theory (coursera)](Game_Theory_(coursera))

[Category:Game Theory](Category_Game_Theory)