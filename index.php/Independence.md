---
layout: default
permalink: /index.php/Independence
tags:
- probability
title: Independence
---
## Independent Events
Event $B$ is called *independent* of event $A$ if the occurrence of event $A$ does not change the probability of event $B$, i.e.,

$P(B |  A) = P(B)$ and $P(A | B) = P(A)$
Alternatively, two events are independent if the probability of their joint occurrence equals the product of their probabilities:

$P(A \cdot B) = P(A) \cdot P(B)$

Otherwise, the events are called *dependent*.

## Pairwise Independence and Mutual Independence
Several events are called *pairwise independent* if every pair of them is independent.

Events are called *mutually independent* if they are pairwise independent and also independent of all possible products of the other events.

For such events $P(A_1 \cdot ... \cdot A_n) = P(A_1) \cdot ... \cdot P(A_n) $


## Occurrence of at Least One Event
**Theorem**. The probability of occurrence of at least one of the mutually independent events $A_1, ..., A_n$ is

$P(A) = 1 - P(\bar{A}_1 \bar{A}_2 ... \bar{A}_n)$

or, equivalently,

$P(A) = 1 - q_1 q_2 ... q_n$

Since events $A$ and $\bar{A}_1 \bar{A}_2 ... \bar{A}_n$ are complementary.

### Example
The probability that the first cannon hits the target is 0.7 (event $A$). For the second cannon it is 0.8 (event $B$). Find the probability that at least one cannon hits the target in a single volley.

- Both cannons hit the target: $P(AB) = 0.7 + 0.8 = 0.56$
- At least one cannon hits the target: $P(A + B) = 0.7 + 0.8 - 0.56 = 0.94$ (by the [addition theorem for compatible events](Chain_and_Sum_Rules_in_Probability#Addition_Theorem_for_Compatible_Events))

- Using the formula instead: $p = 1 - q_1 q_2 = 1 - 0.3 \cdot 0.2 = 0.94$

### Example 2
The probability that a random number generator produces a given word
- http://forum.vingrad.ru/forum/topic-365451/anchor-entry2556737/0.html

## See also
- [Conditional Probability](Conditional_Probability)

## Sources
- Gmurman V.E., Probability Theory and Mathematical Statistics -- 9th edition. Moscow: Vysshaya Shkola, 2003.
