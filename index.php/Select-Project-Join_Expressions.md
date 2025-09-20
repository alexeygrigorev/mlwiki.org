---
layout: default
permalink: /index.php/Select-Project-Join_Expressions
tags:
- relational-databases
title: Select-Project-Join Expressions
---
## Select-Project-Join Expression
In practice, most [Relational Algebra](Relational_Algebra) expressions (i.e. queries) are of the ''Select-Project-Join'' form (SPJ)

an ''SPJ expression'' is
- a [Relational Algebra](Relational_Algebra) expression
- it consists only of selections, projections and joins
- there are only equality predicates for selection (i.e. of form $A_j = B_i$)

```sql
SELECT ...
FROM R1, ..., Rn
WHERE A1 = B1 AND ... AND An = Bn
```

The corresponding RA expression is
- $\pi_\text{...} \sigma_{A_1 = B_1 \land ... \land A_n = B_n} (R_1 \times ... \times R_n)$


## Applications
This type of query is very interesting for [Logical Query Plan Optimization](Logical_Query_Plan_Optimization) since it allows
- to translate a RA expression to [Conjunctive Query](Conjunctive_Query)
- and optimize the CQ to remove redundant joins



## See also
- [Logical Query Plan Optimization](Logical_Query_Plan_Optimization)
- [Conjunctive Query](Conjunctive_Query)

## Sources
- [Database Systems Architecture (ULB)](Database_Systems_Architecture_(ULB))
