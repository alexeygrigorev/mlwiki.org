---
title: "Negative Binomial Distribution"
layout: default
permalink: /index.php/Negative_Binomial_Distribution
---

# Negative Binomial Distribution

## Negative Binomial Distribution
The negative binomial distribution is a Discrete [Distribution](Distribution) of [Random Variable](Random_Variable)s
- [Geometric Distribution](Geometric_Distribution): probability of observing first success on $n$th trial 
- NBD: probability of observing $k$th success on $n$th trial 
- so NBD is a generic case of Geometric Distribution


A distribution is NBD if:
- trials are independent 
- each trial is a [Bernoulli Trial](Bernoulli_Trial) - i.e. has only two outcomes - success and failure
- $p$ is the same for all the trials
- the last trial must be success 


NBD:
- $k$ - number of successes, $n$ - total number of trials
- $p$ - probability of success, $q = 1 - p$ - probability of failure
- [pmf](Probability_Mass_Function): $Pr(X = x) = C^{k-1}_{n-1} q^{n-k} p^{k}$




## Example
### Example 1
A footballer can go home only after he scores 4th goal 
- $p$ - probability of success 

Suppose he made 6 attempts 
- what's the probability that he scored 4 goals, and <u>the last trial led to success</u>?

Let's write down all possible sequences when the 4th kick is on the 6th attempt:

```python
from itertools import permutations
p = set([x for x in permutations('SSSSFF')])
[x for x in p if x[-1] == 'S']
```

|   1   |  F  |  S  |  S  |  F  |  S  |  S ||   2   |  S  |  S  |  F  |  S  |  F  |  S ||   3   |  S  |  F  |  F  |  S  |  S  |  S ||   4   |  F  |  F  |  S  |  S  |  S  |  S ||   5   |  F  |  S  |  F  |  S  |  S  |  S ||   6   |  S  |  F  |  S  |  S  |  F  |  S ||   7   |  S  |  F  |  S  |  F  |  S  |  S ||   8   |  S  |  S  |  F  |  F  |  S  |  S ||   9   |  S  |  S  |  S  |  F  |  F  |  S ||   10   |  F  |  S  |  S  |  S  |  F  |  S |

There are 10 sequences that lead to this outcome 
- note that Success is always last|   | |Let's calculate the probability of going home after 6 kicks (having 6th kick successful)
- so $P(\text{go home}) = \sum_{i=1}^{10} P(\text{seq}_i)$
- each sequence has the same probability of occurring:
  - $P(\text{seq}_i) = P(\text{seq}) = q^{n-k} p^{k}$
  - this is the probability of observing $n-k$ failures and $k$ successes
- there are ${n - 1 \choose k - 1}$  ways to pick these elements ($C_{n - 1}^{k - 1}$)


## Sources
- [OpenIntro Statistics (book)](OpenIntro_Statistics_(book))
- https://en.wikipedia.org/wiki/Negative_binomial_distribution


[Category:Probability](Category_Probability)
[Category:Distributions](Category_Distributions)