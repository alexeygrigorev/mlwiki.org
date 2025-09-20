---
layout: default
permalink: /index.php/Inventory_Management
tags:
- decision-engineering
title: Inventory Management
---
## Inventory Management
The idea behind all these Inventory Management models is to 
- help to decide when to order new goods to replenish the stocks 


=== Wilson Model (EOQ Model) === 
EOQ = Economic Order Quantity model
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/de/im/em-basic-eoq.png" alt="Image">
- This is the simplest model
  - we start with some level of stock
  - every day the stock decreases at the same number $\lambda$ (the ''demand'' is constant)
  - when where are no goods, we do re-stocking
  - another assumption: no waiting time, the stock is refilled immediately 
- variables of the model
  - $n$ - the number of items ordered at once 
- we need to find the optimal solution: variables $n$
  - if $n$ is big, we'll have one strategy (a)
  - if $n$ is small, we'll have another (b)
  - <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/de/im/em-basic-eoq-var.png" alt="Image">
- parameters of the model:
  - $c_f$ - fixed cost of ordering (and delivering) goods 
  - $c_s$ - storage cost per day per item 
  - $\lambda$ - the demand, # of items sold every day
  - $T = \cfrac{n}{\lambda}$ - time to empty the stock ($n$ is divisible by $\lambda$)
- What is the optimal value of $n$? 


Costs:
- '''daily order cost''': how much we pay on average ''per day'' for ordering items
  - it's the cost of ordering divided by $T$ - time to empty the stock
  - $\text{doc}(n) = \cfrac{c_f}{T} = c_f \cdot \cfrac{\lambda}{n}$
- '''daily storage cost''': how much we pay on average ''per day'' for keeping items
  - this is the total # of items we store divided by $T$
  - total # of items is the square of our triangle 
  - <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/de/im/em-basic-eoq-dailycos.png" alt="Image">
  - $\text{dsc}(n) = \underbrace{\{\color{red}\{S_{\triangle}\}\} \cdot \cfrac{1}{T}}_\text{avg items per day} \cdot c_s$
  - $\text{dsc}(n) = \{\color{red}\{\cfrac{n \cdot T}{2}\}\} \cdot \cfrac{1}{T} \cdot c_s = \cfrac{n}{2} \cdot c_s$
- total cost:
  - $\Gamma(n) = \text{doc}(n) + \text{dsc}(n) = c_f \cdot \cfrac{\lambda}{n} + \cfrac{n}{2} \cdot c_s$


Optimization 
- to optimize the cost w.r.t. $n$ we calculate the derivative $\Gamma'(n)$
- $\Gamma'(n) = - \cfrac{\lambda \cdot c_f}{n^2} + \cfrac{c_s}{2} = 0$
- $ \cfrac{n^2}{c_f \cdot \lambda} = \cfrac{2}{c_s} $
- $\tilde{n} = \sqrt{\cfrac{2 \cdot c_f \cdot \lambda}{c_s} }$



### EOQ with Gradual Replenishment
Now consider a model where stock is not replenished immediately:
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/de/im/em-grad.png" alt="Image">
- new parameters:
  - $V$ - speed of filling the stock, items per day ($V > \lambda$)
  - so the order is fulfilled in $\cfrac{n}{V}$ days

Calculations
- period $T$
  - the peak is reached in $\frac{n}{V}$ days
  - but at this day $\frac{n}{V} \cdot \lambda$ items were already sold (a)
  - so the height of the peak is $(n - \frac{n}{V} \cdot \lambda)$ items 
  - to sell these items up we need $[n - \frac{n}{V} \cdot \lambda] / \lambda$ days (b)
  - the total period $T$ is: (a) time to reach the peak + (b) time till the end
  - $T = {\color{grey}{(a)}} \ \cfrac{n}{V} +  {\color{grey}{(b)}} \  \cfrac{n}{\lambda} - \cfrac{n}{V}$
  - $T = \cfrac{n}{\lambda}$
- '''daily order cost'''
  - the same as before
  - $\text{doc}(n) = \cfrac{c_f}{T} = c_f \cdot \cfrac{\lambda}{n}$
- '''daily storage cost'''
  - this is the total # of items we store divided by $T$
  - total # of items is the square of our triangle 
  - <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/de/im/em-basic-stcost.png" alt="Image">
  - the peak is $n - \cfrac{n}{V} \cdot \lambda = n \cdot \cfrac{V - \lambda}{V}$
  - $S_{\triangle} = T \cdot \cfrac{V - \lambda}{V} \cdot {n}{2}$
  - $\text{dsc}(n) = c_s \cdot \cfrac{S_{\triangle}}{T} = c_s \cdot \cfrac{V - \lambda}{V} \cdot \cfrac{n}{2}$
- total cost:
  - $\Gamma(n) = \text{doc}(n) + \text{dsc}(n) = c_f \cdot \cfrac{\lambda}{n} + c_s \cdot \cfrac{V - \lambda}{V} \cdot \cfrac{n}{2}$


Optimization
- to optimize the cost w.r.t. $n$ we calculate the derivative $\Gamma'(n)$
- $\Gamma'(n) = - \cfrac{\lambda \cdot c_f}{n^2} + c_s \cdot \cfrac{V - \lambda}{2 \cdot V} = 0$
- $\cfrac{c_t \cdot \lambda}{n^2} = \cfrac{c_s (V - \lambda)}{2 V} $
  - $\cfrac{n^2}{c_t \cdot \lambda} = \cfrac{2 V}{c_s (V - \lambda)} $
  - $n^2 = 2V \cdot \cfrac{c_t \cdot \lambda}{c_s (V - \lambda)} $
- $\tilde{n} = \sqrt{2V \cdot \cfrac{c_t}{c_s} \cdot \cfrac{\lambda}{V - \lambda} }$


### EOQ with Planned Storage
Suppose now there's a delay with refilling: $T_s$
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/de/im/em-plst.png" alt="Image">
  - refill itself happens immediately, but there's some delay before it can happen 
  - so customers come and say that "we will buy these items when you have them" 
  - which is why the number of items can go down 0 - they are still sold
- variables
  - $n$ - number of items in one order
  - $p$ - number of items that we sell in advance 
  - so now we have two variables|   |- parameters  |  - $\lambda$ - demand
  - $c_s$ - cost of storing
  - $c_f$ - cost of ordering
  - $c_p$ - cost of postponing the refill for each item that is delayed
  - $T_s$ - time span with positive amount of goods
  - $T_p$ - time span with negative amount of goods (they have not yet arrived yet)
  - so $T_p$ - delay before refilling the stock


Calculations 
- $T = T_s + T_p$ - the whole period (i.e. time between two orders)
  - $T_s = \cfrac{n - p}{\lambda}$ - # of days before no items left
  - $T_p = \cfrac{p}{\lambda}$ - # of days before the next refill
  - $T = \cfrac{n - p}{\lambda} + \cfrac{p}{\lambda} = \cfrac{n}{\lambda}$
- '''daily order cost'''
  - the same as before
  - $\text{doc}(n) = \cfrac{c_f}{T} = c_f \cdot \cfrac{\lambda}{n}$
- '''daily storage cost'''
  - <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/de/im/em-plst-sim-triangles.png" alt="Image">
  - the store items only during $T_s$, when we at $T_p$ there's nothing to store
  - $S_{\color{blue}{\blacktriangle}} = \cfrac{(n - p) \cdot T_s}{2}$ 
  - $\text{dsc}(n, p) = S_{\color{blue}{\blacktriangle}} \cdot \cfrac{1}{T}$
  - note that since the blue triangle and the big orange triangle are similar $\cfrac{T_s}{T} = \cfrac{n-p}{n}$
  - so we have $\text{dsc}(n, p) = c_s \cdot S_{\color{blue}{\blacktriangle}} \cdot \cfrac{1}{T} = c_s \cdot \cfrac{(n - p) \cdot {\color{blue}{T_s}}}{2} \cdot {\color{blue}{\cfrac{1}{T}}} = c_s \cdot \cfrac{(n - p)^2}{2n}$
- '''daily postponing cost'''
  - the average cost of postponing per day 
  - this is the square of the red triangle
  - $S_{\color{red}{\blacktriangle}} = \cfrac{p \cdot T_p}{2}$
  - $\text{dpc}(n, p) = S_{\color{red}{\blacktriangle}} \cdot \cfrac{1}{T}$
  - since the red triangle and the big orange one are similar, $\cfrac{T_p}{T} = \cfrac{p}{n}$
  - so we have $\text{dpc}(n, p) = S_{\color{red}{\blacktriangle}} \cdot \cfrac{1}{T} = c_p \cdot \cfrac{p \cdot {\color{red}{T_p}}}{2} \cdot {\color{red}{\cfrac{1}{T}}} = c_p \cdot \cfrac{p^2}{2n}$
- the total cost is the sum of all these costs:
  - $\Gamma(n, p) = \text{doc}(n) + \text{dst}(n, p) + \text{dpc}(n, p) = c_f \cdot \cfrac{\lambda}{n} + c_s \cdot \cfrac{(n - p)^2}{2n} + c_p \cdot \cfrac{p^2}{2n}$


Optimization 
- we need to optimize $\Gamma(n, p)$ w.r.t. both $n$ and $p$
- $\cfrac{\partial \Gamma(n, p)}{\partial p} = - c_s \cdot \cfrac{n - p}{n} + c_p \cdot \cfrac{p}{n} = 0$
  - $-c_s \cdot n + c_s \cdot p + c_p \cdot p = 0$
  - $p \cdot (c_s + c_p) = n \cdot c_p $
  - $\tilde{p} = \cfrac{c_s}{c_s + c_p} \cdot \tilde{n} $
- $\cfrac{\partial \Gamma(n, p)}{\partial n} = - c_f \cdot \cfrac{\lambda}{n^2} + \cfrac{c_s}{2} \cdot \cfrac{n^2 - p^2}{n_2} - c_p \cdot \cfrac{p^2}{2n^2} = 0$
  - $- 2 \lambda c_f + (n^2 - p^2) c_s - p^2 c_p = 0$
  - $- 2 \lambda c_f + n^2 c_s - p^2 c_s - p^2 c_p = 0$
  - $- 2 \lambda c_f + n^2 c_s - p^2 (c_s + c_p) = 0$ (replace $p$ with the value of $\tilde{p}$)
  - $- 2 \lambda c_f + n^2 c_s - \cfrac{c^2_s}{c_s + c_p} \cdot n^2 = 0$
  - $c_s n^2 \left(1 - \cfrac{c_s}{c_s + c_p}\right) = 2 \lambda c_f$
  - $c_s n^2 \cfrac{c_p}{c_s + c_p} = 2 \lambda c_f$
  - $n^2 = \cfrac{2 \lambda c_f}{c_s} \cdot  \cfrac{c_s + c_p}{c_p}$
  - $\tilde{n} = \sqrt{\cfrac{2 \lambda c_f}{c_s} \cdot  \cfrac{c_s + c_p}{c_p}}$



## Sources
- [Decision Engineering (ULB)](Decision_Engineering_(ULB))
