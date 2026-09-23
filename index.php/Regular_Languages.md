---
layout: default
permalink: /Regular_Languages
tags:
- algorithms
- coursera
title: Regular Languages
---

## Regular Languages
This is a class of [Formal Languages](Formal_Languages) that can be defined by
- Final State Automata
- [Regular Expression](Regular_Expression)

A language $L$ is called *regular* if
- it's accepted by some DFA

## Examples
### Example 1
$L_3 = \big\{ w \ | \ w \in \{0, 1\}^* \land w \mod 23 = 0 \big\} $
- we can show that this language is regular by building a DFA for it 

Let $A$ be the automata that recognizes $L_3$
- $Q = \{0, 1, ..., 22 \}$ - all possible remainders for 23 
- $q_0 = 0$ 
- $F = \{ q_0 \} $: if a number is divisible by 23, the remainder should be 0
- $\delta$:
  - suppose $w$ represents integer $i$ in binary format
  - $\delta(0, w)$ = i \mod 23$
  - $w.0$ represents $2 \cdot i$ 
    - $\delta(i \mod 23, 0) = 2 \cdot i \mod 23$
    - $i = 23 \cdot a + b$
    - $2 \cdot i = 46 \cdot a + 2 \cdot b = 2 \cdot b \mod 23$
  - $w.1$ represents $2 \cdot i + 1$
    - $\delta(i \mod 23, 1) = (2 \cdot i + 1) \mod 23$

For example:
- $\delta(15, 0) = 30 \mod 23 = 7$, not accepted
- $\delta(11, 1) = 23 \mod 23 = 0$, accepted

## Not Regular Languages
Not all languages are regular 

For example,
- it is not possible to check with a DFA if we say the exact number of zeros and ones on their input
- or check if parentheses are balanced in an arithmetic expression

Other examples 
- $a^i \equiv \underbrace{a \ a  ... a }_{i \text{ times}}$
- $L_1 = \{ 0^n 1^n \ | \ n \geqslant 1 \}$
- $L_2 = \big\{ w \ | \ w \in \{(, )\} \land b \text{ is balanced} \big\} $
