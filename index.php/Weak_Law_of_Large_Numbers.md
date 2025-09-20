---
layout: default
permalink: /index.php/Weak_Law_of_Large_Numbers
tags:
- probability
- russian
- подготовка-к-шад
title: Weak Law of Large Numbers
---
## Weak Law of Large Numbers

(Chebyshev's Theorem)

'''Теорема.''' Если $X_1, ..., X_n$ - попарно независимые случайные величины, причём их дисперсии равномерно ограничены (т.е. не превышают некоторого постоянного числа $C$), то, как бы мало не было число $\epsilon$, вероятность того, что

$\left|  \frac{X_1 + ... + X_n}{n} - \frac{M(X_1) + ... + M(X_n)}{n} \right| < \epsilon$ |
будет как угодно близко к единице, если число случайных событий достаточно велико.

Или, 

$\lim_{n \rightarrow \infty} P\left(\left|  \frac{X_1 + ... + X_n}{n} - \frac{M(X_1) + ... + M(X_n)}{n} \right| < \epsilon\right) = 1$ |

### Доказательство

- Рассмотрим случайную величину $\bar{X} = \frac{X_1 + ... + X_n}{n}$
- Найдем $M(\bar{X}) = M\left(\frac{X_1 + ... + X_n}{n}\right) = \frac{M(X_1) + ... + M(X_n)}{n}$
- Применяя к $\bar{X}$ [неравенство Чебышева](Chebyshev's_Inequality), получим
: $P\left(\left|  \frac{X_1 + ... + X_n}{n} - \frac{M(X_1) + ... + M(X_n)}{n} \right| < \epsilon\right) \geqslant 1 - \frac{D(\frac{X_1 + ... + X_n}{n})}{\epsilon^2}$ |- Т.к. $X_1 + ... + X_n$ независимые, то 
: $D\left(\frac{X_1 + ... + X_n}{n}\right) = \frac{D(X_1) + ... + D(X_n)}{n^2}$
- Все дисперсии $D(X_i)$ ограничены постоянным числом $C$: $D(X_i) \leqslant C$, поэтому 
: $\frac{D(X_1) + ... + D(X_n)}{n^2} \leqslant \frac{C + ... + C}{n^2} = \frac{nC}{n^2} = \frac{C}{n}$
: т.е. $D\left(\frac{X_1 + ... + X_n}{n}\right) \leqslant \frac{C}{n}$
- Подставляя в неравенство, имеем
: $P\left(\left|  \frac{X_1 + ... + X_n}{n} - \frac{M(X_1) + ... + M(X_n)}{n} \right| < \epsilon\right) \geqslant 1 - \frac{C}{n \epsilon^2}$ |- переходя к пределу при $n \rightarrow \infty$ получим
: $\lim_{n \rightarrow \infty} P\left(\left|  \frac{X_1 + ... + X_n}{n} - \frac{M(X_1) + ... + M(X_n)}{n} \right| < \epsilon\right) \geqslant 1$ |: т.к. вероятность не может быть больше единицы, получаем равенство 
: $\lim_{n \rightarrow \infty} P\left(\left|  \frac{X_1 + ... + X_n}{n} - \frac{M(X_1) + ... + M(X_n)}{n} \right| < \epsilon\right) = 1$ |
'''Q.E.D.'''



Если все случайные величины $X_i$ имеют одно и то же математическое ожидание $a$, то формула принимает вид 
$\lim_{n \rightarrow \infty} P\left(\left|  \frac{X_1 + ... + X_n}{n} - a \right| < \epsilon\right) = 1$ |

## Значение
Отдельные случайные величины могут иметь значительнй разброс, но их среднее арифметическое рассеяно мало, и можно предвидеть, какое значение оно (ср. ар.) примет. 

Или, среднее арифметическое достаточно большого количества независимых случайных величин утрачивает характер случайной величины. Объясняется это тем, что что отклонения каждой из случайных величин от своих мат. ожиданий могут быть как положительными, так и отрицательными, а в среднем арифметическом они взаимно погашаются. 


## See also
- [Chebyshev's Inequality](Chebyshev's_Inequality)
- [Laws of Large Numbers](Laws_of_Large_Numbers)

## Sources
- Гмурман В.Е., Теория вероятностей и математическая статистика -- 9-е издание. М.: Высш. шк., 2003.
