---
title: "Kernel Methods"
layout: default
permalink: /index.php/Kernel_Methods
---

# Kernel Methods

{{draft}} {{stub}}

## Kernel Methods

[Support Vector Machines](Support_Vector_Machines)



[Kernel](Kernel) is a generalized dot product 
- [Latent Semantic Analysis](Latent_Semantic_Analysis) captures semantic relations between terms 
- drawback: computationally expensive

[Kernel Methods](Kernel_Methods)
- data items are mapped into some high-dimensional space where we use [Inner Product](Inner_Product) for constructing models
- kernel acts as an "interface" between the model and the high-dimensional space
- by defining (often implicitly) a mapping function that transform the input space to some (possibly very high dimensional) feature space

Just dot product is enough for many algorithms:
- [Perceptron](Perceptron)
- [Principal Component Analysis](Principal_Component_Analysis) -> [Kernel PCA](Kernel_PCA)
- [Ridge Regression](Ridge_Regression) -> [Kernel Ridge Regression](Kernel_Ridge_Regression)





## Use of Kernels
### [Classification](Classification)
[Support Vector Machines](Support_Vector_Machines)

### [Text Mining](Text_Mining)
[Latent Semantic Kernels](Latent_Semantic_Kernels): Use [Latent Semantic Analysis](Latent_Semantic_Analysis)

### [Clustering Analysis](Clustering_Analysis)


### [Regression](Regression)
Support Vector Regression
- Smola, Alex J., and Bernhard Schölkopf. "A tutorial on support vector regression." 2004. [http://lasa.epfl.ch/teaching/lectures/ML_Phd/Notes/nu-SVM-SVR.pdf]


### [Anomaly Detection](Anomaly_Detection)

### [Gaussian Processes](Gaussian_Processes)

### [Kernel Density Estimation](Kernel_Density_Estimation)


## Kernels
### Data Span Solution
Choosing a kernel $\equiv$ choosing a feature space 
- $k(\mathbf x, \mathbf z) = \langle \varphi(\mathbf x), \varphi(\mathbf z) \rangle$
- given a dataset, apply $k$ to each pair and get a Kernel Matrix (also called [Gram Matrix](Gram_Matrix))

$$K = \begin{bmatrix}
k(\mathbf x_1, \mathbf x_1) & k(\mathbf x_1, \mathbf x_2) & \cdots & k(\mathbf x_1, \mathbf x_n) \\ 
k(\mathbf x_2, \mathbf x_1) & k(\mathbf x_2, \mathbf x_2) & \cdots & k(\mathbf x_2, \mathbf x_n) \\ 
\vdots & \vdots & \ddots & \vdots\\ 
k(\mathbf x_n, \mathbf x_1) & k(\mathbf x_n, \mathbf x_2) & \cdots & k(\mathbf x_n, \mathbf x_n) \\ 
\end{bmatrix}$$


If we have a linear learning machine with parameters $\mathbf w$, 
- then the function we try to learn is modeled by $f(\mathbf x) = \mathbf w^T \varphi(\mathbf x)$
- we can express $\mathbf w$ as a combination of training points: $\mathbf w = \sum_{i = 1}^{n} \alpha_i \, \varphi(\mathbf x_i)$ (i.e. the solution lies in the span of the data)
- then $f(\mathbf x) = \sum_{i = 1}^{n} \alpha_i \, k(\mathbf x_i, \mathbf x)$


### Mercer Kernels


### Types
We can combine Kernels: 
- given base kernel $k(\mathbf x, \mathbf z)$ (can be a dot product $k(\mathbf x, \mathbf z) = \langle \mathbf x, \mathbf z \rangle)$)
- Polynomial Kernel: $k'(\mathbf x, \mathbf z) = \big( k(\mathbf x, \mathbf z) + D \big)^p$
- Gaussian Kernel: $k'(\mathbf x, \mathbf z) = \exp \left( \cfrac{k(\mathbf x, \mathbf x) - 2 \, k(\mathbf x, \mathbf z) + k(\mathbf z, \mathbf z)}{\sigma^2} \right)$


## References
- Hofmann, Thomas, Bernhard Schölkopf, and Alexander J. Smola. "Kernel methods in machine learning." 2008. [http://www.kernel-machines.org/publications/pdfs/0701907.pdf]


## Sources
- Cristianini, Nello, John Shawe-Taylor, and Huma Lodhi. "Latent semantic kernels." 2002. [http://eprints.soton.ac.uk/259781/1/LatentSemanticKernals_JIIS_18.pdf]

[Category:Kernels](Category_Kernels)