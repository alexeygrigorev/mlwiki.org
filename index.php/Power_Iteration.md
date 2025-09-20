---
layout: default
permalink: /index.php/Power_Iteration
tags:
- linear-algebra
- machine-learning
- python
title: Power Iteration
---
## Power Iteration
This is a linear algebra method for computing [Eigenvalues and Eigenvectors](Eigenvalues_and_Eigenvectors)


## Symmetric Matrices
Suppose $A$ is symmetric
- then [Eigendecomposition](Eigendecomposition) of $A$ is $A = Q \Lambda Q^T$ 
- and $A^k = Q \Lambda^k Q^T$
- let $\mathbf q_i$ be the columns of $Q$

When $k \to \infty$
- suppose $\lambda_1 > \lambda_2$, 
- then, as $k$ increases, $\lambda_1^k / \lambda_i^k \to 0$ for $i \geqslant 2$ 
- so $A^k \to \lambda_1^k \mathbf q_1 \mathbf q_1^T$
- so we can find $\lambda_1$ by powering $A$ 


Performance:
- computing $A \cdot A^{k-1}$ is costly
- instead, can compute $A \, A^{k-1} \mathbf x$ where $\mathbf x$ is some random unit vector
- $A^k \mathbf x \approx \lambda_1^k \, \mathbf q_1 \, (\mathbf q_1^T \mathbf x) = \alpha \cdot \mathbf q_1$
- so it's some scalar times a unit vector $\mathbf q_1$
- thus, to recover $\mathbf q_i$, use $A^k \mathbf x / \|  A^k \mathbf x \| = \mathbf q_i$ |

## Finding Other Eigenvectors
- $A = Q \Lambda Q^T$, so $A = \sum_{i = 1}^n \lambda_i \mathbf q_i \mathbf q_i^T$
- use power iteration to find $\mathbf q_1$ and $\lambda_1$
- then let $A_2 \leftarrow A - \lambda_1 \mathbf q_1 \mathbf q_1^T$ 
- repeat power iteration on $A_2$ to find $\mathbf q_2$ and $\lambda_2$
- continue like this for $\lambda_3, \ ... \ , \lambda_n$



## Issues
- if $\lambda_1 - \lambda_2 \gg 0$, then it's fine, but if $\lambda_1 - \lambda_2$ is small, it will take a lot of time to converge


## Implementation
### NumPy
```python
def eigenvalue(S, w):
    return w.T.dot(S).dot(w)

def power_iteration(X, debug=True):
    n, d = X.shape
    converged = False

    S = X.T.dot(X)
    w = np.ones(d) / np.sqrt(d)
    error = eigenvalue(S, w)

    while not converged:
        Sw = S.dot(w)
        w_new = Sw / np.linalg.norm(Sw)

        error_new = eigenvalue(S, w_new)
        converged = np.abs(error - error_new) < 0.01
    
        w = w_new
        error = error_new

    return w
```


### Mahout Samsara
```javascript
var x: Vector = 1 to dim map (_ => 1.0 / Math.sqrt(dim))
var converged = false

while (|  converged) { |  val Ax = A %*% x |  var x_new = Ax.collect(::, 0)
  x_new = x_new / x_new.norm(2)

  val diff = (x_new - x).norm(2)
  converged = diff < 1e-6
  x = x_new
}
```


## Applications
- [Principal Component Analysis](Principal_Component_Analysis)
- [Stochastic Matrices](Stochastic_Matrices) and [PageRank](PageRank)


## Sources
- Hopcroft, John, and Ravindran Kannan. "Foundations of Data Science1." (2014) [http://research.microsoft.com/en-US/people/kannan/book-mar-30-2014.pdf]
- [Machine Learning 1 (TUB)](Machine_Learning_1_(TUB))
