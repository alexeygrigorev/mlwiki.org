---
layout: default
permalink: /index.php/Conditional_Probability
tags:
- probability
title: Conditional Probability
---
## Conditional Probability
*Conditional Probability* $P(B \mid A)$ (or $P_A (B)$) is the probability that $B$ happens provided that $A$ has already happen.

The conditional probability is calculated by the following formula:
- $P(B  \mid  A) = \cfrac{P(A \land B)}{P(A)}$


### Intuition
Suppose that there are two events $A$ and $B$
- $A$ and $B$ are not independent
- $A$ may happen before $B$ or $B$ may happen before $A$
- what the probability that both $A$ and $B$ happen?

<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/de/ru/bayesian-formula.png" alt="Image">
- $P(A \land B) = P(A) \cdot P(B \mid A) = P(B) \cdot P(A \mid B)$
- it's either $A$ happens first and then $B$ happens (given that $A$ has happened)
- or $B$ happens first and then $A$ happens (given that $B$ has happened)
- these probabilities are equal
- thus we can calculate $P(A \mid B)$ as
  - $P(A \mid B) = \cfrac{P(A) \cdot P(B \mid A)}{P(B)}$
- how to calculate $P(B)$ if we only have the information from the left?
- $P(B) = P(A) \cdot P(B \mid A) + P(\overline{A}) \cdot P(B  \mid  \overline{A})$


## Examples
### Example 1
An urn contains three red and three blue balls. Two balls are drawn. What is the probability of drawing a red ball, given that the first ball drawn was blue?

- Let event $A$ be drawing a blue ball, and $B$ be drawing a red ball.
- Then we find $P(B \mid A) = \frac{P(AB)}{P(A)}$
- $P(AB)$ is the probability of drawing one red and one blue ball. The total number of outcomes is the number of [partial permutations](Partial_Permutations) of 2 from 6, i.e. $A^2_6 = 6 \cdot 5 = 30$. Out of 30, 9 are favorable to event $AB$, so $P(AB)=\frac{9}{30}$
- $P(A)$ is the probability of drawing a blue ball, $P(A) = 1 / 2$
- $P(B \mid A) = \frac{P(AB)}{P(A)} = \frac{9 / 30}{1 / 2} = \frac{3}{5}$


## See Also
- [Law of Total Probability](Law_of_Total_Probability)
- [Bayes Rule](Bayes_Rule)

## Sources
- Gmurman V.E., Probability Theory and Mathematical Statistics -- 9th edition. Moscow: Vyssh. shk., 2003.
- [Lecture notes on probability theory and mathematical statistics](http://www.dropbox.com/s/j9yxtvkd0ns5eot/Probability_and_Statistics_exams_c.pdf#9)
