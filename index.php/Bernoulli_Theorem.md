---
layout: default
permalink: /index.php/Bernoulli_Theorem
tags:
- probability
- russian
- подготовка-к-шад
title: Bernoulli Theorem
---
## Bernoulli Theorem
'''Теорема.''' Если в каждом из n независимых испытаний вероятность $p$ появления события $A$ постоянна, то как угодно близка к единицы вероятность того, что отклонение относительной частоты от вероятности $p$ будет сколь угодно малым, если число испытаний достаточно велико.

$\lim_{n \rightarrow \infty} P\left(\left| \frac{m}{n} - p\right| < \epsilon\right) = 1$ |

### Доказательство
- $X_i$ - число появлений события в испытании $i$. Принимает два значения:
  - 1: событие наступило
  - 0: событие не наступило
: $P(X_i = 1) = p, P(X_i = 0) = q = 1 - p$
- Все величины попарно-независимы (т.к. испытания независимы)
- Их дисперисии ограничены
: $D(X_i) = pq$ (т.к. число испытаний $n = 1$) ('''TODO''': линк)
: и не превышает 1/4
: (произведение 2-х сомножителей максимально при их равенстве, т.е. $p = q = 0.5$)
: $D \leqslant \frac{1}{4}$, следовательно, дисперсии ограничены числом $C = \frac{1}{4}$
- Все условия для применения [теоремы Чебышева](Weak_Law_of_Large_Numbers) соблюдены, поэтому
: $\lim_{n \rightarrow \infty} P\left(\left|  \frac{X_1 + ... + X_n}{n} - p \right| < \epsilon\right) = 1$ (т.к. для всех $M(X_i)$ мат. ожидание есть $M(X_i) = p$) |- $\frac{1}{n} \sum X_i = \frac{m}{n}$ - относительная частота появления события $A$. т.е
: $\lim_{n \rightarrow \infty} P\left(\left|  \frac{m}{n} - p \right| < \epsilon\right) = 1$ |
'''Q.E.D.'''


## See also
- [Laws of Large Numbers](Laws_of_Large_Numbers)
- [Weak Law of Large Numbers](Weak_Law_of_Large_Numbers)

## Sources
- Гмурман В.Е., Теория вероятностей и математическая статистика -- 9-е издание. М.: Высш. шк., 2003.
