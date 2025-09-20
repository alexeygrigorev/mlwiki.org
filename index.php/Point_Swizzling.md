---
layout: default
permalink: /index.php/Point_Swizzling
tags:
- database-systems-architecture
title: Point Swizzling
---
How to manage pointers to blocks and records if they are moved between main and secondary memory? 

## Translation Table
Translation table
- when a record is stored on disk, it's pointers are in physical address form 
- but when we load it into memory, it remains in this form 
- to convert the physical address to the main memory address we use the same idea as for ''map table'':
- we keep a ''translation table'' to do that
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/dbsa/translation-table.png" alt="Image">


When following a pointer,
- if the block is already in the translation table (and therefore in the main memory) - it's okay, don't need to load it
- if not - need to load it into the main memory, and add to the table


## Point Swizzling
But for some frequently accessed pointers we don't want to repeatedly look up the address 
- to avoid that we use ''pointer swizzling'' techniques
- pointer is ''swizzled'' when it's translated to main memory address (and saved in this form)

So in memory with these techniques a pointer consists of 
- a bit indicating whether this pointer is a physical address or (swizzled) memory address
- and physical or memory address itself


### Example
<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/dbsa/point-swizzling.png" alt="Image">

- At the beginning both records are on disk 
- Then we load the first one to memory 
- It points to two other records 
  - first gets swizzled because it points to another record that is also in the memory
  - another one doesn't, because it points to a record not yet brought to memory


## Strategies
There are several strategies to do that 

### Automatic Swizzling
as soon as block is brought into memory, we swizzle the pointers and enter them into translation table

### On Demand
- leave all pointers unswizzled, just enter the addresses to the translation table 
- when we follow a pointer, we swizzle it if it's not swizzled and leads to a block in memory

### No Swizzling
- always consult the translation table
- advantage: gives us flexibility so we can move blocks around as we like, and when moving we just need update the address in the table

### Programmer Control
- application programmer may know if some pointers are likely to be followed more frequently than other
- e.g. if he knows that the block will be heavily accessed (because it's the root of a [B-Tree](B-Tree)), then it needs to be swizzled
- so he can say which pointers need swizzling and which don't

## Unswizzling
When a block is flushed back to dist, all pointers in the block must be unswizzled (memory addressed replaced by physical addresses)

This can be done using the transformation table but in the opposite direction 


## Pinning
A block in memory is ''pinned'' if it cannot be moved back to disk safely
- a bit signifying if a block is pinned in located in header

reasons for pinning 
- if a block $B_1$ has a swizzled pointer $B_2$ then we must be careful about moving block $B_2$ to avoid dangling pointers
  - blocks like $B_2$ that are referred from outside, should be pinned 

So when we write a block back, we need to make sure it's not pinned and then unswizzle all pointers 
To unpin a pinned block we need to unswizzle any pointers to it

Consequently the translation table must record for each DB address
- where are the swizzled pointers 

Possible approaches 
- keep the list of references to a memory address
  - can be a linked list attached to an entry in the translation table
- if memory address is significantly shorter than the physical address, we can relace the PA with
  - the swizzled pointer
  - another pointer to the next occurrence of usage of this pointer 
  - together they will form a linked list of all pointer occurrences 
  - <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/dbsa/translation-table-unswizzling.png" alt="Image">


## See also
- [Physical Data Organization (databases)](Physical_Data_Organization_(databases))

## Sources
- Database Systems: The Complete Book (2nd edition) by H. Garcia-Molina, J. D. Ullman, and J. Widom
