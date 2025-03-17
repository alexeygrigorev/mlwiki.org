---
title: Conjunctive Query/Containment Exercise
layout: default
permalink: /index.php/Conjunctive_Query_Containment_Exercise
---

# Conjunctive Query/Containment Exercise

## Exercises
These are exercises for containment of [Conjunctive Queries](Conjunctive_Query)


### Exercise 1
Given the queries 
- $Q_1(x, y) \leftarrow Q(x, a), Q(a, b), Q(b, y)$
- $Q_2(x, y) \leftarrow Q(x, a), Q(a, b), Q(b, c), Q(c, y)$
- $Q_3(x, y) \leftarrow Q(x, a), Q(a, 1), Q(1, b), Q(b, y)$
- $Q_4(x, y) \leftarrow Q(x, y), Q(y, x)$

Find all pairs $(Q_i, Q_j)$ s.t. $Q_i \subseteq Q_j$. Are there any equivalent queries? 


$Q_1 \subseteq Q_2$?

Informal reasoning:
- For $Q_1$ path $x \to a \to b \to y$ is of length 3;
- For $Q_2$ path $x \to a \to b \to c \to y$ is of length 4.
- $\Rightarrow$ containment doesn't hold. Let's show that formally.


Formal reasoning:
- $
D_{Q_1} = 
\begin{array}{ |  l l | } |  \hline
  C_x & C_a \\
  C_a & C_b \\
  C_b & C_c \\
  C_c & C_y \\
  \hline
\end{array}$
  - note that instead of creating a database with the body of $Q_1$, we created constant that correspond to the variables (to avoid confusion)
- Evaluate $Q_2(D_{Q_1})$:
- $Q_2(x, y) \leftarrow \underbrace{Q(x, a)}_{(1)}, \underbrace{Q(a, b)}_{(2)}, \underbrace{Q(b, c)}_{(3)}, \underbrace{Q(c, y)}_{(4)}$
- Let's build a candidate substitution. We want this substitution to be a matching.
  - First we map the head of $Q_2$ to associated constants: $x \mapsto C_x, y \mapsto C_y$ (because we want $(C_x, C_y)$ be in $Q_2(D_{Q_1})$)
  - Then we evaluate (1) atom $Q(x, a)$ and map $a \mapsto C_a$ 
  - For (2) we map $b \mapsto C_b$, for (3) $c \mapsto C_y$, but for (4) we cannot find a tuple $(C_y, ?)$ in $D_{Q_2}$ with $C_y$ in the first position. 
  - Therefore this substitution is not a matching.
- We have constructed a counter-example $\Rightarrow$ $Q_1 \not \subseteq Q_2$


$Q_2 \subseteq Q_1$?
- $
D_{Q_2} = 
\begin{array}{ |  l l | } |  \hline
  C_x & C_a \\
  C_a & C_b \\
  C_b & C_y \\
  \hline
\end{array}$
- Evaluate $Q_1(D_{Q_2})$
- $Q_1(x, y) \leftarrow \underbrace{Q(x, a)}_{(1)}, \underbrace{Q(a, b)}_{(2)}, \underbrace{Q(b, y)}_{(3)}$
- For head we map $x \mapsto C_x$, $y \mapsto C_y$, for (1): $a \mapsto C_a$, for (2) $b \mapsto C_b$, for (3) we would have to map $y \mapsto C_c$, but we cannot do it since we already have mapped $y \mapsto C_y$.
- Therefore, this candidate substitution is not a function and $Q_2 \not \subseteq Q_1$


$Q_1 \subseteq Q_3$?
- $
D_{Q_1} = 
\begin{array}{ |  l l | } |  \hline
  C_x & C_a \\
  C_a & C_b \\
  C_b & C_c \\
  C_c & C_y \\
  \hline
\end{array}
$
- We evaluate $Q_3(D_{Q_1})$
- $Q_3(x, y) \leftarrow \underbrace{Q(x, a)}_{(1)}, \underbrace{Q(a, 1)}_{(2)}, \underbrace{Q(1, b)}_{(3)}, \underbrace{Q(b, y)}_{(4)}$
- For head we have $x \mapsto C_x$, $y \mapsto C_y$, for (1) $a \mapsto C_a$, but for (2) there's no tuple $(C_a, 1)$ in $D_{Q_1}$ so we cannot find a matching.
- Therefore $Q_1 \not \subseteq Q_3$


$Q_3 \subseteq Q_1$?
- $
D_{Q_3} =
\begin{array}{ |  l l | } |  \hline
  C_x & C_a \\
  C_a & 1 \\
  1 & C_b \\
  C_b & C_y \\
  \hline
\end{array}
$
- We evaluate $Q_1(D_{Q_3})$
- $Q_1(x, y) \leftarrow \underbrace{Q(x, a)}_{(1)}, \underbrace{Q(a, b)}_{(2)}, \underbrace{Q(b, y)}_{(3)}$
- For head we have $x \mapsto C_x$, $y \mapsto C_y$, for (1) $a \mapsto C_a$, for (2) $b \mapsto C_1$, but for (3) we would have to map $y \mapsto C_b$, and we already established $y \mapsto C_y$
- Therefore $Q_3 \not \subseteq Q_1$


$Q_1 \subseteq Q_4$?
- $
D_{Q_1} = 
\begin{array}{ |  l l | } |  \hline
  C_x & C_a \\
  C_a & C_b \\
  C_b & C_c \\
  C_c & C_y \\
  \hline
\end{array}
$
- Evaluate $Q_4(D_{Q_1})$
- $Q_4(x, y) \leftarrow \underbrace{Q(x, y)}_{(1)}, \underbrace{Q(y, x)}_{(2)}$
- For head we have $x \mapsto C_x$, $y \mapsto C_y$, and for (1) we would have to map $y \mapsto C_a$, but we already established $y \mapsto C_y$.
- Therefore $Q_1 \not \subseteq Q_4$


$Q_4 \subseteq Q_1$?
- $
D_{Q_4} =
\begin{array}{ |  l l | } |  \hline
  C_x & C_y \\
  C_y & C_x \\
  \hline
\end{array}$
- Evaluate $Q_1(D_{Q_4})$
- $Q_1(x, y) \leftarrow \underbrace{Q(x, a)}_{(1)}, \underbrace{Q(a, b)}_{(2)}, \underbrace{Q(b, y)}_{(3)}$
- For head we have $x \mapsto C_x$, $y \mapsto C_y$, for (1) $a \mapsto C_y$, for (2) $b \mapsto C_x$ and atom (3) matches tuple $(C_x, C_y)$.
- Our candidate substitution $x \mapsto C_x, y \mapsto C_y, a \mapsto C_y, b \mapsto C_x$ is a matching and therefore $Q_4 \subseteq Q_1$.


$Q_2 \subseteq Q_3$?
- $
D_{Q_2} = 
\begin{array}{ |  l l | } |  \hline
  C_x & C_a \\
  C_a & C_b \\
  C_b & C_y \\
  \hline
\end{array}$
- Evaluate $Q_3(D_{Q_2})$
- $Q_3(x, y) \leftarrow \underbrace{Q(x, a)}_{(1)}, \underbrace{Q(a, 1)}_{(2)}, \underbrace{Q(1, b)}_{(3)}, \underbrace{Q(b, y)}_{(4)}$
- For head we have $x \mapsto C_x$, $y \mapsto C_y$, for (1) $a \mapsto C_a$, but for (2) there's no tuple $(C_a, 1)$ in $D_{Q_2}$, so there's no matching. 
- $\Rightarrow Q_2 \not \subseteq Q_3$


$Q_3 \subseteq Q_2$?
- $
D_{Q_3} =
\begin{array}{ |  l l | } |  \hline
  C_x & C_a \\
  C_a & 1 \\
  1 & C_b \\
  C_b & C_y \\
  \hline
\end{array}$
- Evaluate $Q_2(D_{Q_3})$
- $Q_2(x, y) \leftarrow \underbrace{Q(x, a)}_{(1)}, \underbrace{Q(a, b)}_{(2)}, \underbrace{Q(b, c)}_{(3)}, \underbrace{Q(c, y)}_{(4)}$
- For head we have $x \mapsto C_x$, $y \mapsto C_y$, for (1) $a \mapsto C_a$, for (2), $b \mapsto 1$, for (3) $c \mapsto C_b$, and atom (4) matches tuple $(C_b, C_y)$
- Our candidate substitution $x \mapsto C_x, y \mapsto C_y, a \mapsto C_a, b \mapsto 1, c \mapsto C_b$ is a matching and therefore $Q_3 \subseteq Q_2$.


$Q_2 \subseteq Q_4$?
- $
D_{Q_2} = 
\begin{array}{ |  l l | } |  \hline
  C_x & C_a \\
  C_a & C_b \\
  C_b & C_y \\
  \hline
\end{array}$
- Evaluate $Q_4(D_{Q_2})$
- $Q_4(x, y) \leftarrow \underbrace{Q(x, y)}_{(1)}, \underbrace{Q(y, x)}_{(2)}$
- For head we have $x \mapsto C_x$, $y \mapsto C_y$, for (1) we would have to map  $y \mapsto C_a$, but we've already established $y \mapsto C_y$.
- $Q_2 \not \subseteq Q_4$


$Q_4 \subseteq Q_2$?
- $
D_{Q_4} =
\begin{array}{ |  l l | } |  \hline
  C_x & C_y \\
  C_y & C_x \\
  \hline
\end{array}$
- Evaluate $Q_2(D_{Q_4})$
- $Q_2(x, y) \leftarrow \underbrace{Q(x, a)}_{(1)}, \underbrace{Q(a, b)}_{(2)}, \underbrace{Q(b, c)}_{(3)}, \underbrace{Q(c, y)}_{(4)}$
- For head we have $x \mapsto C_x$, $y \mapsto C_y$, for (1) $a \mapsto C_y$, for (2) $b \mapsto C_x$, for (3) $c \mapsto C_y$, but for (4) there's no tuple $(C_y, C_y)$ in $D_{Q_4}$.
- Therefore $Q_4 \not \subseteq Q_2$


$Q_3 \subseteq Q_4$?
- $
D_{Q_3} =
\begin{array}{ |  l l | } |  \hline
  C_x & C_a \\
  C_a & 1 \\
  1 & C_b \\
  C_b & C_y \\
  \hline
\end{array}$
- Evaluate $Q_4(D_{Q_3})$
- $Q_4(x, y) \leftarrow \underbrace{Q(x, y)}_{(1)}, \underbrace{Q(y, x)}_{(2)}$
- For head we have $x \mapsto C_x$, $y \mapsto C_y$, for (1) we would have to map  $y \mapsto C_a$, but we've already established $y \mapsto C_y$.
- $Q_3 \not \subseteq Q_4$


$Q_4 \subseteq Q_3$?
- $
D_{Q_4} =
\begin{array}{ |  l l | } |  \hline
  C_x & C_y \\
  C_y & C_x \\
  \hline
\end{array}$
- Evaluate $Q_3(D_{Q_4})$
- $Q_3(x, y) \leftarrow \underbrace{Q(x, a)}_{(1)}, \underbrace{Q(a, 1)}_{(2)}, \underbrace{Q(1, b)}_{(3)}, \underbrace{Q(b, y)}_{(4)}$
- For head we have $x \mapsto C_x$, $y \mapsto C_y$, for (1) $a \mapsto C_y$, but for (2) there's no tuple $(C_y, 1)$ in $D_{Q_4}$.
- $Q_4 \not \subseteq Q_3$


'''Recap''':  $Q_4 \subseteq Q_1$, $Q_3 \subseteq Q_2$, no equivalent queries 


## See Also
- [Conjunctive Query](Conjunctive_Query)

## Sources
- [Database Systems Architecture (ULB)](Database_Systems_Architecture_(ULB))
- Database Systems Architecture lecture notes #2 by S. Vansummeren [https://dl.dropboxusercontent.com/sh/r0zvy3zaycbevx8/U0XnqCSwGZ/lect2-notes-conjunctive.pdf]


[Category:Exercises](Category_Exercises)
[Category:Relational Databases](Category_Relational_Databases)