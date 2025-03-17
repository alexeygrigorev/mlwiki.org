---
title: Multi-Criteria Decision Aid
layout: default
permalink: /index.php/Multi-Criteria_Decision_Aid
---

# Multi-Criteria Decision Aid

## Multi-Criteria Decision Aid
This is a tool that helps a decision maker to choose a solution when he is facing conflicting criteria and cannot decide.

For example, you want to buy a new car:
- One is expensive, speed is good; 
- another is cheap but slow and with little comfort. 
- These criteria (cost vs speed) are conflicting. 

We need to find a compromise that answers the expectation of a decision maker


<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/de/mcda/mcda.png" alt="Image">
- Step 1: Define the set of alternatives $A = \{a_1, ..., a_n\}$
- Step 2: Define the set of criteria $G = \{g_1, ..., g_k\}$
- Step 3: Define the Preferences (the expectations of a decision maker)
- Step 4: Apply methods to find the best alternative


## Alternatives
$A$ - set of alternatives (actions, options, items, decisions, etc)

$A$ can be
- finite or infinite
- countable or uncountable
- stable (always the same) or evolving


## Criteria
A ''criterion'' $g_i$ is a mapping from the set of alternatives $A$ to some totally ordered set $E_i$:
- $g_i: A \mapsto E_i$
- $g_i \in G$ form a set of criteria

With $E_i$ we can rank all elements of $A$ from best to worst

Examples:
- $E = \mathbb{R}$
- $E = \{\text{VB}, \text{B}, \text{M}, \text{G}, \text{VG}\}$

A set can be:
- ordinal (operations $<, =, >$)
  - $E = \{\text{VB}, \text{B}, \text{M}, \text{G}, \text{VG}\}$
- interval (operations $<, =, >, +, -$)
  - temperature
- ratio (operations $<, =, >, +, -, \cdot, / $)
  - $E = \mathbb{R}$


Restrictions on $G$:
- For a set to be ordered, operations $<$ and $>$ must be defined there
- A set of criteria $G$ ideally should form a [Consistent Family of Criteria](Consistent_Family_of_Criteria)


### [Dominance](Dominance) Principle
Some alternatives can be eliminated by Dominance principle
- If for two alternatives $a$ and $b$ for all criteria they are equally good
- but there exists one criteria at which $a$ is better than $b$
- then $b$ is dominated by $a$ and will never be chosen


Consider this example
- we're choosing a car
- there are 4 criteria: price, power, consumption, comfort
- there are 6 alternatives

|    |  Price  |  Power  |  Consumption  |  Comfort  |  <font color="grey">Avg A.</font>  |  <font color="grey">18</font>  |  <font color="grey">75</font>  |  <font color="grey">8</font>  |  <font color="grey">3</font> ||  Sport  |  18.5  |  110  |  9  |  2 ||  <font color="red">Avg B.</font>  |  <font color="red">17.5</font>  |  <font color="red">85</font>  |  <font color="red">7</font>  |  <font color="red">3</font> ||  Lux 1  |  24  |  90  |  8.5  |  5 ||  Exonomic  |  12.5  |  50  |  7.5  |  1 ||  Lux 2  |  22.5  |  85  |  9  |  4 |

By [Dominance](Dominance) principle:
- We see that '''Avg B''' is always better than '''Avg. A'''
- then nobody will ever choose Avg A: A is dominated by B
- but no other alternative can be eliminated this way

How to chose which one is the best?
- Need ''subjective'' preferences 


## Preferences
To be able to find the best solution we need to know ''subjective preferences''
- these are binary relations provided by a decision maker 
- defined analogously to [Voting Theory Relations](Voting_Theory_Relations)

Given two alternatives $a$ and $b$ a decision maker can say if
- $a \ P \ b$ or $b \ P \ a$: $a$ is preferred to $b$ - ''the preference relation''
- $a \ I \ b$ - the indifference relation (not transitive|   see [Luce's Coffee Cups](Luce's_Coffee_Cups)) |- $a \ J \ b$ - the incomparability relation, when you cannot compare things |

<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/de/mcda/mcda-dm.png" alt="Image">

How to represent a Decision Maker's preferences in some model?

With [Modeling Preferences](Modeling_Preferences):
- [Complete Pre-Order Preference Structure](Complete_Pre-Order_Preference_Structure) ($I$ is not transitive)
- [SemiOrder Preference Structure](SemiOrder_Preference_Structure) ($I$ is transitive, no $J$)
- [Partial Order Preference Structure](Partial_Order_Preference_Structure) (with $J$)
- [Valued Preference](Valued_Preference)


Important condition when modeling preferences:
- [Preferential Independence](Preferential_Independence)



## Methods
There some important families of criteria:
- MAUT (Utility): [Multi-Attribute Utility Theory](Multi-Attribute_Utility_Theory)
- Outranking methods 


### Outranking
Outranking methods perform pair-wise comparisons (like in the [Condorcet's Rule](Condorcet's_Rule))

Most famous methods:
- [ELECTRE](ELECTRE) 
- [PROMETHEE](PROMETHEE)

Problems of outranking methods:
- [Rank Reversal](Rank_Reversal)


## [Multi-Objective Optimization](Multi-Objective_Optimization)
Once we found the [Pareto-optimal](Dominance) set of solutions in a  problem, we need to find the best solution, and MCDA can help with it


## Links
- http://www.lamsade.dauphine.fr/~bouyssou/TranspaOrbel16.pdf
- http://www.liacs.nl/~emmerich/moda03mcda.pdf


## Sources
- [Decision Engineering (ULB)](Decision_Engineering_(ULB))
- Multiple Criteria Decision Analysis: State of the Art Surveys, 2005 

[Category:Multi-Criteria Decision Aid](Category_Multi-Criteria_Decision_Aid)