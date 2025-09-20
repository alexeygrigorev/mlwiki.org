---
layout: default
permalink: /index.php/Term_Contribution
tags:
- feature-selection
title: Term Contribution
---
## Term Contribution
Idea: result of clustering highly depends on how similar are documents

so contribution of a term $t$ is how much it contributes to similarity of two documents

Text clustering is highly dependent on the documents similarity.
- Suppose use a [Dot Product](Dot_Product) based similarity:
- $\text{similarity}(d_i, d_j) =  \sum_{t \in V} f(t, d_i) \times f(t, d_j)$
  - where $f(t, d)$ represents the weight of term $t$ in document $d$


The contribution of each term is the overall contribution to documents’ similarities and shown by the following equation:

- $\text{TC}(t) = \sum_{i,j} f(t, d_i) \times f(t, d_j)$


It's slow - $O(n^2)$
- sample to speed it up



## Sources
- Liu, Tao, et al. "An evaluation on feature selection for text clustering." ICML. Vol. 3. 2003. [http://www.aaai.org/Papers/ICML/2003/ICML03-065.pdf]
- Aggarwal, Charu C., and ChengXiang Zhai. "A survey of text clustering algorithms." Mining Text Data. Springer US, 2012. [http://ir.nmu.org.ua/bitstream/handle/123456789/144935/d1784ebed3eab2708026b202b2b65309.pdf?sequence=1#page=90]
- http://cs.gmu.edu/~carlotta/teaching/INFS-795-s05/readings/INFS795_MCayci.ppt
