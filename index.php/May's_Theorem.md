---
title: "May's Theorem"
layout: default
permalink: /index.php/May's_Theorem
---

# May's Theorem

## May's Theorem
May's Theorem is a [Voting Theory](Voting_Theory) theorem

Desirable Properties 
- Neutrality - we don't look at the names of candidates
- Anonymity - we just count the votes without looking at the names of voters
- [Monotonicity](Monotonicity)

### Theorem
With two candidates ($A = \{a, b\}$) the only voting mechanism that satisfies all these three  properties is [Plurality Voting](Plurality_Voting)

; Anonymity:
- the only possible thing to do is to count the number of voters that prefer $a$ to $b$ and $b$ to $a$:
- let $N(a > b)$ denote the number of people who prefer $a$ to $b$ and $N(b > a)$ - $b$ to $a$
- by neutrality we can say without loss of generality that $N(a > b) > N(b > a)$

For the case when $N(a > b) > N(b > a)$ there are two possible outcomes:
1. $a$ is elected - this case is the [Plurality Voting](Plurality_Voting) case
1. $b$ is elected - not [Plurality Voting](Plurality_Voting)

Case 2
: $N(a > b) > N(b > a)$ but $b$ wins over $a$ - let's show that this assumption leads to contradiction

So suppose that the candidate who receives less votes gets elected
- $N(a > b) > N(b > a) \Rightarrow N(a > b) = N(b > a) + k$ for some $k > 0$
- by applying the [Monotonicity](Monotonicity) principle (we assume it's satisfied) we improve $b$'s position:
: $N(a > b) = N(b > a) + 1$: $b$ still gets elected
- continue improving $b$'s positions
: $N(a > b) = N(b > a) - k' \Rightarrow N(a > b) < N(b > a)$
- since the candidate with fewer votes gets elected, not $a$ wins
- thus [Monotonicity](Monotonicity) is not satisfied: by improving his position $b$ no longer wins
- contradiction: by monotonicity $b$ should remain elected, but by the assumption - $a$


Therefore the only possible outcome under the assumed principles is $a$ wins - which is the [Plurality Voting](Plurality_Voting) mechanism.

$\square$


## See also
- [Arrow's Impossibility Theorem](Arrow's_Impossibility_Theorem)

## Sources
- [Decision Engineering (ULB)](Decision_Engineering_(ULB))

[Category:Voting Theory](Category_Voting_Theory)