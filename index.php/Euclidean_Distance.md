---
title: "Euclidean Distance"
layout: default
permalink: /index.php/Euclidean_Distance
---

# Euclidean Distance

## Euclidean Distance
Euclidean distance is a geometric [Distance](Distance) between two datapoints
- distance between $\mathbf x_1$ and $\mathbf x_2$ is 
- length of the line that connects these two points:
- $\|  \mathbf x_1 - \mathbf x_2 \| = \sqrt{ (\mathbf x_1 - \mathbf x_2)^T (\mathbf x_1 - \mathbf x_2) } = \sqrt{\sum_i (x_{1i} - x_{2i})^2}$ |

It's the most common distance metric, also called $L_2$ norm


### Properties
The Euclidean distance is translation invariant
- let $\mathbf a$ be some vector
- then consider the distance in the translated space :
- $\|  (\mathbf x_1 - \mathbf a) - (\mathbf x_2 - \mathbf a) \| = \| \mathbf x_1 - \mathbf a - \mathbf x_2 + \mathbf a \| = \| \mathbf x_1 - \mathbf x_2 \|$ |- so the distance in the translated space is the same as in the original space




## High Dimensionality
Euclidean distance is not always meaningful for high dimensional data

Consider this example:

|    |  $A_1$  |   $A_2$  |   $A_3$  |  $A_4$  |  $A_5$  |  $A_6$  |  $A_7$  |  $A_8$  |  $A_9$  |  $A_{10}$  |  $\mathbf p_1$  |  3  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0 ||  $\mathbf p_2$  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  4 ||  $\mathbf p_3$  |  3  |  2  |  4  |  0  |  1  |  2  |  3  |  1  |  2  |  0 ||  $\mathbf p_4$  |  0  |  2  |  4  |  0  |  1  |  2  |  3  |  1  |  2  |  4 |

- distance between $\mathbf p_1$ and $\mathbf p_2$ is $\|  \mathbf p_1 - \mathbf p_2\| = 5$ |- distance between $\mathbf p_3$ and $\mathbf p_4$ is $\|  \mathbf p_3 - \mathbf p_4\| = 5$ |- so Euclidean distance between these two vectors is the same|   |- but suppose these vectors correspond to documents and words ([Vector Space Models](Vector_Space_Models)) |- $\mathbf p_3$ and $\mathbf p_4$ must be more similar to each other than $\mathbf p_1$ and $\mathbf p_2$: $\mathbf p_3$ and $\mathbf p_4$ have 7 words in common whereas $\mathbf p_1$ and $\mathbf p_2$ have none


When the data is sparse it's better to use different measure of distance/similarity
- we need to ignore records where both vectors have 0 
- for example:
- [Dot Product](Dot_Product) and [Cosine Similarity](Cosine_Similarity)
- [Jaccard Coefficient](Jaccard_Coefficient)




## Sources
- http://en.wikipedia.org/wiki/Euclidean_distance
- Ertöz, Levent, Michael Steinbach, and Vipin Kumar. "Finding clusters of different sizes, shapes, and densities in noisy, high dimensional data." 2003. [http://static.msi.umn.edu/rreports/2003/73.pdf]
- Korenius, Tuomo, Jorma Laurikkala, and Martti Juhola. "On principal component analysis, cosine and Euclidean measures in information retrieval." 2007. [http://www.sciencedirect.com/science/article/pii/S0020025507002630] 


[Category:Distances](Category_Distances)
[Category:Norms](Category_Norms)