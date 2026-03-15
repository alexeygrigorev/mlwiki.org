---
layout: default
permalink: /index.php/Law_of_Total_Probability
tags:
- probability
title: Law of Total Probability
---
## Law of Total Probability

Suppose event $A$ can occur given the occurrence of one of the events $B_1, B_2, ..., B_n$, which form a complete group of events. Suppose the probabilities of these events $P(B_1), P(B_2), ..., P(B_n)$ are known, as well as the conditional probabilities $P(A| B_1), P(A|B_2), ..., P(A|B_n)$ of event $A$ given each of $B_1, ..., B_n$.

**Theorem.** The probability of event $A$, which can occur only given the occurrence of one of the mutually exclusive events $B_1, B_2, ..., B_n$ forming a complete group, is

$P(A) = P(B_1) P(A| B_1) + P(B_2) P(A|B_2) + ... + P(B_n) P(A|B_n)$

This formula is called the *law of total probability* (it follows from the [definition of conditional probability](Conditional_Probability)).


### Proof
Since $B_1, B_2, ..., B_n$ are mutually exclusive, the occurrence of $A$ means the occurrence of one of $B_1 A, B_2 A, ..., B_n A$.

By the addition theorem we get
: $P(A) = P(B_1 A) + P(B_2 A) + ... + P(B_n A)$

And, applying the multiplication theorem to each term of the sum, we get
: $P(A) = P(B_1) P(A| B_1) + P(B_2) P(A|B_2) + ... + P(B_n) P(A|B_n)$.

### Example
A store receives products from three factories in proportions of 20%, 30%, and 50%. The first factory produces 10% premium-grade products, the second -- 5%, and the third -- 20%. What is the probability that a randomly purchased product is premium grade?

- Let event $B_i$ be the purchase of a product from factory $i$.
- Then $P(B_1) = 0.2$, $P(B_2) = 0.3$, and $P(B_3) = 0.5$.
- $A$ is the purchase of a premium-grade product.
- Then $P(A| B_1) = 0.1$, $P(A|B_2) = 0.05$, and $P(A|B_3) = 0.2$.
- By the law of total probability we get
: $P(A) = \sum_{i = 1}^{3} P(B_i) P(A| B_i) = 0.135$

## See also
- [Conditional Probability](Conditional_Probability)
- [Bayes Rule](Bayes_Rule)


## Sources
- Gmurman V.E., Probability Theory and Mathematical Statistics -- 9th edition. Moscow: Vysshaya Shkola, 2003.
- [Lecture notes on Probability Theory and Mathematical Statistics](http://www.dropbox.com/s/j9yxtvkd0ns5eot/Probability_and_Statistics_exams_c.pdf#13)
