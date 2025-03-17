---
title: Hypergeometric Distribution
layout: default
permalink: /index.php/Hypergeometric_Distribution
---

# Hypergeometric Distribution

## Hypergeometric Distribution

Пусть в партии из $N$ изделий $M$ стандартных ($M < N$). Из партии отбирают n изделий, причём изделия обратно не возвращаются. 

$X$ - случайная величина, число m стандартных изделий среди n отобранных. Возможные значения $X: 0, 1, ..., \min(M, n)$


Probability того, что $X = m$:
- Общее число исходов $C_N^n$
- Число благоприятствующих исходов $X = m$:

$C_M^m \cdot C_{N - M}^{m - n}$

(число способов извлечь $m$ из $M$ умножить на число способов извлечь оставшиеся нестандартные детели)


Таким образом, 

$P(X = m) = \frac{C_M^m \cdot C_{N - M}^{m - n}}{C_N^n}$

Эта формула определяет ''гипергеометрическое распределение''.


### Пример
Среди 50 изделий 20 окрашеных. Найти вероятность того, что из 5 извлёченных изделий 3 будут окрашенными. 

- $N = 50, M = 20, n = 5, m = 3$
- $P(X = 3) = \frac{C_{20}^3 \cdot C_{30}^2}{C_{50}^5} = 0.234$

## See also
- [Геометрическое распределение](Геометрическое_распределение)

## Sources
- Гмурман В.Е., Теория вероятностей и математическая статистика -- 9-е издание. М.: Высш. шк., 2003.

[Category:Russian](Category_Russian)
[Category:Probability](Category_Probability)
[Category:Probability Distributions](Category_Probability_Distributions)
[Category:Подготовка к ШАД](Category_Подготовка_к_ШАД)