---
layout: default
permalink: /Voting_Theory
tags:
- voting-theory
title: Voting Theory
---
## Voting Theory
Voting Theory studies how to take individual rankings of voters and aggregate them to form the global ranking.

Examples:
- Votes for a president of a company/country, etc. All voters communicate their results and based on that the president is chosen
- Search engines: there are many results, how to show them? 


## Notation and Relations
- let $A = \{a, b, c, ...\}$ be the set of candidates
- there are $N$ voters 
- each voter can express his preference on the basis of a *total order*
  - i.e. he has to rank all the candidates 

For this notation we define the following relations ([Voting Theory Relations](Voting_Theory_Relations))
- Weak and Strong Preference
- Indifference


## Voting Mechanisms and Principles
A *voting mechanism* (or *voting procedure* or *voting method*) takes a collection of votes (individual preferences of the candidates from set $A$) and forms the global ranking. Usually it choses a single candidate from the set $A$.

<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/de/vt/voting-mechanism.png" alt="Image">

There are several voting procedures:
- [Plurality Voting](Plurality_Voting)
- [Two-Round Voting](Two-Round_Voting)
- [Borda's Rule](Borda's_Rule)
- [Condorcet's Rule](Condorcet's_Rule)


### Criteria
How to characterize "good" voting methods?

There are several criteria 
- [Monotonicity](Monotonicity)
- [Independence to Third Alternatives](Independence_to_Third_Alternatives)
- Condorcet Fairness Criterion
- Solution Existence 
- [Separability](Separability)


|    |  PV  |  2PV  |  Borda  |  Cond.  |   Monotonicity  |  Yes ||  No  ||  Yes ||  No ||   Solution Existence  |  Yes  |  Yes  |  Yes  |  No ||   Manipulation  |  No ||  No  ||  No  ||  No ||   Separability  |  Yes ||  No  ||  Yes ||  Yes ||   Condorcet Fairness  |  No  ||  No  ||  No  ||  Yes |

Other principles:
- [Unanimity](Unanimity)


## Theorems
- [May's Theorem](May's_Theorem)
- [Arrow's Impossibility Theorem](Arrow's_Impossibility_Theorem)


## Examples and Exercises
- [Voting Theory Exercises](Voting_Theory_Exercises)
- [Voting Theory Examples](Voting_Theory_Examples)


## Misc.
- [Banzhaf Power Index](Banzhaf_Power_Index) - shows how strong a party is
- [Parliamentary Allocation](Parliamentary_Allocation) - how to allocate seats between parties in a parliament


## Links
- Mathematics of Voting - slides [link](http://www.ms.uky.edu/~lee/ma111fa09/slides01.pdf) 
- Criteria [link](http://www.ctl.ua.edu/math103/voting/whatdowe.htm)
- EC228 Voting Theory Lecture Notes [link](http://www2.warwick.ac.uk/fac/soc/economics/current/modules/ec228/details/lecturenotes/lecturenotesbook.pdf)
- Social Choice Theory and Multicriteria Decision Aiding [link](http://www-desir.lip6.fr/publications/pub_1389_1_BouyssouMarchantPerny_soc_choice.pdf)
- Book: Voting, Arbitration, and Fair Division [link](http://xaravve.trentu.ca/pivato/Teaching/voting.pdf)
- Methods vs Voting Criteria [link](http://en.wikipedia.org/wiki/Voting_system_criterion)

## Sources
- [Decision Engineering (ULB)](Decision_Engineering_%28ULB%29)
- The mathematics of voting and elections: Paradox, deception, and chaos [link](http://xaravve.trentu.ca/pivato/Teaching/votingslides.pdf)
