---
title: Physical Operators (databases)
layout: default
permalink: /index.php/Physical_Operators_(databases)
---

# Physical Operators (databases)

## Intro
Each node in a Logical [Query Plan](Query_Plan) may be executed in several ways 
- there is no single implementation that is always better than the others 
- so we need to compare alternatives based on their costs (in [I/O Model of Computation](I_O_Model_of_Computation) it's # of I/O operations)

### Statistics
To estimate a cost we use the following statistics from [Database System Catalog](Database_System_Catalog):
- $B(R)$ - # of blocks that relation $R$ holds
- $T(R)$ - # of tuples in $R$
  - typically can be used to calculate $B(R)$ when we know how many bytes we have per block
- $V(R, A_1, ..., A_n) = |  \delta \pi_{A_1, ..., A_n} (R)  |$ - # of distinct values  |
### Parameters
And also we use 
- $M$ - number of available main memory buffers 

To simplify we suppose that the situation is ideal
- all buffers of [Buffer Manager](Database#Buffer_Manager) are available 
- there are no other operations that concurrently claim the space


## Operators Overview

|   Type $\downarrow$  |   [Bag Union](#Bag_Union)  |   [Set Union](#Set_Union)  |   [Set Intersection](#Set_Intersection)  |   [Bag Intersection](#Bag_Intersection)  |   [Set Difference](#Set_Difference)   |   [Bag Difference](#Bag_Difference)  |   [Join](#Join)  |   One-Pass  |  [{{yes}}](#Bag_Union) ||  [{{yes}}](#One-Pass_Set_Union) ||  [{{yes}}](#One-Pass_Set_Intersection) ||  [{{yes}}](#One-Pass_Bag_Intersection) ||  [{{yes}}](#One-Pass_Set_Difference) ||  [{{yes}}](#One-Pass_Bag_Difference) ||  [{{yes}}](#One-Pass_Join) ||   Sort-Based   |  {{no}} ||  [{{yes}}](#Sort-Based_Set_Union) ||  [{{yes}}](#Sort-Based_Set_Intersection) ||  [{{yes}}](#Sort-Based_Bag_Intersection) ||  [{{yes}}](#Sort-Based_Set_Difference) ||  [{{yes}}](#Sort-Based_Bag_Difference) ||  [{{yes}}](#Sort-Based_Join) ||   Hash-Based  |  {{no}} ||  [{{yes}}](#Hash-Based_Set_Union) ||  not here ||  not here ||  not here ||  not here ||  [{{yes}}](#(Partition)_Hash_Join) |
Also:
- For Joins: [#Nested Loop Join](#Nested_Loop_Join)


## Bag Union
$R \cup_B S$
- all elements from both
- no need to remove duplicates
- for this operation just need to use one buffer block 
- load elements to the block and then just output 

'''Algorithm'''
- for each block $B_R \in R$
  - load $B_R$ to buffer $N$
  - for each tuple $t_R \in N$
    - output $t_R$
- for each block $B_S \in S$
  - load $B_S$ to buffer $N$
  - for each tuple $t_S \in N$
    - output $t_S$

'''Cost'''
- $B(R) + B(S)$
- we don't count output 
- and we must have some available buffers: $M \geqslant 1$


## Set Union
$R \cup_B S$
- this time we care about duplicates
- assume that $R$ is smaller than $S$

### One-Pass Set Union
$R$ fits into memory:
- We assume that we have $B(R) + 1$ available buffers 
- i.e. $R$ can fit into memory and after that there's at least one remaining available buffer

Idea:
- load all elements of $R$ 
- using 1 extra buffer go through all blocks of $S$
- output element if only it's not in $R$

'''Algorithm'''
- load $R$ to $N_1, ..., N_{B(R)}$ buffers
- for each tuple $t_R \in \cup_i N_i$
  - output $t_R$
- for each block $B_S \in S$
  - load $B_S$ to $N_0$
  - for each tuple $t_S \in N_0$
    - if $t_S \not \in \cup_i N_i$, output $t_S$

'''Cost'''
- $B(R) + B(S)$
- pass once through $R$ and once through $S$
- we ignore the cost of searching in memory - interested only in I/O cost

Problem: 
- We can do it only when one of the relations fin into memory 
- usually they don't fit|   | |
### Sort-Based Set Union
what if there's no enough memory available? 

Algorithm:
- Sort $R$ with [External Merge Sort](External_Merge_Sort)
- Sort $S$ with [External Merge Sort](External_Merge_Sort)
- Iterate Synchronously over $R$ and $S$
  - like in [External Merge Sort](External_Merge_Sort), but don't output repeating values
  - i.e.: increase both pointers when see a duplicate 

Synchronous Iteration:
- load block of $R$ to $N_R$, block of $S$ to $N_S$
- iterate over tuples $t_R \in N_R$ and $t_S \in N_S$ ''synchronously''
  - if $t_R < t_S$
    - output $t_R$ 
    - move $t_R$ pointer to the next tuple in $R$ (load next block if needed)
  - if $t_R > t_S$
    - output $t_S$ 
    - move $t_S$ pointer to the next tuple in $S$ (load next block if needed)
  - if $t_R = t_S$
    - output $t_S$ 
    - move '''both''' $t_R$ and $t_S$

Cost:
- $2 B(R) \lceil \log_M B(R) \rceil$: cost of sorting $R$
- $2 B(S) \lceil \log_M B(S) \rceil$: cost of sorting $S$
- $B(R) + B(S)$ to iterate synchronously to output the results


#### Optimization
- Synchronous Iteration of Sort-Based Union is very similar to the merge phase of [External Merge Sort](External_Merge_Sort)
- Sometimes we can combine them - and avoid doing the last pass of Merge Sort|   | |Algorithm:
- Sort $R$, but don't execute the last merge phase
  - we know that after that $R$ is divided into $l$ sorted lists
  - $1 < l \leqslant M$
- Sort $S$, but don't execute the last merge phase
  - we know that after that $S$ is divided into $k$ sorted lists
  - $1 < k \leqslant M$
- if $l + k \leqslant M$ then we can apply the optimization
  - because there are enough buffers available to synchronously iterate through both set of sub-results


Cost:
- $2 B(R) \big( \lceil \log_M B(R) \rceil - 1 \big)$: cost of sorting $R$ without last pass
- $2 B(S) \big( \lceil \log_M B(S) \rceil - 1 \big)$: cost of sorting $S$ without last pass
- $B(R) + B(S)$ to iterate synchronously to output the results
- or $2 B(R) \lceil \log_M B(R) \rceil + 2 B(S) \lceil \log_M B(S) \rceil - B(R) - B(S)$
- we save $B(R) + B(S)$ I/Os|   | |
Note that
- this optimization is only possible if $k + l \leqslant M$
- can calculate $k$ and $l$ as
  - $l = \left\lceil \cfrac{B(R)}{ M^{\lceil \log_M B(R) \rceil - 1} } \right\rceil $ - # of passes to sort $R$ - 1
  - $k = \left\lceil \cfrac{B(S)}{M^{\lceil \log_M B(S) \rceil - 1}} \right\rceil$ - # of passes to sort $S$ - 1

it's usually sufficient to have only 2 passes for sorting
- in this case can apply optimization if 
- $\left\lceil \cfrac{B(R)}{M} \right\rceil  + \left\lceil \cfrac{B(S)}{M} \right\rceil \leqslant M$ or
- $B(R) + B(S) \leqslant M^2$
- cost in this case is $3B(R) + 3B(S)$ with optimization 
- $5B(R) + 5B(S)$ without optimization


#### Example
Suppose $M = 15, B(R) = 100, B(S) = 120$
- to sort $R$ need $\lceil \log_M B(R) \rceil = 2$ passes
- to sort $S$ need $\lceil \log_M B(S) \rceil = 2$ passes
- $l = \left\lceil \cfrac{100}{15^2} \right\rceil$
- $k = \left\lceil \cfrac{120}{15^2} \right\rceil$
- $l + k = 15 \leqslant M$, therefore we can apply optimization
- cost is $2 \cdot 100 \cdot 2 + 2 \cdot 120 \cdot 2 - 100 - 120 = 660$


### Hash-Based Set Union
Main idea: we want to partition both $R$ and $S$ in such a way that
- if a tuple appears in some bucket from $R$ it should appear in the corresponding bucket from $S$
- each bucket contains no more that $M - 1$ blocks 
- so it is possible to apply [One-Pass Set Union](#One-Pass_Set_Union) to each bucket

#### Record distribution
- $B(R) < B(S)$ - $R$ is smaller than $S$
- we suppose that we can partition $R$ in $k$ buckets $R_i$
  - to do that we apply some hash function $h$
- and then distribute tuples from $S$ also into $k$ buckets $S_i$
  - also by applying $h$ 
- all records in $R_i$ and $S_i$ ended up in the bucket $i$ because they have the same hash value
  - if there's a record that occurs both in $R_i$ and $S_i$, it's a duplicate 
  - and we need to consider only these buckets, this record cannot appear in buckets other than $i$


#### Computing Set Union
- to compute set union we compute unions for all buckets $i$: $R_i \cup_S S_i$ 
- since $R_i$ contains at most $M - 1$ block can do that in one pass


#### Partitioning $R$
How to partition $R$ in blocks of size at most $M - 1$?

Algo
- first pass
  - we load each block of $R$ into buffer $N_0$
  - and we have $M - 1$ remaining buffers - we will use them as buckets
  - for each tuple $t_R \in R$ we calculate $h(t_R)$ to find which bucket it belongs to
  - once a bucket buffer is full, we flush it to disk to some block, empty the buffer and continue 
  - $\Rightarrow$ after first pass we'll have $M - 1$ buckets of $\cfrac{B(R)}{M - 1}$ blocks (assuming $h$ distributes records uniformly)
- 2+ passes 
  - if there are buckets that have more that $M - 1$ blocks we need to hash them again
  - but this time with another hash function $h'$ (otherwise the old $h$ will just put all the tuples back to the same bucket)
  - so we repeat the first pass again, but for each overfull bucket separately
  - $\Rightarrow$ after second pass we'll have $(M - 1)^2$ buckets of $\cfrac{B(R)}{(M - 1)^2}$ blocks
- continue this process until all buckets have no more than $M - 1$ blocks 
  - $\Rightarrow$ after $k$ passes we'll have $(M - 1)^k$ buckets of $\cfrac{B(R)}{(M - 1)^k}$ blocks


One level of partitioning is usually enough
- so we need two passes
- 1st: to partition
- 2nd: to do pair-wise single pass unions of buckets
- it's sufficient when $\cfrac{B(R)}{M - 1} \leqslant M - 1$ or $\approx B(R) \leqslant M^2$

Cost of partitioning
- $2B(R) \underbrace{\lceil log_{M - 1} B(R) - 1 \rceil}_\text{# of passes}$:
- at each pass we read and write $R$ once
- so for one pass it's just $2B(R)$ 


#### Cost
Total cost of partitioning
- $2B(R) \lceil \log_{M - 1} B(R) - 1 \rceil$ for $R$
- $2B(S) \lceil \log_{M - 1} B({ \color{blue}{R} }) - 1 \rceil$ for $S$
  - note that number of passes for $S$ is the same as of $R$
- $B(R) + B(S)$ one pass union for each bucket
- if one pass is sufficient, then the total cost is $3B(R) + 3B(R)$


## Set Intersection
$R \cap_S S$
- assume $R$ is smaller than $S$

### One-Pass Set Intersection
Essentially same as [#One-Pass Set Union ](#One-Pass_Set_Union_) 
- if $R$ is small enough to fit into $M - 1$ buffers 

Algorithm 
- load $R$ to $K_R = N_1, ..., N_{B(R)}$ buffers
- for each block $B_S \in S$
  - load $B_S$ to $N_0$
  - for each tuple $t_S \in N_0$
    - if $t_S \in K_R$, output $t_S$

### Sort-Based Set Intersection
- same as [#Sort-Based Set Union](#Sort-Based_Set_Union)
- output $t$ if it appears in both $R$ and $S$


## Bag Intersection
$R \cap_B S$
- assume $R$ is smaller than $S$

### One-Pass Bag Intersection
Essentially same as [#One-Pass Set Union](#One-Pass_Set_Union) 
- if $R$ is small enough to fit into $M - 1$ buffers 
- but for each distinct value we associate a '''count''' - number of times this tuple occurred
  - generally, this structure can take more that $M - 1$ memory buffer if there are few duplicates
  - but if there are a lot of duplicates - this way of organizing will take less room than $M - 1$


Algorithm
- load $R$ to $K_R = N_1, ..., N_{B(R)}$ buffers
- for each block $B_S \in S$
  - load $B_S$ to $N_0$
  - for each tuple $t_S \in B_S$
    - if $t_S \in K_R$
      - output $t_S$
      - decrease '''count''' of $t_S$ in $K_R$
      - if '''count''' = 0 then remove this tuple from memory


### Sort-Based Bag Intersection
- same as [#Sort-Based Set Union](#Sort-Based_Set_Union)
- output $t$ the number of times it appears both in $R$ and $S$


## Set Difference
Note that this operation is not commutative
- $S -_S R$ is not the same as $R -_S S$
- assume that $R$ is smaller than $S$

### One-Pass Set Difference
For this we assume $R$ fits into $M-1$ blocks


$S -_S R$ case 
- read $R$ into buffers $K_R = N_1, ..., N_{B(R)}$
- for each block $B_S \in S$
  - load $B_S$ into $N_0$
  - for each tuple $t_S \in B_S$
    - if $t_S \not \in K_R$ output $t_S$


$R -_S S$ case
- read $R$ into buffers $K_R = N_1, ..., N_{B(R)}$
- for each block $B_S \in S$
  - load $B_S$ to $N_0$
  - for each tuple $t_S \in B_S$
    - if $t_S \in K_R$ remove $t_S$ from $K_R$ 
- for each tuple $t_R$ that is still in $K_R$ output $t_R$

### Sort-Based Set Difference
- same as [#Sort-Based Set Union](#Sort-Based_Set_Union)
- output $t$ if it appears in $R$ but not in $S$


## Bag Difference
- same as in [#Bag Intersection](#Bag_Intersection): we '''count''' the number of occurrences
- also two cases: $S -_B R$ and $R -_B S$

### One-Pass Bag Difference
For this we assume $R$ fits into $M-1$ blocks


$S -_B R$ case: count $c$ in this case is $c$ reasons not to output a tuple
- read tuples of $R$ to $K_R = N_1, ..., N_{B(R)}$, '''count''' the number of occurrences
- load each block $B_S$ to $N_0$
  - for each tuple $t_S \in B_S$
    - if $t_S \not \in K_R$: output $t_S$
    - otherwise 
      - decrement '''count''' of $t_S$ and 
      - remove $t_S$ from $K_S$ if count = 0


$R -_B S$ case
- read tuples of $R$ to $K_R = N_1, ..., N_{B(R)}$, '''count''' the number of occurrences
- load each $B_S$ to $N_0$
  - if $t_S \in K_R$
    - decrement '''count''' for $t_S$ in $K_R$
    - remove $t_S$ from $K_R$ if '''count''' = 0
- for each remaining $t_R \in K_R$
  - output $t_R$ '''count''' times

### Sort-Based Bag Difference
- same as [#Sort-Based Set Union](#Sort-Based_Set_Union)
- for each tuple $t$
  - let $c_R$ = number of times $t$ appears in $R$
  - let $c_S$ = number of times $t$ appears in $S$
  - if $c = c_R - c_S \leqslant 0$ don't output anything
  - otherwise output $t$ $c$ times


## Join
Join is most costly operator to evaluate
- sometimes it's quadratic (when it's equivalent to cartesian product)

Suppose we want to evaluate $R(X, Y) \Join S(Y, Z)$
- $Y$ is a matching attribute and we will join on it
- we again assume that $B(R) < B(S)$

### One-Pass Join
To be able to do it in one pass $R$ must fit into memory
- $R(B) \leqslant M -1$

Algo
- load $R$ into buffers $N_1, ..., N_{B(R)}$
- for each block $B_S \in S$
  - load $B_S$ to $N_0$
  - for each tuple $t_S \in N_0$
    - for each matching tuple $t_R \in \U_i N_i$
    - output $t_R \Join t_S$

Cost
- $B(R) + B(S)$
- again ignore cost of finding matching tuple in memory


### Nested Loop Join
#### Tuple-Based Nested Join Loop
First variant is ''tuple-based nested join loop''
- for each $r \in R$
- for each $s \in S$
  - if $r$ matches $s$ output $r \Join s$

We need only one buffer for $R$ and one buffer for $S$

Cost
- $T(R) \times T(S)$ - very expensive|   | |#### Block-Based Nested Join Loop
- We divide $R$ into segments of $M - 1$ blocks
- and for each such segment we go through entire $S$

Algo
- load each segment of $R$ into buffers $N_1, ..., N_{M - 1}$
- for each block $B_S \in S$
  - load $B_S$ into $N_0$
  - for each tuple $t_R \in \cup_i N_i$ 
    - for each matching tuple $t_S \in N_0$: output $t_R \Join t_S$

### Sort-Based Join
Essentially the same as [#Sort-Based Set Union](#Sort-Based_Set_Union)
- but in this case we need to take care about duplicates that may be in both $R$ and $S$

Algo
- Sort $R$ on matching attribute $Y$
- Sort $S$ on matching attribute $Y$
- Iterate Synchronously through $R$ and $S$ 
  - if $t_R.Y < t_S.Y$ then advance pointer $t_R$
  - if $t_R.Y > t_S.Y$ then advance pointer $t_S$
  - if $t_R.Y = t_S.Y$ then
    - for each pointers $t'_S$ with same $Y$ value that follow $t_S$ (including $t_S$ itself)
      - output $t_R \Join t'_S$ 
    - advance pointer $t_R$ and rewind $t'_S$ to $t_S$
    - (this way we join each tuple from $R$ that has value $Y$ with each tuple from $S$ that also has value $Y$)


Cost
- usually depends of the number of tuples with equal values 
- worst case: all tuples have the same value for $Y$ - in this case the cost is $B(R) \times B(S)$
- but joins are usually performed on foreign keys 
  - i.e. tuples in $R$ have distinct values for $Y$ 
  - and for each tuple $t_R$ we have several (maybe 0) tuples $t_S$ - one-to-many relationship
  - so we don't need to rewind the pointer for $t_S$
  - in this case the cost analysis is similar to the [#Sort-Based Set Union](#Sort-Based_Set_Union)
    - sorting cost + $B(R) + B(S)$
  - it's also possible to optimize and save additional $B(R) + B(S)$ I/Os
    - sorting cost - $B(R) - B(S)$
- '''NB''': if there's a [clustered index](Indexing_(databases)#Clustered_Index) on $Y$ we don't need to sort it - it's already sorted


### (Partition) Hash Join
- Essentially the same as [#Hash-Based Set Union](#Hash-Based_Set_Union)
- the only difference is that we hash the join attribute and not the whole tuple

Algo
- partition $R$ by hashing $Y$ into buckets each with at most $M-1$ blocks
- let $k$ be the number of buckets we got in result
- partition $S$ by hashing $Y$ into $k$ buckets
- let $R_i$ and $S_i$ be blocks of bucket #$i$ that ended up there because their $Y$ values have the same hash
  - a tuple $t_S \in S$ matches $t_R \in S$ $\iff$ there $\exists$ a bucket $i$ s.t. $t_R \in R_i$ and $t_S \in S_i$
- we compute join by calculating $R_i \Join S_i$ for all $i$ using [#One-Pass Join](#One-Pass_Join) algorithm

Cost
- same as for Hash-Based Set Union
- $k = \lceil \log_{M - 1} B(R) - 1 \rceil$
- total # of I/Os: $2B(R) \cdot k + 2B(S) \cdot k + B(R) + B(S)$



## See also
- [Query Plan](Query_Plan)
- [Query Processing](Query_Processing)

## Sources
- [Database Systems Architecture (ULB)](Database_Systems_Architecture_(ULB))
- Database Systems: The Complete Book (2nd edition) by H. Garcia-Molina, J. D. Ullman, and J. Widom

[Category:Database Systems Architecture](Category_Database_Systems_Architecture)