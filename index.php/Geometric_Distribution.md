---
title: Geometric Distribution
layout: default
permalink: /index.php/Geometric_Distribution
---

# Geometric Distribution

## Geometric Distribution
A geometric distribution is a Discrete [Distribution](Distribution) of [Random Variable](Random_Variable)s


Assume we run a series of [Bernoulli Trial](Bernoulli_Trial)s where the probability of seing the event $A$ is $p$, and, therefore, the probability of not seing $A$ is $q = 1 - p$

The trials stop once $A$ occures, i.e. if $A$ occures at $k$-th trial, it didn't occur in previous $k -1$ trials

[Random Variable](Random_Variable) $X$ is the number of trials we should run until we see $A$ 
- the distribution of $X$ is called ''Geomentric''

Formally, Geometric Distribution describes the waiting time until a success for indepented and identically distributed Bernoulli Random Variables



Typical questions:
- How long should we flip a coin until we get head? 
- How many times we roll a dice until we get 1?


## [Cumulative Distribution Function](Cumulative_Distribution_Function)
Пусть в $k-1$-ом испытании событие не появилось, а в $k$-ом появилось. Тогда по [теореме умножения вероятностей независимых событий](Chain_and_Sum_Rules_in_Probability#Теорема_произведения_вероятностей) имеем следующую функцию распределения:

$P(X = k) = q^{k - 1} p$

Таким образом, для каждого $k = 0, 1, 2, ...$ получим геометрическую прогрессию, в которой p - первый член прогрессии, q - знаменатель:

$p, qp, q^2 p, ..., q^{k - 1} p, ...$

## Moments
- $E[X] = \cfrac{p}{1 - p}$
- $\text{Var}[X] = \cfrac{q}{p^2}$


## See Also
- [Hypergeometric Distribution](Hypergeometric_Distribution)
- [Negative Binomial Distribution](Negative_Binomial_Distribution) - general case of Geometric distribution

## Sources
- Гмурман В.Е., Теория вероятностей и математическая статистика -- 9-е издание. М.: Высш. шк., 2003.
- [OpenIntro Statistics (book)](OpenIntro_Statistics_(book))

[Category:Russian](Category_Russian)
[Category:Probability](Category_Probability)
[Category:Distributions](Category_Distributions)