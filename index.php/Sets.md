---
layout: default
permalink: /index.php/Sets
tags:
- combinatorics
title: Sets
---
## Sets

A *set* is a collection of distinct objects united into a whole by some criterion.

The objects that make up a set are called *elements* of the set. A set cannot contain more than one identical element.

- $a \in A$ - element a belongs to set $A$
- $a \notin A$ - element a does not belong to set $A$


The *empty set* is a set containing no elements. It is denoted by $\varnothing$

Sets are divided into *finite* sets (for example, the number of residents of a city) and *infinite* sets (the number of points on a segment).

### Ways of Defining Sets

- Enumeration:
  $A = \{a_1, a_2, ..., a_n\}$

- Characteristic properties:
  $A = \{ x |  P(x) \}$, where $P(x)$ is a property possessed by elements $x \in A$ and not possessed by $x \notin A$.  |: For example, $X = \{x |  x^2 - 3x + 2 = 0\}$
### Subsets
If every element of set $A$ is also an element of set $B$, then $A$ is a *subset* of $B$. This is denoted $A \subset B$.

Every non-empty set $A$ has at least two subsets: $A$ itself and $\varnothing$. These sets are *improper* subsets of $A$, and all other subsets (if they exist) are *proper* subsets.

If $A \subset B$ and $B \subset C$, then $A \subset C$. That is, the subset relation satisfies the *transitivity* condition.

If $A \subset B$ and $B \subset A$, then $A$ and $B$ are *equal*.

The *universal set* $U$ is a set that includes all possible elements. That is, for any set $A$, $A \subset U$.

## Euler Diagrams
*Euler diagrams* are a geometric scheme for visually representing the relationship between subsets.


## Operations

### Intersection
The *intersection* (product) of sets $A$ and $B$ is the set consisting of elements that belong to both $A$ and $B$ simultaneously.

$A \cap B = \{ x |  x \in A \mbox{~and~} x \in B\}$
### Union
The *union* (sum) of $A$ and $B$ is the set of all elements belonging to at least $A$ or $B$.

$A \cup B = \{ x |  x \in A \mbox{~and~} x \in B\}$
### Difference
The *difference* of $A$ and $B$ is the set consisting of all elements that belong to $A$ and do not belong to $B$.

$A \backslash B = \{ x |  x \in A \mbox{~or~} x \notin B\}$
The *symmetric difference* of $A$ and $B$ is the set of elements belonging to either $A$ or $B$, but not to both $A$ and $B$ simultaneously.

The *complement* of set A with respect to the universal set U is the set of all elements not belonging to set A, denoted $\bar{A}$.

$\bar{A} = U \backslash A = \{ x |  x \in A \mbox{~and~} x \notin U \}$
### Cartesian Product
The Cartesian product of sets $A$ and $B$ is the set of all ordered pairs $(a, b)$ such that $x \in A, y \in B$:

$A \times B = \{ (x, y) |  x \in A, y \in B \}$
Given $n$ sets $X_1, X_2, ..., X_n$, the Cartesian product $X_1 \times X_2 \times ... \times X_n$ is the set of all possible ordered tuples $\alpha = (x_1, x_2, ..., x_n)$ such that $x_1 \in X_1, x_2 \in X_2, ..., x_n \in X_n$:

$X_1, X_2, ..., X_n = \{ (x_1, x_2, ..., x_n) |  x_i \in X_i, i = 1, ..., n \}$
Each tuple $\alpha = (x_1, x_2, ..., x_n)$ is called a tuple of length $n$, composed of elements of the set $X^n = X \times X \times ... \times X$. The element $x_i$ is called the $i$-th component of the tuple.

Differences between a tuple and a set:
- in a set, order does not matter, but in a tuple it does;
- in a set, all elements are distinct, but in a tuple they may repeat


## Algebra of Sets

- Union and intersection are commutative
  $A \cup B = B \cup A$
  $A \cap B = B \cap A$
- Union and intersection are associative
  $(A \cup B) \cup C = A \cup (B \cup C)$
  $(A \cap B) \cap C = A \cap (B \cap C)$
- Distributivity of union over intersection and distributivity of intersection over union
  $(A \cap B) \cup C = (A \cup C) \cap (D \cup C)$
  $(A \cup B) \cap C = (A \cap C) \cup (B \cap C)$
- $A \cup A = A$
- $A \cup U = U$ and $A \cap U = A$
- $A \cup \varnothing = A$ and $A \cap \varnothing = \varnothing$
- $\Bar{\Bar{A}} = A$
- $\bar{U} = \varnothing$ and $\bar{\varnothing} = U$
- De Morgan's Laws
  $\overline{A \cup B} = \overline{A} \cap \overline{B}$ and
  $\overline{A \cap B} = \overline{A} \cup \overline{B}$





## Inclusion-Exclusion Principle

Given $m$ objects $x_1, x_2, ..., x_m$ and $n$ sets $\alpha_1, \alpha_2, ..., \alpha_n$. The elements $x_i$ may belong to any arbitrary $\alpha_i$ or may not belong to any.

Let us introduce the notation:
- $N$ - the total number of objects, $N = m$
- $N(\alpha_i \alpha_j ... \alpha_k)$ - the number of elements belonging to the set $\alpha_i \cup \alpha_j \cup ... \cup \alpha_k$,
- $N(\overline{\alpha_i \alpha_j ... \alpha_k})$ - the number of elements not belonging to any of $\alpha_i \alpha_j ... \alpha_k$ (i.e., not belonging to $\alpha_i \cap \alpha_j \cap ... \cap \alpha_k$).


Let us compute $N(\overline{\alpha_1 \alpha_2 ... \alpha_n})$ - i.e., count the number of elements not belonging to any of the sets.


$N(\overline{\alpha_1 \alpha_2 ... \alpha_n}) = N - N(\alpha_1) - N(\alpha_2) - ... - N(\alpha_n) + N(\alpha_1 \alpha_2) + N(\alpha_1 \alpha_3) + N(\alpha_1 \alpha_4) + ... N(\alpha_1 \alpha_n) + ... + N(\alpha_{n-1} \alpha_n) - N(\alpha_1 \alpha_2 \alpha_3) - ... + (-1)^n N(\alpha_1 \alpha_2 ... \alpha_n)$


The term $N(...)$ has a "+" sign if the number of sets is even, and a "-" sign if it is odd.

This formula can be written schematically as $N(\overline{\alpha \beta ... \omega})$ = $N(1 - \alpha)(1 - \beta)...(1 - \omega)$, and after expanding the brackets, replace $N\alpha\beta...\omega$ with $N(\alpha\beta...\omega)$.

### Proof

By induction:

Step 1: for 1

$N(\overline{\alpha_1}) = N - N(\alpha_1})$

Step 2: for $n - 1$

$N(\overline{\alpha_1 \alpha_2 ... \alpha_{n - 1}}) = N - N(\alpha_1) - ... + N(\alpha_1 \alpha_2) + ... - N(\alpha_1 \alpha_2 \alpha_3) - ... + (-1)^{n-1} N(\alpha_1 \alpha_2 ... \alpha_{n-1})$

Step 3: for $n$

Consider the group of elements belonging to $\alpha_n$

$N(\overline{\alpha_1 \alpha_2 ... \alpha_{n - 1}} \alpha_n) = N(\alpha_n) - N(\alpha_1 \alpha_n) - ... + N(\alpha_1 \alpha_2 \alpha_n) + ... - N(\alpha_1 \alpha_2 \alpha_3 \alpha_n) - ... + (-1)^{n-1} N(\alpha_1 \alpha_2 ... \alpha_{n-1} \alpha_n)$

Subtract $N(\overline{\alpha_1 \alpha_2 ... \alpha_{n - 1}} \alpha_n)$ from $N(\overline{\alpha_1 \alpha_2 ... \alpha_{n - 1}})$

- $N(\overline{\alpha_1 \alpha_2 ... \alpha_{n - 1}})$ is the number of elements that may or may not belong to \alpha_n
- $N(\overline{\alpha_1 \alpha_2 ... \alpha_{n - 1}} \alpha_n)$ is the number of elements that definitely belong to \alpha_n
- Their difference is exactly the number of elements not belonging to any of $\alpha_1 \alpha_2 ... \alpha_n$


Thus,
$N(\overline{\alpha_1 \alpha_2 ... \alpha_n}) = N(\overline{\alpha_1 \alpha_2 ... \alpha_{n - 1}}) -  N(\overline{\alpha_1 \alpha_2 ... \alpha_{n - 1}} \alpha_n)$.

**Q.E.D.**


## Sources
- Kireenko S.G., Grinshpon I.E. Elements of Set Theory (textbook). Tomsk, 2003. http://portal.tpu.ru/lyceum/innovacion/workroom/sets.pdf
- Vilenkin N.Ya. Combinatorics. Moscow, Nauka, 1969.
