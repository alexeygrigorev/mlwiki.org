---
layout: default
permalink: /index.php/Budget_Pacing
tags:
- adtech
- machine-learning
title: Budget Pacing
---
## Budget Pacing
Budget pacing control:
- take the daily budget as input
- calculate the delivery schedule
- based on the schedule, DSP tries to spread the actions throughout the day

Notation:
- $n$ ad requests 
- $x_i = \{0, 1\}$, decision whether to bid on $i$ or not
- $v_i$ - value if we win on $i$ and show it to user
- $c_i$ - cost of showing $i$ 
- $\hat{c}_i$ - how much we are willing to bid
  - for second price option, $\hat{c}_i = c_i + \epsilon_i$, and $\epsilon_i$ is unknown to the bidder at bid time
- $B$ total budget, allocated in $T$ slots $b_t$ s.t. $\sum b_t = B$

Goal:
- maximize $\sum v_i x_i$
- s.t. $\sum_j c_j x_j \leqslant b_t$ for all $j$ of $b_t$ 


## Optimization
Metrics: 
- eCPC or eCPA, want to minimize them 

More notation:
- let  $s(t) = \sum c_j x_j$ - how much we actually spent during $t$ 
- want $\sum s(t)$ be as close to $B$ as possible
- and $s(t)$ to be close to $b_t$ 


Assumption: 
- $s(t)$ is proportional to the number of impressions served at the time
- it means that the price of individual impressions are approximately the same during this time slot
- the length of the time slot can be chosen s.t. this assumption is not violated

### Setting Bid Rate

For each ad spot for time $t$ we assign a bid rate (pacing rate): 
- $s(t)$ is proportional to number of impressions served
- $\text{requests}(t)$: # of received bid requests
- $\text{bids}(t)$: # of times we decided to bid
- $\text{imps}(t)$: # of shown impressions at $t$
- $\text{bid_rate}(t)$: rate at which we decide to bid on the request
  - $\text{bid_rate}(t) = \text{bids}(t) \, / \, \text{requests}(t)$
- $\text{win_rate}(t)$: rate at which we win the bid
  - $\text{win_rate}(t) = \text{imps}(t) \, / \, \text{bids}(t)$
- $s(t) \sim \text{request}(t) \cdot \text{bid_rate}(t) \cdot \text{win_rate}(t)$

So we can control $s(t)$ by changing our $\text{bid_rate}(t)$

Changing bid_rate:

Adjusting bid rate for slot $t+1$:
- take feedback from slot $t$ 
- use this for $t+1$ 

we can control $\text{bid_rate}(t+1)$


### Budget Schedule
Selecting $b_t$
- uniform - not the best one
- traffic is different during each hour
- should allocate more budget for periods with better quality traffic
- i.e. to the time where the target audience is more active

History-based:
- for each $b_t$ calculate $p_t$ 
- $p_t$ is probability of success (click or conversion)
- $\sum p_t = 1$ 

so, ideal spending for the next time slot can be calculated as 

$$\left(B - \sum_{m=1}^{t} s(m) \right) \cdot \cfrac{p_{t+1}}{\sum_{m=t+1}^{T} p_m}$$

two parts
- remaining budget: how much money we still have
- how good is the next slot compared to all other remaining slots

note that if $p_t = 0$ for some $t$, the system will never explore this time slots, so should always give it some chance 

Once we calculate the desired bid rate, we can 
- select top quality ad requests to bid on
- choose the price we are willing to bid for these requests 


### Selecting Good Quality Ad Requests
for each impression $i$ we can choose the price to bid with

construct bidding histogram $c^*$
- this is historical average of costs $c_i$ in $b_t$ 
- now we know which $b_t$ is cheapest
- take base price and scale it up/down considering bid rate 

### Bid Price
bid_rate vs bid_price:
- bid_rate controls the frequency of bidding 
- but bid price is important
- if it's not high enough, we don't win the impression
- if it's too high, CPA rises


bid price adjustments
- split requests into 3 groups based on bid rate:
- define $\beta_1$, $\beta_2$ s.t. $0 < \beta_1 < \beta_2 < 1$

bid_rate can be in one of these 3 groups:
- safe: $0 < br \leqslant \beta_1$, no delivery issues
- critical: $\beta_1 < br \leqslant \beta_2$, normal delivery
- danger: $\beta_2 < br \leqslant 1$ and cannot win enough impressions

Let $u_i$ be the base bid price however set based on CTR/AR model
- (AR - action rate or conversion rate)


Safe region: learning $\hat{c}_i$ 
- look at submitted bid price $\hat{c}_i$ and actual price $c_i$ 
- let $\theta_i = c_i \, / \, \hat{c}_i$
- build a histogram of $\theta_i$, choose $\theta^*$ as the bottom 1-2 percentile
- submit $\hat{c}_i = \theta^* \cdot u_i$

Critical region:
- bid $\hat{c}_i = u_i$ 

Danger region:
- Reasons for being in this region:
- audience is too specific, not enough bid requests that satisfy all the criteria 
- bid price is too low to win impressions 
- Can increase the bid price by some coefficient $\rho \geqslant 1$


## Models
### Estimation of CTR/AR
Why estimate AR?
- to predict the quality of an ad request
- to set the bid price: e.g. AR * CPA goal 

Ways to do it:
- [Hierarchical Bandits](Hierarchical_Bandits)
- [Logistic Regression](Logistic_Regression)
- [Factorization Machines](Factorization_Machines)


## Problems
### Cold Start Problem
Ideas:
- use content features for models to estimate CTR/AR
- epsilon-greedy strategy for online bid optimization


### Overspending
Because of unusual unexpected activity spikes we might spend all the budget earlier than expected 

solution:
- monitor total spend and stop the campaign when we spend more than B
- monitor spend at $t$ and allow to spend no more than $b_t + \delta$, and pause until $t+1$ if the limit is exceeded 


### System

 Ad request -> check bid rate -> evaluate CTR/AR -> bid -> ...
 ... -> SSP -> ...
 ... -> bid log with win -> save to db
 db <-> train CTR/AR models
    <-> compute good bid rate


## Sources
- Real Time Bid Optimization with Smooth Budget Delivery in Online Advertising: https://arxiv.org/abs/1305.3011
