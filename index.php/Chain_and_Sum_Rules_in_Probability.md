---
layout: default
permalink: /index.php/Chain_and_Sum_Rules_in_Probability
tags:
- probability
title: Chain and Sum Rules in Probability
---
## Addition Theorem of Probabilities

The *sum* $A + B$ of two events $A$ and $B$ is the event consisting of the occurrence of event $A$ or event $B$.

**Theorem**. The probability of occurrence of one of two mutually exclusive events equals the sum of their probabilities:

$P(A + B) = P(A) + P(B)$

Proof:
$n$ - total number of outcomes, $m_a$ - outcomes favorable to $A$, $m_b$ - outcomes favorable to $B$

$P(A + B) = \frac{m_a + m_b}{n} = \frac{m_a}{n} + \frac{m_b}{n} = P(A) + P(B)$


### Corollaries
- The sum of probabilities of all events $A_i \in \Omega$ forming a [complete group of events](Probability#Events_and_Trials) equals one.
  $P(A_1) + ... + P(A_n) = 1$
- The sum of the probability of event $A$ and its complementary event $\bar{A}$ equals one, since $A$ and $\bar{A}$ form a complete group of events.
  $P(A) + P(\bar{A}) = 1$


## Addition Theorem for Compatible Events
Two events are called *compatible* if the occurrence of one does not exclude the occurrence of the other in the same trial.


**Theorem.** The probability of occurrence of at least one of two compatible events equals the sum of their probabilities minus the probability of their joint occurrence:

$P(A + B) = P(A) + P(B) - P(AB)$

Proof:
- $A + B$ occurs if $A\bar{B}$, $\bar{A}B$, or $AB$ occurs. Since these events are mutually exclusive, by the addition theorem we have
  $P(A + B) = P(A\bar{B}) + P(\bar{A}B) + P(AB)$ (**\***)
- $A$ occurs if either $AB$ or $A\bar{B}$ occurs. By the addition theorem,
  $P(A) = P(A\bar{B}) + P(AB)$ or
  $P(A\bar{B}) = P(A) - P(AB)$ (**\*\***)
- Similarly, $B$ occurs if either $AB$ or $\bar{A}B$ occurs. That is,
  $P(B) = P(\bar{A}B) + P(AB)$ or
  $P(\bar{A}B) = P(B) - P(AB)$ (**\*\*\***)
- Substituting (**\*\***) and (**\*\*\***) into (**\***), we get
  $P(A + B) = P(A) + P(B) - P(AB)$

## Multiplication Theorem of Probabilities
The *product* of events $A$ and $B$ is the event $A \cdot B$ consisting of the joint occurrence of these events.

Example:
- $A$ - the part is functional
- $B$ - the part is painted
- $A \cdot B$ - the part is functional and painted

**Theorem**. Consider two events $A$ and $B$. We know $P(A)$ and $P(B\mid A)$. How do we find the probability that both $A$ and $B$ occur?
$P(A \cdot B) = P(A) \cdot P(B \mid A)$ - by the definition of [conditional probability](Conditional_Probability).
For [independent events](Independence) the multiplication theorem becomes

$P(A \cdot B) = P(A) \cdot P(B)$

## See also
- [Sum and Product Rules](Sum_and_Product_Rules) (Combinatorics)

## Sources
- Gmurman V.E., Probability Theory and Mathematical Statistics -- 9th edition. Moscow: Vysshaya Shkola, 2003.
