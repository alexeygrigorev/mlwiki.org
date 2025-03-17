---
title: Latent Semantic Analysis
layout: default
permalink: /index.php/Latent_Semantic_Analysis
---

# Latent Semantic Analysis

## Latent Semantic Analysis
Latent Semantic Analysis (LSA) is an [NLP](NLP) method: 
- mathematical/statistical method for modeling the meaning of words/passages by analysis of text via extracting and inferring relations of expected contextual usage of words in texts 
- idea: words that are used in the same contexts tend to have the same meaning



### Problems with Text
Issues with text data:
- synonymy: many ways to refer to the same object 
- synonymy tends to decrease [recall](Precision_and_Recall)
- polysemy: many words have more than one distinct meaning (e.g. "chip", "trunk")
- polysemy tends to decrease [precision](Precision_and_Recall)


Overcoming Synonymy:
- term extraction, thesauri construction

Overcoming Polysemy: 
- using controlled vocabulary
- or use [Word Sense Disambiguation](Word_Sense_Disambiguation)


### WEIRD
WEIRD (Koll1979) is the first IR system that dealt with these problems automatically, not with some controlled vocabulary
- the goal of WIERD: to go from term matching to concept matching
- can use statistical analysis to empirically find relations among terms 
- so it analyzed term-to-term co-occurrence matrix 
- can use [Factor Analysis](Factor_Analysis) to identify the right basis for terms s.t. there's little or no loss of information
- in WEIRD only 7 dimensions were used - based on 7 completely non-overlapping documents found in the collection


The space built by WEIRD acts like an implicit thesaurus 
- synonyms will map to the same concept 


### LSA
LSA/LSI solves these problems as well
- it goes further than WIERD: it uses all documents to build a space 
- it does that by applying SVD as a [Dimensionality Reduction](Dimensionality_Reduction) - which reveals latent structure and "denoises" the data
- Similarity estimates derived by LSA are not just frequencies or co-occurrences counts: it can infer deeper relations: hence "Latent" and "Semantic" 
- so LSA learns the latent semantic structure of the vocabulary


### LSI
Latent Semantic Analysis (LSA) $\approx$ Latent Semantic Indexing (LSI) 
- LSI is the alias of LSA for [Information Retrieval](Information_Retrieval)
- indexing and retrieval method that uses [SVD](Singular_Value_Decomposition) to identify patterns in relations between terms and concepts
- instead of literal match between query and documents (e.g. using cosine in the traditional vector space morels), convert both into the Semantic Space and calculate the cosine there






## LSA Steps
3 major steps (by Evangelopoulos2012)

- Prepare documents 
- Construct [Term-Document matrix](Vector_Space_Models) $D$
- Reduce dimensionality of $D$ via [SVD](SVD)


### Document preparation
- [Term selection](Feature_Selection): exclude [Stop Words](Stop_Words) and low and high frequency terms
- [Stem](Stemming) or [Lemmatize](Lemmatization) could also be helpful
- see [NLP Pipeline](NLP_Pipeline)


### Representation: [Vector Space Models](Vector_Space_Models)
Construct a matrix $D$
- $D$ is Term-Document Matrix if rows of $D$ - terms, columns of $D$ - documents/passages
- $D$ is Document-Term Matrix if rows of $D$ - documents/passages, and columns of $D$ - terms
- each cell - typically a frequency with which a word occurs in a doc
- also apply weighting: TF or [TF-IDF](TF-IDF) 


### [SVD](SVD) and [Dimensionality Reduction](Dimensionality_Reduction)
Let $D$ be an $t \times p$ Term-Passage matrix 
- $t$ rows are terms, $p$ columns are passages, $\text{rank } D = r$
- then SVD decomposition is $D = T \cdot \Sigma \cdot P^T$ 
- $T$ is $t \times r$ [Orthogonal Matrix](Orthogonal_Matrix), contains left singular vectors, corresponds to term vectors
- $\Sigma$ is $r \times r$ a diagonal matrix of singular values
- $P$ is $r \times p$ [Orthogonal Matrix](Orthogonal_Matrix), contains right singular vectors, corresponds to passage vectors
- and then $T \sqrt\Sigma$ are loadings for terms and $P \sqrt\Sigma$ - for passages



Now reduce the dimensionality:
- want to combine the surface text information into some deeper abstraction
- finding the optimal dimensionality for final representation in the Semantic Space is important to properly capture mutual usage of words
- the "True Semantic Space" should address the Text Problems


So, Apply reduced-rank [SVD](SVD)
- $D \approx T_k \cdot \Sigma_k \cdot P^T_k$
- keep only $k$ largest singular values
- the result: best $k$-dim approximation of the original matrix $D$
- for NLP $k = 300 \pm 50$ usually works the best 
- but it should be [tuned](Model_Selection) because it heavily depends on the domain


## Semantic Space
LSA constructs a semantic space via SVD:
- $T$ is $t \times r$ [Orthogonal Matrix](Orthogonal_Matrix), contains left singular vectors, corresponds to term vectors
- $\Sigma$ is $r \times r$ a diagonal matrix of singular values
- $P$ is $r \times p$ [Orthogonal Matrix](Orthogonal_Matrix), contains right singular vectors, corresponds to passage vectors
- and then $T \sqrt\Sigma$ are loadings for terms and $P \sqrt\Sigma$ - for passages


Language-theoretic interpretation: 
- LSA vectors approximate:
- the meaning of a word as its average effect of the meaning of passages in which they occur
- the meaning of a passage as meaning of its words 


After doing the SVD, we get the reduced space - this is the semantic space
- the effect of reducing the dimensionality:
- removed the noise effect of synomymy and polysemy 


### Comparisons in the Semantic Space
So we approximated $D$ as $D \approx \hat D = T_k \Sigma_k P_k^T$
- lets omit index $k$: so below by $T$ we will assume $T_k$


Term comparisons:
- How similar are terms $\mathbf t_i$ and $\mathbf t_j$? 
- In $D$ we would compare rows of $D$. How to compare them in the semantic space?
- $\hat D \hat D^T$ gives a term-term [Gram Matrix](Gram_Matrix) 
  - $\hat D \hat D^T = T \Sigma \Sigma^T T^T = T \Sigma \, (T \Sigma)^T$
  - thus $\big[\hat D \hat D^T\big]_{ij}$ is the dot product between $i$th and $j$th rows of $T \Sigma$
- rows of $T \Sigma$ are coordinates for terms in the semantic space


Document comparisons:
- how similar are documents $\mathbf p_i$ and $\mathbf p_j$ in the semantic space? 
- $\hat D^T \hat D$ gives a document-document [Gram Matrix](Gram_Matrix) 
- $\hat D^T \hat D = P \Sigma \Sigma^T P^T = P \Sigma \,  (P \Sigma)^T$
- so to compute document $i$ and $j$ you compute the dot product between $i$th and $j$th rows of $P \Sigma$



### Generalization to Unseen Documents
What about objects that didn't originally appear in the training set? 
- e.g. a query $\mathbf q$ 
- how do we represent $\mathbf q$ in the semantic space? 
- first, let's see how original documents $\mathbf p_i$ are represented in this space


$\hat D = T \Sigma P^T$
- multiply by $(T \Sigma)^{-1}$ on the left
- $(T \Sigma)^{-1} \hat D = P^T$
- $\Sigma^{-1} T^T \hat D = P^T$
- $P = D^T T \Sigma^{-1}$
- if $\mathbf d_i$ be some document in the original space (column of $\hat D$) and $\mathbf p_i$ the corresponding representation of $\mathbf d_i$ in the document basis, then
- $\mathbf p_i = \mathbf d_i^T T \Sigma^{-1}$


This, can represent $\mathbf q$ the same way:
- $\hat{\mathbf q} = \mathbf q^T T \Sigma^{-1}$
- where $\hat{\mathbf q}$ is the representation of $\mathbf q$ in the document basis
- to compare $\hat{\mathbf q}$ all we need to do is to scale it by $\Sigma$ and then compute a dot product



## Example
### Article Titles Example
Let's consider titles of some articles (from Deerwester90):

- $c_1$: "Humanmachine interface for ABC computer applications"
- $c_2$: "A survey of user opinion of computer system response time"
- $c_3$: "The EPS user interface management system"
- $c_4$: "Systemand human system engineering testing of EPS"
- $c_5$: "Relation of user perceived response time to error measurement"
- $m_1$: "The generation of random, binary, ordered trees"
- $m_2$: "The intersection graph of paths in trees"
- $m_3$: "Graph minors IV: Widths of trees and well-quasi-ordering"
- $m_4$: "Graph minors: A survey"

Matrix:

$D = \left[\begin{array}{c| cccccccc} |& c_1 & c_2 & c_3 & c_4 & c_5 & m_1 & m_2 & m_3 & m_4 \\
\hline
\text{human} & 1 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
\text{interface} & 1 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
\text{computer} & 1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
\text{user} & 0 & 1 & 1 & 0 & 1 & 0 & 0 & 0 & 0 \\
\text{system} & 0 & 1 & 1 & 2 & 0 & 0 & 0 & 0 & 0 \\
\text{response} & 0 & 1 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
\text{time} & 0 & 1 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
\text{EPS} & 0 & 0 & 1 & 1 & 0 & 0 & 0 & 0 & 0 \\
\text{survey} & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \\
\text{trees} & 0 & 0 & 0 & 0 & 0 & 1 & 1 & 1 & 0 \\
\text{graph} & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 & 1 \\
\text{minors} & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 \\
\end{array}\right]$


Note:
- row vectors for "human" and "user" are orthogonal: their dot product is zero, but they are supposed to be similar, so it must be positive
- also, "human" and "minors" are orthogonal, but they are not similar, so it must be negative

Let's apply SVD: 
- $D = W \Sigma P$
- 2-dim approximation: $D_2 = W_2 \Sigma_2 P_2$

$D_2 = \left[\begin{array}{c| cccccccc} |& c_1 & c_2 & c_3 & c_4 & c_5 & m_1 & m_2 & m_3 & m_4 \\
\hline
\text{human} & 0.16 &  0.4  &  0.38 &  0.47 &  0.18 & -0.05 & -0.12 & -0.16 & -0.09 \\
\text{interface} & 0.14 &  0.37 &  0.33 &  0.4  &  0.16 & -0.03 & -0.07 & -0.1  & -0.04 \\
\text{computer} & 0.15 &  0.51 &  0.36 &  0.41 &  0.24 &  0.02 &  0.06 &  0.09 &  0.12 \\
\text{user} & 0.26 &  0.84 &  0.61 &  0.7  &  0.39 &  0.03 &  0.08 &  0.12 &  0.19 \\
\text{system} & 0.45 &  1.23 &  1.05 &  1.27 &  0.56 & -0.07 & -0.15 & -0.21 & -0.05 \\
\text{response} & 0.16 &  0.58 &  0.38 &  0.42 &  0.28 &  0.06 &  0.13 &  0.19 &  0.22 \\
\text{time} & 0.16 &  0.58 &  0.38 &  0.42 &  0.28 &  0.06 &  0.13 &  0.19 &  0.22 \\
\text{EPS} & 0.22 &  0.55 &  0.51 &  0.63 &  0.24 & -0.07 & -0.14 & -0.2  & -0.11 \\
\text{survey} & 0.1  &  0.53 &  0.23 &  0.21 &  0.27 &  0.14 &  0.31 &  0.44 &  0.42 \\
\text{trees} &-0.06 &  0.23 & -0.14 & -0.27 &  0.14 &  0.24 &  0.55 &  0.77 &  0.66 \\
\text{graph} &-0.06 &  0.34 & -0.15 & -0.3  &  0.2  &  0.31 &  0.69 &  0.98 &  0.85 \\
\text{minors} &-0.04 &  0.25 & -0.1  & -0.21 &  0.15 &  0.22 &  0.5  &  0.71 &  0.62 \\
\end{array}\right]$



What's the effect of dimensionality reduction here?
- words appear less or more frequent than originally
- consider two cells: ("survey", $m_4$) and ("trees", $m_4$)
- original document: 1 and 0
- reduced document: 0.42 and 0.66
- because $m_4$ contains "graph" and "minor", the 0 for "trees" was replaced by 0.42 - they are related terms
- so it can be seen as estimate of how many times word "trees" would occur in other samples that contain "graph" and "minor"
- the count for "survey" went down - it's not expected in this context

So in the reconstructed space:
- dot product between "user" and "human" is positive
- dot product between "human" and "minors" is negative
- it tells us way better whether terms are similar or not even when they never co-occur together


Taking 2 principal components is the same as taking only 2 abstract concepts
- each word in the vocabulary has some amount of these 2 concepts (we see how much by looking at 1st and 2nd column of $W$)


The idea:
- we don't want to reconstruct the underlying data perfectly, but instead we hope to find the correlation and the abstract concepts



### Python code
```numpy
import numpy as np
import numpy.linalg as la
 
D = [[1, 0, 0, 1, 0, 0, 0, 0, 0],
     [1, 0, 1, 0, 0, 0, 0, 0, 0],
     [1, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 1, 0, 1, 0, 0, 0, 0],
     [0, 1, 1, 2, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 1, 0, 0, 0, 0],
     [0, 1, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 1, 1, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 1, 1, 1, 0],
     [0, 0, 0, 0, 0, 0, 1, 1, 1],
     [0, 0, 0, 0, 0, 0, 0, 1, 1]]
D = np.array(D)
 
rows = ['human', 'interface', 'computer', 'user', 'system', 
        'response', 'time', 'EPS', 'survey', 'trees', 'graph', 'minors']
idx = {n: i for (i, n) in enumerate(rows)}
 
D[idx['human']].dot(D[idx['user']]) # 0
D[idx['human']].dot(D[idx['minors']]) # 0
 
 
T, S, P = la.svd(D) # T=terms, P=passages
 
np.set_printoptions(precision=2, suppress=True)
print T[:, 0:2], S[0:2], P[0:2, :]
 
D_hat = T[:, 0:2].dot(np.diag(S[0:2])).dot(P[0:2, :])
 
D_hat[idx['human']].dot(D_hat[idx['user']]) # 0.955
D_hat[idx['human']].dot(D_hat[idx['minors']]) # -0.251
```


Can do the same without building $\hat D$:


```text only
T = T[:, 0:2]
S = np.diag(S[0:2])
P = P[0:2, :].T

human = T.dot(S)[idx['human']]
user = T.dot(S)[idx['user']]
human.dot(user) # same result: 0.955
```


Finally, let's calculate cosine between human and user:

```scdoc
human.dot(user) / (la.norm(human) * la.norm(user))
# 0.88784582874340123
```




## Practical Notes
### Applications
- [Document Classification](Document_Classification)
- [Document Clustering](Document_Clustering)
- Text search in [Information Retrieval](Information_Retrieval)


### Limitations
- makes no use of words order, punctuation
- if the original terms are already descriptive enough (e.g. for [Document Classification](Document_Classification)), they may be lost during the transformation


### When Not Good
- Sometimes Semantic Spaces alone are not good
- but we can mix the original vector space and the semantic space together 


### Mean Centering
LSA and [Principal Component Analysis](Principal_Component_Analysis) are related via [SVD](SVD)
- but for PCA we often do mean centering. Why not here? 
- Angle (and cosine) is not preserved when doing mean-correction, so it may affect pair-wise similarities 
- <img src="https://habrastorage.org/files/60e/825/3b3/60e8253b34ba496da20ed47df2e21bf2.png" alt="Image">
- Term-Document matrices are typically very sparse, and if we mean-center, we'll lose the sparsity
- because of the sparsity, the mean of rows is very close to 0 anyway
- also, see here: http://stats.stackexchange.com/questions/152879/latent-semantic-indexing-and-data-centering





## Extensions of LSA
- add probability over documents: [Probabilistic LSA](Probabilistic_LSA)
- and a similar technique: [Latent Dirichlet Allocation](Latent_Dirichlet_Allocation)
- can also use [Non-Negative Matrix Factorization](Non-Negative_Matrix_Factorization) to discover latent structure of data



## Links
- Soft for doing LSA: gensim https://radimrehurek.com/gensim/ (also for [Topic Modeling](Topic_Modeling))

## Sources
- Koll, Matthew B. "WEIRD: An approach to concept-based information retrieval." 1979.
- Landauer, Thomas K., Peter W. Foltz, and Darrell Laham. "An introduction to latent semantic analysis." 1998. [http://tottdp.googlecode.com/files/LandauerFoltz-Laham1998.pdf]
- http://www.scholarpedia.org/article/Latent_semantic_analysis
- http://edutechwiki.unige.ch/en/Latent_semantic_analysis_and_indexing
- Evangelopoulos, Nicholas, Xiaoni Zhang, and Victor R. Prybutok. "Latent semantic analysis: five methodological recommendations." (2012). [[http://scholar.google.com/scholar?cluster=13322286620975267196&hl=ru&as_sdt=0,5](http://digital.library.unt.edu/ark:/67531/metadc288006/m2/1/high_res_d/Evangelopoulos2012_EJIS-Pre-print.pdf])
- Deerwester, Scott C., et al. "Indexing by latent semantic analysis." 1990. [http://www.cob.unt.edu/itds/faculty/evangelopoulos/dsci5910/LSA_Deerwester1990.pdf]
- Berry, Michael W., Susan T. Dumais, and Gavin W. O'Brien. "Using linear algebra for intelligent information retrieval." (1995). [http://machinelearningtext.pbworks.com/w/file/fetch/47378285/lsiPaper_ut-cs-94-270.pdf]
- Korenius, Tuomo, Jorma Laurikkala, and Martti Juhola. "On principal component analysis, cosine and Euclidean measures in information retrieval." 2007. [http://www.sciencedirect.com/science/article/pii/S0020025507002630] 
- Zhukov, Leonid, and David Gleich. "Topic identification in soft clustering using PCA and ICA". 2004. [http://leonidzhukov.ru/papers/soft-clustering-pca-ica.pdf]


[Category:Document Clustering](Category_Document_Clustering)
[Category:NLP](Category_NLP)
[Category:Information Retrieval](Category_Information_Retrieval)