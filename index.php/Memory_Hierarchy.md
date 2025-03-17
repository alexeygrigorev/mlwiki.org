---
title: Memory Hierarchy
layout: default
permalink: /index.php/Memory_Hierarchy
---

# Memory Hierarchy

## The Memory Hierarchy
<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/dbsa/memory-hierarchy.png" alt="Image">

Two main categories:
- ''volatile'': forgets what it stores when power goes off
- ''non-volatile'': can persist data for a long time

Normally data is moved only between adjacent levels of hierarchy 


### Cache
- size: 1 mb or more
- access time: a few nanoseconds 

data and instructions are moved to cache from the main memory when they are needed by the CPU

### Main Memory
- to more from memory to cache/processor: 10-100 nanoseconds 

stores all data and instructions

### [Secondary Storage](Secondary_Storage)
- 10 milliseconds to transfer data from disk to memory 

''Secondary storage'': disks and other devices that can store large amounts of data 

### Virtual Memory
''Virtual Memory'' is an address space (32 or 64 bits) 
- the OS manages VM keeping needed parts at hand (in the main memory)
- and the rest on disk 

So beware: data can be moved to and fro by the OS|   | |### Tertiary Storages
- very high read/write times
- may be optical disks stored somewhere 

a storage with very large capacity (petabytes, etc)


## See also
- [Secondary Storage](Secondary_Storage)

## Sources
- Database Systems: The Complete Book (2nd edition) by H. Garcia-Molina, J. D. Ullman, and J. Widom


[Category:Computer Architecture](Category_Computer_Architecture)