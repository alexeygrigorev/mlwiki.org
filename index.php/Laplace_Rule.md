---
title: "Laplace Rule"
layout: default
permalink: /index.php/Laplace_Rule
---

# Laplace Rule

## Laplace Rule
How to choose an alternative in [Decision Under Uncertainty](Decision_Under_Uncertainty)? The Laplace Rule, also called the Principle of Insufficient Reasoning, helps to do that.


### Main idea
- (using notation from [Decision Under Uncertainty](Decision_Under_Uncertainty))
- since there is no way to assess probabilities in [Decision Under Uncertainty](Decision_Under_Uncertainty) models - assume the uniform distribution
- so each state of nature $e \in E$ is expected to happen with probability $1 / | E|$ |- and we compute the expected values of the consequences based on these probabilities


So,
- choose $a \in A$ that solves the following:
- $\max_{a \in A} \sum_{e \in E} \cfrac{1}

### Example
Consider this matrix:

|   $c$  |  $e_1$  |  $e_2$  |  $e_4$  |    |   $a_1$   |  40  |  70  |  -20  |  90/3 ||   $a_2$   |  -10  |  40  |  100  |  <font color="blue">130/3</font> ||   $a_3$   |  20  |  40  |  -5  |  55/3 |

So we choose $a_2$ because it gives the best result on average


### Remarks
- it must be meaningful to make a linear combination of the consequences 
  - i.e. the scale should be numerical
- the principle should be used with caution
  - you either become the king of Belgium or not - are these events equally likely?

### Manipulation
can manipulate the results by adding new alternatives 
- ([Independence to Third Alternatives](Independence_to_Third_Alternatives) is not satisfied)

Suppose we have two scenarios:
- $E$ and $\overline{E}$
  - by the principle we have $P(E) = P(\overline{E}) = 0.5$
- suppose we modify an alternative by adding something that is always true
  - $\overline{E} \equiv \overline{E} \land (R \lor \overline{R})$
  - then we can distribute the OR and have $[\overline{E} \land R] \lor [\overline{E} \land \overline{R}]$
- so now we have 3 alternatives:
  - $E$, $\overline{E} \land R$ and $\overline{E} \land \overline{R}$
  - and now $P(E) = P(\overline{E} \land R) = P(\overline{E} \land \overline{R}) = 1/3$
- i.e. we've manipulated the results



## Sources
- [Decision Engineering (ULB)](Decision_Engineering_(ULB))

[Category:Decision Under Uncertainty](Category_Decision_Under_Uncertainty)