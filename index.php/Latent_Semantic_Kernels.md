---
title: "Latent Semantic Kernels"
layout: default
permalink: /index.php/Latent_Semantic_Kernels
---

# Latent Semantic Kernels

$\require{cancel}$

## Latent Semantic Kernels
In [Information Retrieval](Information_Retrieval) via [Vector Space Model](Vector_Space_Model), retrieval is based on inner product as well
- so can also use [Kernels](Kernels)
- You can already use [SVM](SVM) for text data and get very good performance 
- but also can incorporate additional information by using a kernel
- In traditional [Vector Space Model](Vector_Space_Model) semantic relationships are not taken into account 
- Goal: design a "Semantic Kernel": a kernel which creates a map that captures semantic information


Building the Kernel:
- Use Semantic Network (e.g. [WordNet](WordNet)) to capture similarity between words and encode this information into kernel
- use [Latent Semantic Analysis](Latent_Semantic_Analysis) to learn the semantic space and a mapping function that brings input space to the semantic spaces
- in semantic space documents that don't share any terms still can be close if they terms are semantically related 
- this semantic similarity is inferred by analyzing co-occurrence patterns: terms that co-occur often in the same documents are considered related 
- this statistical co-occurrence is extracted via [SVD](SVD)


== [Vector Space Model](Vector_Space_Model) == 
Suppose we have a term-document matrix $D$
- then $G = D^T D$ is a doc-by-doc matrix and $T = D D^T$ matrix
- can define a base kernel as $k(\mathbf d_1, \mathbf d_2) = \mathbf d_1^T \mathbf d_2$
- suppose we apply some [Linear Transformation](Linear_Transformation) $\phi$: to documents: $\phi(\mathbf d) = P \, \mathbf d$
- (usual VSM: $P = I$)
- then kernel becomes $k(\mathbf d_1, \mathbf d_2) = \mathbf d_1^T P^T P \mathbf d_2$ and the kernel matrix $K = D^T P^T \, P \, D$
- now can build a new kernel $k'$ using the base kernel $k$ (e.g. polynomial or gaussian) - to increase the expressive power of the VSM model




## Semantic Kernels
But in reality usual VSM models have problems with synonymy and polysemy - these kernels can't handle that 

how to enrich kernels with semantic information? 
- document expansion: add all synonyms to the document
- or replace words by concepts (can be taken from a semantic network or learned)
- use information about term-term correlation|    | |So $K = D^T P^T \, P \, D$ 
- let  $P_{ij}$ denote semantic proximity between terms $i$ and $j$
- then is a square symmetric matrix
- so have  $k(\mathbf d_1, \mathbf d_2) = \mathbf d_1^T P^T P \mathbf d_2 = \mathbf d_1^T P^2 \, \mathbf d_2$
- also note that $\|  P\, \mathbf d_1 - P\, \mathbf d_2 \|^2 = \| P \, (\mathbf d_1 - \mathbf d_2) \|^2 = (\mathbf d_1 - \mathbf d_2)^T P^2 \, (\mathbf d_1 - \mathbf d_2)$: can use this to apply Gaussian Kernel |
$P$ can also be concept-term similarity matrix, but then $P$ will not be symmetric


### LSI Kernel
[LSI](Latent_Semantic_Analysis): document feature vector $\mathbf d$ is projected onto the subspace spanned by first $k$ singular vectors if the feature space 
- apply [SVD](SVD) to $D$: $D = U \Sigma V^T$ where $U$ contains the singular vectors of the feature space
- the projection on $k$ first singular values gives $U_k$, so let $P = U_k^T$ 
- $U_k$ identifies terms that co-occur most often 
- this have $k(\mathbf d_1, \mathbf d_2) = (U_k^T \mathbf d_1)^T U_k^T \mathbf d_2 = \mathbf d_1^T U_k \, U_k^T \mathbf d_2$ 


Suppose we have our kernel classifier 
- $f(\mathbf d) = \sum_{i = 1}^{n} \alpha_i \, k(\mathbf d_i, \mathbf d)$
- then by using this kernel, we have
- $f(\mathbf d) = \sum_{i = 1}^{n} \alpha_i \, \big( \mathbf d_i^T U_k \, U_k^T \mathbf d \big)$
- now consider a vector $\boldsymbol \alpha = (\alpha_1, \ ... \ , \alpha_n)$ 
- we can replace $\big( \mathbf d_i^T U_k \, U_k^T \mathbf d \big)$ with a vector $D^T U_k \, U_k^T \mathbf d$ where $D$ has documents $\mathbf d_1, \, ... \, \mathbf d_n$ as columns
- so $f(\mathbf d) = \boldsymbol \alpha^T D^T U_k \, U_k^T \mathbf d = \ ...$ let's replace $D$ with its SVD
  - $... \ = \boldsymbol \alpha^T V \, \Sigma U^T U_k \, U_k^T \mathbf d = \ ...$ replace $U_k = U \, I_k$
  - $... \ = \boldsymbol \alpha^T V \, \Sigma \cancel{U^T U} I_k \, U_k^T \mathbf d = \ ...$ 
  - $... \ = \boldsymbol \alpha^T V \, \Sigma \, I_k \, U_k^T \mathbf d = \ ...$ note that $\Sigma \, I_k = \Sigma_k$
  - $... \ = \boldsymbol \alpha^T V \, \Sigma_k \, U_k^T \mathbf d = \ ...$ 


Can we avoid working on the feature space? We still have $\Sigma_k$ and $U_k$
- $\Sigma_k \, U_k^T \mathbf d$ - need to express in terms of the input space
- $\Sigma_k \, U_k^T \mathbf d = I_k \Sigma \, U^T \mathbf d = \ ...$ 
  - $... \ = \Sigma_k \, U_k^T \mathbf d = I_k \underbrace{V^T V}_{I} \Sigma \, U^T \mathbf d = \ ...$
  - $... \ = \Sigma_k \, U_k^T \mathbf d = I_k V^T \underbrace{V \Sigma \, U^T}_{D^T} \mathbf d = \ ...$ 
  - $... \ = \Sigma_k \, U_k^T \mathbf d = I_k V^T D^T \mathbf d$ 
- let's plug it to $f(\mathbf d)$:
  - $f(\mathbf d) = \boldsymbol \alpha^T V \, I_k V^T D^T \mathbf d$
- so we avoid working on the feature space directly: 
- $V$ can be computed by [Eigendecomposition](Eigendecomposition) of the kernel matrix $K$ 


Bottleneck: 
- decomposing $K$ 
- approximate: Smola, Alex J., and Bernhard Schölkopf. "Sparse greedy matrix approximation for machine learning." 2000. [http://citeseer.ist.psu.edu/viewdoc/summary?doi=10.1.1.43.3153]



## Sources
- Cristianini, Nello, John Shawe-Taylor, and Huma Lodhi. "Latent semantic kernels." 2002. [http://eprints.soton.ac.uk/259781/1/LatentSemanticKernals_JIIS_18.pdf]

[Category:Kernels](Category_Kernels)