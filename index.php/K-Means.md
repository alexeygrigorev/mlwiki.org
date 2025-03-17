---
title: K-Means
layout: default
permalink: /index.php/K-Means
---

# K-Means

## $K$-Means
This is the most popular [clustering](Cluster_Analysis) algorithm 


## Lloyd Algorithm
Lloyd algorithm is the most popular way of implementing k-means 


### Algorithm
- First we choose $k$ - the number of clusters we want to get
- Then we randomly initialize k cluster centers (cluster centroids)

This is an iterative algorithm, and on each iteration it does 2 things 
- cluster assignment step
- move centroids step

Cluster Assignment Step:
- go through each example and choose the closest centroids 
- and assign the example to it

Move Centroids Step:
- Calculate the average for each group
- and move the centroids there

Repeat this until converges 


### Pseudo Code
$k$-means($k$, $\{ \mathbf x_i \}$):
- randomly initialize $k$ cluster centroids $\boldsymbol \mu = \Big( \mu_1, \mu_2, \, ... \, , \mu_k \Big) \in \mathbb{R}^{k + 1}$
- repeat: 
- cluster assignment step:
  - for $i = 1$ to $m$:
  - $c_i \leftarrow$ closest to $\mathbf x_i$ centroid using [Euclidean Distance](Euclidean_Distance) $\text{dist} = \|  \mathbf x_i - \boldsymbol \mu_i \|^2$ |- move centroids step: 
  - for $i = 1$ to $k$:
  - $\boldsymbol \mu_k \leftarrow$ average of all points assigned to $c_k$


### Optimization Objective
Let's have the following notation 
- $c_i \in \{ 1, 2, \ ... \ , k \}$ - index of cluster to which example $\mathbf x_i$ is assigned
- $\boldsymbol \mu_k$ - cluster centroid $k$ ($\boldsymbol \mu_k \in \mathbb{R}^n$)
- $\mu_{c_i}$ - cluster centroid of example $\mathbf x_i$

e.g. 
- $\mathbf x_i$ is assigned to $5$
- $c_i = 5$ and
- $\mu_{c_i} = \boldsymbol \mu_5$


So optimization objective (cost function, or sometimes called ''distortion''): 
- $J(c_1, \ ... \ , c_m, \boldsymbol \mu_1, \ ... \ , \boldsymbol \mu_k) = \cfrac{1}{m} \sum_i \left\|  \mathbf x_i - \boldsymbol \mu_{c_i} \right\|^2$ |

we want to find $\min J(c_1, \ ... \ , c_m, \boldsymbol \mu_1, \ ... \ , \boldsymbol \mu_k)$ with respect to $c_1, \ ... \ , c_m, \boldsymbol \mu_1, \ ... \ , \boldsymbol \mu_k$
- cluster assignment - minimizes $J$ 
  - with $c_1, \ ... \ , c_m$
  - holding $\boldsymbol \mu_1, \ ... \ , \boldsymbol \mu_k$ fixed
- move centroids - minimizes $J$  
  - with $\boldsymbol \mu_1 \ , ... \ , \boldsymbol \mu_k$
  - holding $c_1, \ ... \ , c_m$ fixed



### Seed Selection
Seed selection is the process of selecting the initial centroids 



## Implementation Notes
### Random Initialization
How to initialize centroids $\mu = \Big( \boldsymbol \mu_1, \boldsymbol \mu_2, \, ... \, , \boldsymbol \mu_k \Big)$?
- should have $k < m$
- randomly pick $k$ training examples
- set $\boldsymbol \mu_1, \ ... \ , \boldsymbol \mu_k$ to these $k$ examples


Different clusters
- So $k$-means may converge to different clusters depending on how the centroids were initialized 
- Particularly it may end up in a local optimum - and the split won't be the best 
- what we can do is to try it several times and choose the best 


'''Algorithm''':
- repeat $n$ times (typically 50 - 1000)
  - randomly initialize $k$ centroids 
  - run k-means, get $c_1, \ ... \ , c_m, \boldsymbol \mu_1, \ ... \ , \boldsymbol \mu_k$
  - compute the cost function $J$
- pick clustering with lowest cost


If the number of clusters $k$ is 2-10 then the random initialization makes sense, otherwise - probably not



### No Data Assigned
If at iteration step we end up with a cluster with no assigned data points, we can:
- get rid of it - look for $k-1$ clusters at the next step (advised)
- randomly re-initialize that cluster centroid (if you really want $k$ clusters)


## Choosing the Number of Clusters
How to choose $k$? 
- manually - by looking at the data (best)
- other methods: e.g. the Elbow Method


### Elbow Method
We can plot values of our distortion function for different $k$
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/legacy/kmeans-elbow.png" alt="Image">
- at first it goes down rapidly
- then goes down slowly 
- this is called an "elbow"
- so in this case we choose $k = 3$ because of the elbow


### Domain Knowledge
But often it gives a smooth curve with no visible elbow
- In this case you need to use a metrics how well it performs for a particular purpose
- Use domain knowledge, if possible, to come up with good $k$



## Disadvantages
- Quite sensitive to initial seeds - so may need to choose them carefully
- For high dimensional data such as [documents](Document_Clustering) may be not practical
  - centroids may contain lots of words - but we usually want to have sparse centroids
- doesn't perform well on data with outliers or with clusters of different sizes or shapes



## Seed Selection
Seed selection procedure is very important 
- K-means is sensitive to the initial position (which is why in random initialization we run it many times)
- especially it's noticeable in data with high dimensionality


Can try do it smarter than random
- e.g. sample and then select seeds using [Hierarchical Clustering](Hierarchical_Clustering) (like in [Scatter/Gather](Scatter_Gather))
- if have some partial knowledge about labels - use it (it'll be so-called [Semi-Supervised Clustering](Semi-Supervised_Clustering))


### K-Means++
It's a smart way of doing seed selection
- see http://en.wikipedia.org/wiki/K-means%2B%2B


## Variants
=== [Weighted K-Means](Weighted_K-Means) === 
Objective:
- $$J(\boldsymbol \mu_1, \dots, \boldsymbol \mu_K) = \cfrac{\sum_{i} w_i \min_k \|  \mathbf x_i- \boldsymbol \mu_k\|^2}{\sum_{i} w_i},$$ |- $\boldsymbol \mu_i$ is $i$ centroid 
- $w_i$ is weight assigned to each $\mathbf x_i$


Solution:
- Expectation step:
  - Find the nearest centroid for each data point:
  - $$\forall \ 1 \leqslant k \leqslant K: \quad \mathcal{C}(k) \leftarrow \Big\{ i ~:~ k = \mathrm{arg}\min_k \|  \mathbf x_i - \boldsymbol \mu_k \|^2 \Big\}$$ |- Minimization step:
  - Recompute the centroid as a the (weighted) mean of the associated data points:
  - $$\forall \ 1 \leqslant k \leqslant K: \quad c_k \leftarrow \frac{\sum_{i \in \mathcal{C}(k)} w_i \cdot \mathbf x_i}{\sum_{i \in \mathcal{C}(k)} w_i}$$
- until $J$ converges


### [K-Medoids](K-Medoids)
Instead of mean, we take the "medoid" of each cluster to represent its centroid
- works better for non-euclidean distances than k-means


### Bisecting K-Means
This is a variant of K-Means 
- it's a [Hierarchical Clustering](Hierarchical_Clustering) method, and it's useful for [Document Clustering](Document_Clustering)


Algorithm:
- start with a single cluster
- repeat until have desired number of clusters
  - choose a cluster to split (e.g. the largest one)
  - find two subclusters using K-means with $k = 2$ and split 
  - may repeat this procedure several times and take the clusters with highest overall similarity


### [Scatter/Gather](Scatter_Gather)
- a special version of k-means for [Document Clustering](Document_Clustering)
- uses [Hierarchical Clustering](Hierarchical_Clustering) on a sample to do seed selection



### Approximate K-Means
- Philbin, James, et al. "Object retrieval with large vocabularies and fast spatial matching." 2007. [http://research.microsoft.com/pubs/64602/philbin07.pdf]


### Mini-Batch K-Means
Lloyd's classical algorithm is slow for large datasets (Sculley2010)
- Use [Mini-Batch Gradient Descent](Mini-Batch_Gradient_Descent) for optimizing K-Means
- reduces complexity while achieving better solution than [Stochastic Gradient Descent](Stochastic_Gradient_Descent)

Notation:
- $f(C, \mathbf x)$ returns the nearest centroid for $\mathbf x$


Algorithm:
- given $k$, batch size $b$, max. number of iterations $t$ and dataset $X$
- initialize each $\boldsymbol \mu$ with randomly selected elements from $X$ 
- repeat $t$ times:
- $M \leftarrow b$ random examples from $X$ 
- for $\mathbf x \in M$:
  - $d[\mathbf x] = f(C, \mathbf x)$ // cache the centroid nearest to $\mathbf x$
- for $\mathbf x \in M$:
  - $\boldsymbol \mu \leftarrow d[\mathbf x]$
  - $v[\boldsymbol \mu] = v[\boldsymbol \mu] + 1$ // counts per centroid
  - $\eta = 1 / v[\boldsymbol \mu]$ // per-centroid learning rate
  - $\boldsymbol \mu \leftarrow (1 - \eta) \cdot \boldsymbol \mu + \eta \cdot \mathbf x$ //gradient step


Can enforce sparsity by $L_1$ regularization: see Sculley2010


Implementation:
- [MiniBatchKMeans](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html) in scikit-learn


### [Fuzzy C-Means](Fuzzy_C-Means)
Modify the membership function s.t. it outputs the degree of association between item and cluster
- degree of membership to the cluster depends on the distance from the document to the cluster centroid


Reference:
- Bezdek, James C., Robert Ehrlich, and William Full. "FCM: The fuzzy c-means clustering algorithm." 1984. [http://web-ext.u-aizu.ac.jp/course/bmclass/documents/FCM%20-%20The%20Fuzzy%20c-Means%20Clustering%20Algorithm.pdf]



## Implementation
Usual version:

<code>D = distmat(X, C)</code> calculates the squared distance matrix $D$ between each $x_i \in X$ and each $\mathbf c_k \in C$

```scdoc
def distmat(X, C):    
    X2 = np.sum(X * X, axis=1, keepdims=True)
    C2 = np.sum(C * C, axis=1, keepdims=True)

    XC = np.dot(X, C.T)

    D = X2 - 2 * XC + C2.T
    return D
```

<code>A = closest(D)</code>: returns the closest centroid matrix $A$: with $(A)_{ik} = 1$ if $w_i \in c_k$ and $(A)_{ik} = 0$ if $w_i \not \in c_k$


```carbon
def closest(D):
    D_min = D.min(axis=1, keepdims=True)
    return (D == D_min).astype(int)
```


<code>C = new_centers(X, A, w)</code> calculates new centroids 

```tera term macro
def newcenters(X, A):
    summed = np.dot(X, A.T)
    counts = np.sum(A, 1)
    return summed / counts
```


For weighted k-means it would be 

```scdoc
def new_centers(X, A, w):
    W = A * w.reshape(-1, 1)
    weighted_sum = np.dot(W.T, X)
    weights = np.sum(W, axis=0).reshape(-1, 1)
    return weighted_sum / weights
```


Finally, the cost function for weights:

```scdoc
def J(X, D, w):
    D_min = D.min(axis=1)
    return (w * D_min).sum() / w.sum()
```


The algorithm:

```carbon
def kmeans(X, k):
    d, n = X.shape
    M_idx = np.random.choice(np.arange(n), k, replace=False)
    M = X[:, M_idx]
    
    converged = False
    while not converged:
        D = kmu.distmat(M, X)
        A = kmu.closest(D)
        M_new = kmu.newcenters(X, A)

        converged = np.abs(M_new - M).sum() <= 1e-8
        M = M_new    
    return M
```

With weighted <code>J</code>:

```scdoc
while not converged:
    D = distmat(X, M)
    M = closest(D)
    J_new = J(X, D, w)

    M_new = new_centers(X, A, w)
    converged = np.abs(J_new - J_old) <= 0.01

    M = M_new
    J_old = J_new
```


See ipython notebook for complete code:
- [sheet06-kmeans.ipynb](http://nbviewer.ipython.org/github/alexeygrigorev/notebooks/blob/master/studies/tub-ml1/sheet06-kmeans.ipynb) 


## Sources
- [Machine Learning (coursera)](Machine_Learning_(coursera))
- [Python for Machine Learning (TUB)](Python_for_Machine_Learning_(TUB))
- [Machine Learning 1 (TUB)](Machine_Learning_1_(TUB))
- Steinbach, Michael, George Karypis, and Vipin Kumar. "A comparison of document clustering techniques." 2000.
- Aggarwal, Charu C., and ChengXiang Zhai. "A survey of text clustering algorithms." Mining Text Data. Springer US, 2012. [http://ir.nmu.org.ua/bitstream/handle/123456789/144935/d1784ebed3eab2708026b202b2b65309.pdf?sequence=1#page=90]
- Oikonomakou, Nora, and Michalis Vazirgiannis. "A review of web document clustering approaches." 2010. [https://scholar.google.com/scholar?cluster=1261203777431390097&hl=ru&as_sdt=0,5]
- Sculley, David. "Web-scale k-means clustering." 2010. [http://www.ra.ethz.ch/CDstore/www2010/www/p1177.pdf]


[Category:Machine Learning](Category_Machine_Learning)
[Category:Unsupervised Learning](Category_Unsupervised_Learning)
[Category:Cluster Analysis](Category_Cluster_Analysis)
[Category:Python](Category_Python)