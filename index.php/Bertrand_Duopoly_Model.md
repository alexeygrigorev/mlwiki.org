---
title: "Bertrand Duopoly Model"
layout: default
permalink: /index.php/Bertrand_Duopoly_Model
---

# Bertrand Duopoly Model

## The Bertrand Duopoly Model
This is a game from the [Game Theory](Game_Theory) that models interaction between two firms that produce the same product. 

This model is similar to the [Cournot Duopoly Model](Cournot_Duopoly_Model).


### The Model
Consider a market with two firms $1$ and $2$ that produce identical products
- let $q = A - p$ be the total quantity sold for the price $p$ and demand $A$ 
- if both firms have the same price, then each sells a half of the total 
- if one firm has a lower price, it sells everything 
- the marginal cost of a firm $i$ is $c_i$
- the restrictions are $c_1 > 0, c_2 > 0, c_1 \ne c_2$

The earned money of each firm:
- $\pi_1 = \left\{\begin{matrix}
A - p_1 & \text{if } p_1 < p_2 \\  
\cfrac{A - p_1}{2} & \text{if } p_1 = p_2 \\
0 &  \text{if } p_1 > p_2
\end{matrix}\right.$
- $\pi_2 = \left\{\begin{matrix}
A - p_2 & \text{if } p_2 < p_1 \\  
\cfrac{A - p_2}{2} & \text{if } p_2 = p_1 \\
0 &  \text{if } p_2 > p_1
\end{matrix}\right.$


But we need to take into account the cost of production.

So the utilities are:
- $u_1 = q_1 (p_1 - c_1)$ 
- $u_2 = q_2 (p_2 - c_2)$ 
- $p_1 - c_1$ are the marginal earns per product - so we multiply it on sold quantity
- each player wants $u_i \geqslant 0$ (i.e. $p_i \geqslant c_i$)


Consider the constraints 
- for player 1
  - $p_1 \leqslant A$ can't exceed the maximal price (the demand)
  - $p_1 \geqslant c_1$ can't be lower than the cost of production
  - $\Rightarrow c_1 \leqslant p_1 \leqslant A$
- for player 2
  - $c_2 \leqslant p_2 \leqslant A$
- $c_1 \ne c_2$

Therefore "interesting" values (ones that get profit) are:
- $p_1 \leqslant p_2$ for firm 1
  - or $c_1 \leqslant p_1 \leqslant p_2$
- $p_2 \leqslant p_1$ for firm 1
  - or $c_2 \leqslant p_2 \leqslant p_1$

Since $c_1 \ne c_2$ there could be two cases:
- $c_1 < c_2$ - worst case for firm 2
  - in order to increase their marginal utilities and take the whole market they will constantly lower the price 
  - until eventually $c_2 = p_2$ (the utility is still not negative - so it's good)
  - but firm 1 can continue to lower the price - and therefore it will get the whole market 
  - i.e. $p_1 \leftarrow  c_2 - \epsilon, (\epsilon > 0)$ makes 1 win the market
- the same for $c_2 < c_1$ - worst case for firm 1
  - firm 2 wins the market
- the only possible equilibrium in such case would be $c_1 = c_2$

 
## See also
- [Cournot Duopoly Model](Cournot_Duopoly_Model)

## Sources
- [Decision Engineering (ULB)](Decision_Engineering_(ULB))

[Category:Game Theory](Category_Game_Theory)