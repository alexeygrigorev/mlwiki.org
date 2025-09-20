---
layout: default
permalink: /index.php/SemiOrder_Preference_Structure
tags:
- multi-criteria-decision-aid
title: SemiOrder Preference Structure
---
## Semi Order
This is a preference structure for [Modeling Preferences](Modeling_Preferences) in [MCDA](MCDA) that takes indifference threshold into account (and therefore can model situations such as in [Luce's Coffee Cups](Luce's_Coffee_Cups))

Also called semi-order
$\forall a,b \in A:$
- $a \ P \ b \iff g(a) > g(b) + q$
- $a \ I \ b \iff |  g(a) - g(b) | \leqslant q$ |
$q$ - some threshold


## Properties
### Property 1
$I$ is not transitive now:
- $g(b) = g(a) + 2/3 \cdot q \Rightarrow a \ I b$
- $g(c) = g(b) + 2/3 \cdot q \Rightarrow b \ I c$
- $a \ \overline{I} \ c$ because $| g(c) - g(a) | = 4/3 \cdot t > q \Rightarrow a \ P \ c$ |

## Exercises
### Exercise 1
$a \ P \ b, b \ P \ c, a \ I \ d \Rightarrow d \ P \ c$
- (1) $a \ P \ b \iff g(a) > g(b) + q$
- (2) $b \ P \ c \iff g(b) > g(c) + q$
- (3) $a \ I \ d \iff |  g(a) - g(d) | \leqslant q \iff -q + g(d) \leqslant g(a) \leqslant q + g(d)$ |- (4), (1) + (2): $g(a) + g(b) > g(b) + g(c) + 2q, g(a) > g(c) + 2q$
- (3) & (4) $q + g(d) \geqslant g(a) > g(c) + 2q  \Rightarrow g(d) > g(c) + q \iff d \ P \ c$

<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/de/mcda/threshold-model-prop1.png" alt="Image">

### Exercise 2
$a \ P \ b, b \ I \ c, c \ P \ d \Rightarrow a \ P \ d$
- (1) $a \ P \ b \iff g(a) > g(b) + q$
- (2) $b \ I \ c \iff |  g(b) - g(c) | \leqslant q  \iff g(b) - q \leqslant g(c) \leqslant g(b) + q$ |- (3) $c \ P \ d \iff g(c) > g(d) + q$
- (4), (3) & left of (2): $g(d) + q < g(c) \leqslant g(b) + q \Rightarrow g(b) + q> g(d) + q$
- (1) & (4): $g(a) > g(b) + q > g(d) + q \Rightarrow g(a) > g(d) + q \Rightarrow a \ P \ d$ 



## Sources
- [Decision Engineering (ULB)](Decision_Engineering_(ULB))
