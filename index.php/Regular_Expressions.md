---
layout: default
permalink: /Regular_Expressions
tags:
- algorithms
- coursera
title: Regular Expressions
---
{% raw %}


## Regular Expressions
Regular Expressions 
- is an algebraic way of describing [Regular Languages](Regular_Languages)
- they are common for describing patters in the text, etc

### Preliminaries
Basic notations 
- $E$ - regular expression 
- $L(E)$ - [formal language](Formal_Languages) that $E$ describes

Basic algebraic operations 
- Union $L \cup M$
  - same as for sets
  - (languages are also sets!)
- Concatenation of languages $L$ and $M$ is $LM$ (or $L.M$)
  - $\forall w.x \in LM: w \in L, x \in M$
  - it's quite similar to Cartesian product: take a word from $L$ and concatenate it with all words from $M$
  - $\{01, 111, 10\} \{00, 01\} \equiv \{0100, 0101, 11100, 11101, 1000, 1001\}$
- The Kleene Star (or just Star): for language $L$ the Star is $L^*$
  - $L^*$ is the set of strings formed by concatenating 0 or more strings from $L$ in any order
  - $L^* \equiv \{ \epsilon \} \cup L \cup LL \cup LL \cup ...$
  - example: $\{0, 10\}^* \equiv \{\epsilon, 0, 10, 00, 010, 100, 1010, ...\}$

### Definition
Inductive definition of a regular expression (RE)

Basis:
- Basis 1
  - if $'a'$ is a symbol, then $a$ is an RE
  - $L(a) = \{'a'\}$ (a language that contains one string of len 1)
- Basis 2
  - $\epsilon$ is a RE, and 
  - $L(\epsilon) = \{\epsilon\}$
- Basis 3 (empty set)
  - $\varnothing$ is a RE and
  - $L(\varnothing) = \varnothing$

Induction 
- $E_1$ and $E_2$ are REs
- Induction 1
  - $E_1 + E_2$ is a RE and 
  - $L(E_1 + E_2) \equiv L(E_1) \union L(E_2) $
- Induction 2
  - $E_1 E_2$ is a RE and
  - $L(E_1 E_2) \equiv L(E_1) L(E_2)$
- Induction 3
  - if $E$ is a RE, then $E*$ is a RE and
  - $L(E*) \equiv \big( L(E) \big)^*$

#### Precedence

| Priority | Operation | RE | Algebra |
|---|---|---|---|
| highest | the Star | $*$ | $\text{exp}$ |
|  | Concatenation |  | $\times$ or $\cdot$ |
|  | Union | $+$ | $\cup$ or $+$ |

Parentheses used to enforce the order

### Examples
- $L(01) = \{ 01 \}$
  - concatenation of two languages: $0$ and $1$
  - result - a language containing a string "01"
  - in general, any string of symbols as a RE represents a language that contains only that one string 
- $L(01 + 0) = \{ 01, 0 \}$
- $L \big(0(1 + 0) \big) = \{ 01, 00 \}$
  - note the use of ()s to show the precedence
- $L(0^*) = \{ \epsilon, 0, 00, 000, ... \}$
  - any string of 0's, including the empty string
- $L \big( (0 + 10)^* (\epsilon + 1)  \big)$
  - $(0 + 10)^*$ anything that is followed by 0
  - plus either nothing or 1
  - defines a language over $ \{ 0 , 1 \} $ without two concentrative 1's 

## Equivalence of REs and Finite Automata
need to show the following
- $\forall$ RE $E$ $\exists$ a FA $A$ (1: $E \to A$)
- $\forall$ FA $A$ $\exists$ a RE $E$ (2: $A \to E$)

### RE $\to$ [$\epsilon$-NFA](Non-Deterministic_Finite_Automata)
The construction is by induction on the number of operators ($+, ., {}^*$) in the RE

To form an $\epsilon$-NFA we try to adhere to the following construct 
- re-to-nfa.png
- we have a "start" state: only it can have external predecessors 
- and a "final" state: only it can have external successors
- any number of states and edges in the middle, but no edges from or to outside

Induction Basis
- re-to-nfa-basis.png
- we get to the final state on $a$, on $\epsilon$, or don't get to it

Induction Step
- Union: $E_1 + E_2$
  - the IH applies to the subexpressions $E_1$ and $E_2$:
  - we assume that there $\exists$ $\epsilon$-NFA $A_1$ for $E_1$ and $A_2$ for $E_2$
  - re-to-nfa-step1.png
  - so we form $\epsilon$-NFA for $E_1 + E_2$ by introducing a new start and a new final states 
  - the old start and final states are no longer final 
  - if there's a path from the new start to the new final, it starts with $\epsilon$-transition and continuous entirely in $A_1$ or in $A_2$ (since there are no external arcs)
- Concatenation $E_1 E_2$
  - by the IH we assume that there $\exists$ $\epsilon$-NFA $A_1$ for $E_1$ and $A_2$ for $E_2$
  - re-to-nfa-step2.png
  - we add an $\epsilon$-transition from the final state of $A_1$ to the start state of $A_2$
  - in this construction any path first must pass through $A_1$ and then through $A_2$
  - there's no other way
- The Star $E^*$
  - suppose that we already have $\epsilon$-NFA $A$ for $E$
  - re-to-nfa-step3.png
  - we introduce new start and final states 
  - add $\epsilon$-transitions:
    - old final $\to$ new final and old final $\to$ old start 
    - new start $\to$ old start (to have 1 or more repetitions: concat $EE$)
    - new start $\to$ new final (to have 0 repetitions)

### [DNFA](Deterministic_Finite_Automata) $\to$ RE
This construction is on $k$ for $k$-paths:
- the maximum state number that we're allowed to traverse along a path 

#### $k$-Paths
a $k$-path is a path from any stat to any state 
- but it doesn't go through states numbered higher than $k$
- this applies only to the states along the way (in the middle), the end points may be of any state 

The induction is on $k$
- i.e. there's a RE whose language is the set of labels of all $k$-paths from state $i$ to state $j$
- we start with $0$-paths and by the time we get to $n$-paths, there are no restrictions 

Example
- nfa-to-re-kpaths.png
- $0$-paths from 2 to 3 is the language of the RE $\textbf{0}$
  - reason: 
  - we can only follow an arc $2 \to_{0} 3$ (with a label "0")
  - it's the only path from 2 to 3 that doesn't go through any other state 
- $1$-paths from 2 to 3 
  - now we can go thought state $1$, but not thought $2$ or $3$
  - plus we can still follow $2 \to_{0} 3$
  - so we have $2 \to_{1} 1 \to_{1} 3$ and $2 \to_{0} 3$
  - and the RE is $0 + 11$
  - note that once we get to $1$, we cannot get back to $2$ - so no cycles there
- $2$-paths
  - now the only state we cannot pass is $3$ 
  - from $2$ we can go to $1$ and back to $2$ zero or more times 
    - plus we have to follow $0$ to end up in $3$
    - thus we have $(10)^* 0$
  - alternative plan is to oscillate between $1$ and $2$ 
    - go to $1$ (by doing $2 \to_1 1$) $for the first time
    - and do $01$ (following $1 \to_0 2 \to_1 1$) as many times as you want
    - and finally follow $1 \to_1 3$
    - thus the RE is $1 (01)^* 1$
  - the RE for the $2$-paths is the union of these two
    - $(10)^* 0 + 1 (01)^* 1$
- $3$-paths
  - there's also a RE for $3$-paths from $2$ to $3$
  - but it's quite complicated 

#### DNFA $\to$ RE Induction on $k$-Paths
Notation
- let $R^k_{ij}$ be RE for the set of labels of $k$-path from $i$ to $j$

Basis: $k = 0$
- $0$-paths cannot have intermediate states at all 
- so it's a set of paths from state $i$ to state $j$, each consisting of a single arc
  - in special cases ($i = j$) - of no arcs at all
- we can construct a RE for this language
  - connect with $+$ all the labels, and in case of $i=j$, also connect with $\epsilon$
  - no arcs from $i$ to $j$, then the RE is $\varnothing$
- example:
  - nfa-to-re-basis-ex.png
- $R^0_{ij}$ = sum of all labels of arcs from state $i$ to state $j$
  - $R^0_{ij} = \varnothing$ if no such arcs
  - $\epsilon \in R^0_{ij}$ if $i = j$

Example: Basis 
- nfa-to-re-kpaths.png
- $R^0_{12} = 0$ - a label from $2$ to $3$
- $R^0_{11} = \varnothing + \epsilon = \epsilon$ 
  - $\varnothing$: no arc from $1$ to $1$
  - but since $i=j$, we add $\epsilon$
  - (note an algebraic law: $\varnothing + x = x$)

$k$-Path Inductive Case
- we assume that we've written all the REs  $R^{k-1}_{ij}$ and need to write REs for $R^k_{ij}$
- note that a $k$-path from $i$ to $j$ either
  - never goes through $k$
  - goes through $k$ one or more times 
- so we can write $R^k_{ij}$ in terms of $R^{k-1}_{ij}$s
  - $R^k_{ij} = \color{grey}{\underbrace{{\color{black}{ \ R^{k-1}_{ij} \ }}}_{\small\text{(1)}} {\color{black}{+}} \underbrace{{\color{black}{ \ R^{k-1}_{ik}  \  }}}_{\small\text{(2)}} \underbrace{{\color{black}{  \  \big( R^{k-1}_{kk} \big)^*  \  }}}_{\small\text{(3)}} \underbrace{{\color{black}{  \  R^{k-1}_{kj}  \  } }}_{\small\text{(4)}}}$
  - (1) doesn't go through $k$ - every $k-1$-path is also a $k$-path
  - all other paths get to $k$ at least once
  - (2) goes from $i$ to $k$ 1st time (all paths that get us from $i$ to $k$)
  - (3) all paths from $k$ to $k$ 0 or more times 
  - (4) finally, we need to get to $j$
  - this generates the labels of all paths from $k$ to $j$ that don't pass $k$ or higher

Illustration
- nfa-to-re-induction.png
- vertical axis - the number of state (here $j$ is above $i$, but it can be the other way around)
- first possibility: the path never goes through state $k$
- or it could go to $k$ for the first time
  - from $k$ to $k$ you can go only through lower states 0 or more times
- and finally you go from $k$ to $j$ through states numbered lower than $k$

Final step 
- the RE with the same language as the DFA is the sum (union) of all $R^n_{ij}$ where
- $n$ is the total number of states (i.e. the $k$-paths are unconstrained)
- $i$ is the start state 
- $j$ is the final state 
  - we do it for each final state $j$ and take a union over the results 

Example again:
- nfa-to-re-ex.png
- suppose that $2$ is the start state and $3$ is the final state 
- the RE we want is $R^3_{23}$
- $R^3_{23} = R^2_{23} + R^2_{23} \big( R^2_{22} \big)^* = R^2_{23} \big( R^2_{22} \big)^* $ 
  - $R^2_{23}$ appeared in two places so we can simplify the expression
  - $R^2_{23} = (10)^* 0 + 1 (01)^* 1 $
  - $R^2_{33} = \epsilon + 0 (10)^* (1+00) + 1(10)^*(0+11)$
    - paths that go from $3$ to $3$ that never go through $3$
    - so it can jump from $1$ to $2$ and back to $1$ until it returns to $3$ 
- So $R^3_{23} = \big[ \big]$
{% endraw %}
