---
layout: default
permalink: /index.php/Non-Negative_Matrix_Factorization
tags:
- linear-algebra
- matrix-decomposition
- python
title: Non-Negative Matrix Factorization
---
## Non-Negative Matrix Factorization
Non-Negative Matrix Factorization (NMF) is a [Matrix Decomposition](Matrix_Decomposition) technique that is especially good for [Cluster Analysis](Cluster_Analysis)



## Algorithms for Computing NMF
See Lee2001
- Norm Minimization (NMF-ED)
- [KL Divergence](KL_Divergence) Minimization (NMF-KL)


### Norm Minimization Algorithm
Let $A$ be an $m \times n$ matrix 
- we want to find $k$-rank approximation of $A$ (or, in other words, create $k$ clusters)


to do this, we want to find matrices $U$ and $V$ s.t. 
- $J = \cfrac{1}{2} \|  A - U V^T \|_F$ where the norm is the [Frobenius Norm](Frobenius_Norm) |- $U$ is $m \times k$ matrix
- $V$ is $n \times k$ matrix 
- columns of $V$ are the basis 

- as we minimize $J$ we get $UV^T \approx A$
- if $\mathbf a$ is a row of $A$, then $\mathbf a \approx \mathbf u V^T$ where $u$ is a corresponding row of $U$
- so $\mathbf a$ is rewritten using the basis from the columns of $V$ 


This can be solved analytically
- for any matrix $Q$, $\|  Q \|_F = \text{tr}(QQ^T)$, where $\text{tr}(QQ^T)$ is the [Trace](Trace_(Matrix)) of $QQ^T$ (see properties of [Frobenius Norm](Frobenius_Norm)) |- so $J = 0.5 \text{tr}\Big( (A - UV^T)^T \, (A - UV^T) \Big) = \text{tr}\Big( AA^T - 2 A U V^T + U V^T V U^T \Big) = \frac{1}{2} \, \text{tr} (AA^T) - \text{tr}(A U V^T) + 0.5 \text{tr}(U V^T V U^T)$
- additionally, we have constraints $u_{ij} \geqslant 0$, $v_{ij} \geqslant 0$: use [Lagrange Multipliers](Lagrange_Multipliers) for this
- let $\boldsymbol \alpha$ be a matrix of $\alpha_{ij}$ of the same dimension as $U$ and $\boldsymbol \beta$ be a batrix of $\beta_{ij}$ of the same dimension as $V$ 
- note that $\text{tr}(\boldsymbol \alpha \, U^T) = \sum_{ij} \alpha_{ij} u_{ij}$ and $\text{tr}(\boldsymbol \alpha \, U^T) = \sum_{ij} \alpha_{ij} u_{ij}$ - so we'll use them as lagrangian constraints


Let's solve it:
- $L = J + \text{tr}(\boldsymbol \alpha U^T) + \text{tr}(\boldsymbol \beta V^T)$
- $\cfrac{\partial L}{\partial U} = -AV + U V^T V + \boldsymbol \alpha = 0$
- $\cfrac{\partial L}{\partial V} = -A^T V + V U^T U + \boldsymbol \beta = 0$


The [KTT Condition](KTT_Condition) $\alpha_{ij} \, u_{ij} = 0$ and $\beta_{ij} \, v_{ij} = 0$:
- $(AV)_{ij} \cdot u_{ij} - (U V^T V)_{ij} \cdot u_{ij} = 0$
- $(A^T U)_{ij} \cdot v_{ij} - (V U^T U)_{ij} \cdot v_{ij} = 0$
- these are independent of $\boldsymbol \alpha$ and $\boldsymbol \beta$


So we have the following update rule:
- $u_{ij} = \cfrac{(AV)_{ij} \cdot u_{ij}}{(U V^T V)_{ij}}$
- $v_{ij} = \cfrac{(A^T U)_{ij} \cdot v_{ij}}{(V U^T U)_{ij}}$


## [SVD](SVD) vs NMF
- SVD: basis is orthonormal, NMF is not
- components of NMF are always non-negative
- vectors in the basis of NMF directly correspond to clusters 
- we can learn cluster membership by taking the largest component of the vector (in the new representation)




## Applications
### [Latent Semantic Analysis](Latent_Semantic_Analysis)
Why SVD is bad for LSA?
- if want to apply [Cluster Analysis](Cluster_Analysis) to cluster documents in the semantic space produced by SVD, need to use an external algorithm, e.g. [K-Means](K-Means)
- negative values are hard to interpret
- objective of SVD is to find the orthogonal basis, which doesn't always result in a good basis for the Semantic Space:
- <img src="http://i.stack.imgur.com/PMhBY.png" alt="Image"> (source: Xu2003)


Can use NMF instead of [SVD](SVD) to reveal the latent structure and find the Semantic Space
- if $k$ is small (compared to original $n$), then NMF is bound to discover latent structure (i.e. "topics") in data
- non-negativity is good for interpretability:
- it ensures that documents can be interpreted as non-negative combination of the key concepts (topics/clusters)
- it can find clusters for both terms and documents: columns of $V$ are basis for docs, columns of $U$ are basis for terms




### [Document Clustering](Document_Clustering)
Assumptions:
- there are clusters of documents that correspond to coherent topics
- suppose we have a [document-term matrix](Vector_Space_Model) $D$ 
- and want to project documents (rows of $D$) to a $k$-dimensional semantic space 
- i.e. we want to represent each document as a linear (non-negative) combination of $k$ topics 


Result of NMF can be interpreted as clustering directly:
- decide on cluster membership by finding the base topic with greatest projection value
- can also be [fuzzy](Fuzzy_Clustering): e.g. take all topics larger than some projection value



## Local NMF
It's a variant of NMF (Li2001)
- in usual NMF vectors are not orthogonal and may be more similar to each other than desired
- LNMF addresses this issue


3 additional constants on $U$ and $V$ that aim to find the local features in the original matrix
- max sparsity in $V$: want to have as many 0's as possible
- expressiveness of $U$: retain only those components of $U$ that carry most information about the matrix
- max orthogonality of $U$ 


Results reported by Osinski2006:
- slow convergence 
- not good for [Information Retrieval](Information_Retrieval) clustering because of sparsity 


## Implementation
### NMF-ED in Python/Numpy
NMF-ED = Euclidean distance minimization 
- Algorithm from Lee1999

```python
import numpy as np

def seung_objective(V, W, H):
    ''' calculated the non-negative matrix factorization objective
        
    Usage:
        W, H = seung_update(V, W, H)
    Parameters:
        V: a (d x n)-array containing n observations in the columns
        W: (d x k)-array of non-negative basis images (components)
        H: (k x n)-array of weights, one column for each of the n observations
    Returns:
        F: a scalar objective
    '''    
    d, n = V.shape
    WH = np.dot(W, H)

    F = (V * np.log(WH) - WH).sum() / (d * n)
    return F


def seung_updateW(V, W, H):
    ''' performs the multiplicative non-negative matrix factorization updates for W
        
    Usage:
        W, H = seung_update(V, W, H)
    Parameters:
        V: a (d x n)-array containing n observations in the columns
        W: (d x k)-array of non-negative basis images (components)
        H: (k x n)-array of weights, one column for each of the n observations
    Returns:
        W: (d x k)-array of updated non-negative basis images (components)
    '''
    
    WH = np.dot(W, H)
    W_new = W * np.dot(V / WH, H.T)
    W_new = W_new / np.sum(W_new, axis=0, keepdims=True)    
    return W_new

def seung_updateH(V, W, H):
    ''' performs the multiplicative non-negative matrix factorization updates
        
    Usage:
        W, H = seung_update(V, W, H)
    Parameters:
        V: a (d x n)-array containing n observations in the columns
        W: (d x k)-array of non-negative basis images (components)
        H: (k x n)-array of weights, one column for each of the n observations
    Returns:
        H: (k x n)-array of updated weights, one column for each of the n observations
    '''
    
    WH = np.dot(W, H)
    H_new = H * np.dot((V / WH).T, W).T
    return H_new


def seung_nmf(V, k, threshold=1e-5, maxiter=500):
    ''' decomposes X into r components by non-negative matrix factorization
        
    Usage:
        W, H = seung_nmf(X, r)
    Parameters:
        V: a (d x n)-array containing n observations in the columns
        k: number of components to extract
        threshold: relative error threshold of the iteration
        maxiter: maximum number of iterations
    Returns:
        W: (d x k)-array of non-negative basis images (components)
        H: (k x n)-array of weights, one column for each of the n observations
    '''
    
    d, n = V.shape
    W = np.random.rand(d, k)
    H = np.random.rand(k, n)
    F = seung_objective(V, W, H)
    
    it_no = 0
    converged = False

    while (not converged) and it_no <= maxiter:
        W_new = seung_updateW(V, W, H)
        H_new = seung_updateH(V, W_new, H)    
        F_new = seung_objective(V, W_new, H_new)

        converged = np.abs(F_new - F) <= threshold 
        W, H = W_new, H_new
        it_no = it_no + 1
    
    return W, H
```


## References
- Lee, Daniel D., and H. Sebastian Seung. "Learning the parts of objects by non-negative matrix factorization." 1999. [http://john.cs.olemiss.edu/~ychen/courses/CSCI582S07/seung-nonneg-matrix.pdf]
- Lee, Daniel D., and H. Sebastian Seung. "Algorithms for non-negative matrix factorization." 2001. [http://papers.nips.cc/paper/1861-alg]
- Li, Stan Z., et al. "Learning spatially localized, parts-based representation." 2001. [http://cvl.ice.cycu.edu.tw/meeting/2008.12.02.pdf]

## Sources
- Aggarwal, Charu C., and ChengXiang Zhai. "A survey of text clustering algorithms." Mining Text Data. Springer US, 2012. [http://ir.nmu.org.ua/bitstream/handle/123456789/144935/d1784ebed3eab2708026b202b2b65309.pdf?sequence=1#page=90]
- Xu, Wei, Xin Liu, and Yihong Gong. "Document clustering based on non-negative matrix factorization." 2003. [http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.117.2293&rep=rep1&type=pdf]
- Osinski, Stanislaw. "Improving quality of search results clustering with approximate matrix factorisations." 2006. [http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.107.74&rep=rep1&type=pdf]
- [Python for Machine Learning (TUB)](Python_for_Machine_Learning_(TUB))
