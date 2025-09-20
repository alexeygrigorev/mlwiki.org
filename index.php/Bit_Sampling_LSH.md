---
layout: default
permalink: /index.php/Bit_Sampling_LSH
tags:
- database-indexes
- hashing
- lsh
title: Bit Sampling LSH
---
## Bit Sampling LSH
- LSH for the [Hamming Distance](Hamming_Distance)
- can convert [$L_1$](Manhattan_Distance) to Hamming distance
- NNs are usually the same for $L_1$ and [$L_2$](Euclidean_Distance) 
  - see Figiel et al. "The dimension of almost spherical sections of convex bodies." 1977. [http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.308.2113]
- so it can be ("sort of") used for Euclidean spaces


### Hamming LSH
Suppose we have $P = \{ \mathbf p_i \}$ where $\mathbf p_i \in H^{d} = \{0, 1\}^{d}$ - i.t. points are in the (binary) [Hamming Space](Hamming_Space) of dimensionality $d$ (or $Cd$, in $C$ chunks of size $d$)


Hash Functions
- sample $L$ subsets $I_1, \ ... \ , I_L$ of size $k$ uniformly (with replacement) from \{1 \ ... \ d \}$
- let $g_j(\mathbf p)$ be the projection of $\mathbf p$ on $I_j$: it selects coordinate positions per $I_j$ and concatenates bits on these positions


### Indexing
Preprocessing (indexing):
- store each $\mathbf p \in P$ in the bucket $g_j(\mathbf p)$ for all $j = 1 \, .. \, L$
- total number of resulting buckets may be large ($g_j(\mathbf p)$'s are sparse), so reduce the desparsify and reduce dimensionality using usual hashing


So have two levels of hashing:
- LSH Hash to map $\mathbf p$ to bucket $g_j(\mathbf p)$
- standard hash function to map $g_j(\mathbf p)$ to a hash table of size $M$ 


Pseudocode:
- Input: database $P$, number of hash tables $L$
- Output: $L$ hash tables $\tau_j$
- generate $L$ random hash functions $g_j(\cdot)$  - for each $\tau_j$
- for each $\mathbf p_i \in P$ and for each $(g_j, \tau_j)$:
- $\tau_j\big[ g_j(\mathbf p_i) \big] = \mathbf p_i$



### Querying
Querying: 
- given $\mathbf q$ 
- search all buckets $g_j(\mathbf q)$ until:
- either encounter $c \cdot L$ points ($c$ to be specified)
- or checked all $L$ indexes
- then for all candidates keep only $K$ closest


Pseudocode:
- input: 
  - a query point $\mathbf q$, 
  - number of nearest neighbors $K$,
  - $L$ tables $\tau_i$ 
- output: $K$ (or less) NNs
- let $S \leftarrow \varnothing$ be a candidate list
- for each  $(g_j, \tau_j)$
  - $S \leftarrow S \cup \tau_j \big[ g_j(\mathbf q) \big]$
- return $K$NNs from $S$ (can be found using linear search)


### Parameters
- $L$: number of subsets $I_j$'s and hence the # of hash functions
- $k$: size of $I_j$'s: $k$ is chosen s.t. 
  - it maximizes the probability that if $\mathbf p$ is close to $\mathbf q$, then they must end up in the same bucket
  - it minimizes the prob that if $\mathbf p$ and $\mathbf q$ ending up in the same bucket when $\mathbf p$ is not close to $\mathbf q$
  - $k \approx 700$ is a good value for $d \approx 64$ 


### Embedding $L_1$ to Hamming
For converting from $L_1$ to Hamming:
- All $\mathbf p \in P$ are positive integers 
- coordinates may be made all-positive by translating the origin


Let $C$ be the largest coordinate in all points in $P$
- then we can embed $P$ into a Hamming cube $\{0, 1\}^{Cd}$ where $d$ is the dimensionality of the original space

- transform each $\mathbf p = (p_1, \ ... \ , p_d$ into a binary vector:
- let $v(\mathbf p) = \big( \text{unary}_C(p_1), \ ... \ , \text{unary}_C(p_d) \big)$
- $\text{unary}_C(p)$ denotes the binary representation of $p$: a sequence of $p$ ones followed by $C - p$ zeros
- e.g. for $C = 10$ and $p = 4$, we'd have $\text{unary}_{10}(4) = 11110 \, 00000$
- for a vector $\mathbf p = (3, 4, 5)$ we would have $v(\mathbf p) = ( 11100 \, 00000 \, 11110 \, 00000 \, 11111 \, 00000 )$


Now, 
- if $\mathbf p, \mathbf q \in \{1 \, .. \, C \}$ 
- then $d_1 \big(\mathbf p, \mathbf q \big) = d_H \big(v(\mathbf p), v(\mathbf q) \big)$
- i.e. this embedding preserves the $L_1$ distance between points



Mapping $\mathbf p \in \mathbb R^d$ to $\mathbf p' \in H^{Cd}$: (effective hashing calculation)
- choose $I$: a $k$-vector of indexes sampled from $\{0, \, .. \, C \}$
- we need to compute a projection on $I$
- for each component $p_i$ of $\mathbf p$ do:
  - let $I^{(i)}$ denote coordinates of $I$ that correspond to $p_i$ 
    - these are some of the $C$ coordinates of $p_i$ in the Hamming embedding that got selected in $I$
  - order indexes inside $I^{(i)}$
  - when we project $\mathbf p$ on $I^{(i)}$, the result is a monotone sequence of bits: there are 1's followed by 0's 
  - let $o_i$ be the number of 1's of $p_i$
  - let $\mathbf p'_i$ denote the part of $\mathbf p'$ that corresponds to coordinate $p_i$
  - so, to represent $\mathbf p'_i$ it's enough to know only $o_i$ 
- thus $\mathbf p'$ can be represented by $\{o_1, o_2, \ ... \ , o_d \}$


Computing $o_i$ fast:
- there's a way to compute $o_i$ fast
- finding $o_i$ is equivalent to finding the number of elements in sorted array $I^{(i)}$ which are smaller than $p_i$
- can be done via Binary Search in $O(\log C)$
- or even in constant time if we use a precomputed array of $C$ bits 


Total projection time
- then total time to project $\mathbf p$ to $\mathbf p'$ is 
- $O(d \, \log C)$ for Binary Search or
- $O(d)$ for precomputed arrays



## Sources
- Gionis, Aristides, Piotr Indyk, and Rajeev Motwani. "Similarity search in high dimensions via hashing." 1999. [http://www.cs.princeton.edu/courses/archive/spring13/cos598C/Gionis.pdf]
