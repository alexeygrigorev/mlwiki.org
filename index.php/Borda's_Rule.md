---
title: "Borda's Rule"
layout: default
permalink: /index.php/Borda's_Rule
---

# Borda's Rule

## Borda's Rule
Borda was a director for the French Academy of science. He proposed a Voting Mechanism for [Voting Theory](Voting_Theory) based on points:
- assign weights to all the candidates in the ranking
- do not consider just the most preferable 


The Borda Rule: 
- $k$ candidates from set $A$  
- $N$ voters communicate their individual preferences $P_i$
- for each individual preference $P_i$ assign the points:
  - the 1st candidate in $P_i$ gets $k$ points
  - the 2nd candidate in $P_i$ gets $k - 1$ points
  - the $j$th candidate in $P_i$ gets $k - j + 1$ points
  - the $k$th candidate in $P_i$ gets 1 point
  - so define the ''individual Borda score'' $S_i(a)$ as the score that candidate $a$ receivers from a voter $i$
  - $S_i(a) = k - \text{pos}_i (a)$ where $\text{pos}_i(a)$ is the position of $a$ in $R_i$
- define the ''Borda score'' $B(c)$ for candidate $c$ as the sum of points from all $P_i$
  - $B(c) = \sum_j S_j(c)$
- the candidate with the highest Borda score wins the election


### Example
Individual preferences:
- $a > b > c$ - 11 votes
- $b > a > c$ - 8 votes
- $c > b > a$ - 2 votes

Scores:
- $B(a) = 3 \cdot 11 + 2 \cdot 8 + 1 \cdot 2 = 51$
- $B(b) = 3 \cdot 8 + 2 \cdot 11 + 2 \cdot 2 = 50$
- $B(c) = 1 \cdot 11 + 1 \cdot 8 + 2 \cdot 3 = 25$

$a$ gets elected


## Criteria
This method satisfies:
- [Monotonicity](Monotonicity)
- [Separability](Separability)

This method does not satisfy:
- [Independence to Third Alternatives](Independence_to_Third_Alternatives)
- [Condorcet Fairness](Condorcet's_Rule#Fairness)


### [Monotonicity](Monotonicity)
- let $A$ be the set of candidates: $A = \{a, b, c, ...\}$
- $N$ voters 
- suppose $x$ improves its positions only for one voter $j$
  - i.e. there's a new preference ranking $P'_j$ where the candidate $x$ has a better position than in the old preference ranking $P_j$
  - if $a$ improved his ranking on $m$ positions, then $S'_j(x) = S_j(x) + m$ ($m > 0$)

Now let's analyze how it will affect the global score
- the score before: $B(x) = \sum_i S_i(x)$ 
- the score after: $B'(x) = \sum_i S'_i(x) = ...$
  - $... \sum_{i \ne j} S'_x(x) + S'_j(x) = ...$ 
  - the scores for $i \ne j$ has not changed, so can replace them by the old score
  - $... \sum_{i \ne j} S_x(x) + S'_j(x) = ...$
  - and  $S'_j(x) = S_j(x) + m$
  - $... \sum_{i \ne j} S_x(x) + S_j(x) + m = B(x) + m$
- so $B'(x) = B(x) + m \Rightarrow B'(x) > B(x)$
- and therefore the Monotonicity principle is respected


### [Separability](Separability)
[Separability](Separability) is respected if
- we divide the region $\Omega$ into two regions $N$ and $\overline{N}$
- the global ranking is the same in $N$ and $\overline{N}$ and the same candidate $a$ wins
- then if considered the whole region $\Omega$, the global ranking should be the same and the same candidate $a$ should win

Suppose that 
- $S_N(a) \geqslant S_N(b)$ and $S_\overline{N}(a) \geqslant S_\overline{N}(b)$
  - and therefore $B_N(a) \geqslant B_N(b)$ and $B_\overline{N}(a) \geqslant B_\overline{N}(b)$ (1)
  - i.e. in two regions the relation between candidates $a$ and $b$ is the same
- consider the whole region $\Omega$: 
  - $B(a) = \sum_j S_j(a) = ...$ 
  - can split the sum into two parts: for $N$ and for $\overline{N}$
  - $... \sum_{j \in N} S_j(a) + \sum_{j \not \in N} S_j(a) = B_N(a) + B_\overline{N}(a)$ 
  - the same for $b$: $B(b) = B_N(b) + B_\overline{N}(b)$
- so because of (1) can say that $B(a) \geqslant B(b)$
- thus the Separability principle is respected


### [Independence to Third Alternatives](Independence_to_Third_Alternatives)
Consider this example:
- $N = 7, A = \{a, b, c, d\}$

Preferences:
- 3 voters: $c > b > a > d$
- 2 voters: $b > a > d > c$
- 2 voters: $a > d > c > b$
- The outcome is $a > b > c > d$

$d$ decides to withdraw - anyway he has no chance of winning
- but it has a strong effect on the result|   |- Now the global ranking is $c > b > a$ - the complete opposite|  | |
Another example:
- $N = 5, A = \{a, b, c\}$

Preferences:
- 2: $a > b > c$
- 1: $c > a > b$
- 2: $b > c > a$

Scores:
- $B(a) = 9, B(b) = 11, B(c) = 9$ 
- outcome: $b > a \geqslant c$

Now $d$ also decides to participate:
- 2: $a > d > b > c$
- 1: $c > a > d > b$
- 2: $b > c > a > d$

Scores are:
- $B(a) = 15 > B(b) = 14 > B(c) = 10 > B(d) = 9$
- note that even though $d$ is the last one in the global rating, adding him changed the winner|   | |
So we see that by carefully choosing new candidates it's possible to manipulate the results. 


### [Condorcet Fairness](Condorcet's_Rule#Fairness)
Consider these individual rankings for $A = \{a, b, c\}, N = 5$
- 3: $a > b > c$
- 2: $b > c > a$

Borda Score:
- $S(a) = 3 \cdot 3 + 2 \cdot 1 = 11$
- $S(b) = 3 \cdot 2 + 2 \cdot 3 = 12$
- $S(c) = 2 \cdot 2 + 3 \cdot 1 = 7$
- $b$ wins the election

However in pair-wise comparison we see that 
- $a > b$ for 3 voters
- $b > a$ for 2 voters

$\to$ the majority prefers $a$ over $b$ but $b$ wins the election
- the Condorcet Fairness criterion is not satisfied 


## "Modified" Borda's Rule
Slightly different approach
- instead of assigning points to all $k$ candidates
- assign points to $n < k$ candidates
- i.e. assign $n$ points to 1st, $n-1$ to 2nd, ..., $1$ to $n$th and 0 to the rest


## Links
- http://www.ctl.ua.edu/math103/voting/borda.htm

## Sources
- [Decision Engineering (ULB)](Decision_Engineering_(ULB))
- Voting Fairness Criteria [http://www.math.unl.edu/~bharbourne1/M203JSpr09/VotingFairnessHandout.pdf]

[Category:Voting Theory](Category_Voting_Theory)