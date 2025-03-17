---
title: I/O Model of Computation
layout: default
permalink: /index.php/I_O_Model_of_Computation
---

# I/O Model of Computation

## I/O Model of Computation
'''The Rule:''' Dominance of I/O cost
- The time taken to perform a [disk access](Secondary_Storage) is much larger than the time needed for manipulating data in the [main memory](Memory_Hierarchy)
- Thus, the number of block accesses (Disk I/Os) is a good approximation to the time needed for an algorithm

### Example
- read a block is ~11 mls (see [Secondary Storage#Accessing](Secondary_Storage#Accessing))
- search for a tuple within a block when it's in the main memory is ~1000 instructions (even with sequential search)
- i.e. search in the main memory is less than %1 of the block access time, can neglect it safely


## Sources
- Database Systems: The Complete Book (2nd edition) by H. Garcia-Molina, J. D. Ullman, and J. Widom
- [Database Systems Architecture (ULB)](Database_Systems_Architecture_(ULB))

[Category:Database Systems Architecture](Category_Database_Systems_Architecture)