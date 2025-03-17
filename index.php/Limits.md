---
title: "Limits"
layout: default
permalink: /index.php/Limits
---

# Limits

## Limits
$\lim\limits_{x \to a} f(x) = L$ 


### Definition
the limit of $f(x)$ as $x \to a$ is $L$:
- if $\forall \varepsilon > 0 \ \ \exists\, \delta > 0$ s.t. $x \ne a$ is within $\delta$ of $a$
- then $f(x)$ is within $\varepsilon$ of $L$ 

### Interpretation
Interpretation: 
- if as $x$ gets closer to $a$, $f(x)$ gets closer to $L$
- then $L$ is the limit of $f(x)$ 

or
- choose some ''output tolerance'' $\varepsilon$ 
- then there exists some ''input tolerance'' $\delta$ such that $L$ lies within $\varepsilon$ of $f(x)$
- if you change $\varepsilon$, you need to be able to update $\delta$ - this has to be true for any $\varepsilon$

<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/crs/calc/limit-def.png" alt="Image">


### $x \to \infty$
- $a = \infty$ then 
- $\lim\limits_{x \to \infty} f(x) = L$ 

What does it mean? Can think if it as of the "end" of the real line

Definition:
- the definition needs to be slightly adapted 
- if $\forall \varepsilon > 0 \ \ \exists\, M > 0$ s.t. $| f(x) - L| < \varepsilon$ when $x > M$ |- if there's no such $M$, then the limit does not exist


Interpretation:
- instead of input tolerance $\infty \pm \delta, we mean some very large $M$:
- we always can find some large $M$ after which $f(x)$ is always within $\varepsilon$ of $L$ 

<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/crs/calc/limit-def-infty.png" alt="Image">

as $\varepsilon$ becomes tighter, we still should be able to find larger $M$ for which the function lies within $\varepsilon$


## Non-Existent Limits
Some functions are not well-behaved, so things can go wrong

### Discontinuity
The limit does not exist because the limit from the left and the limit from the right are not equal.

<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/crs/calc/limit-discontinuity.png" alt="Image">


### Blow-Up
The function has a vertical asymptote:
- functions gets to $\infty$ as $x \to a$ 

<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/crs/calc/limit-blowup.png" alt="Image">


### Oscillation
The function oscillates up and down as the input approaches some value

<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/crs/calc/limit-oscillation.png" alt="Image">


## Rules
Rules for limits

Suppose $\lim\limits_{x \to a} f(x)$ and $\lim\limits_{x \to a} g(x)$ exist. Then
- '''Sum Rule''': $\lim \big(f(x) + g(x) \big) = \lim f(x) + \lim g(x)$
- '''Product Rule''': $\lim \big(f(x) \cdot g(x) \big) = \left[\lim f(x)\right] \cdot \left[ \lim g(x) \right]$
- '''Quotient Rule''': $\lim \cfrac{f(x)}{g(x)} = \cfrac{\lim f(x)}{\lim g(x)}$ (when $\lim g(x) \ne 0$)
- '''Chain Rule''' (or '''Composition Rule'''): $\lim f \big(g(x) \big) = f \big(\lim g(x) \big)$ if $f$ is continuous 


## [L'Hopital's Rule](L'Hopital's_Rule)
$$\lim_{x \to a} \cfrac{f(x)}{g(x)} = \lim_{x \to a} \cfrac{f'(x)}{g'(x)}$$

Gives a way to solve ambiguous limits:
- $\lim \cfrac{0}{0}$
- $\lim \cfrac{\infty}{\infty}$
- $\lim \infty \cdot 0$
- $\lim (\infty - \infty)$
- $\lim \infty^0$



## Some Important Limits
### $\lim\limits_{x \to 0} \cfrac{\sin x}{x}$
What is $\lim\limits_{x \to 0} \cfrac{\sin x}{x}$?
- cannot apply the Quotient Rule because $x \to 0$ 
- let's [Taylor Expand](Taylor_Series) $\sin x$ 
- $\lim\limits_{x \to 0} \cfrac{\sin x}{x} = \lim\limits_{x \to 0} \cfrac{x - \frac{1}{3|  }\, x^3 + \frac{1}{5!}\, x^5 - \ ...}{x} = \ ...$ |  - $... \ = \lim\limits_{x \to 0} \cfrac{x\, \left(1 - \frac{1}{3| }\, x^2 + \frac{1}{5!}\, x^4 - \ ... \ \right)}{x} = \ ...$ |  - $... \ = \lim\limits_{x \to 0} \left(1 - \frac{1}{3| }\, x^2 + \frac{1}{5!}\, x^4 + \ ... \ \right) = 1$ | |
Can also show this using the [L'Hopital's Rule](L'Hopital's_Rule)
- $\lim\limits_{x \to 0} \cfrac{\sin x}{x} = \lim\limits_{x \to 0} \cfrac{\cos x}{1} = 1$

## Sources
- [Calculus: Single Variable (coursera)](Calculus__Single_Variable_(coursera))

[Category:Calculus](Category_Calculus)
[Category:Functions](Category_Functions)
[Category:Limits](Category_Limits)