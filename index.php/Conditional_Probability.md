---
title: Conditional Probability
layout: default
permalink: /index.php/Conditional_Probability
---

# Conditional Probability

## Conditional Probability
''Conditional Probability'' $P(B \mid A)$ (or $P_A (B)$) is the probability that $B$ happens provided that $A$ has already happen.

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
В урне находятся три красных и три синих шара. Вытащим два шара. Какая вероятность появления красного шара, если при первом извлечении выл вытащен синий?

- Пусть событие $A$ - извлечение синего шара, а $B$ - красного.
- Тогда найдем $P(B \mid A) = \frac{P(AB)}{P(A)}$
- $P(AB)$ - вероятность вытащить красный и синий. Общее число исходов - это число [размещений](Partial_Permutations) 2 по 6, т.е. $A^2_6 = 6 \cdot 5 = 30$. Из 30 событию $AB$ благоприятствуют 9, поэтому $P(AB)=\frac{9}{30}$
- $P(A)$ - вероятность вытащить синий шар, $P(A) = 1 / 2$
- $P(B \mid A) = \frac{P(AB)}{P(A)} = \frac{9 / 30}{1 / 2} = \frac{3}{5}$


## See Also
- [Law of Total Probability](Law_of_Total_Probability) 
- [Bayes Rule](Bayes_Rule)

## Sources
- Гмурман В.Е., Теория вероятностей и математическая статистика -- 9-е издание. М.: Высш. шк., 2003.
- [Конспект по теории вероятности и математической статистике](http://www.dropbox.com/s/j9yxtvkd0ns5eot/Probability_and_Statistics_exams_c.pdf#9)

[Category:Russian](Category_Russian)
[Category:Probability](Category_Probability)