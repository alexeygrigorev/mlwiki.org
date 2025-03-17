---
title: "Cournot Duopoly Model"
layout: default
permalink: /index.php/Cournot_Duopoly_Model
---

# Cournot Duopoly Model

## The Cournot Duopoly Model
This is a game from the [Game Theory](Game_Theory) that models interaction between two firms that produce the same product. 


### The Game
Set Up:
- there are two companies $p_1$ and $p_2$
- they produce the same product and have to decide how much they are going to produce 
  - $q_1$ is the number of produced units for $c_1$
  - $q_2$ is the number of produced units for $c_2$
  - so the set of actions each firm can take is $\mathbb{N}$ - all positive numbers
- $q = q_1 + q_2$
- but the market has limits
  - if both companies decide to produce too much, not everything will be sold
  - and the price will go down
- let $p(q) = A - q$ be the price per unit, where $A$ is some constant
  - this models that the more units you sell, the less money (per unit) you get
- for the firm $p_i$ the cost of producing one item is $c_i$
  - $c_i > 0$
  - the total cost of producing is $c_i \cdot q_i$


The Game:
- the companies want to determine what's the best strategy for both 
- the actions here is the number of unit they want to produce 
- variables:
  - $q = q_1 + q_2$ - total quantity
  - $P(q) = A - q$ - the price
- the payoffs
  - $\Pi_1(q_1, q_2) = -\underbrace{c_1 \cdot q_1}_\text{(1)} + \underbrace{q_1 \cdot P(q)}_\text{(2)} = q_1 \cdot (A - q_1 - q_2) - c_1 \cdot q_1$
  - (1) - cost of producing 
  - (2) - the gain
  - note that the payoff of $p_1$ is affected by the choice of $p_2$ 
  - $\Pi_2(q_1, q_2) = -c_2 \cdot q_2 + q_2 \cdot P(q) = q_2 \cdot (A - q_1 - q_2) - c_2 \cdot q_2$


We want to maximize the payoff
- the best strategy for $p_1$
  - for $\Pi_1 - q_1$ is a variable and the rest are parameters 
  - therefore to maximize the payoff we take a partial derivative with respect to $q_1$ and equal it to 0
  - $\cfrac{\partial \Pi_1(q_1, q_2)}{\partial q_1} = 0$
  - $\cfrac{\partial}{\partial q_1} \big(q_1 (A - q_1 - q_2 - c_1 q_1 \big) = A - q_1 - q_2 + (-q_1) - c_1 = 0$
  - or $A - c_1 = q_2 + 2q_1$
- do the same for $p_2$
  - $\cfrac{\partial \Pi_2(q_1, q_2)}{\partial q_2} = 0$
  - or $A - c_2 = q_1 + 2 q_2$
- so assuming they cooperate and both want to find the best strategy, we have
  - $
\left\{\begin{matrix}
A - c_1 = q_2 - 2q_1 \\ 
A - c_2 = q_1 + 2q_2
\end{matrix}\right.$
- now we can take express $q_1$ via $q_2$
  - $q_1 = \cfrac{1}{2} (A - c_1 - q_2)$
  - $2A - 2c_2 = A - c_1 - q_2 + 4q_2$
  - $3q_2 = 2A - A - 2c_2 + c_1$
  - $q_2 = \cfrac{1}{3} (A - 2c_1 + c_2)$
  - this is the best strategy for $p_2$
- same for $p_1$
  - $q_1 = \cfrac{1}{3} (A - 2c_1 + c_2)$
  - this is the best strategy for $p_1$


This action profile is a [Nash Equilibrium](Nash_Equilibrium) - no one will have an incentive to deviate 
- so applying this we can calculate the right number of items to produce



## Links
- http://www2.isye.gatech.edu/~pinar/teaching/isye6230-spring2004/duopoly-models-part1.pdf

## See also
- [Bertrand Duopoly Model](Bertrand_Duopoly_Model)

## Sources
- [Decision Engineering (ULB)](Decision_Engineering_(ULB))

[Category:Game Theory](Category_Game_Theory)