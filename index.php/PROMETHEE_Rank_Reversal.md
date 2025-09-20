---
layout: default
permalink: /index.php/PROMETHEE_Rank_Reversal
tags:
- multi-criteria-decision-aid
title: PROMETHEE/Rank Reversal
---
## [Rank Reversal](Rank_Reversal) in [PROMETHEE](PROMETHEE)
Can be caused by 
- removing [Non-Discriminating Criteria](Non-Discriminating_Criteria)
- [Dominated](Dominance) criteria 


### Removing [Non-Discriminating Criteria](Non-Discriminating_Criteria)
A criterion $f_k$ is non-discriminating it for all alternatives it evaluates to some value $\alpha$

Notation:
- $f_k$ is a non-discriminating criteria that evaluates to 0: $\forall a_i \in A: f_k(a_i) = 0$
- $\Phi(a_i)$ - original netflow score, $\Phi'(a_i)$ netflow score of an evaluation table without $f_k$
- $\Phi_j(a_i)$ - the netflow score of evaluation of criteria $j$
- we want to show that $\Phi(a_i) > \Phi(a_j) \iff \Phi'(a_i) > \Phi'(a_j)$


In PROMETHEE removal of such criteria doesn't lead to Rank Reversal:
- let $W_k = \sum_{j \ne k} w_j$ and $w'_j = \cfrac{w_j}{W_k}$ - we normalized the weights so when we remove the $w_k$, the rest still sum up to 1
- $\Phi(a_i) = \sum_{j=1}^q w_j \cdot \Phi_j(a_i) = \sum_{j \ne k} w_j \cdot \Phi_j(a_i) = ...$ (we removed the term that is always 0)
- $... = W_k  \sum_{j \ne k} \cfrac{w_j}{W_k} \Phi_j(a_i) = W_k  \sum_{j \ne k} w'_j \Phi_j(a_i) = ... $ (we multiplied and divided by a non-negative normalization factor)
- $... = W_k \cdot \Phi'_(a_i)$
- so we know that when removing $f_k$, all netflow scores will change on the same non-negative value
- therefore, $\Phi(a_i) > \Phi(a_j) \iff \Phi'(a_i) > \Phi'(a_j)$

$\square$


### [Dominated](Dominance) Criteria
Suppose an alternative $a_i \in A$ dominates $a_j \in A$:
- $\forall k: f_k(a_i) \geqslant f_k(a_j) \land \exists k': f_{k'}(a_i) > f_{k'}(a_j)$
- so $a_i$ has better or the same score as $a_j$:
- $\Phi(a_i) = \cfrac{1}{n-1} \sum_{k=1}^q w_k \sum_{b \in A} [ \pi_k (a_i, b) - \pi_k (b, a_i) ] \geqslant \Phi(a_j) = \cfrac{1}{n-1} \sum_{k=1}^q w_k \sum_{b \in A} [ \pi_k (a_j, b) - \pi_k (b, a_j) ]$
- compare to some other alternative $b$
  - preference $a_i$ over $b$ is bigger than preference $a_j$ over $b$
  - preference $b$ over $a_1$ is less than preference $b$ over $a_j$
- it means that 
  - $\Phi(a_i) \geqslant \Phi(a_j)$ with whatever $b$  
  - <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/de/mcda/promethee-rankreversal-dominance.png" alt="Image">

So a dominated alternative $b$ can never have a score higher score than the alternative $a$ that dominates $b$


### General Rank Reversal Analysis
- let $A_y = A - {y}$ - all alternatives except $y$
- and $\Phi_y(a)$ - a net flow score over $A_y$, i.e. calculated after $y$ is removed


RR is not possible if 
- $[\Phi(a) - \Phi(b)] \cdot [\Phi_y(a) - \Phi_y(b)] > 0$ i.e. both parts are either positive or negative
- i.e. if something is better (worse), it should remain better (worse) when we remove $y$


RR is possible when $\Phi(a) - \Phi(b) > \cfrac{2}{n - 1}$
- $\Phi_y(a) = \cfrac{1}{n-2} \sum_{x \in A_y} [ \pi(a, x) - \pi(x, a) ]$
- $\Phi(a) = \cfrac{1}{n-1} \sum_{x \in A} [ \pi(a, x) - \pi(x, a) ] = ...$
  - move the item with $y$ out of the sum
  - $... \cfrac{n - 2}{\{\color{red}\{n - 2\}\}} \cfrac{\{\color{red}\{1\}\}}{n - 1} \sum_{x \in A, x \ne y} [ \pi(a, x) - \pi(x, a) ] + \cfrac{1}{n - 1} [ \pi(a, y) - \pi(y, a) ] = ...$
  - $... = \cfrac{n - 2}{n - 1} \Phi_y(a) +  \cfrac{1}{n - 1} [ \pi(a, y) - \pi(y, a) ]$
- Thus we can express $\Phi_y(a)$ via $\Phi(a)$:
  - $\Phi_y(a) = \cfrac{n - 2}{n - 1} - \cfrac{1}{n - 2} \cdot [ \pi(a, y) - \pi(y, a) ]$
- Assume $\Phi_y(a) - \Phi_y(b) > 0$, i.e. $a$ is ranked higher than $b$ after removing $y$
  - $\Phi_y(a) - \Phi_y(b) = \cfrac{n - 2}{n - 1} [\Phi(a) - \Phi(b)] - \cfrac{1}{n - 2} [ \pi(a, y) - \pi(y, a) - (\pi(b, y) - \pi(y, b) ) ]$
- for RR not happen it should hold that $\Phi - \Phi_y > 0$
  - i.e. $a$ was also ranked higher than $b$ before removing $y$
  - thus, $\Phi_y(a) - \Phi_y(b) = \cfrac{n - 2}{n - 1} [\Phi(a) - \Phi(b)] - \cfrac{1}{n - 2} [ \pi(a, y) - \pi(y, a) - (\pi(b, y) - \pi(y, b) ) ] > 0$
  - or $\cfrac{n - 1}{n - 2} [ \Phi(a) - \Phi(b) ] > \cfrac{1}{n - 2} [ \pi(a, y) - \pi(y, a) - (\pi(b, y) - \pi(y, b) ) ]$ 
  - $\Rightarrow \Phi(a) - \Phi(b) > \cfrac{ \pi(a, y) - \pi(y, a) - (\pi(b, y) - \pi(y, b) ) }{n - 1}$
- suppose we take the most pessimistic position
  - we remove such $y$ that maximizes this sum:
  - $\Phi(a) - \Phi(b) > \cfrac{ \max_y [ \pi(a, y) - \pi(y, a) - (\pi(b, y) - \pi(y, b) ) ] }{n - 1}$
  - the most pessimistic values are $\pi(a, y) = 1, \pi(y, a) = 0,  \pi(b, y) = 0, \pi(y, b) = 1$
  - i.e. $\Phi(a) - \Phi(b) > \cfrac{2}{n - 1}$


Thus, [Rank Reversal](Rank_Reversal) can happen only when $\Phi(a) - \Phi(b) > \cfrac{2}{n - 1}$


In other words
- this happens only when two alternatives have very close net flow scores
- i.e. they are almost the same: the difference $\frac{2}{n - 1}$ is quite small, especially for larger $n$


## Links
- Paper: Verly, De Smet, Some considerations about rank reversal occurrences in the PROMETHEE method. 

## Sources
- [Decision Engineering (ULB)](Decision_Engineering_(ULB))
- An Introduction to Multicriteria Decision Aid: The PROMETHEE and GAIA Methods, Yves De Smet, Karim Lidouh, 2013
