---
title: Decision Analysis
layout: default
permalink: /index.php/Decision_Analysis
---

# Decision Analysis

## Decision Analysis
### Decision Under Certainty
Let
- $A$ be a finite set of alternatives (possible decisions)
- $X$ be a set of consequences (usually some financial metrics)
- $c: A \mapsto X$ a consequence function
  - $c(a) \in X$ is a consequence of implementing action $a \in A$

Problem: 
- to compare alternatives and find the optimal one 
- on the basis of their consequences

- When $| A|$ is very large - need [Optimization](Optimization) techniques |- When $x \in X$ is multi-dimensional, i.e. $x = (x_1, ..., x_m)$ need to apply [Multi-Objective Optimization](Multi-Objective_Optimization) and/or [MCDA](MCDA)

For these models we make a strong assumption:
- we can quantify the consequences of taking different actions with certainty


However this assumption is not always true
- we often can face situations when consequences $c(a)$ of taking a decision $a$ are not known with certainty 

There are two categories of decision analysis tools that help model this:
- [Decision Under Risk](Decision_Under_Risk)
- [Decision Under Uncertainty](Decision_Under_Uncertainty)


### [Decision Under Uncertainty](Decision_Under_Uncertainty)
- we are not able to asses the distribution, but we can list all possible scenarios

Methods
- [Max Min Strategy](Max_Min_Strategy) - extreme pessimism 
- [Max Max Strategy](Max_Max_Strategy) - extreme optimism
- [Hurwitz's Index](Hurwitz's_Index) - between the extreme pessimism and the extreme optimism
- [Min Max Regret Strategy](Min_Max_Regret_Strategy) - when we want to minimize the regret of a missed opportunity
- [Laplace Rule](Laplace_Rule) - the principle of insufficient reasoning


### [Decision Under Risk](Decision_Under_Risk)
- $c(a)$ is not known with certainty, but we know the probability distribution on the set of $X$

[Decision Trees](Decision_Tree_(Decision_Theory))
- [Expected Values for Lotteries](Expected_Values_for_Lotteries)
- [Expected Utility Theory](Expected_Utility_Theory)



## Links
- http://answers.mheducation.com/business/economics/business-economics/decisions-under-risk-and-uncertainty
- http://ids355.wikispaces.com/Ch.+5s+Decision+Making - Questions and Answers

## Sources
- [Decision Engineering (ULB)](Decision_Engineering_(ULB))

[Category:Decision Engineering](Category_Decision_Engineering)