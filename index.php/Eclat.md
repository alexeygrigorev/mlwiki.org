---
title: Eclat
layout: default
permalink: /index.php/Eclat
---

# Eclat

## Eclat
This is an algorithm for [Frequent Pattern Mining](Frequent_Pattern_Mining) based on [Depth-First Search](Depth-First_Search) traversal of the itemset [Lattice](Lattice)
- but it's rather a DFS traversal of the prefix tree than lattice
- and the [Branch and Bound](Branch_and_Bound) method is used for stopping


### Downward Closure
This method uses the property of this Lattice: 
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/ufrt/kddm/downward-closure.png" alt="Image">
- $X \subseteq Y, \text{supp}(Y) = t \Rightarrow \text{supp}(X) \geqslant t$
- $X \supseteq Y, \text{supp}(X) < \text{min_t} \Rightarrow \text{supp}(Y) < \text{min_t}$



### Idea
- TidList - list of transaction identifiers
- represent each item $i$ as a list of transaction where it participated ("inverted list")
- and calculate support as the size of intersection of TidLists


Example
- items ${a,b,c,d,e,f}$
- 4 transactions: $T_1: abc, T_2: acdef, T_3: abc, T_4: de$
- $N = 4$, # of transactions

TidLists: 
- $\text{Tid}(a) = \{ T_1, T_2, T_3 \}$
- $\text{Tid}(b) = \{ T_1, T_3 \}$
- $\text{Tid}(c) = \{ T_1, T_2, T_3 \}$
- $\text{Tid}(d) = \{ T_2, T_4 \}$
- $\text{Tid}(e) = \{ T_2, T_4 \}$
- $\text{Tid}(f) = \{ T_2 \}$

Support:
- $\text{supp}(ab) = \cfrac{\big|  \text{Tid}(a) \cap \text{Tid}(b) \big |

## Eclat Algorithm
### Algorithm
Eclat(prefix $X$, items $I$)
- let $C$ be candidate itemsets and remove non-frequent items of $C$
- $C = \big\{ X \cup {i} \ |  \ \forall i \in I \ : \ \text{freq}(X \cup {i}) \geqslant \text{min_th} \big\}$ |- $F = \varnothing$
- $C_\text{it} \leftarrow C$
- for each frequent item $i$ added to $C$
  - let $X_i = X \cap \{i\}$
  - update $C_\text{it} = C_\text{it} - \{ i \}$
  - $F \leftarrow F + X_i + \text{Eclat}(X_i, C_\text{it})$
- return $F$

```scdoc
th = 2

def eclat(prefix, items, D):
    if not items: return
    candidates = [(prefix |  {i}, frequency(D, prefix | {i}), i) |                  for i in items if i not in prefix]
    frequent = filter(lambda x: x[1] >= th, candidates)

    for new_prefix, freq, i in frequent:
        frequent_items.append(new_prefix)
        items = items - {i}
        eclat(new_prefix, items, D)

eclat(set(), set(I), D)
```


### Example
- items ${a,b,c,d,e,f}$
- threshold $t = 3$
- 4 transactions 
  - $\{ abc, acdef, abc, de \}$
- notation: (item to add; prefix $\to$ frequency(prefix))


Let's run the algorithm on this input:
# eclat(prefix: $\{\}$, items: $acbedf$) (step 1)
#*  candidates $(a: a \to 3), (c: c \to 3), (b: b \to 2), (e: e \to 2), (d: d \to 2), (f: f \to 1)$
#*  frequent patterns $(a: a \to 3), (c: c \to 3), (b: b \to 2), (e: e \to 2), (d: d \to 2)$
#*  adding $a$ to $F$
# eclat(prefix: $a$, items: $cbedf$) (step 2)
#*  candidates $(c: ac \to 3), (b: ab \to 2), (e: ae \to 1), (d: ad \to 1), (f: af \to 1)$
#*  frequent patterns $(c: ac \to 3), (b: ab \to 2)$
#*  adding $ac$ to $F$
# eclat(prefix: $ac$, items: $bedf$) (step 3)
#*  candidates $(b: acb \to 2), (e: ace \to 1), (d: acd \to 1), (f: acf \to 1)$
#*  frequent patterns $(b: acb \to 2)$
#*  adding $acb$ to $F$
# eclat(prefix: $acb$, items: $edf$) (step 4)
#*  candidates $(e: acbe \to 0), (d: acbd \to 0), (f: acbf \to 0)$
#*  frequent patterns $\{\}$
#*  adding $ab$ to $F$
# eclat(prefix: $ab$, items: $edf$) (step 5)
#*  candidates $(e: abe \to 0), (d: abd \to 0), (f: abf \to 0)$
#*  frequent patterns $\{\}$
#*  adding $c$ to $F$
# eclat(prefix: $c$, items: $bedf$) (step 6)
#*  candidates $(b: cb \to 2), (e: ce \to 1), (d: cd \to 1), (f: cf \to 1)$
#*  frequent patterns $(b: cb \to 2)$
#*  adding $cb$ to $F$
# eclat(prefix: $cb$, items: $edf$) (step 7)
#*  candidates $(e: cbe \to 0), (d: cbd \to 0), (f: cbf \to 0)$
#*  frequent patterns $$
#*  adding $b$ to $F$
# eclat(prefix: $b$, items: $edf$) (step 8)
#*  candidates $(e: be \to 0), (d: bd \to 0), (f: bf \to 0)$
#*  frequent patterns $\{\}$
#*  adding $e$ to $F$
# eclat(prefix: $e$, items: $df$) (step 9)
#*  candidates $(d: ed \to 2), (f: ef \to 1)$
#*  frequent patterns $(d: ed \to 2)$
#*  adding $ed$ to $F$
# eclat(prefix: $ed$, items: $f$) (step 10)
#*  candidates $(f: edf \to 1)$
#*  frequent patterns $\{\}$
#*  adding $d$ to $F$
# eclat(prefix: $d$, items: $f$) (step 11)
#*  candidates $(f: df \to 1)$
#*  frequent patterns $\varnothing$

Result
: $[a, ac, acb, ab, c, cb, b, e, ed, d]$



### Algorithm with TidList
To be able to calculate support quicker, 
- use TidList




## Links
### Presentations
- http://www.analysis-of-patterns.net/files/bgoethals.pdf

### Implementations
- http://www.borgelt.net/eclat.html
- http://adrem.ua.ac.be/sites/adrem.ua.ac.be/files/code/eclat.py


## See Also
- [Local Pattern Discovery](Local_Pattern_Discovery)
- [Frequent Pattern Mining](Frequent_Pattern_Mining)
- [Apriori](Apriori)

## Sources
- [Data Mining (UFRT)](Data_Mining_(UFRT))

[Category:Rule Mining](Category_Rule_Mining)
[Category:Python](Category_Python)