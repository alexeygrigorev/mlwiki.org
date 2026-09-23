---
layout: default
permalink: /Permutations_with_Replacement
tags:
- probability
- combinatorics
title: Permutations with Replacement
---

## Permutations with Replacement

This case occurs when we wish to select k objects with replacement from a population of n objects and selection order is distinguished. Replacement implies that the same object could be selected multiple times. What is required is to count the number of distinct sets of k objects could be selected in this way. We can view this selection process by considering the ways in which each of the positions, $1,\dots ,n$, of the set are filled. Note that there are n choices in the population to fill the first position, and since the object selected for this first position is then returned to the population, there are n choices available for the second selection as well. Therefore, there are $n^2$ ways to fill the first two positions. Continuing this argument, we can see that there are $n^k$ ways to select k objects with replacement from a population of n distinguishable objects. 

https://www.utdallas.edu/~ammann/stat3355/node14.html
