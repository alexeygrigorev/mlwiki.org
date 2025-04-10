---
title: "Poisson Limit Theorem"
layout: default
permalink: /index.php/Poisson_Limit_Theorem
---

# Poisson Limit Theorem

## Poisson Limit Theorem

Пусть производятся $n$ независимых испытаний, в каждом из которых вероятность появления события $A$ равна $p$. 

Для определения вероятности $k$ появлений события в этих испытаниях используют [формулу Бернулли](Формула_Бернулли). Если $p$ велико, то используют [ассимптотическую формулу Лапласса](Ассимптотическая_формула_Лапласса). Однако и она непригодна, если $p \leqslant 0.1$.

Если $n$ велико, то можно использовать формулу Пуассона.

Итак, найдем вероятность того, что при большом количестве испытаний событие наступит ровно $k$ раз.


- Т.к. произведение $np$ сохраняет постоянное значение, то пусть $np = \lambda$
- По формуле Бернулли $P_n(k) = C_n^k p^k (1-p)^{n-k} $
- Т.к. $np = \lambda$, то $p = \frac{\lambda}{n}$
- $P_n(k) = C_n^k \left(\frac{\lambda}{n}\right)^k \left(1 - \frac{\lambda}{n}\right)^{n - k}$
- Т.к. $n$ большое, то найдем $\lim_{k \rightarrow \infty} P_n(k)$ [опущено - см. Гмурман, с. 68]
- Получаем $P_n(k) = \frac{\lambda^k}{k|  } e^{-\lambda}$ | |
Эта формула выражает закон распределения Пуассона вероятности массовых ($n$ велико) и редких ($p$ мала) событий.



## Пример
Завод отправил 5000 изделий. Probability того, что изделие повредится - 0.0002. Найти вероятность того, что прибудут 3 негодных изделия

- $n = 5000, p = 0.0002, k = 3$
- $\lambda = np = 5000 \cdot 0.0002 = 1$
- По формуле Пуассона, искомая вероятность приблизительно равна 
: $P_{5000}(3) = \lambda^k \frac{e^{-\lambda}}{k|  } = \frac{e^{-1}}{3!} = \frac{1}{6e} \approx 0.06$ | |
## See also
- [Формула Бернулли](Формула_Бернулли)
- [Poisson Process](Poisson_Process)
- [Poisson Distribution](Poisson_Distribution)

## Sources
- Гмурман В.Е., Теория вероятностей и математическая статистика -- 9-е издание. М.: Высш. шк., 2003.

[Category:Russian](Category_Russian)
[Category:Probability](Category_Probability)