---
layout: default
permalink: /index.php/Mini-Batch_K-Means
tags:
- cluster-analysis
- machine-learning
title: Mini-Batch K-Means
---

## Mini-Batch K-Means

```latex
\begin{algorithm}
\caption{MiniBatch $K$-Means}
\label{algo:minibatch-k-means}

\begin{algorithmic}[0]
  \Statex
  \Function{MiniBatch-K-Means}{no. clusters $k$, no. iterations $t$, batch size $b$, documents $\mathcal D$}
    \For{$j \leftarrow 1 \ .. \ k$} \Comment{random initialization}
      \Let{$\boldsymbol \mu_j$}{random $\mathbf d \in \mathcal D$}
    \EndFor

    \Repeat{\ $t$ times}
      \Let{$\mathcal M$}{$b$ random examples from $\mathcal D$}

      \For{each $\mathbf d_i \in \mathcal M$}
        \Let{$\text{centroids}[\mathbf d_i]$}
            {$\operatorname{arg\, min}_j \| \mathbf d_i - \boldsymbol \mu_j \|^2$}
             \Comment{cache the centroid nearest to $\mathbf d_i$}
      \EndFor

      \For{each $\mathbf d_i \in \mathcal M$}
        \Let{$c_i$}{$\text{centroids}[\mathbf d_i]$}
                                       \Comment{the centroid index of document $\mathbf d_i$}
        \Let{$v[c_i]$}{$v[c_i] + 1$}   \Comment{counts per centroid $c_i$}
        \Let{$\eta$}{$1 / v[c_i]$}     \Comment{per-centroid learning rate}
        \Let{$\boldsymbol \mu_{c_i}$}
        {$(1 - \eta) \cdot \boldsymbol \mu_{c_i} + \eta \cdot \mathbf d_i$}
                                        \Comment{gradient step}
      \EndFor
    \Until{converged}

    \State \Return{$(c_1, c_2, \ ... \ , c_n)$}
  \EndFunction
\end{algorithmic}
\end{algorithm}
```
