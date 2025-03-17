---
title: L'Hopital's Rule
layout: default
permalink: /index.php/L'Hopital's_Rule
---

# L'Hopital's Rule

## L'Hôpital's Rule
The rule has this form:
$$\lim_{x \to a} \cfrac{f(x)}{g(x)} = \lim_{x \to a} \cfrac{f'(x)}{g'(x)}$$


### $0/0$ case
- suppose $\lim\limits_{x \to a} \cfrac{f(x)}{g(x)} = \cfrac{0}{0}$
- i.e. $f(a) = 0$ and $g(a) = 0$
- if $f(x)$ and $g(x)$ are continuous 
- then the rule is $$\lim_{x \to a} \cfrac{f(x)}{g(x)} = \lim_{x \to a} \cfrac{f'(x)}{g'(x)}$$


Can show this using [Taylor Expansion](Taylor_Expansion) about $x = a$:
- $\lim\limits_{x \to a} \cfrac{f(x)}{g(x)} = \lim\limits_{x \to a} \cfrac{f(a) + f'(a)\, (x - a) + \ ...}{g(a) + g'(a)\, (x - a) + \ ...}$
  - know that $f(a) = g(a) = 0$, so have 
- $\lim\limits_{x \to a} \cfrac{f(x)}{g(x)} = \lim\limits_{x \to a} \cfrac{f'(a)\, (x - a) + \ ...}{g'(a)\, (x - a) + \ ...}$
- can factor $(x - a)$ out, so we have: 
- $\lim\limits_{x \to a} \cfrac{f(x)}{g(x)} = \lim\limits_{x \to a} \cfrac{f'(a) + \ ...}{g'(a) + \ ...}$
- the leading order terms are $f'(a)$ and $g'(a)$, and the rest vanish under the limit


Examples:
- $\lim\limits_{x \to 0} \cfrac{\sin x}{x} = \lim\limits_{x \to 0} \cfrac{\cos x}{1} = 1$
- $\lim\limits_{x \to 0} \cfrac{1 - \cos x}{x} = \lim\limits_{x \to 0} \cfrac{\sin x}{1} = 0$


### $\infty / \infty$ case
- suppose $\lim\limits_{x \to a} \cfrac{f(x)}{g(x)} = \cfrac{\infty}{\infty}$
- i.e. $f(a) = \infty$ and $g(a) = \infty$
- if $f(x)$ and $g(x)$ are continuous 
- then the rule is $$\lim_{x \to a} \cfrac{f(x)}{g(x)} = \lim_{x \to a} \cfrac{f'(x)}{g'(x)}$$


Example: 
- $\lim\limits_{x \to \infty} \cfrac{\ln x}{\sqrt{x}}$
- both go to $\infty$, but the rate at which they approach $\infty$ is different 
- by taking the derivative, we can see which one grows faster 
- is this case, $\sqrt{x}$ dominates $\ln x$: it grows much faster
- so the limit is 0

To say that one function grows faster than other, we can use the [Big-O notation](Order_of_Growth)


### Other Cases
See http://calculus.seas.upenn.edu/?n=Main.LHopitalsRule


## Sources
- [Calculus: Single Variable (coursera)](Calculus__Single_Variable_(coursera))

[Category:Calculus](Category_Calculus)
[Category:Limits](Category_Limits)