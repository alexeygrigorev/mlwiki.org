---
layout: default
permalink: /index.php/Voting_Theory_Exercises
tags:
- voting-theory
title: Voting Theory Exercises
---
## [Voting Theory](Voting_Theory) Exercises
- Exercises: [https://www.dropbox.com/s/lfu7jt16n99pmyj/session-01-voting%20theory.pdf]
- Solutions: [https://www.dropbox.com/s/69u5we1cuux1z67/session-01-voting%20theory%20solutions.pdf]
- Used Notation: [Voting Theory Relations](Voting_Theory_Relations)


## Exercise 4
- $N = 10$, $A$ - set of candidates
- define a relation $a \ B \ b$ as "$a$ is better than $b$"
- if this relation transitive and can it have cycles?

### Exercise 4.1
Define $a \ B \ b$ as 
- $a \ B \ b \iff n_{ab} \geqslant 6$ where $n_{ab}$ is the number of people who rank $a$ before $b$ (like in [Condorcet's Rule](Condorcet's_Rule))

This voting system is very similar to the [Condorcet's Rule](Condorcet's_Rule)

We can show that it means to be transitive:
- ex-transitivity.png
- i.e. if there exists a loop then there can be no transitivity 
- so it suffices to show that there can be cycles and it will answer both questions

Consider the following ranking:
- $3: a > b > c$
- $3: b > c > a$
- $4: c > a > b$

Now calculate the $B$ relationship:
- $a \ B \ b$ since $n_{ab} = 7$
- $b \ B \ c$ since $n_{bc} = 6$
- $c \ B \ a$ since $n_{ca} = 7$

We have a cycle:
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/de/vt/condorcet-monotonicity-2.png" alt="Image"> 


### Exercise 4.1
Define $a \ B \ b$ as 
- $a \ B \ b \iff n_{ab} \geqslant 7$ where $n_{ab}$ is the number of people who rank $a$ before $b$

In this case $B$ also is not always transitive.

Consider the following example: 
- $4: a > b > c$
- $3: b > c > a$
- $3: c > a > b$
- in this case there are not enough votes to have an edge $c \to a$
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/de/vt/ex-not-completeness.png" alt="Image">
- note that his shows that the relation $B$ is not complete (this can also be the case for the previous exercise)

And there can be no cycles: too few voters for this 
- consider the case with 3 candidates: $A = \{a, b, c\}$
- there are 6 possible individual rankings for elements from $A$: there are 3|   permutations of $A$ |  - $R_1: a < b < c$ -- $n_1$ voters |  - $R_2: a < c < b$ -- $n_2$ voters
  - $R_3: b < a < b$ -- $n_3$ voters
  - $R_4: b < c < a$ -- $n_4$ voters
  - $R_5: c < a < b$ -- $n_5$ voters
  - $R_6: c < b < a$ -- $n_6$ voters
  - $n_i$ - the number of voters with ranking $R_i$
- to have a cycle we need to have:
  - $n_{ab} = n_1 + n_2 + n_6 \geqslant 7$
  - $n_{ba} = n_1 + n_3 + n_4 \geqslant 7$
  - $n_{ca} = n_4 + n_5 + n_6 \geqslant 7$
- let's sum up these 
  - $2 \cdot n_1 + n_2 + n_3 + 2 \cdot n_4 + n_5 + 2 \cdot n_6 \geqslant 21$ (1)
- recall that we have only 10 voters:
  - $n_1 + n_2 + n_3 + n_4 + n_5 + n_6 = 10$ (2)
- now let's calculate (1) - (2):
  - $n_1 + n_4 + n_6 \geqslant 11$
  - this cannot happen: we have only 10 voters
- contradiction



## Sources
- [Decision Engineering (ULB)](Decision_Engineering_(ULB))
