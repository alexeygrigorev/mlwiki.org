---
layout: default
permalink: /index.php/Geometric_Series
tags:
- calculus
title: Geometric Series
---

## Geometric Series

$1 + \cfrac{1}{2} + \left( \cfrac{1}{2} \right)^2 + \left( \cfrac{1}{2} \right)^3 + \ ... \ = \sum\limits_{k=0}^\infty \left( \cfrac{1}{2} \right)^k$
It [converges](Series_Convergence) to 2 

$1 + x + x^2 + x^3 + \ ... \ = \sum\limits_{k=0}^\infty x^k = \cfrac{1}{1 - x}$

- let $y = 1 + x  + x^2 + x^3 + \ ...$ / multiply by $-x$: 
- $-xy = -x\, (1 + x^2 + x^3 + \ ...) = -x  -x^2 - x^3 - \ ...$
- $y - xy = (1 + x^2 + x^3 + \ ... \ ) -x  -x^2 - x^3 - \ ... = 1$
- $y - xy = y\, (1 - x) = 1$
- so $y = \cfrac{1}{1 - x}$ 

But it holds only for $|x| < 1$

Suppose $x = 1$
- $1 + 1 + 1 + \ ... \ \to \infty$
- $y = \cfrac{1}{1 - x} = \cfrac{1}{0}$ not defined 

- $x = -1$ 
- $1 - 1 + 1 - 1 + 1 - \ ... \ = 0$? 
- let's try to group terms
- $(1 - 1) + (1 - 1) + (1 - 1) + \ ... \ = 0$
- $1 - (1 - 1) - (1 - 1) - (1 - 1) - \ ... \ = 1$
- maybe take the average? $\cfrac{0 + 1}{2} = 0.5$
- but none of these is correct: this series does not converge

## Sources
- [Calculus: Single Variable (coursera)](Calculus__Single_Variable_%28coursera%29)
