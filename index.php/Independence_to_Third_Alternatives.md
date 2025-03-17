---
title: Independence to Third Alternatives
layout: default
permalink: /index.php/Independence_to_Third_Alternatives
---

# Independence to Third Alternatives

## Independence to Third Alternatives
Independence to Third Alternatives, or Independence to Irrelevant alternatives is a principle of [Voting Theory](Voting_Theory).
- it says that if another alternative is added or removed, the position of a candidate should remain at least as good as it was
- this is an important principle in [Arrow's Impossibility Theorem](Arrow's_Impossibility_Theorem)
- also in [MCDA](MCDA) methods violation of this principle leads to [Rank Reversal](Rank_Reversal)


### Definition
- Suppose we have a set of alternatives (candidates) $A^*$
- Let us consider 4 different individual rankings over the sets $A^*$ and $A$ s.t. $A \subset A^*$ 
: (note that $A$ is a strict subset of $A^*$)
- The rankings are $R_1, R_2$ and $R'_1, R'_2$
- $S_1, S_2, S'_1, S'_2$ are indifference relations defined by these orderings (respectively)
- we assume that $R_1 \equiv R'_1$ and $R_2 \equiv R'_2$ for the set $A$
- : that is, $\forall x,y \in A$: 
  - $x \ S_1 \ y \iff x \ S'_1 \ y$ 
  - $x \ S_2 \ y \iff x \ S'_2 \ y$ 

Example:
- $A^* = \{x, y, z\}$
  - $R_1: x > y > z, R'_1: z > y > z$
  - $R_2: z > y > x, R'_2: y > x > z$ 
- now restrict ourselves to $A = \{x, y\} \subset A^*$
  - $R_1 \equiv R'_1$ and $R_2 \equiv R'_2$ 
  - the only thing that changes is the relative position of $z$ within the pairs of rankings


A voting method $H$ is ''independent to third alternatives'' if 
- the global ordering produced by $H$ under the set $A$ is the same for both rankings such rankings:
- $H(R_1, R_2) | _A \equiv  H(R'_1, R'_2) |_A$ |
In other words, ordering of the set $A^* - A$ is irrelevant to the choice over $A$


### Example 1
- Consider two dishes: beef and lamb
- The choice between these two alternatives should not change when pork is also available
- pork is ''irrelevant alternative'' to the preference ordering of beef and lamb


### Example 2
Suppose there exist two ways to subscribe to some newspaper:
- paper subscription $P$: 100 USD
- web version $W$: 60 USD

Note that for the publisher the web version costs nearly nothing


The publisher proposes the following:
- $P$: 100 USD, $W$: 60 USD, $P+W$ also 100 USD.
- in this case we see that no rational decision taker will ever take just $P$, but always $P+W$

Before the preposition the distribution of readers could be this:
- $P$ for 100 USD: 30%
- $W$ for 60 USD: 70%

After: 
- $P$ for 100 USD: 0%
- $W$ for 60 USD: 30%
- $P+W$ for 100 USD: 70% 

The part of readers switched $\Rightarrow$ More money


----

There are several ways in which a method may suffer from dependence to 3rd alternatives:
- Risk of Manipulation



## Risk of Manipulation
A method suffers from the ''Risk of Manipulation'' if the outcome of an election can be changed by
- adding a new candidate or
- deleting a candidate 

This manipulation is also sometimes called ''control''.

Manipulation:
- suppose somebody knows the individual rankings 
- they may propose a new candidate that will take some votes 
- this way influencing the final result

Methods that suffer from the manipulation:
- [Plurality Voting](Plurality_Voting)
- [Two-Round Voting](Two-Round_Voting)
- [Condorcet's Rule](Condorcet's_Rule)
- [Borda's Rule](Borda's_Rule)



## Sources
- [Decision Engineering (ULB)](Decision_Engineering_(ULB))
- EC228 Voting Theory Lecture Notes [http://www2.warwick.ac.uk/fac/soc/economics/current/modules/ec228/details/lecturenotes/lecturenotesbook.pdf]

[Category:Voting Theory](Category_Voting_Theory)