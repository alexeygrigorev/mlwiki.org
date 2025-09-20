---
layout: default
permalink: /index.php/Hash_Tables
tags:
- algorithms
- data-structures
title: Hash Tables
---
## Hash tables
Purpose
- maintain a set of things with all operations in $O(1)$ time 
- $O(1)$ when data is not pathological
- need to use a [Hash Function](Hash_Function) to do that


### Operations
$O(1)$ operations:
- insert
- delete
- lookup


### Details
- given: Universe $U$ - really really big
- goal: want to maintain set $S \subset U$

Solution:
- pick $n$ - number of buckets
- choose a [Hash Function](Hash_Function) $h: U \mapsto \{0, 1, ..., n-1\}$
- use array $A$ of length $n$ to store $x$ in $A[h(x)]$


## Collisions
This approach leads to collisions ([Birthday paradox](Birthday_paradox))

There are two ways to address collisions:
- Separate Chaining 
- Open Addressing


### Separate Chaining
- keep a linked list in each bucket
- given a key $x$, perform insert/delete in the list in $A[h(x)]$
- $A[h(x)] $returns a list


### Open Addressing
- hash function now specifies a succession $h_1(x), h_2(x), ...$
- keep trying until find an open slot


## Parameters
### Number of buckets
- should be prime
- and not close to a power of 2 or 10

### Load factor
- $\alpha$ = number of objects / number of buckets
- for good performance, need to control load


## Applications
### De-duplication
- given: a "stream" of objects
- goal: ignore duplicates 

solution
- when a new object $x$ arrives
- look $x$ up in the hash table $H$
- if not found, insert $x$ into $H$


### 2-sum problem
input
- unsorted array $A$ of $n$ integers
- target sum $t$

goal
- determine if there are two numbers $x, y \in A$
- such that $x + y = t$

solution
- insert elements of $A$ into hash table $H$ ($\Theta(n)$ time)
- for each $x \in A$ lookup $l - x$ ($\Theta(n)$ time)
 

### Symbol tables in compilators
- historical application 
etc 



## Implementation
Simplest implementation in Java:

```java
public class HashTable {
    private final int buckets;
    private HashTableNode[] hashTable;

    public HashTable(int buckets) {
        this.buckets = buckets;
        this.hashTable = new HashTableNode[buckets];
    }

    public void add(int i) {
        if (|  contains(i)) { |            int hash = h(i); |            HashTableNode oldNode = hashTable[hash];
            hashTable[hash] = new HashTableNode(oldNode, i);
        }
    }

    public void remove(int i) {
        if (|  contains(i)) { |            return; |        }

        int hash = h(i);
        HashTableNode prevNode = hashTable[hash];

        if (prevNode.getValue() == i) {
            hashTable[hash] = prevNode.getNext();
            return;
        }

        HashTableNode node = prevNode.getNext();
        while (node |  = null) { |            if (node.getValue() == i) { |                prevNode.setNext(node.getNext());
                return;
            }

            prevNode = node;
            node = node.getNext();
        }
    }

    public boolean contains(int i) {
        HashTableNode node = hashTable[h(i)];
        while (node |  = null) { |            if (node.getValue() == i) { |                return true;
            }
            node = node.getNext();
        }
        return false;
    }

    private int h(int number) {
        return Math.abs(number) % buckets;
    }
}

public class HashTableNode {
    private int value;
    private HashTableNode next;

    public HashTableNode(HashTableNode next, int value) {
        this.next = next;
        this.value = value;
    }

    public int getValue() {
        return value;
    }

    public HashTableNode getNext() {
        return next;
    }

    public void setNext(HashTableNode next) {
        this.next = next;
    }
}
```


## See also
- [Bloom Filters](Bloom_Filters)

## Sources
- [Algorithms Design and Analysis Part 1 (coursera)](Algorithms_Design_and_Analysis_Part_1_(coursera))
