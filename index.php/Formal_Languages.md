---
layout: default
permalink: /Formal_Languages
tags:
- algorithms
- coursera
title: Formal Languages
---

## Formal Languages
### Alphabet
An *alphabet* $\Sigma$ is any finite set of symbols
- ASCII, unicode
- $\{0, 1\}$, $\{a,b,c\}$
- set of signals used in some protocol

A *string* (*sequence* or *word*) over an alphabet $\Sigma$ is 
- a list of elements from $\Sigma$
- $001, \Sigma = \{0, 1\}$
- the length of a string is the number of positions is this string
- $\epsilon$ is the empty word, its length is zero for any language $\Sigma$

*Powers* of alphabet 
- $\Sigma^k$ is a collection of all possible strings from $\Sigma$ of length $k$
- for $\Sigma = \{a, b\}$, $\Sigma^0 = \{ \epsilon \}, \Sigma^1  = \{ a, b \}, \Sigma^2  = \{ aa, ab, ba, bb \}, \Sigma^3  = \{ aaa, aab, aba, abb, baa, bab, bba, bbb \}, ...$

The Kneele Star
- $\Sigma^*$ is a set of all possible strings over alphabet $\Sigma$
- $\Sigma^* = \Sigma^0 \cup \Sigma^1 \cup \Sigma^2 \cup ...$
- for $\Sigma = \{a, b\}, \Sigma^* = \{\epsilon, a, b, aa, ab, ba, bb, aaa, aab, ... \}$
- $\Sigma^+$ is a set of all strings except $\epsilon$
- $\Sigma^* = \Sigma^1 \cup \Sigma^2 \cup ...$
- i.e. $\Sigma^* = \{\epsilon \} \cup \Sigma^+ $

### Language
- for alphabet $\Sigma$ a *language* $L$ is $L \subseteq \Sigma^*$ - some subset of all possible strings formed by $\Sigma$
- a language can be finite or infinite 

Examples of Languages:
- English, French (finite languages)
- all strings of $n$ zeros followed by $n$ ones ($\infty$)
- strings with equal number of 1s and 0s ($\infty$)
- strings with no consecutive ones: $L = \{ \epsilon, 0, 1, 00, 01, 000, ... \}$

Empty Language
- a language $\{ \epsilon \} $ is not empty: it consists of one empty string
- a language $\varnothing$ is empty: there's nothing
- note that $\varnoting \not \equiv \{ \epsilon \} $

Ways to define languages 
- verbal description: "sequences containing equal number of 1s and 0s"
- set notation $ \{ w | \text{zeros}(w) = \text{ones}(w) \} $
- [Finite State Automata](Finite_State_Automata)
- [Regular Expressions](Regular_Expressions)

### Typical Conventions
Usually we use the following conventions:
- $..., w, x, y, z$ - words
- $a, b, c, ...$ - symbols
- to distinguish between a word $\texta$ and a character $a$, word is made bold

## [XML](XML) Languages

## Sources
- [Automata (coursera)](Automata_%28coursera%29)
- [XML and Web Technologies (UFRT)](XML_and_Web_Technologies_%28UFRT%29)
