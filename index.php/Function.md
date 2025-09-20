---
layout: default
permalink: /index.php/Function
tags:
- calculus
- linear-algebra
- mathematics
title: Function
---
## Function
In mathematics, a function $f(\cdot)$ is a set of pairs $x, f(x)$, where
- $x$ is input, $f(x)$ is output 
- all possible inputs $x$ that a function can take is the ''domain'' of $f$
- all possible outputs $f(x)$ of a function $f(\cdot)$ is the ''range'' of $f$

<img src="<img src="http://alexeygrigorev.com/wiki-figures/crs/calc/function.svg" alt="Image">"/>

## Operations on Functions
### Composition
For two functions $f$ and $g$, composition is $f \circ g$
- $(f \circ g) (x) = f(g(x))$
- $g$ is applied first, then $f$ 

<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/crs/calc/composite.png" alt="Image">


For example, 
- $\sqrt{1 - x^2}$
- $g = x^2$, it's inside
- $f(t) = \sqrt{1 - t}$, it's outsize


### Inverse
For $f$ its inverse is $f^{-1}$
- $x = f^{-1}(x)$  if $f(f^{-1}(x)) = x$
- $f^{-1}(\cdot)$ is a function that "undoes" $f(\cdot)$



## Single Variable Functions
That's the simplest type of functions: they have one input and one output

### Important Function Classes
- [Polynomial Functions](Polynomial_Functions): $P(x) = C_0 + C_1 x + \ ... \ + C_n x^n = \sum_{k=0}^n C_k x^k$, $n$ is degree of $P(\cdot)$
- Rational Functions: $\cfrac{P(x)}{Q(x)}$, s.t. $Q(x) \ne 0$. e.g. $\cfrac{3x - 1}{x^2 - x - 6}$
- [Trigonometric Functions](Trigonometric_Functions): $\sin x$, $\cos x$, $\tan x$, etc
- [Exponential Function](Exponential_Function) and [Logarithm](Logarithm)

### [Continuous Functions](Continuous_Functions)
- Functions are [continuous](Continuous_Functions) is their [Limits](Limits) always exist
- otherwise functions are discontinuous 
- these are important functions in Calculus


## Multi Variable Functions
These functions are more complex:
- they can have multiple inputs and multiple outputs
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/crs/calc/function-multi.png" alt="Image">

## [Function Spaces](Function_Spaces)
Functions, like [Vectors](Vectors), can form [Vector Spaces](Vector_Spaces)
- they are called [Function Spaces](Function_Spaces) for functions


## Sources
- [Calculus: Single Variable (coursera)](Calculus__Single_Variable_(coursera))
