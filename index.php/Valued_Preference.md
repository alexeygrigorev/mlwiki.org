---
layout: default
permalink: /index.php/Valued_Preference
tags:
- multi-criteria-decision-aid
- voting-theory
title: Valued Preference
---
## Valued Preference
This is a preference structure for [Modeling Preferences](Modeling_Preferences) in [MCDA](MCDA).


In this case the relation $P$ is not binary
- instead of saying $a \ P \ b$ or $b \ P \ a$ we express the intensity of preference:
- $v(a, b)$ is valued preference of $a$ to $b$ 
- $v(b, a)$ is valued preference of $b$ to $a$ 
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/de/mcda/valued-pref.png" alt="Image">

### [Voting Theory](Voting_Theory) Analog
We can see the valued preference function as the proportion voters:
- $v(a, b)$ is the proportion of voters who prefer $a$ to $b$ 
- $v(b, a)$ is the proportion of voters who prefer $b$ to $a$, $v(b, a) = 1 - v(a, b)$

This is quite similar to [Condorcet's Rule](Condorcet's_Rule):
- $v(a, b) = \cfrac{N(a > b)}{N}$ and $v(b, a) = \cfrac{N(b > a)}{N}$

<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/de/mcda/graph-3.png" alt="Image">


## Sources
- [Decision Engineering (ULB)](Decision_Engineering_(ULB))
