---
title: Skolem Function
layout: default
permalink: /index.php/Skolem_Function
---

# Skolem Function

## Skolem Function
### Intuition
Suppose, we have the following [Conjunctive Query](Conjunctive_Query):
- $Q(u,v) \leftarrow T(w,u), U(v,w), R(v,u)$
- For this query, [FOL](First_Order_Logic) meaning is 
- $\forall \ u, v \Big[ Q(u, v) \Rightarrow \exists \ w \ : \ T(w, u) \land U(v, w) \land R(v, u)  \Big]$

Now consider that we have a tuple $(a, b)$ 
- $(a, b)$ belongs to the data source that backs $V_1$
  - so we have a fact $Q(a, b)$
- from this fact $Q(a, b)$ can infer that $R(b, a)$ 
  - $Q(a, b) \Rightarrow R(b, a)$
  - (all conjuncts have to be true for a statement to be true, so it means the last conjuncts holds true)


But we can infer other things as well
- e.g. $Q(a, b) \Rightarrow \exists \ d_1 \ : \ T(d_1, a) \land U(b, d_1)$ 
- where $d_1$ is some constant
  - we don't know its value, but we know it exists (since it's existentially qualified) and 
  - it depends on constants $a$ and $b$
- so we can denote this dependency as $d_1 = f_1(a, b)$


''Skolem Function''
- the symbol $f_1(u, v)$ is a Skolem Function of arity 2
  - $f_1(u, v)$ denotes that there exists some constant that depends on values of $u$ and $v$
- given two distinct Skolem terms, e.g. $f_1(1, 2)$ and $f_1(2, v_3)$ we never can say if they belong to the same constant or not


## Sources
- Web Data Management book [http://webdam.inria.fr/Jorge]

[Category:Logic](Category_Logic)