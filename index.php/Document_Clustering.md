---
layout: default
permalink: /index.php/Document_Clustering
tags:
- cluster-analysis
- document-clustering
- thesis
- unsupervised-learning
title: Document Clustering
---
## Document Clustering
The goal of text clustering is
- to assign documents to different topics or topic hierarchies
- i.e. when the topics/hierarchies are not known in advance
- as opposed to [Document Classification](Document_Classification) when labels are known
- It's a [Cluster Analysis](Cluster_Analysis) task: [Unsupervised Learning](Unsupervised_Learning) applied to textual data


Objects to be clustered are 
- documents, paragraphs, sentences
- or terms ([Term Clustering](Term_Clustering))


Applications:
- [Cluster Analysis](Cluster_Analysis) is also useful in [Text Mining](Text_Mining) 
- E.g. organizing documents for better [Information Retrieval](Information_Retrieval)
- Organizing documents intro hierarhical clusters  Cutting1992
- see Anick1997, Cutting1993 ([Scatter/Gather](Scatter_Gather))
- Corpus Summarization 
- Improving [Document Classification](Document_Classification) - see Baker1998 and Bekkerman2001



## Preprocessing
Usual [NLP](Natural_Language_Processing)/[IR](Information_Retrieval)


### Document Representation
The most commonly used document representation is [Vector Space Model](Vector_Space_Model):
- extract a list of unique terms and weight them
- weighted with TF or [TF-IDF](TF-IDF)

Alternative representation:
- terms as a [Probability Distribution](Probability_Distribution): [Language Models](Language_Models)
- then we can measure (dis)similarity with a symmetric variation of [KL Divergence](KL_Divergence) 


### [Feature Selection](Feature_Selection)
Concept of distance and similarity may be not meaningful in high-dimensional space 
- so may need to reduce dimensionality

In text mining usually referred as "Term Selection":
- [Remove stop words](Stop_Words)
- use document frequency to cut away infrequent and very frequent words. such words usually don't contribute much (or anything) to similarity computation
- [Subset Selection](Subset_Selection) and [Feature Filtering](Feature_Filtering) won't work because we don't have labels 


### [Dimensionality Reduction](Dimensionality_Reduction)
- [Term Clustering](Term_Clustering): find clusters of terms and replace the terms by their centroids
- [PCA](PCA) gives the basis for [Latent Semantic Analysis](Latent_Semantic_Analysis)
- [Non-Negative Matrix Factorization](Non-Negative_Matrix_Factorization)



## Clustering
- [Hierarchical Clustering](Hierarchical_Clustering): good for Document clustering because it creates a tree structure
- Partitioning Clustering Algorithms
  - [K-Means](K-Means)
  - [Scatter/Gather](Scatter_Gather)
- Parametric Modeling Methods like [Expectation Maximization](Expectation_Maximization)




### Distances and Similarity
Popular choice: 
- [Euclidean Distance](Euclidean_Distance) is not very good for high-dimensional data
- [Jaccard Coefficient](Jaccard_Coefficient) or [Cosine Similarity](Cosine_Similarity) are better


If not [Vector Space Models](Vector_Space_Models):
- [Language Models](Language_Models): symmetric variant [KL Divergence](KL_Divergence)
- Keep documents as strings: [Edit Distance](Edit_Distance) (but it'll most likely be extremely slow)


Papers:
- Strehl2000: Survey on distances for documents
- Sahami2006: When text segments are too short (e.g. tweets or sentences)


Direct similarity measures are not always reliable for high-dimensional clustering (see Guha1999)
- high dimensional data is sparse and therefore on average similarity is low 
- also see [Curse of Dimensionality](Curse_of_Dimensionality)
- SNN Distance solves it: Shared Nearest Neighbors Distance, # of [KNN](KNN)s two documents share (as used in [SNN Clustering](SNN_Clustering))


## Algorithms
### [K-Means](K-Means)
- centroids = weighed average of all docs in the cluster 
- to compare a document with a cluster, calculate cosine between document and cluster

A variation of K-Means: 
- Bisecting K-Means: gives good performance for document clusters
- [K-Medoids](K-Medoids) for non-Euclidean distances, using medoid ($\approx$ median) instead of mean for selecting a centroid
- [Scatter/Gather](Scatter_Gather): 
  - smart seed selection
  - centroid = concatenation of all docs in the cluster
  - Split and Join refinement operations


### [Two-Phase Document Clustering](Two-Phase_Document_Clustering)
Main idea:
- use [Mutual Information](Mutual_Information) to find best term clustering
- and then use mutual information to find best document clustering


### [Co-Clustering](Co-Clustering)
Clustering terms and documents at the same time 
- clustering of terms and clustering of documents are dual problems
- take advantage of that
- also can use [Non-Negative Matrix Factorization](Non-Negative_Matrix_Factorization) $A \approx UV^T$ where $U$ are clusters of docs and $V$ are clusters of terms 


### [Latent Semantic Analysis](Latent_Semantic_Analysis)
Using [PCA](PCA) define new features from terms 
- it creates a new semantic space where problems like symomymy or polysemy are solved 
- term-document matrix is decomposed using [SVD](SVD)


Not only SVD is good:
- can also use [Non-Negative Matrix Factorization](Non-Negative_Matrix_Factorization) techniques 
- this way it's easy to interpret and [clusters can be fuzzy](Fuzzy_Clustering)


### [Topic Models](Topic_Models)
- define some probabilistic generative models for text documents
- in some way it's similar to LSA, but it's probabilistic
- see [Probabilistic LSA](Probabilistic_LSA) or [Latent Dirichlet Allocation](Latent_Dirichlet_Allocation)


### [Semi-Supervised Clustering](Semi-Supervised_Clustering)
Use prior knowledge to help clustering 
- e.g. if you know some of the labels, do better seed selection for [K-Means](K-Means)



## Performance
Issues
- Text data usually has very high dimensionality
- especially important for large corpus - it will be very slow, especially for hierarchical algorithms


### [Inverted Index](Inverted_Index)
Idea:
- usually a document contains only a small portion of terms 
- so document vectors are very sparse
- typical distance is cosine similarity - it ignores zeros. for cosine to be non-zero, two docs need to share at least one term
- $D^T$ is the inverted index of the term-document matrix $D$


this, to find docs similar to $d$:
- for each $w_i \in d$
- let $D_i = \{ d_i \} - d = \text{index}[w_i]$ be a set of documents that also contain $w_i$
- then take the union of all $D_i$ 
- calculate similarity only with documents from this union


### Term Selection
Idea:
- Only top high-weighted terms contribute substantially to the norm 
- so keep only those weights that contribute 90% of the norm
- and set the rest to 0


It can reduce the number of documents to consider but without losing much information


## References
- Anick, Peter G., and Shivakumar Vaithyanathan. "Exploiting clustering and phrases for context-based information retrieval."  1997. 
- Cutting, Douglass R., et al. "Scatter/gather: A cluster-based approach to browsing large document collections." 1992. [http://courses.washington.edu/info320/au11/readings/Week4.Cutting.et.al.1992.Scatter-Gather.pdf]
- Cutting, Douglass R., David R. Karger, and Jan O. Pedersen. "Constant interaction-time scatter/gather browsing of very large document collections." 1993.
- Baker, L. Douglas, and Andrew Kachites McCallum. "Distributional clustering of words for text classification." 1998. [http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.42.7488&rep=rep1&type=pdf]
- Bekkerman, Ron, et al. "On feature distributional clustering for text categorization." 2001. [http://scholar.google.com/scholar?cluster=1445350076343942781&hl=ru&as_sdt=0,5] 
- Sahami, Mehran, and Timothy D. Heilman. "A web-based kernel function for measuring the similarity of short text snippets." 2006. [http://research.google.com/intl/en/pubs/archive/32.pdf]
- Strehl, Alexander, Joydeep Ghosh, and Raymond Mooney. "Impact of similarity measures on web-page clustering." 2000. [http://strehl.com/download/strehl-aaai00.pdf]
- Guha, Sudipto, Rajeev Rastogi, and Kyuseok Shim. "ROCK: A robust clustering algorithm for categorical attributes." 1999. [http://www.cacs.louisiana.edu/~jyoon/grad/adb/References/clustering/ROCK-clus99icde.pdf]

## Sources
- Steinbach, Michael, George Karypis, and Vipin Kumar. "A comparison of document clustering techniques." 2000. ([https://wwws.cs.umn.edu/tech_reports_upload/tr2000/00-034.ps])
- Larsen, Bjornar, and Chinatsu Aone. "Fast and effective text mining using linear-time document clustering." 1999. ([http://comminfo.rutgers.edu/~muresan/IR/Docs/Articles/sigkddLarsen1999.pdf])
- Aggarwal, Charu C., and ChengXiang Zhai. "A survey of text clustering algorithms." Mining Text Data. Springer US, 2012. [http://ir.nmu.org.ua/bitstream/handle/123456789/144935/d1784ebed3eab2708026b202b2b65309.pdf?sequence=1#page=90]
- Jing, Liping. "Survey of text clustering." (2008). [http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.112.3476&rep=rep1&type=pdf]
- Ertöz, Levent, Michael Steinbach, and Vipin Kumar. "Finding clusters of different sizes, shapes, and densities in noisy, high dimensional data." 2003. [http://static.msi.umn.edu/rreports/2003/73.pdf]
