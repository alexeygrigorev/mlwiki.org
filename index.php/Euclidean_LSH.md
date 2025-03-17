---
title: Euclidean LSH
layout: default
permalink: /index.php/Euclidean_LSH
---

# Euclidean LSH

## Euclidean LSH
Euclidean LSH - [LSH](LSH) for the [Euclidean Space](Euclidean_Distance)
- Also called E2LSH or $p$-stable LSH
- Unlike [Bit Sampling LSH](Bit_Sampling_LSH) this LSH Family words directly on $L_p$ without embedding it into [Hamming Space](Hamming_Distance)


## $p$-Stable Distributions
A family of hash functions $\mathcal H$ is $(r_1, r_2, p_1, p_2)$-sensitive if 
- for all $\mathbf p, \mathbf q$
- if $\mathbf p \in B(\mathbf q, r_1)$ then $P_{\mathcal H} \Big[ h(\mathbf q) = h(\mathbf p)  \Big] \geqslant p_1$
- if $\mathbf p \not \in B(\mathbf q, r_2)$ then $P_{\mathcal H} \Big[ h(\mathbf q) = h(\mathbf p)  \Big] \leqslant p_2$

Here: choose $r_1 = R$ and $r_2 = c \cdot R$


A [Probability Distribution](Probability_Distribution) $D$ over $\mathbb R$ is $p$-stable 
- if there exists $p \geqslant 0$ s.t. for any $n$ real numbers $v_1, ..., v_n$
- and iid samples from distribution $D$: $\ X_1, X_2, \ ... \ , X_n \sim D$
- the [Random Variable](Random_Variable) $\sum v_i \, X_i$ follows the same distribution as $\left( \sum | v_i|^p \right)^{1/p} \cdot X = \| \mathbf v \| \cdot X$ where $X \sim D$ |

Known $p$-stable Distribution:
- [Cauchy Distribution](Cauchy_Distribution) for $p = 1$
- [Gaussian Distribution](Gaussian_Distribution) for $p = 2$ 

In CS $p$-stable distributions are useful for [Sketching](Sketching)
- can be used to estimate $\|  \mathbf v \|_p$ |

Papers:
- Nolan, J. "Stable distributions." 2009. [[http://academic2.american.edu/~jpnolan/stable/chap1.pdf](http://academic2.american.edu/~jpnolan/stable/stable.html])
- Indyk, Piotr. "Stable distributions, pseudorandom generators, embeddings, and data stream computation." 2006. [http://old-madalgo.au.dk/img/SumSchoo2007_Lecture%20slides/Bibliography/p3-Indyk_JACM_06.pdf]


## E2 LSH
A hash function family is ''locality-sensitive'' if 
- "similar" $\mathbf v_1, \mathbf v_2$ - i.e. have small $\|  \mathbf v_1 - \mathbf v_2 \|_p$  |- they should collide: have same hash value with high probability


Consider $\mathbf a \cdot \mathbf v$ - it's a projection of $\mathbf v$ to a real line 
- it follows from the $p$-stability that for two $\mathbf v_1, \mathbf v_2$ distance between the projections $\mathbf a \cdot \mathbf v_1 - \mathbf a \cdot \mathbf v_2$ is distributed as $\|  \mathbf v_1 - \mathbf v_2 \|_p \cdot X$  |- so if we chop the real line into equi-width segments of $w$, then the hash functions should be locality-preserving


### Random Projections
The [Dot Product](Dot_Product) is a projection 
- this is at the core of LSH
- let $\mathbf v$ be the query and $\mathbf x$ some random vector with each $x_i \sim N(0, 1)$ (components of $\mathbf x$ are sampled from the [Normal Distribution](Normal_Distribution)) 
- the hash function is then defined as $h(\mathbf v) = \mathbf v \cdot \mathbf x$

Quantization:
- then we quantize $h(\mathbf v)$ into a set of hash buckets - hoping that nearby items will fall into the same bin
- i.e. we get the following hash function:
- $h_{\mathbf x, b}(\mathbf v) = \left\lfloor \cfrac{\mathbf v \cdot \mathbf x + b}{w} \right\rfloor$
- where $w$ is the length of each quantization bucket
- and $b$ is a [Random Variable](Random_Variable) sampled from the [Uniform Distribution](Uniform_Distribution): $b \sim \text{unif}[0, w]$
- $w$ - quantization step


Requirements for the projection operator
- let $\mathcal H$ be a family of LSH functions
- for any $\mathbf p, \mathbf q \in \mathbb R^d$ that are close to each other, i.e. for $\| \mathbf p - \mathbf q \| \leqslant R_1$ |- probability that they end up in the same bucket should be high, i.e. $P_{\mathcal H} \Big[ h(\mathbf p) = h(\mathbf q) \Big] \geqslant p_1$ 
- if $\mathbf p, \mathbf q$ are far apart, i.e. $\| \mathbf p - \mathbf q \| \geqslant R_2$ |- probability that they end up in the same bucket is low, i.e. $P_{\mathcal H} \Big[ h(\mathbf p) = h(\mathbf q) \Big] \leqslant p_2$


I.e. $\|  h(\mathbf p) - h(\mathbf q) \| \sim \| \mathbf p - \mathbf q \|$ ($\sim$ = "distributed proportionally to") |


### $L$ Random Projections
Can magnify the difference between $P_1$ and $P_2$ by performing projection on $K$ random directions in parallel

$\left( \cfrac{p_1}{p_2} \right)^K > \cfrac{p_1}{p_2}$


- So given a query $\mathbf v$ apply $K$ individual dot products
- and obtain $K$ real numbers $h_i (\mathbf v) \in \mathbb R$ (all quantified - i.e. put into buckets - separately)
- so $H(\mathbf v) = \Big[ h_1(\mathbf v), h_2(\mathbf v), \ ... \ , h_K(\mathbf v) \Big] \in \mathbb R^K$


Now we say that $\mathbf u$ is a NN candidate for $\mathbf v$ if they end up in the same bucket, i.e. $H(\mathbf u) = H(\mathbf v)$ (for all $h_i(\cdot)$)


Note that for $K$ dot products the probability of having the same bucket is $p_1^K$ - which decreases as we increase $K$
- to reduce this effect form $L$ independent projections - i.e. we'll have $L$ hash functions $H_1, \ ... \ , H_L$
- then $\mathbf u$ is a candidate if it ends up in the same bucket as $\mathbf v$ for at least one projection $H_i$
- it's very unlikely that the true NN will be absent in all $L$ bins


### Hash Implementation
(E2 LSH)

$\{ H_i \}$ put each data point into a hash bucket described by $K$-vector 
- this $K$-dim space is very sparse - can densify it 
- use exact hashes - i.e. "classical" [Hash Tables](Hash_Tables) for this
- so let $T_1(\mathbf v) = \mathbf w_2^T H(\mathbf v)  \ \mod P_1$ for some random weight vector $\mathbf w$ and a big prime number $P_1$ (which is also the size of the hash table)


Unrelated points may collide to the same bucket 
- how to handle it? 
- have another function $T_2$ with different weights $\mathbf w_2$ and $P_2$
- let $T_2(\mathbf v)$ be the "fingerprint" of $\mathbf v$ 
- we store the fingerprint of $\mathbf v$ in the bin chosen by $T_1$
- then during retrieval we can find the true match by comparing fingerprints: they are short and their comparison is fast
- chances that both $T_1$ and $T_2$ collide are very small


Accuracy 
- accuracy is determined by the probability it will find the true NN


### $p$-Stable Distributions
A distribution is $p$-stable if 
- for iid sample $X_1, \ ... \ , X_n \sim D$
- for any $v_1, \ ... \ , v_n \in \mathbb R$ 
- $\sum v_i \, X_i$ follows the same distribution as the random variable $\left( \sum_i \| v_i \big \|_p \right)^{1 / p} \cdot X$ |- where $\|  \, \cdot \, \|_p$ is $L_p$ norm |- and $X \sim D$
- [PDF](Probability_Density_Function) of this RV is $f_p$


For $p=2$ Gaussian is $p$-stable

What it means:
- $\mathbf u = \|  \mathbf p - \mathbf q \|$ will always be small if $\mathbf p$ and $\mathbf q$ are close  |- but because of quantization they may end up in different buckets 


Probability of getting to the same bucket: 
- $P_{\mathbf a, b} = P \Big [ h_{\mathbf a, b}(\mathbf p) = h_{\mathbf a, b}(\mathbf q)  \Big] = \int\limits_{0}^{w} \frac{1}{\mathbf u} \cdot f_p(\frac{t}{\mathbf u}) \, (1 - \frac{t}{w}) , \text{d}t$


## Sources
- Slaney, Malcolm, and Michael Casey. "Locality-sensitive hashing for finding nearest neighbors [lecture notes]." 2008. [http://web.iitd.ac.in/~sumeet/Slaney2008-LSHTutorial.pdf]
- Datar, Mayur, et al. "Locality-sensitive hashing scheme based on p-stable distributions." 2004. [http://www.cs.princeton.edu/courses/archive/spring05/cos598E/bib/p253-datar.pdf]

[Category:Hashing](Category_Hashing)
[Category:LSH](Category_LSH)
[Category:Database Indexes](Category_Database_Indexes)