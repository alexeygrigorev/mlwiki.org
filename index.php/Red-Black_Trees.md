---
title: "Red-Black Trees"
layout: default
permalink: /index.php/Red-Black_Trees
---

# Red-Black Trees

{{stub}}

## Red-Black trees
In [Binary Search Trees](Binary_Search_Trees) the worst case running time depends on the height of a tree. How we can make sure the tree doesn't turn into a linked list - and is kept balanced? 

Idea
- the height is maintained at $O(\log n)$
- therefore all operations are in $O(\log n)$

## Red-Black invariants
- each node is red or black
- root is black
- not 2 reds in a row
  - red node => only black children
- every path from the root to NULL-nodes passed the same amount of black nodes

## Operations
All the operations expect insert and delete are performed as usual in [Binary Search Trees](Binary_Search_Trees)


## See also
- [Binary Search Trees](Binary_Search_Trees)

## Sources
- [Algorithms Design and Analysis Part 1 (coursera)](Algorithms_Design_and_Analysis_Part_1_(coursera))


[Category:Algorithms](Category_Algorithms)
[Category:Data Structures](Category_Data_Structures)