---
title: Banzhaf Power Index
layout: default
permalink: /index.php/Banzhaf_Power_Index
---

# Banzhaf Power Index

## Banzhaf Power Index
''Coalition'' is a group of people/parties that need to achieve some quota when voting for a law. Otherwise this law will not pass. 

The ''Banzhaf Power Index'' shows how strong a party is.


Suppose we have a company with 200 shares in total. 

There are three shareholders: 
- $D$ Doug: 101 shares,
- $N$ Nicolas: 97 shares,
- $E$ Elizabeth: 2 shares

For a decree to pass it should have 103 shares

Is $N$ 48 times more important then $E$? To assess the importance we use the Banzhaf index:


### The Power Index
Critical Voter:
- A coalition is ''winning'' if it has enough power to pass a low/decree/whatever. 
- A voter in a winning coalition is ''critical'' if his withdrawal causes the coalition to become a loosing coalition 

Example:
- there are $2^3$ coalitions in total, and $3$ of them are winning
- $\{D, E\}$
  - 103 votes - this is a winning coalition
  - $E$ is a critical voter: if she withdraws, the coalition is no longer winning
  - $D$ also is a critical voter
- $\{D, N\}$
  - both $D$ and $N$ are critical
- $\{D, N, E\}$ ([Unanimity](Unanimity))
  - everybody agrees: 200 votes
  - $D$ and $N$ are critical voters
  - but now $E$ is not: if she withdraws, the coalition is still winning


The Power: 
- The ''Banzhaf Power'' $BP(a)$ of a voter $a$ is the number of winning coalitions in which $a$ is critical. 
- The ''Total Banzhaf Power'' of a voting game is the sum of all Bahnzaf powers of all voters: $TBP = \sum_{a} BP(a)$
- The ''Banzhaf Index'' of a voter $a$ is $\cfrac{BP(a)}{TBP}$


Example:
|   Voter  |  $BP$  |  Index  |  $D: 101$  |  3  |  3/5 ||  $N: 97$  |  1  |  1/5 ||  $D: 101$  |  1  |  1/5 ||   |  $TBP = 5$  |   |
So we see that both $N$ and $E$ are equally important, even though they don't have the same number of shares.


## Example: Nassau County
Consider the following districts:
|    |  District  |  Weight  |  (1)  |  Hempstead 1  |  31 ||  (2)  |  Hempstead 2  |  31 ||  (3)  |  Oyster Bay  |  28 ||  (4)  |  North Hempstead  |  21 ||  (5)  |  Long Beach  |  2 ||  (6)  |  Glen Cove  |  2 |
The threshold for a law to pass is $Q=58$

In this example all the power in equally distributed withing the 3 first districts (1), (2) and (3). 
- any 2 of these 3 always form a winning coalition
- no other two districts can form such a winning coalition



## Links
- http://en.wikipedia.org/wiki/Banzhaf_power_index

## See also
- [Shapley Value](Shapley_Value)

## Sources
- [Decision Engineering (ULB)](Decision_Engineering_(ULB))

[Category:Voting Theory](Category_Voting_Theory)