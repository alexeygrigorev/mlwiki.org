---
title: "Correlation"
layout: default
permalink: /index.php/Correlation
---

# Correlation

## Независимые случайные величины
Если $X$ и $Y$ независисые, то распределение одной не влияет на значение второй. Иначе случайные величины называют зависимыми.


## Ковариация
Ковариация - мера линейной зависимости двух случайных величин. 

$\text{cov}(X, Y) = M[(X - M(X)) \cdot (Y - M(Y))] = M(XY) - M(X)M(Y)$


### Ограниченность ковариации
'''Теорема.'''
Абсолютная величина коэффициента ковариации двух случайных величин $X$ и $Y$ не превышает $\sigma(X) \sigma(Y)$

$| \text{cov}(X, Y)| \leqslant \sigma(X) \sigma(Y)$ |

'''Доказательство.''' Рассмотрим две случайные величины $Z_1 = \sigma(Y) X - \sigma(X) Y$ и $Z_2 = \sigma(Y) X + \sigma(X) Y$


<details>
<summary>Вывод $D(Z_1) = 2\sigma^2(X)\sigma^2(Y) - 2\sigma(X)\sigma(Y) \text{cov}(X, Y)$</summary>

- $D(Z_1) = M(Z_1)^2 - M^2(Z_1) = M[\sigma(Y) X - \sigma(X) Y]^2 - M^2[\sigma(Y) X - \sigma(X) Y] = $
- $M[\sigma^2(Y) X^2 - 2\sigma(X)\sigma(Y)XY + \sigma^2(X) Y^2] + [\sigma(Y) M(X) - \sigma(X) M(Y)]^2 = $
- $\sigma^2(Y) M(X^2) - 2\sigma(X)\sigma(Y) M(XY) + \sigma^2(X) M(Y^2)$ $ - \sigma^2(Y) M^2(X) - \sigma(X)\sigma(Y) M(X)M(Y) + \sigma^2(X) M^2(Y) = $ 
- $\sigma^2(Y)(M[X^2] - M^2[X]) - $ $ 2\sigma(X)\sigma(Y) (M[XY] - M[X]M[Y]) + \sigma^2(X)(M[Y^2] - M^2[Y]) =$ 
- $2\sigma^2(X)\sigma^2(Y) - 2\sigma(X)\sigma(Y) \text{cov}(X, Y)$
</details>


Аналогично, $D(Z_2) = 2\sigma^2(X)\sigma^2(Y) + 2\sigma(X)\sigma(Y) \text{cov}(X, Y)$


Т.к. любая дисперсия неотрицательна, получим,
- $D(Z_1) \geqslant 0$
- $2\sigma^2(X)\sigma^2(Y) - 2\sigma(X)\sigma(Y) \text{cov}(X, Y) \geqslant 0$
- $2\sigma^2(X)\sigma^2(Y) \geqslant 2\sigma(X)\sigma(Y) \text{cov}(X, Y)$
- $\text{cov}(X, Y) \leqslant \sigma(X)\sigma(Y)$

Аналогично, для $D(Z_2)$
- $2\sigma^2(X)\sigma^2(Y) + 2\sigma(X)\sigma($Y) \text{cov}(X, Y) \geqslant 0
- $\text{cov}(X, Y)  \geqslant -\sigma(X)\sigma(Y)$

Или, $| \text{cov}(X, Y)| \leqslant \sigma(X)\sigma(Y)$. |
'''Q.E.D'''


=== Свойства ковариации === 
- Ковариация симметрична
: $\text{cov}(X, Y) = \text{cov}(Y, X)$
- Ковариация ограничена (см. теорему)
: $| \text{cov}(X, Y)| \leqslant \sigma(X)\sigma(Y)$ |- Ковариация переменной самой с собой - ее дисперсия
: $\text{cov}(X, X) = M(X^2) - M^2(X) = D(X)$
- $\text{cov}(100 \cdot X, Y) = 100 \cdot \text{cov}(X, Y)$
- Если $X$ и $Y$ независимы, то $\text{cov}(X, Y) = 0$


### Интерпретация
- Если ковариация положительна, то с ростом одной С.В. значения второй С.В. имеют тенденцию возрастать, а если ковариация отрицательна - то убывать.


## Корреляция
По абсолютному значению ковариации нельзя судить о том, насколько сильно величины взаимосвязаны, т.к. её масштаб зависит от дисперсий. 

Однако масштаб можно отнормировать, поделив на $\sigma(X) \sigma(Y)$ и получив при этом ''линейный коэффициент корреляции'' (так же называемый коэффициентом корреляции Пирсона).

$r(X, Y) = r = \cfrac{\text{cov}(X, Y)}{\sigma(X) \sigma(Y)}$


Так как $| \text{cov}(X, Y)| \leqslant \sigma(X)\sigma(Y)$, то $-1 \leqslant r \leqslant 1$ |

## Sources
- Гмурман В.Е., Теория вероятностей и математическая статистика -- 9-е издание. М.: Высш. шк., 2003.
- http://ru.wikipedia.org/wiki/Ковариация
- http://ru.wikipedia.org/wiki/Корреляция

[Category:Russian](Category_Russian)
[Category:Probability](Category_Probability)
[Category:Подготовка к ШАД](Category_Подготовка_к_ШАД)