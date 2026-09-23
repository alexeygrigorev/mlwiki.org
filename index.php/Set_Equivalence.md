---
layout: default
permalink: /index.php/Set_Equivalence
tags:
- algorithms
- coursera
title: Set Equivalence
---

## Containment And Equivalence
We say that for sets $A$ and $B$ $A \equiv B$ ($A$ is equivalent to $B$) $\iff$
- $A \subseteq B \land B \subseteq A$
- i.e. when $A$ is contained in $B$ and $B$ is contained in $A$ at the same time 
- that is
  - $a \in A \to a \in B$
  - and $b \in B \to b \in A$

## Automata
### Example
Suppose that we have two sets 
- set $S = L(\mathcal{A})$ is defined by a DFA (LINK!!!!!!!!!!!!!!!!) $\mathcal{A}$
  - automaton-no11.png
- and set $T$ is defined as 
  - $T = \big\{  w  \ | \ w \in \{0, 1\}^* \land \forall a_i, a_{i+1} \in w a_i . a_{a+1} \ne 1 . 1 \big\} $
  - i.e. it's a set of all possible sequences from $\{0, 1\}$ without 2 consecutive 1s 
- we want to show that [Formal Languages](Formal_Languages) defined by these sets are equivalent 
- i.e. $S \equiv T$
  - for that we need to prove two parts: $S \subseteq T$ and $T \subseteq S$

#### Part 1
Part 1: $S \subseteq T$ 
; if $w$ is accepted by \mathcal{A}, it has no consecutive 11s 

Proof: Induction of the length of $w$ 
- there are two accepting states: $A$ and $B$ 
- we want to distinguish whether on $w$ $\mathcal{A}$ gets to state $A$ or $B$ 
- Inductive Hypothesis 
  - (1) if $\delta(A, w) = A$ then $w$ has no 11's and doesn't end with 1
  - (2) if $\delta(A, w) = B$ then $w$ has no 11's, but ends with 1

Induction on $| w |$ - length of $w$:
- basis: $| w | = 0$, i.e. $w \equiv \epsilon$
  - (1) holds: $\epsilon$ has no 11's: $\delta(A, w) = A$
  - (2) holds: but $\delta(A, w) \ne B$
    - if the **if** part of (2) is false, the statement is still true
    - this is called "to hold vacuously"
- assume (1) and (2) are true for strings that are shorter than $w$, and $| w | \geqslant 1$
- inductive step:
  - because $w \ne \epsilon$, we can write $w = x . a$ where
    - $a$ is the last symbol of $w$ and $a$ is the prefix of $w$ (maybe empty)
    - by the Inductive Hypothesis (IH), it holds for $x$: there are no 11's, $\Rightarrow$ <u>it doesn't end with 11</u>
  - $\Rightarrow \delta(A, x)$ must be $A$ or $B$ 
  - if it's $A$ then $x$ ends with 0, thus the IH no matter what $a$ is
  - if it's $B$ then $x$ ends with 1, 
    - if $a = 0$ then the IH holds
    - if $a = 1$ then this word has 11's 
      - $\delta(B, 1) = C$ (i.e. $A$ gets to not accepting state) and $A$ doesn't accept this string $w$
      - and also $w \not \in T$ so the IH still holds

#### Part 2
Part 2: $T \subseteq S$ 
; if $w$ has no 11's then it will be accepted by $\mathcal{A}$

First, we'll restate the in *contrapositive* 
- (contrapositive  of $A \to B$ is $\lnot B \to \lnot A$)
  - they're logically equivalent: $A \to B \equiv \lnot A \lor B \equiv b \lor \lnot A \equiv \lnot B \to \lnot A$
- if $w$ is not accepted by $\mathcal{A}$, then $w$ has 11's 

Proof: 
- since $\mathcal{A}$ is a DFA, each symbol in $w$ gets $\mathcal{A}$ exactly to one state 
- $w$ is not accepted only if $\mathcal{A}$ gets to $C$: $\delta(A, w) = C$
- we can get to $C$ if we're in $B$ and get 1, i.e. 
  - $w = x . 1 . y$ and $\delta(A, x) = B$ (don't care about $y$)
- if $\delta(A, x) = B$ then $x = z . 1$ for some $z$, because we need to have 1 to get to $B$ from $A$ 
- thus, $w = z . 11 . y$, i.e. it contains 11's

$\square$

## [Conjunctive Query](Conjunctive_Query)
There also is a notion of containment for database queries 
- this is used for checking for equivalence of two queries 
- See [Conjunctive Query#Containment And Equivalence](Conjunctive_Query#Containment_And_Equivalence)

## Sources
- [Automata (coursera)](Automata_%28coursera%29)
