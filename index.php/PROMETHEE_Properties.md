---
title: "PROMETHEE/Properties"
layout: default
permalink: /index.php/PROMETHEE_Properties
---

# PROMETHEE/Properties

## [PROMETHEE](PROMETHEE)/Properties
### The PROMETHEE Property
Note that this pair-wise gives us [Valued Preference](Valued_Preference) Graph
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/de/mcda/promethee-valued-pref.png" alt="Image">
- this is local information, but we want to get the global final rankings


Suppose that $S$ is some method for computing global scores
- $s_i = S(a_i)$ and $s_j = S(a_j)$ 
- we use these scores to establish the global ranking

We expect that the following constraint is satisfied:
- $\pi_{ij} - \pi_{ji} = \pi(a_i, a_j) - \pi(a_j, a_i) \approx s_i - s_j$
- the difference between alternatives should be reflected in the global scores 
- and the difference in global scores should be as close as possible to the initial differences


; The PROMETHEE property:
- the netflow score $\Phi(a_i)$ is a centered score $s_i$ ($\forall i$) that minimizes the following $Q$:
- $Q = \sum_{i=1}^n \sum_{j=1}^n \big[ (s_i - s_j) - (\pi_{ij} - \pi_{ji}) \big]^2 $
- i.e. $Q$ is the sum of squared deviation and we want to minimize it


Proof ([La Grange Optimization](La_Grange_Optimization))
- let $L(s_1, ..., s_n, \lambda)$ be the function we want to minimize
  - $L(s_1, ..., s_n, \lambda) = \sum_{i=1}^n \sum_{j=1}^n \big[ (s_i - s_j) - (\pi_{ij} - \pi_{ji}) \big]^2 - \lambda \cdot \sum_{i=1}^n s_i$
  - note that due to symmetry when we fix all variables expect a certain $s_i$ we can rewrite the double sum as twice the single sum:
  - $L | _{s_i} = 2 \cdot \sum_{j=1,i \ne j}^n \big[ (s_i - s_j) - (\pi_{ij} - \pi_{ji}) \big]^2 - \lambda \cdot \sum_{i=1}^n s_i$ |- to optimize we take all partial derivatives plus the Lagrangian and equal them to 0:
  - $\forall s_i: \cfrac{\partial L(s_1, ..., s_n, \lambda)}{\partial s_i} = 0$
  - $\forall s_i: \cfrac{\partial L(s_1, ..., s_n, \lambda)}{\partial \lambda} = 0$
- optimization:
  - $\cfrac{\partial L}{\partial s_i} = 4 \cdot \sum_{j \ne i} \big[ (s_i - s_j) - (\pi_{ij} - \pi_{ji}) \big] - \lambda = ...$ (open the brackets for the sum)
  - $... = 4 \cdot \left[ \sum_{j \ne i} s_i - \sum_{j \ne i} s_j - \sum_{j \ne i} (\pi_{ij} - \pi_{ji}) \right] - \lambda = ...$ 
  - $... = 4 \cdot \left[ (n - 1) \cdot s_i - \sum_{j \ne i} s_j - \sum_{j \ne i} (\pi_{ij} - \pi_{ji}) \right] - \lambda = ...$  (by property $\sum_i s_i = 0$, $s_i = \sum_{j \ne i} s_j$ ) 
  - $... = 4 \cdot \left[ ns_i - \sum_{j \ne i} (\pi_{ij} - \pi_{ji}) \right] - \lambda = 0$
- therefore
  - $s_i = \cfrac{1}{n} \cdot \sum_{j \ne i} (\pi_{ij} - \pi_{ji}) = \cfrac{n-1}{n} \Phi(a_i)$
  - i.e. the scores $s_i$ that satisfy the desired property are directly proportional to the netflow scores
  - this is a justification why calculating netflow scores is a good idea


### Property 1
; $\Phi(a_i) \in [-1, 1]$
Easy to see that by the way we construct $\Phi(a_i)$


### Property 2
Want to show that  $\sum_{i = 1}^N \Phi(a_i) = 0$
- $N$ - the number of alternatives
- Let's show this property by induction


; Proof (by induction)


Basis: $N = 2$
- $\Phi(a_1) + \Phi(a_2) = \cfrac{1}{1} [\pi (a_1, a_2) - \pi (a_2, a_1) ] + \cfrac{1}{1} [\pi (a_2, a_1) - \pi (a_1, a_2) ] = 0$


Hypothesis: 
- Assume it holds for $N = k$


Induction step: Show that it also holds for $N = k + 1$
- $\sum_{i = 0}^{k+1} \Phi (a_i) = ...$  (expand $\Phi$)
- $... \sum_{i = 0}^{k + 1} \left[ \cfrac{1}{k} \sum_{j = 1}^{k + 1} [ \pi(a_i, a_j) - \pi(a_j, a_i) ] \right] = \ ... $ 
  - take one element of the outer sum outside
  - note that we don't care about the case when $i=j$ since the difference $\pi(a_i, a_i) - \pi(a_1, a_i)$ is always 0 
- $... \ = \cfrac{1}{k} \sum_{i = 1}^{\{\color{blue}\{k\}\}} \sum_{j = 1}^{k + 1} [ \pi(a_i, a_j) - \pi(a_j, a_i) ] + \cfrac{1}{k} \sum_{j=1}^{k+1} [ \pi(a_{k+1}, a_j) - \pi(a_j, a_{k+1}) ] = \ ...$ 
  - now take all $k+1$th elements outside of that sum as well
- $...\  = \cfrac{1}{k} \sum_{i = 1}^{k} \sum_{j = 1}^{\{\color{blue}\{k\}\}} [ \pi(a_i, a_j) - \pi(a_j, a_i) ] + \ ... $
  - $ ... \ + \cfrac{1}{k} \sum_{j=1}^{k+1} [ \pi(a_{k+1}, a_j) - \pi(a_j, a_{k+1}) ] + \cfrac{1}{k} \sum_{i=1}^{k+1} [ \pi(a_i, a_{k+1}) - \pi(a_{k+1}, a_i) ] = \ ...$
- $... \ = \cfrac{k-1}{k} \underbrace{ \left[ \cfrac{1}{k-1} \sum_{i = 1}^{k} \sum_{j = 1}^{k} [ \pi(a_i, a_j) - \pi(a_j, a_i) ] \right]  }_\text{= 0 by ind. hypothesis} + \ ... $
  - $... \ + \underbrace{\left[ \cfrac{1}{k} \sum_{j=1}^{k+1} [ \pi(a_{k+1}, a_j) - \pi(a_j, a_{k+1}) ] + \cfrac{1}{k} \sum_{i=1}^{k+1} [ \pi(a_i, a_{k+1}) - \pi(a_{k+1}, a_i) ] \right] }_\text{= 0} = \ ...$
- $... \ = 0$



## [Preferential Independence](Preferential_Independence)
PROMETHEE respects the [Preferential Independence](Preferential_Independence) hypothesis

Suppose we 
- divided the set of criteria $G$ into $J$ and $\overline{J}$ and 
- have alternatives $a,b,c,d \in A$ for which the following holds 
- $(*)
\left\{\begin{matrix}
  g_i(a) = g_i(b), \forall i \not \in J \\ 
  g_i(c) = g_i(d), \forall i \not \in J \\ 
  g_i(a) = g_i(a), \forall i \in J \\
  g_i(b) = g_i(d), \forall i \in J
\end{matrix}\right. $


Now we show that $J$ is preferentially independent, i.e. $a \ P \ c \iff b \ P \ d$
- compute the netflow score for $a$:
  - $\Phi(a) = \sum_{j = 1}^q w_i \cdot \Phi_j(a) = ...$ 
  - since we have two subsets of criteria, we can rewrite it as following:
  - $... = \underbrace{\sum_{j \in J} w_j \Phi_j(a)}_\text{(1)} + \sum_{j \not \in J} w_j \Phi_j(a) = ...$
  - for (1) because of (*) we can replace each $\Phi_j(a)$ with $\Phi_j(b)$
  - $... = \sum_{j \in J} w_j \Phi_j(b) + \sum_{j \not \in J} w_j \Phi_j(a)$
- can do the same for $c$:
  - $\Phi(c) = \sum_{j = 1}^q w_i \cdot \Phi_j(c) = \underbrace{\sum_{j \in J} w_j \Phi_j(c)}_\text{(2)} + \underbrace{\sum_{j \not \in J} w_j \Phi_j(c)}_\text{(3)} = ...$ 
  - because of (*) for (2) we can replace $\Phi_j(c)$ with $\Phi_j(d)$ and for (3) $\Phi_j(d)$ with $\Phi_j(a)$
  - $... = \sum_{j \in J} w_j \Phi_j(d) + \sum_{j \not \in J} w_j \Phi_j(a)$
- $a \ P \ c \Rightarrow \Phi(a) > \Phi(c)$
  - thus $\sum_{j \in J} w_j \Phi_j(b) + {\color{red}{\sum_{j \not \in J} w_j \Phi_j(a)}} >  \sum_{j \in J} w_j \Phi_j(d) + {\color{red}{\sum_{j \not \in J} w_j \Phi_j(a)}}$
  - we cross out the red parts and have the following:
  - $\sum_{j \in J} w_j \Phi_j(b) > \sum_{j \in J} w_j \Phi_j(d)$
  - now add $\sum_{j \not \in J} w_j \Phi(b)$ to both parts:
  - $\sum_{j \in J} w_j \Phi_j(b) + \{\color{blue}\{\sum_{j \not \in J} w_j \Phi(b)\}\} > \sum_{j \in J} w_j \Phi_j(d) + \{\color{blue}\{\sum_{j \not \in J} w_j \Phi(b)\}\}$
  - since $g_j(b) = g_j(d) \forall j \not \in J$, we have replace $b$ to $d$ on the right side
  - $\sum_{j \in J} w_j \Phi_j(b) + \sum_{j \not \in J} w_j \Phi(b) > \sum_{j \in J} w_j \Phi_j(d) + \sum_{j \not \in J} w_j \{\color{blue}\{\Phi(d)\}\}$
- thus $b \ P \ d$


## [Arrow's Impossibility Theorem](Arrow's_Impossibility_Theorem)
### [Monotonicity](Monotonicity)
The Monotonicity property is satisfied 

Let's show that
- $A = \{a, ..., a_i, ..., a_n\}$ - set of alternatives, $F = \{f_1, ..., f_q\}$ - set of criteria
- let $A'$ be a set $A' = \{a, ..., a'_i, ..., a_n\}$ where for $a'_i$:
  - $f_k(a'_i) > f_k(a_i)$ for some $f_k \in F$
  - $f_i (a'_i) = f_i (a_i)$ for all other criteria $f_j \in F, f_i \ne f_k$
  - i.e. $a'_i$, compared to $a_i$, improved its positions only in one criteria
- let $\Phi'(a)$ be a netflow score for $a \in A'$
  - here we have:
  - $\pi_j (a'_i, b) = \pi_j (a_i, b)$ and $\pi_j (b, a'_i) = \pi_j (b, a_i)$ for all $j \ne k$
  - since $f_k(a'_i) > f_k(a_i)$ we have $\pi_k (a'_i, b) \geqslant \pi_k(a_i, b)$ and $\pi_k (b, a'_i) \leqslant \pi_k(b, a_i)$
- calculate $\Phi'(a'_i)$: 
  - $\Phi'(a'_i) = \cfrac{1}{n - 1} \sum_{b \in A'} [ \pi(a'_i, b) - \pi(b, a'_i) ] = \ ...$
  - $... \ = \cfrac{1}{n - 1} \sum_{b \in A'} \left[ \sum_{j=1}^q w_j [ \pi_j(a'_i, b) - \pi_j(b, a'_i) ]  \right] = \ ...$ (now let's take the item with $\pi_k$ out of the sum)
  - $... \ = \cfrac{1}{n - 1} \sum_{b \in A'} \left[ \sum_{j=1, j \ne k}^q w_j [ \pi_j(a'_i, b) - \pi_j(b, a'_i) ] + w_k \{\color{blue}\{[  \pi_k(a'_i, b) - \pi_k(b, a'_i) ]\}\} \right] = \ ...$
  - consider $\pi_k(a'_i, b) - \pi_k(b, a'_i)$ alone:
    - $\pi_k (a'_i, b) \geqslant \pi_k(a_i, b)$ and $\pi_k (b, a'_i) \leqslant \pi_k(b, a_i)$
    - $\Rightarrow  \pi_k(a'_i, b) - \pi_k(b, a'_i) \geqslant \pi_k(a_i, b) - \pi_k(b, a_i)$
  - that means that $\Phi'(a'_i) \geqslant \Phi(a_i)$ 
- similarly, $\forall a \in A, a \ne a_i: \Phi'(a) \leqslant \Phi(a)$
  - $\Phi'(a) = \cfrac{1}{n - 1} \sum_{b \in A'} [ \pi(a'_i, b) - \pi(b, a'_i) ] = \ ...$
  - there's $a'_i$ somewhere in $b \in A'$ - let's take it away from the sum
  - $... = \cfrac{1}{n - 1} \sum_{b \in A', b \ne a'_i} [ \pi(a'_i, b) - \pi(b, a'_i) ] + \cfrac{1}{n-1} [ \{\color{blue}\{\pi(a, a_i) - \pi(a_i, a)\}\} ] $
  - the blue part is expanded to $\sum_{j = 1}^q w_j [ \pi_j(a, a'_i) - \pi_j(a'_i, a) ]$
  - we know that for one of these $j$ there's $k$, move it from the sum
  - consider $\pi_k(a, a'_i) - \pi_k(a'_i, a)$ alone:
    - $\pi_k(a, a'_i) \leqslant  \pi_k(a, a_i)$ and  $\pi_k(a'_i, a) \geqslant  \pi_k(a_i, a)$
    - thus $\pi_k(a, a'_i) - \pi_k(a'_i, a) \leqslant \pi_k(a, a_i) - \pi_k(a_i, a)$
  - that shows that $\Phi'(a) \leqslant \Phi(a)$

So we see that [Monotonicity](Monotonicity) is satisfied


## Sources
- [Decision Engineering (ULB)](Decision_Engineering_(ULB))
- An Introduction to Multicriteria Decision Aid: The PROMETHEE and GAIA Methods, Yves De Smet, Karim Lidouh, 2013

[Category:Multi-Criteria Decision Aid](Category_Multi-Criteria_Decision_Aid)