---
title: Hamilton's Method
layout: default
permalink: /index.php/Hamilton's_Method
---

# Hamilton's Method

## Hamilton's Method
This is a [Parliamentary Allocation](Parliamentary_Allocation) method, also known as the ''Largest Remainder method'' with the ''Hare Quota''.

The task is:
- given 
  - $p_i$ - the number of voters in favor of party $i$ 
  - $N$ - total number of parties, $i \in \{ 1, 2, ..., N\} \equiv P$
  - $n$ - total number of voters
  - the quota of $i$ is $q_i = S \cdot \cfrac{p_i}{n}$. Note that $q_i$ is a read number, not integer
- allocate $S$ seats in parliament
  - $(s_1, ..., s_N)$ s.t. $\sum s_i = S$
  - $s_i$ must be an integer

So $s_i$ should be either $\lfloor q_i \rfloor$ or $\lfloor q_i \rfloor + 1$
- it's always integer, so we either round down or up

Rule:
- initially allocate $\lfloor q_i \rfloor$ seats 
- then order all parties by their decimal part of the quota 
- the party with the highest decimal part gets the seat

Formally,
- $\forall i, j \in P: s_i = \lfloor q_i \rfloor + 1 \land s_j = \lfloor q_j \rfloor \iff q_i - \lfloor q_i \rfloor \geqslant q_j - \lfloor q_j \rfloor$ 
- $i$ gets the additional seat if its decimal part is larger than $j$'s 


### Example
$S = 10$ 

|    |  $p_i$  |  $q_i$  |  $\lfloor q_i \rfloor$  |  $s_i$  |  $P_1$  |  6373  |  6.373  |  6  |  6  ||  $P_2$  |  2505  |  2.505  |  2  |  2  ||  $P_3$  |  602  |  0.602  |  0  |  0 ||  $P_4$  |  520  |  0.520  |  0  |  0  |
There remain 2 places to allocate: $\sum_i s_i = 8, S = 10$
- we order the parties by the decimal part of their quota:
- ${\color{blue}{P_3: 0.602, P_4: 0.520}}, P_2: 0.505, P_1: 0.373$
- so in this case $P_3$ and $P_4$ get the additional seats


|    |  $p_i$  |  $q_i$  |  $\lfloor q_i \rfloor$  |  $s_i$  |  $P_1$  |  6373  |  6.373  |  6  |  6  ||  $P_2$  |  2505  |  2.505  |  2  |  2  ||  $P_3$  |  602  |  0.602  |  0  |  1 ||  $P_4$  |  520  |  0.520  |  0  |  1  |


It's not always possible to split the seats

|    |  $p_i$  |  $q_i$  |  $\lfloor q_i \rfloor$  |  $s_i$  |  $P_1$  |  6373  |  6.373  |  6  |  6  ||  $P_2$  |  2512  |  2.512  |  2  |  ?  ||  $P_3$  |  603  |  0.603  |  0  |  1 ||  $P_4$  |  512  |  0.513  |  0  |  ? |
We have a tie
- ties are broken arbitrarily


## Implementation
### Python & Numpy
```python
def hamilton_allocation(ratios, k):
    frac, results = np.modf(k * ratios)
    remainder = int(k - results.sum())
    
    indices = np.argsort(frac)[::-1]
    results[indices[0:remainder]] += 1
 
    return results.astype(int)
```

ratios here sum up to 1, and k is the total number of seats


## Paradoxes
### Alabama Paradox
At first we have only 7 positions to allocate: $S = 7$


|    |  $p_i$  |  $q_i$  |  $\lfloor q_i \rfloor$  |  $s_i$  |  $P_1$  |  20  |  1.<u>373</u>  |  1  |  2 ||  $P_2$  |  34  |  2.333  |  2  |  2  ||  $P_3$  |  48  |  3.294  |  3  |  3 ||   $\sum$  |   102  |   |  6  |  7 | |
But suddenly we have an additional seat: $S = 8$

|    |  $p_i$  |  $q_i$  |  $\lfloor q_i \rfloor$  |  $s_i$  |  $P_1$  |  20  |  1.569  |  1  |  ${\color{red}{\fbox{1}}}$ ||  $P_2$  |  34  |  2.667  |  2  |  3 ||  $P_3$  |  48  |  3.<u>765</u>  |  3  |  4 ||   $\sum$  |   102  |   |  6  |  7 | |
$P_1$ loses one seat|    |- no [Monotonicity](Monotonicity)|  |- even with one additional vote $P_1$ cannot regain the seat|  | |
|    |  $p_i$  |  $q_i$  |  $\lfloor q_i \rfloor$  |  $s_i$  |  $P_1$  |  21  |  1.631  |  1  |  1 ||  $P_2$  |  34  |  2.641  |  2  |  3 ||  $P_3$  |  48  |  3.<u>728</u>  |  3  |  4 ||   $\sum$  |   103  |   |  6  |  7 | |
This is called the ''Alabama paradox'': increasing in the number of seats causes a party to lose a sit


### Population Paradox
$S=20$

|    |  $p_i$  |  $q_i$  |  $\lfloor q_i \rfloor$  |  $s_i$  |  $P_1$  |  1786  |  9.654  |  9  |  10 ||  $P_2$  |  1246  |  6.719  |  6  |  7 ||  $P_3$  |  671  |  3.627  |  3  |  3 ||   $\sum$  |   3700  |   |  18  |  20 | |
But assume that we have forgotten about additional 65 votes:
- 19 votes for $P_1$
- 40 votes for $P_2$
- and only 6 votes for $P_3$

|    |  $p_i$  |  $q_i$  |  $\lfloor q_i \rfloor$  |  $s_i$  |  $P_1$  |  1805  |  9.588  |  9  |  '''9''' ||  $P_2$  |  1283  |  6.815  |  6  |  7 ||  $P_3$  |  677  |  3.596  |  3  |  '''4''' ||   $\sum$  |   3700  |   |  18  |  20 | |Even though $P_1$ was winning and received more additional votes than $P_3$, $P_3$ takes one seat from $P_1$

So the outcome is not robust and it is possible to manipulate the result.


### Population Transfer Paradox
Shows that [Independence to Third Alternatives](Independence_to_Third_Alternatives) is not satisfies

$S = 5$

|    |  $p_i$  |  $q_i$  |  $\lfloor q_i \rfloor$  |  $s_i$  |  $P_1$  |  14  |  2.593  |  2  |  3 ||  $P_2$  |  10  |  1.667  |  1  |  2 ||  $P_3$  |  3  |  0.556  |  0  |  0 ||   $\sum$  |   27  |   |  3  |  5 | |
Suppose $P_2$ lost one vote, and $P_3$ received this vote:
- That has an impact on $P_1$|   | ||    |  $p_i$  |  $q_i$  |  $\lfloor q_i \rfloor$  |  s_i  |  $P_1$  |  14  |  2.593  |  2  |  '''2''' ||  $P_2$  |  9  |  1.667  |  1  |  2 ||  $P_3$  |  3  |  0.741  |  0  |  1 ||   $\sum$  |   27  |   |  3  |  5 | |
$P_1$ loses one seat, even though its position remained unchanged


## Links
- http://wiki.electorama.com/wiki/Hamilton_method
- http://wiki.electorama.com/wiki/Largest_remainder_method + the Hare Quote
- http://wiki.electorama.com/wiki/Alabama_paradox
- Alabama and Population Paradoxes http://en.wikipedia.org/wiki/Apportionment_paradox

## See also
- [Jefferson's Method](Jefferson's_Method)

## Sources
- [Decision Engineering (ULB)](Decision_Engineering_(ULB))

[Category:Voting Theory](Category_Voting_Theory)