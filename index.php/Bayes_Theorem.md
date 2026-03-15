---
layout: default
permalink: /index.php/Bayes_Theorem
tags:
- probability
title: Bayes Theorem
---
## Bayes Theorem

Let $H = \{H_1, H_2, ..., H_n\}$ form a complete group of events and $A$ can only occur when one of the $\{ H_i \}$ occurs.

We call events $H_1, H_2, ..., H_n$ ''hypotheses'', since it is not known in advance which one will occur.

''Bayes Theorem'' allows us to re-evaluate the probabilities of the hypotheses after the result of a trial becomes known, following which $A$ has occurred.

$P(H_i |  A) = \frac{P(H_i) P(A | H_i)}{P(H_1) P(A|H_1) + P(H_2) P(A|H_2) + ... + P(H_n) P(A|H_n)}$

$P(H_i)$ is called the ''prior probability'', $P(H_i| A)$ is the ''posterior probability''.
### Derivation
- Suppose a trial has been conducted, as a result of which event $A$ has occurred.
- Let us find the conditional probabilities $P(H_1| A), P(H_2|A), ..., P(H_n|A)$  |: That is, the probabilities of the hypotheses, given that event $A$ has already occurred.

- For $P(H_1| A) $ by the multiplication theorem we have  |: $P(A H_1) = P(A) P(H_1 A) = P(H_1) P(A |  H_1)$ |: That is, $P(H_1 |  A) = \frac{P(H_1) P(A | H_1)}{P(A)}$
- If we replace all $P(A)$ with the total probability formula, we get
  $P(H_1 |  A) = \frac{P(H_1) P(A | H_1)}{P(H_1) P(A|H_1) + P(H_2) P(A|H_2) + ... + P(H_n) P(A|H_n)}$
- Similarly for the other hypotheses. That is,
  $P(H_i |  A) = \frac{P(H_i) P(A | H_i)}{P(H_1) P(A|H_1) + P(H_2) P(A|H_2) + ... + P(H_n) P(A|H_n)}$

### Example 1
Each of three shooters can fire two shots. The hit probabilities are: $P(A_1) = 0.3$, $P(A_2) = 0.5$ and $P(A_3) = 0.8$. One of the shooters fired twice and missed both times. What is the probability that it was the first shooter?

- Let hypothesis $H_1$ be that the first shooter fired, $H_2$ that the second fired, and $H_3$ that the third fired.
- $P(H_1) = P(H_2) = P(H_3) = \frac{1}{3}$.
- $D$ - the shooter misses twice.
- $P(D| H_1) = 0.7 * 0.7 = 0.49$
- $P(D| H_2) = 0.25$
- $P(D| H_3) = 0.04$
Then by Bayes' formula
- $P(H_1| D) = 0.628$
### Example 2
In the first box there are 2 gold coins, in the second one gold and one silver, and in the third two silver coins. A coin is randomly selected and turns out to be gold. What is the probability that the second coin in the same box is also gold?

The second coin can only be gold in the first box, so we need to find the probability that the coin was drawn from the first box.

Let $H_1$ be the hypothesis that the coin was drawn from the first box, $H_2$ from the second, and $H_3$ from the third. Obviously, $P(H_1) = P(H_2) = P(H_3) = \fraq{1}{3}$.

$D$ - the drawn coin is gold. Then $P(D| H_1) = 1$, $P(D|H_2) = 0.5$ and $P(D|H_3) = 0$.
We compute $P(H_1| D)$ using the formula $P(H_1|D) = \frac{ P(H_1) P(A|H_1) }{ \sum_{i=1}^{3} P(H_i) P(D|H_i) }$

## See also
- [Conditional Probability](Conditional_Probability)
- [Law of Total Probability](Law_of_Total_Probability)

## Sources
- Gmurman V.E., Probability Theory and Mathematical Statistics -- 9th edition. Moscow: Vyssh. shk., 2003.
- [Lecture notes on probability theory and mathematical statistics](http://www.dropbox.com/s/j9yxtvkd0ns5eot/Probability_and_Statistics_exams_c.pdf#13)
