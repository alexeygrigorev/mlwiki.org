---
title: Two-Round Voting
layout: default
permalink: /index.php/Two-Round_Voting
---

# Two-Round Voting

## Two-Round Voting
This a voting mechanism from [Voting Theory](Voting_Theory). It is essentially the same as [Plurality Voting](Plurality_Voting), but run in two rounds

Given set $A$ of candidates
- Round 1: Using plurality voting mechanism, choose two candidates $a, b \in A$
- Round 2: Plurality voting only between the two $a$ and $b$ 


Example
- here we assume that preferences are ''stable'': people don't change their preferences between two rounds
- Round 1:
  - $a > b > c$ - 11 votes
  - $b > a > c$ - 8 votes
  - $c > b > a$ - 2 votes
  - $a$ and $b$ win the 1st round
- Round 2:
  - (we just remove $c$ from the previous rankings)
  - $a > b$ - 11 votes
  - $b > a$ - 8 + 2 votes



## Criteria
This method satisfies:


This method does not satisfy:
- [Monotonicity](Monotonicity)
- [Separability](Separability)
- [Condorcet Fairness](Condorcet's_Rule#Fairness)


### [Monotonicity](Monotonicity)
$N = 16$ and $A = \{x, y, z\}$ 

We have the following individual preferences: 
- 6 voters $x > y > z$
- 5 voters $z > x > y$
- 4 voters $y > z > x$
- 2 voters $y > x > z$

Elections:
- Round 1: $x$ and $y$ win ($x=6, z=5, y=6$)
- Round 2: $x$ wins (6+5: $x > y$, 6: $y > x$)


But suppose that $x$ manages to also convince the last two voters that he is better:
- 6 voters $x > y > z$
- 5 voters $z > x > y$
- 4 voters $y > z > x$
- 2 voters $x > y > z$

Note that $x$ by improving his position should remain the winner

Elections:
- Round 1: $x$ and $z$ ($x=6+2, z=5, y=4$)
- Round 2: $z$ wins|   (not $x$!) (6+2: $x > y$, 9: $z > x$) | |This counter-example shows that the [Monotonicity](Monotonicity) principle is not respected by Two-Round Voting method.


### [Separability](Separability)
Suppose we run an election in Belgium
- there are 2 communes - 2 regions
- we have 3 candidates: $A = \{a, b, c\}$
- $N = 13$ for each region

|    |  Region I  |  Region II   |  preferences ||   |- 4: $a > b > c$
- 3: $b > a > c$
- 3: $c > a > b$
- 3: $c > b > a$
|  |- 4: $a > b > c$
- 3: $c > a > b$
- 3: $b > a > c$
- 3: $b > a > c$
|  Round 1 ||  ${\color{blue}{a: 4}}, b: 3, {\color{blue}{c: 6}}$ ||  ${\color{blue}{a: 4}}, {\color{blue}{b: 6}}, c: 3$ ||  Round 2 ||  ${\color{blue}{a: 7}}, c: 6$ ||  ${\color{blue}{a: 7}}, b: 6$ |
In both regions $a$ wins.

But if we consider the global region, we'll have different results:
- Round 1: ${\color{red}{a: 8}}, {\color{blue}{b: 9, c: 9}}$ - note that $a$ loses and doesn't go to the next round
- Round 2: ${\color{blue}{b: 17}}, c: 9$
- $c$ wins

So the separability principle is not satisfied in this example. 


### [Condorcet Fairness Criterion](Condorcet's_Rule#Fairness)
Is not satisfied
- see an example in [Voting Theory Examples#Example 1: Two-Round Voting](Voting_Theory_Examples#Example_1__Two-Round_Voting)



## Links
- http://www.ctl.ua.edu/math103/voting/methodof.htm

## Sources
- [Decision Engineering (ULB)](Decision_Engineering_(ULB))

[Category:Voting Theory](Category_Voting_Theory)