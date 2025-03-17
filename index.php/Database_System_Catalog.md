---
title: "Database System Catalog"
layout: default
permalink: /index.php/Database_System_Catalog
---

# Database System Catalog

## Database System Catalog
To estimate a cost of [Physical operators](Physical_Operators_(databases)) in a DBMS we use the following statistics:
- $B(R)$ - # of blocks that relation $R$ holds
- $T(R)$ - # of tuples in $R$
  - typically can be used to calculate $B(R)$ when we know how many bytes we have per block
- $V(R, A_1, ..., A_n) = |  \delta \pi_{A_1, ..., A_n} (R)  |$ - # of distinct values  |

This statistics in DBMS is a ''system catalog''
- they are regularly collected (when needed, scheduled, etc) 
- and regularly revisited 
- note that this data is kept only for base relations, not for subresults of a query|   | |
## Statistics
For base relations we typically have some [Histogram](Histogram)s that show how values are distributed

### [Equal-Width Histogram](Data_Discretization#Equal-Width_Partitioning)
- In this type of histograms the values are grouped in equal-width buckets
- We assume that the values are distributed uniformly within there buckets 

Example 

|   range   |  [1, 10)   |  [11, 20)  |  [21, 30)  |  [31, 40)  |  [41, 50)  ||   # of tuples   |  50  |  2000  |  2000  |  3000  |  2950  |


## See Also
- [Physical Operators (databases)](Physical_Operators_(databases))
- [Data Discretization](Data_Discretization)

## Sources
- [Database Systems Architecture (ULB)](Database_Systems_Architecture_(ULB))
- Database Systems: The Complete Book (2nd edition) by H. Garcia-Molina, J. D. Ullman, and J. Widom

[Category:Database Systems Architecture](Category_Database_Systems_Architecture)