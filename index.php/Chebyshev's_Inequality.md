---
title: Chebyshev's Inequality
layout: default
permalink: /index.php/Chebyshev's_Inequality
---

# Chebyshev's Inequality

## Chebyshev's Inequality
Probability того, что отклонение [случайной величины](Случайная_величина) X от её [математического ожидания](Математическое_ожидание) по абсолютной величине меньше положительного числа $\epsilon$, не меньше, чем $1 - \frac{D(X)}{\epsilon^2}$:

$P(| X - M(X)| < \epsilon) \geqslant 1 - \frac{D(X)}{\epsilon^2}$ |
## Доказательство

- Рассмотрим событие, обратное $| X - M(X)| < \epsilon$ - это будет событие, что отклонение принимает значение, большее $\epsilon$: $|X - M(X)| \geqslant \epsilon$ |: Эти два события противоположные: $P(| X - M(X)| < \epsilon) + P(|X - M(X)| \geqslant \epsilon) = 1$ |: вычислим $P(| X - M(X)| \geqslant \epsilon)$ |
- $D(X) = \sum_{i = 1}^n (x_i - M(X))^2 p_i$ (*)
: все слагаемые этой суммы больше нуля
- Отбросим все $(x_i - M(X))^2 p_i$, у которых $| x_i - M(X)| < \epsilon$ |: После этого сумма (*) только уменьшится
- Условно будем считать, что отброшено первые $k$ слагаемых 
: $D(X) \geqslant \sum_{j = k + 1}^n (x_j - M(X))^2 p_j$
- $| x_j - M(X)| \geqslant \epsilon, j = k + 1, ..., n$ (по предположению) |: обе части неравенства положительны, поэтому $| x_j - M(X)|^2 \geqslant \epsilon^2$ |- Воспользуемся этим и заменим каждый из множителей на $\epsilon^2$, и при этом неравенство только усилится. Получим
: $D(X) \geqslant \epsilon^2 \cdot (p_{k+1} + ... + p_n) = \epsilon^2 \sum_{j = k + 1}^n p_j$
- По [теореме сложения вероятностей](Chain_and_Sum_Rules_in_Probability#Теорема_сложения_вероятностей), сумма $\sum_{j = k + 1}^n p_j$ - вероятности того, что $X$ примет одно из значений ${x_j}, j = k+1, ..., n$
: При любом $x_j$ удовлетворяется $| x_j - M(X)| \geqslant \epsilon$ |: т.е. $\sum_{j = k + 1}^n p_j$ выражает вероятность $P(| X - M(X)| \geqslant \epsilon)$ |- Поэтому имеем
: $D(X) \geqslant \epsilon^2 \cdot P(| X - M(X)| \geqslant \epsilon)$ |: или $P(| X - M(X)| < \epsilon) \geqslant 1 - \frac{D(X)}{\epsilon^2}$ |


## Sources
- Гмурман В.Е., Теория вероятностей и математическая статистика -- 9-е издание. М.: Высш. шк., 2003.

[Category:Russian](Category_Russian)
[Category:Probability](Category_Probability)
[Category:Подготовка к ШАД](Category_Подготовка_к_ШАД)