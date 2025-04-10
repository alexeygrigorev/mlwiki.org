---
title: "Binomial Theorem"
layout: default
permalink: /index.php/Binomial_Theorem
---

# Binomial Theorem

## Binomial Theorem
Рассмотрим степень $(a + x)^n$ 
- $(a + x)^2 = a^2 + 2xa + x^2 = aa + ax + xa + xx$
- $(a + x)^3 = aaa + aax + axa + axx + xaa + xax + xxa + xxx$

В эти формулы входят все [перестановки с повторениями](Permutations), составленные из символов $x$ и $a$
- $(a + x)^n$ - то же самое, содержит всевозможные перестановки из $a$ и $x$ длины $n$


Найдем, сколько будет членов, в которые входит $k$ символов $x$ и $n - k$ символов $a$
- $P(k, n - k) = C_n^k = \frac{n|  }{k! \cdot (n - k)!}$ (число перестановок с повторениями для двух групп равняется числу [сочетаний](Combinations) размера k из n) |- Т.е. член $x^k \cdot a^{n - k}$ возьмём с коэффициентом $C_n^k$ и получим  |- $(a + x)^n = C_n^0 a^n + C_n^1 a^{n-1} x + ... + C_n^k a^{n-k} x^k + ... + C_n^n x^n$

Эта формула носит название ''Binomial Theorem''


### Общий случай
Для $(x_1 + ... + x_m)^n$ коэффициент при $x_1^{k_1} \cdot x_2^{k_2} \cdot ... \cdot x_m^{k_m}$ будет $P(k_1, k_2, ..., k_m)$.


## Доказательство [свойств сочетаний](Combinations#Свойства_сочетаний)
Назовём функцию вида $(1 + x)^n$ ''производящей''

$(1 + x)^n = C_n^0 + C_n^1 x + ... + C_n^k x^k + ... + C_n^n x^n$.

С помощью этой формулы легко доказывать свойства сочетаний, в частности [свойство 3](Combinations#Свойство_3) и [свойство 6](Combinations#Свойство_6)

Свойство 3: $\sum_{k = 0}^n C_n^k = 2^n$
- Пусть x в производящей функции равно 1. Тогда
- $2^n = C_n^0 + C_n^1 + ... + C_n^k + ... + C_n^n$.


Свойство 6: $C_n^0 - C_n^1 + ... + (-1)^n C_n^k = 0$
- Пусть $x = -1$. Тогда
- $0 = C_n^0 - C_n^1 + ... + (-1)^n C_n^k$.


## See also
- [Combinations](Combinations)

## Sources
- Виленкин Н.Я. Комбинаторика. М., Наука, 1969.


[Category:Combinatorics](Category_Combinatorics)
[Category:Подготовка к ШАД](Category_Подготовка_к_ШАД)