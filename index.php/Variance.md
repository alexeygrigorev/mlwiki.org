---
title: Variance
layout: default
permalink: /index.php/Variance
---

# Variance

## Motivation
[Expected Value](Expected_Value) (Математическое ожидание) can't describe a possible range of values for a [Random Variable](Random_Variable)

Consider the following two RVs

<table>
<tr>
<td>
|   $X$ !! -0.1  |  0.1  |   $p$ !!  0.5  |  0.5 |</td> |<td>
|   $Y$ !! -100  |  100  |   $p$ !!  0.5  |  0.5 |</td> |</tr>
</table>

In both cases $M(X) = M(Y) = 0$
- but values for $X$ are close to the expected value, and values of $Y$ are far


### Deviation
''Deviation of a Random Variable'' (''Отклонение случайной величины'') - absolute difference between the value of an RV and its expected value

Отклонение иногда называют центрированной величиной и обозначают $\dot{X}$

Since $E\big[X - E[X] \big] = 0$, we need another way to describe the spread of some RV


## Variance
''Variance of a Random Variable'' (''Дисперсиия (разброс) случайной величины'') is a measure of spread that describes how far away values get from the expected value

$\text{Var}[X] = E \big[X - E[X] \big]^2 = \big[x_1 - E[X] \big]^2 \cdot p_1 + \big[x_2 - E[X] v]^2 \cdot p_2 + ... + \big[x_n - E[X] \big]^2 \cdot p_n$


### Формула для вычисления дисперсии
'''Теорема.''' Дисперсия равна разности между мат. ожиданием квадрата случайной величины и квадрата её мат. ожидания:

$\text{Var}[X] = E[X^2] - E^2[X]$ (meaning $E[X^2] - (E[X])^2$)

Доказательство: 
- $\text{Var} [X] = E\big[X - E[X]\big]^2 = ... $
- $... = E\big[X^2 - 2X \cdot E[X] + E^2 [X]\big] = ...$
- $... = E[X^2] - 2E[X] \cdot E[X] + E^2(X) = ...$
- $... = E[X^2] - 2E^2[X] + E^2[X] = E[X^2] - E^2[X]$


### Properties
1. $\text{Var}(C) = 0$
1. $\text{Var}(C \cdot X) = C^2 \cdot \text{Var}(X)$
1. $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) + 2[E(XY) - E(X)E(Y)]$
1. : If $X$ and $Y$ are independent, then $E(XY) = E(X)E(Y)$ and $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$
1. : $E(XY) - E(X)E(Y)$ is also called [covariation](Корреляция#Ковариация)
1. for independent $X$ and $Y$ $\text{Var}(X - Y) = \text{Var}(X) + \text{Var}(Y)$ ($\text{Var}(X - Y) = \text{Var}(X + (-1) Y) = \text{Var}(X) + (-1)^2 \text{Var}(Y)$)


## Standard Deviation
$\sigma(X) = \sqrt{ \text{Var} [X] }$


Дисперсия имеет размерность, равную квадрату размерности случайной величины, а среднеквадратичное отклонение совпадает с ней. 

- $\text{Var}(x) = \cfrac{1}{n - 1} \sum (x_i - \bar{x})^2$
- $s(x) = \text{std}(x) = \sqrt{\text{Var}(x)}$

($n - 1$ gives "unbiased" estimate of the variance {{{ TODO |  add link }}}) |
in R: 
```text only
st.dev = sd(data)
```


## Sources
- Гмурман В.Е., Теория вероятностей и математическая статистика -- 9-е издание. М.: Высш. шк., 2003.

[Category:Russian](Category_Russian)
[Category:Probability](Category_Probability)