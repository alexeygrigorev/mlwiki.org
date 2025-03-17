---
title: "Conjunctive Query/Translation"
layout: default
permalink: /index.php/Conjunctive_Query_Translation
---

# Conjunctive Query/Translation

## [Conjunctive Query](Conjunctive_Query) Translation
This describes translation algorithms from [Relational Algebra](Relational_Algebra) to [Conjunctive Queries](Conjunctive_Query) and vise-versa


## Translation to [Conjunctive Queries](Conjunctive_Query)
We can translate a [Relational Algebra](Relational_Algebra) expression that is in [Select-Project-Join](Select-Project-Join_Expressions) form into CQ. Note that it is not possible to translate any other form to it
- for SQL, first [translate SQL to TA](Translating_SQL_to_Relational_Algebra)
- then find the minimal possible [SPJ Expression](Select-Project-Join_Expressions)
- translate it as suggested below 


### Translation by Example
Suppose we have the following logical query plan:

$
\pi_{
  \begin{subarray}{l}
    R_1.A, \\
    S_1.B \\
  \end{subarray}
}
\sigma_{
  \begin{subarray}{l}
    {\color{grey}{(1)}} \ R_1.A = R_2.A \ \land \\
    {\color{grey}{(2)}} \ R_2.B = 4 \ \land \\
    {\color{grey}{(3)}} \ R_2.A = R_3.A \ \land \\
    {\color{grey}{(4)}} \ R_3.B = S_1.B \ \land \\
    {\color{grey}{(5)}} \ S_1.C = S_2.C \ \land \\
    {\color{grey}{(6)}} \ S_2.B = 4
  \end{subarray}
}
\big(
\rho_{R_1}(R) \times \rho_{R_2}(R) \times \rho_{R_3}(R) \times \rho_{S_1}(S) \times \rho_{S_2}(S) 
\big)$

We proceed as follows
- step 1: 
: for each relation we create an atom in body with distinct variables 
- step 2:
: for all the conditions of the selection part we replace the variables that participate in equations by the same symbol

in this case
- step 1:
  - $
\begin{array}{l l}
Q(x_{R_1.A}, y_{S_1.B}) \leftarrow & 
  R(x_{R_1.A}, y_{R_1.B}), \\
& R(x_{R_2.A}, y_{R_1.B}), \\
& R(x_{R_3.A}, y_{R_3.B}), \\
& R(y_{S_1.B}, z_{S_1.C}), \\
& R(y_{S_2.B}, z_{S_2.C}) \\
\end{array}
$
  - in the head we put what we want to see in the output, i.e. the variables specified in the projection
  - variable names like $x_{R_1.A}$ are helpful to keep track of the original names, however it could be anything
  - this query now computes $\rho_{R_1}(R) \times \rho_{R_2}(R) \times \rho_{R_3}(R) \times \rho_{S_1}(S) \times \rho_{S_2}(S)$
- step 2
- : we restrict the query so it outputs only the tuples that match the selection condition
- : for that for every equality we replace all the occurrence of variables in that inequality to the same variable 
  - the name does not matter
  - for constants we put the value of a constant
  - $
\begin{array}{l l}
Q(x_{R_1.A}, y_{S_1.B}) \leftarrow & 
  R(x_{R_1.A} {\color{grey}& R(x_{R_1.A} {\color{grey}& R(x_{R_1.A} {\color{grey}& R(y_{R_3.B} {\color{grey}& R(4 {\color{grey}\end{array}
$
    - here ${\color{grey}- now this is equivalent to the RA expression


## Translation from [Conjunctive Queries](Conjunctive_Query)
Translation from CQ back to [Relational Algebra](Relational_Algebra) is straightforward 
- the number of elements being joined is equal to the number of atoms
  - i.e. the number of joins is (# of atoms) - 1
- we then add the selection
  - with an equality condition for each variable name (if repeated 2 or more times)
  - and for each constant
- finally, only the variables in the head get projected
- of course, we need to know the relational schema to be able to do that 
  - note that in CQ we use positions to denote attributes

### Example
Given: $Q(t) \leftarrow \text{MovieStar}({\color{red}{n}}, a, g, {\color{blue}{1940}}), \text{StarsIn}(t, y, {\color{red}{n}})$

We translate it as 
- $\pi_\text{S.movieTitle}
\sigma_{
  \begin{subarray}{l}
    \text{M.name = S.starName }  \land \\
    \text{M.birthDate = 1940} \\
  \end{subarray}
}
\big(
\rho_M(\text{MovieStar}) \times \rho_S(\text{StarsIn})
\big)$


## See Also
- [Conjunctive Query](Conjunctive_Query)

## Sources
- [Database Systems Architecture (ULB)](Database_Systems_Architecture_(ULB))
- Database Systems Architecture lecture notes #2 by S. Vansummeren [https://dl.dropboxusercontent.com/sh/r0zvy3zaycbevx8/U0XnqCSwGZ/lect2-notes-conjunctive.pdf]


[Category:Relational Databases](Category_Relational_Databases)