---
layout: default
permalink: /index.php/Conjunctive_Query_Homomorphism
tags:
- relational-databases
title: Conjunctive Query/Homomorphism
---
## Conjunctive Query Homomorphism
'''def''': a ''homomorphism'' of a [Conjunctive Query](Conjunctive_Query) $Q_2$ to a Conjunctive Query $Q_1$ is 
- a function $h$ that maps each variable in $Q_2$ to either
  - a variable from $Q_1$ or
  - a constant form $Q_1$
- s.t. 
  - $h(\text{head}_2) = \text{head}_1$
  - $h(\text{body}_2) \subseteq \text{body}_1$
  - i.e. the values returned by queries are always the same, and body of one query is a subset of the other's query body


## Examples
### Example 1
Given
- relation $R(A, B)$ 
- 3 queries
  - $Q_0(x) \leftarrow R(x, 33)$ ($Q_0 \equiv \pi_A \sigma_{B = 33}(R)$)
  - $Q_1(x) \leftarrow R(x, x)$ ($Q_1 \equiv \pi_A \sigma_{A = B}(R)$)
  - $Q_2(x) \leftarrow R(x, y)$ ($Q_0 \equiv \pi_A (R)$)

We can see that 
- $Q_0 \subseteq Q_2$ (obvious from the RA expressions: $Q_0$ just restricts $Q_2$)
- and $Q_1 \subseteq Q_2$ (same reasoning)


Homomorphisms 
- $x \mapsto x, y \mapsto 33$ is a homomorphism of $Q_2$ to $Q_0$
- $x \mapsto x, y \mapsto x$ is a homomorphism of $Q_2$ to $Q_0$
- there is no homomorphism from $Q_0$ to $Q_2$  or from $Q_0$ to $Q_1$:
  - there's a constant in $Q_0$ that occurs neither in $Q_1$ nor in $Q_2$
  - (i.e. for any $h$ there's no atom of the form $R(h(x), 33)$ in the body of $Q_1$ or $Q_2$)
- there is no homomorphism from $Q_1$ to $Q_2$
  - for any $h(x), h(y)$, there is no atom of the form $R(h(x), h(y))$ in the body of $Q_2$


### Example 2
Example from before:
- $A(x, y) \leftarrow R(x, w), G(w, z), R(z, y)$
- $B(x, w) \leftarrow R(x, w), G(w, w), R(w, y)$

There is a homomorphism $h$ from $A$ to $B$
- $h: x \mapsto x, y \mapsto y, w \mapsto w, z \mapsto w$

But there is no homomorphism $h$ from $B$ to $A$
- such $h$ would have to map $G(w, w)$ to $G(w, z)$
- which would imply $w \mapsto w$ and w $\mapsto z$ at the same time
- but it's not possible since $h$ must be a function


### Example 3
Given two queries
- $C_1(x) \leftarrow R(x, y), R(y, z), R(z, w)$
- $C_2(x) \leftarrow R(x, y), R(y, x)$

There's a homomorphism from $C_1$ to $C_2$:
- $h: x \mapsto x, y \mapsto y, z \mapsto x, w \mapsto y$
- i.e.
  - for head $x \mapsto x$
  - for the 1st atom of $C_1$: $y \mapsto y$ (maps to 1st atom of $C_2$)
  - for the 2nd atom of $C_1$: $z \mapsto x$ (maps to 2nd atom of $C_2$)
  - for the 3rd atom of $C_1$: $w \mapsto y$ (maps again to 1st atom of $C_2$)

But there's no homomorphism from $C_2$ to $C_1$
- suppose it existed
- it would assign $x \mapsto x$ to map head of $C_2$ to head of $C_1$
- in this case $R(h(x), h(y)) = R(x, h(y))$ must occur in the body of $C_1$
  - $\to$ the 1st atom of $C_2$ would be mapped to 1st atom of $C_1$
  - $\to$ $h$ must map $y \mapsto y$
- analogously, 2nd atom of $C_2$ must be mapped to 2nd atom of $C_1$
  - $h$ must map $x \mapsto z$
  - but it cannot because we have already established $x \mapsto x$
- since $h$ must be a function, there is no homomorphism from $C_2$ to $C_1$


## See Also
- [Conjunctive Query](Conjunctive_Query)

## Sources
- [Database Systems Architecture (ULB)](Database_Systems_Architecture_(ULB))
- Database Systems Architecture lecture notes #2 by S. Vansummeren [https://dl.dropboxusercontent.com/sh/r0zvy3zaycbevx8/U0XnqCSwGZ/lect2-notes-conjunctive.pdf]
