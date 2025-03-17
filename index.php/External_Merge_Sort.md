---
title: External Merge Sort
layout: default
permalink: /index.php/External_Merge_Sort
---

# External Merge Sort

## External Merge Sort
Full name: ''External Memory Multi-Way Merge Sort''
- same idea as in in-memory [Merge Sort](Merge_Sort), but extended to [Secondary Storage](Secondary_Storage)


## Algorithm
This is a multi-way algorithms. That is, the sorting of relation $R$ is done in several passes
- First Pass - in memory sorting 
- Second and onwards - merging

Notation:
- $R$ relation we want to sort
- $M$ - max # of blocks we can use in memory

### First Pass
1-st pass:
- read $M$ blocks
- sort all elements in memory with any sorting algorithm (say, [Merge Sort](Merge_Sort) or [Quick Sort](Quick_Sort))
- write sorted results back to disk 
- repeat for remaining blocks of $R$ until all are processed

After the first pass we have $\left\lceil \cfrac{B(R)}{M} \right\rceil $ sorted sub-results


### Second Pass
- Since we have $M$ available buffers, we can simultaneously process at most $M$ sorted sub-results from the previous pass 
- So we divide all sub-results into categories with $M$ sub-results in each 
- Since we have $M$ sub-results and $M$ blocks in each, each result of this pass should have $M \times M$ blocks
- After this pass we will have $\left \lceil \cfrac{B(R) / M}{M} \right\rceil  = \left \lceil \cfrac{B(R)}{M^2} \right\rceil$ sorted subresults 


2-nd pass:
- merge the first $M$ sublists to a single sublist of $M^2$ blocks
- by synchronous iteration 


### Synchronous Iteration
This is essentially the merging phase of [Merge Sort](Merge_Sort)

Algorithm:
- load block of $R$ to $N_R$, block of $S$ to $N_S$
- iterate over tuples $t_R \in N_R$ and $t_S \in N_S$ ''synchronously''
  - if $t_R \geqslant t_S$
    - output $t_R$ 
    - move $t_R$ pointer to the next tuple in $R$ (load next block if needed)
  - if $t_R > t_S$
    - output $t_S$ 
    - move $t_S$ pointer to the next tuple in $S$ (load next block if needed)


### Third and Onwards Passes
- if needed - repeat the second pass again 
- until everything is sorted 


## Cost
- at each pass we read and write the entire relation once
- there are $P = \lceil \log_M B(R) \rceil$ passes
- so the total cost is $\underbrace{2 \times B(R)}_\text{1 read + 1 write} \times P =  2 \times B(R) \times \lceil \log_M B(R) \rceil$


## See also
- [Merge Sort](Merge_Sort)
- [Physical Operators (databases)](Physical_Operators_(databases))

## Sources
- [Database Systems Architecture (ULB)](Database_Systems_Architecture_(ULB))
- Database Systems: The Complete Book (2nd edition) by H. Garcia-Molina, J. D. Ullman, and J. Widom

[Category:Database Systems Architecture](Category_Database_Systems_Architecture)
[Category:Algorithms](Category_Algorithms)
[Category:Sorting](Category_Sorting)