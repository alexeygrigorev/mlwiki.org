---
title: "Binary Search Trees"
layout: default
permalink: /index.php/Binary_Search_Trees
---

# Binary Search Trees

## Binary search trees
Binary search trees are [Tree](Tree)s with rank = 2.

Operations on a sorted array
- Search $\Theta(\log n)$
- Select $O(1)$
- min/max $O(1)$
- pred/succ $O(1)$
- rank $O(\log n)$
- insertion/deletion $\Theta(n)$

Is there a data structure that allows better insertion and deletes? 

Balanced trees:
- operations like on sorted arrays
- but with fast (logarithmic) inserts and deletes

Basic version of node
- left child pointer
- right child pointer
- parent pointer

Search tree property: for a node with element $x$ 
- on the left - all elements are less than $x$
- on the right - all elements are greater than $x$


Height
- from $\approx \log_2 n$ to $\approx n$
- worst case - $\approx n$, like a chain
- to avoid the worst case we need trees that can rebalance themselves
  - [Red-Black Trees](Red-Black_Trees)


## Operations
### Search
Search($k$):
- start at the root
- if $k < \text{key}$, go left
- if $k > \text{key}$, go right
- return node with key $k$ or $\text{null}$


### Insert
Insert($k$):
- search for $k$
- rewrite final $\text{null}$ pointer to point to new node with key $k$

worst-case running time $O(\text{height})$


### Min (Max)
Min($k$)/Max($k$):
- start at root
- and follow left (right) child pointer


### Pred
Pred should return next smallest element after given

Pred($k$):
- if $k$'s subtree is not empty, return the max key in the left subtree
- or follow parent pointer until you get a key less than $k$

### In-Order Traversal
goal: to print out keys in increasing order

Traverse():
- recurse on the left tree
- print current node's key
- recurse on the right tree

running time $O(n)$


### Deletion
Delete($k$):
- search for $k$
- if $k$ has no children
  - just delete the node
- if $k$ has one child
  - the child gets the pointer of $k$
- if $k$ has 2 children
  - compute $k$'s predecessor $l$
    - traverse $k$'s non-NULL left child pointer
    - then right-child pointer
    - until no longer possible
  - swap $k$ and $l$
  - in a new position it's easy to delete $k$
    - it has no left child


### Select
goal: to retrieve $i$th order statistics

Need to store additional information for that
- $\text{size}(x)$ - number of subtree nodes at subtree rooted at $x$
- $\text{size}(x) = \text{size}(l) + \text{size}(r) + 1$

Select($i$):
- start at root $x$ with left child $\text{lt}$ and right child $\text{rt}$
- $a = \text{size(lt)}$
- if $a = i - 1$
  - return $x$'s key
- if $a \geqslant i$
  - recursively compute $i$th order statistics on $\text{lt}$
- if $a \leqslant i - 1$
  - recursively compute $(i - a - 1)$th order statistics on $r$

running time $\Theta(\text{height})$


### Rank
Goal: to compute how many keys are less or equal to that value

Rank:
- $a$ = size(lt)
- return $a + 1$


## See also
- [Heap](Heap)
- [Red-Black Trees](Red-Black_Trees)

## Sources
- [Algorithms Design and Analysis Part 1 (coursera)](Algorithms_Design_and_Analysis_Part_1_(coursera))


[Category:Algorithms](Category_Algorithms)
[Category:Data Structures](Category_Data_Structures)