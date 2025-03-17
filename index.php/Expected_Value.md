---
title: "Expected Value"
layout: default
permalink: /index.php/Expected_Value
---

# Expected Value

## Expected Value
''Expected Value'' (''Математическое ожидание'') of a [Random Variable](Random_Variable) X
- is a sum of all possible values from $x_i \in \text{Dom}(X)$ multiplied by their probabilities $p_i$
- denoted $E[X]$ or $M[X]$
- it's often called the center of a [Distribution](Distribution)

For discrete random values the formula is 
- $E[X] = \sum_{i = 1}^{\infty} x_i p_i$


### Mean
Expected Value of $X$ is approximately equal to the mean value of $X$
- $E[X] \approx \bar{X}$

$\bar{X} = x_1 \cfrac{m_1}{n} + x_2 \cfrac{m_2}{n} + ... + x_k \cfrac{m_k}{n}$ where
- $\cfrac{m_i}{n} \approx p_i$ relative frequency of $x_i$


## Properties
- $E[C] = C$
- $E[C \cdot X] = C \cdot E[X]$
- $E[X \cdot Y] = E[X] \cdot E[Y]$, if $X$ and $Y$ are independent (proof?)
- and $E[XYZ] = E[X] E[Y] E[Z]$, also if $X$, $Y$ and $Z$ are independent


## See Also
- [Variance](Variance)

## Sources
- Гмурман В.Е., Теория вероятностей и математическая статистика -- 9-е издание. М.: Высш. шк., 2003.

[Category:Probability](Category_Probability)