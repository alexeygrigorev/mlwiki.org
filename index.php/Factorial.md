---
layout: default
permalink: /index.php/Factorial
tags:
- calculus
- combinatorics
title: Factorial
---

## Factorial

for integers, [Factorial](Factorial) $x! = x\, (x - 1)!$ 
what if $x$ is not an integer? 

can use the [Gamma Function](Gamma_Function):

$x! = \Gamma(x) = \int\limits_{t=0}^\infty t^x\, e^{-t}\, dt$

Stirling Formula 

Very useful in [Probability](Probability)

$\ln (x!) = x\, \ln x - x + O(\ln x)$ 
$x! = \sqrt{2\pi x}\, \left( \cfrac{x}{e} \right)^x\, \left( 1 + O(\cfrac{1}{x}) \right)$
