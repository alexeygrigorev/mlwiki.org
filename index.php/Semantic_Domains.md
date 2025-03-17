---
title: "Semantic Domains"
layout: default
permalink: /index.php/Semantic_Domains
---

# Semantic Domains

## Semantic Domains
- A ''semantic field'' corresponds to words grouped by their meaning
- it consists of words from some domain
- e.g. in English the field "Rain" may include words like "rain", "drizzle", "downpour", "raindrop", "puddle", all of these words can be used to talk about rain


Words within one domain are related by lexical relations
- there are two kinds of lexical relations:
- term lexical relations: relations between words, typically about words that collocate (frequently used together: e.g. words "bird" and "fly")
- paradigm form: synonyms, antonyms, etc. E.g. words "big" and "large"


Forming lexical relations:
- we learn lexical relations to speak correctly 
- each of us has a big mental dictionary organized into a big network of lexical relations
- there are clusters in this network: ''semantic field''


Semantic Domains:
- In [Computational Linguistics](Computational_Linguistics) and [NLP](NLP) Semantic Domains is a computational model for [Lexical Semantics](Lexical_Semantics)
- Semantic domains are a way of finding Semantic Fields 



## The Theory of Semantic Fields
Lexicon (words of a natural language) is structured into Semantic Fields
- Semantic Fields: "clusters" of semantically related terms
- relations among concepts that belong to the same Semantic Field are very dense
- and concept from different Semantic Field are typically unrelated 
- Theory of Semantic Fields: it claims that words are structured into a set of semantic fields 



Structural Semantics models relations between words, like in [WordNet](WordNet)
- The Theory of Semantic Fields goes further by introducing an additional aggregation level
- Semantic Fields form higher-level abstractions
- relations between them are much more stable than between words
- even if word senses change over time, the field still stays the same 
- so, Semantic Fields are usually consistent across languages, cultures and time
- there's a strong connection between Semantic Fields of different Languages: such connections don't exist among the terms themselves



Limitation of this theory:
- it doesn't provide any objective criteria for identifying Semantic Fields in the language
- solution to this problem: Semantic Domains, it's a computational approach for finding Semantic Fields
- use the lexical coherence assumption: words from the same field should co-occur in texts



## Semantic Domains
''Semantic Domains'' are Semantic Fields that are characterized by set of ''domain words'' which often occur in texts about corresponding domain
- words belonging to the same lexical field are called "domain words"
- usually large potion of the language terminology is characterized by domain words 


### Lexical Coherence Assumption
Basic hypothesis: 
- a great percentage of the concepts expressed in the same text belongs to the same domain 
- it's a basic property of any natural language: domain-specific words co-occur with each other in the same text, this property is called "lexical coherence"
- There are common areas of human knowledge such as Economics, Politics, Law, Science, etc. All these areas demonstrate lexical coherence


So, what about Semantic Fields?
- Semantic Fields are lexically coherent: words in one SF tend to co-occur in texts 
- We call these fields "Semantic Domains": they are Semantic Fields characterized by lexically coherent words


Lexical coherence assumption:
- We assume that real-world documents are lexically coherent
- this guarantees the existence of Semantic Domains
- it's also proven by experiments: in real texts if you count the percentage of words that belong to the same domain, you'll see that the most belong to one domain 


There are 3 types of words 
- '''Text-Related Domain words''': words that have at least one sense that contributes to determining the domain of the whore text 
  - e.g. word "bank" in a text about economy
- '''Text-Unrelated Domain words''': words that are from some non-generic domain, but don't contribute to the domain of the text
  - e.g. word "church" in a text about economy
- '''Text-Unrelated Generic words''': don't bring any relevant domain information 
  - e.g. "to be"


Let's put the lexical coherence assumption more formally:
- "One domain per discourse" ($\approx$ text, document) assumption
- if a word is used in one sense in some discourse
- then other occurrences of this word should also have the same sense
- smart way of putting it: "multiple occurrences of a word in coherent portions of texts tend to share the same domain"


The lexical coherence assumption allows us to represent Semantic Domains by the set of domain-specific texts


### Role of Semantic Domains
Characterizing word senses (i.e. lexical concepts)
- typically by assigning domain labels to words in a lexicon
- e.g. Crane has senses in Zoology and Construction
- WordNet Domains - extension of [WordNet](WordNet) that adds the information about domain


Characterizing texts
- can use Semantic Domains for text categorization
- at the textual level, semantic domains are [clusters of texts](Document_Clustering) on similar topics
- so can see Semantic Domains as a collection of domain-specific texts 


practical points of view: Semantic Domains are lists of related terms that describe a particular subject/area



## Representation
### Domain Sets
- domain relations: two words are domain-related if they belong to the same domain
- domain set is used to describe semantic classes of texts 
- semantic classes of strongly related lexical concepts are domain concepts
- so a domain set should relate each word to one or more domain sets


Requirements of an "ideal" domain set:
- completeness: all possible texts should be assigned to at least one domain
- balancement: number of texts belonging to each domain should be uniform
- separability: the same text/concept can't be assigned to more than one domain


Usually not achievable: 
- it's quite difficult to define a complete domain set, general enough to represent all possible aspects of human knowledge
- and it's also not possible to collect a corpus that contains all the human knowledge
- a certain degree of overlapping is unavoidable (e.g. math/physics)



### Domain Model
We can easily obtain term-based representation of documents e.g. by using [Vector Space Models](Vector_Space_Models) 
- but VSMs have lexical ambiguity problem
- domain terms are typically highly correlated within texts: they tend to co-occur inside the same types of text
- this is justified by the lexical coherence property of natural languages (Leacock96)


Domain model is a computational model for Semantic Domains to represent domain information 
- it describes relations at the term level
- it does that by defining a set of term clusters (see also [Term Clustering](Term_Clustering))
- each cluster represent a semantic domain: set of terms that often co-occur in texts with similar topics 
- it's a way to represent domain information at the textual level


Domain Model:
- is a matrix that describes the degree of association between terms in the vocabulary and Semantic Domains
- rows are indexed by words
- columns are the corresponding domains 


Domain Model is a [shallow model](Linguistic_Models) for lexical semantics, but it capture ambiguity and variability


DM is represented by a $n \times k$ rectangular matrix $D$ 
- $D$ contains the domain relevance for each term w.r.t each domain 


E.g. 

|    |  Medicine  |  CS  |  HIV  |  1  |  0 ||  AIDS  |  1  |  0 ||  virus  |  0.5  |  0.5 ||  laptop  |  0  |  1 |

Formally, 
- let $\mathcal D = \{ D_1 , \ ... \ , D_k \}$ be a set of domains 
- and we have $n$ words $V = \{ w_1, \ ... \ , w_n \}$  ($n$ - vocabulary size)
- then $D$ is a $n \times k$ matrix, where $D_{iz}$ is domain relevance of term $w_i$ w.r.t. domain $D_z$

- let $R(D_z, o)$ denote domain relevance of domain $D_z$ w.r.t. some linguistic object $o$ (text, term, concept)
- it gives a measure of association between $D_z$ and $o$ 
- typically higher values indicate higher association and often the value ranges from 0 to 1


DMs can describe ambiguity and variability:
- ambiguity: by associating one term to several domains 
- variability: by associating different terms to the same domain 


A domain Model defines a Domain Space 



### Obtaining Domain Models
Obtaining Domain Models
- Domain Models can be obtained from unsupervised learning or manual annotation
- can use WordNet Domain 
- or by performing [Term Clustering](Term_Clustering)


domain relations among terms can be detected by analyzing co-occurrence in the corpus
- motivated by the lexical coherence assumption
- co-occurring terms have a good chance to show domain relations


### WordNet Based Domain Model
WordNet Domains is an extension of [WordNet](WordNet): 
- each synset here is annotated with one or more domain labels
- it has ~ 200 domain labels


Using WordNet Domain for building a domain model:
- if $\mathcal D = \{ D_1 , \ ... \ , D_k \}$ are domains of the word net domains 
- and $\mathcal C = \{ c_1 , \ ... \ , c_s \}$ are concepts (synsets) from WordNet
- then let $\text{senses}(w)$ be a set of all synsets that contain $w$: $\text{senses}(w) = \{c  \mid  c \in \mathcal C, \text{$c$ is a sense of $w$} \}$
- let $R_s: \mathcal D \times \mathcal C \to \mathbb R$ be a domain relevance function for concepts
- $\text{dom}(c)$ is a domain assignment function, $\text{dom}(c) \subseteq \mathcal D$: returns a set of domains associated with a synset $c$ 
- $R_s(D, c) = \begin{cases}
1 / | \text{dom}(c)| & \text{ if } D \in \text{dom}(c) \\  |1 / k & \text{ if } \text{dom}(c) \equiv \{ \text{Factotum} \} \\ 
0 & \text{ otherwise } \\ 
\end{cases}$
- Factotum = generic concept for all non-domain words
- $k$ - cardinality of $\mathcal D$
- $R_s(D, c) \approx$ estimated prior probability of the domain given the concept 


This is for synsets, not words
- now let $V = \{ w_1 , \ ... \ , w_n \}$ the vocabulary
- then domain relevance of a word is a function $R: \mathcal D \times V \to \mathbb R$ 
- define $R$ as $$R(D_z, w_i) = \cfrac{1}- so it's average relevance of all $w_i$'s senses
- if $w$ has only one sense, then $R(D_z, w) = R_s(D_z, c)$
- a word with several senses ("polysemous") will be less relevant than a word with few senses 
- words with just one sense are ("monosemic") - they will be the most relevant: they provide more information about the domain


This is consistent with the phenomenon that less frequent words are more informative: because they have fewer senses


The domain model $D$ is defined as $D_{ij} = R(D_j, w_i)$


Limitations: 
- $\mathcal D$ is fixed because WordNet Domains is fixed
- WordNet Domains is limited: not complete
- and lexicon in WordNet Domains is also limited



### Corpus-Based Acquisition of Domain Models
We want automatically extract domain models from corpus:
- to avoid subjectivity
- to find more flexible models 


[Term Clustering](Term_Clustering) techniques are usually used for this
- usually need soft clustering techniques for this: want one term to be in several clusters 
- there are several ways: 
- [Fuzzy C-Means](Fuzzy_C-Means), Information bottleneck method, etc
- we'll use [Latent Semantic Analysis](Latent_Semantic_Analysis)


LSA is done by projecting TermVSM and TextVSM to a common LSA space using some linear transformations
- first-order (shallow) relations between terms: their co-occurrence in texts
- it takes into account both second-order relations: their semantics, established by co-occurrence


DO [SVD](SVD):
- $T = W \Sigma P^T$ 
- $W$ (for '''W'''ords) are orthogonal eigenvectors of $T T^T$: word vectors
- $P$ (for '''P'''assages) are orthogonal eigenvectors of $T^T T$: document vectors
- Truncated SVD: use $\Sigma_k$: first $k$ singular values and the rest set to 0
- $T_k = W \Sigma_k P^T \approx T$ the best approximation 


Now let's define the domain matrix 
- $D = I^{\text{N}} W \sqrt{\Sigma}$
- $I^{\text{N}}$ is a diagonal matrix s.t. $I^{\text{N}}_{ii} = \cfrac{1}{\|  w_i \- $w_i$ is $i$th column of $W \sqrt{\Sigma}$ - principal components ($W \sqrt{\Sigma}$ are loadings for words) |



### Domain Space
Domain Models define the Domain Space

Once a DM is determined, we can define a Domain Space 
- it's a geometric space where terms and documents can be represented as vectors 
- it's a [Vector Space Model](Vector_Space_Models)


There are some problems of VSMs:
- TextVSM can't deal with lexical ambiguity and variability
- e.g.: "he's affected by AIDS" and "HIV is a virus" don't have any words in common
- so in the TextVSM the similarity is 0: these vectors are orthogonal even though the concepts are related 
- on the other hand, similarity between "the laptop has a virus" and "HIV is a virus" is not 0: due to the ambiguity of "virus"


Term VSM: 
- feature sparseness 
- if we want to model domain relations, we're mostly interested in domain-specific words 
- such words are quite infrequent compared to non-domain words, so vectors for these words are very sparse, esp in large corpus 
- so similarity between domain words would tend to 0
- and the results overall will not be very meaningful and interesting


Domain Spaces ftw


so a '''Domain Space''' is a cluster-based representation for estimating term and text meaning 
- it's a vector space where both terms and texts can be compared 
- once a domain space is defined by a matrix $D$, can represent both terms and texts by domain vectors
- domain vectors - vectors that represent relevance among linguistic objects and each domain


Domain space is 
- it's an instance of Generalized Vector Space Model
- for text $t_i$ in the [Text VSM](Vector_Space_Models)
- $t_i' = t_i (I^{\text{idf}} D)$ ({{ TODO |  why left multiplication? }}) |- where $I^{\text{idf}}$ is a diagonal matrix s.t. $I^{\text{idf}}_{ii} = \text{idf}(w_i)$ - it's inverse document frequency of word $w_i$ (see [TF-IDF](TF-IDF))
- so we define a mapping function and thus have a generalized VSM

In the domain space the vector representation of terms and documents is "augmented" by domain relations represented by the domain model 


Geometrically: 
- <img src="http://habrastorage.org/files/0fe/98c/f82/0fe98cf82f2b4e369c5043c522b283a6.png" alt="Image">
- source: [Semantic Domains in Computational Linguistics (book)](Semantic_Domains_in_Computational_Linguistics_(book)), Fig 3.2
- both terms and texts are represented in common vector space 
- so comparison between terms and texts are possible
- also, the dimensionality of Domain Space is generally lower 


Domain Space allows to reduce the impact of ambiguity and variability: 
- by introducing non-sparse space 


So advantages of DS:
- lower dimensionality
- sparseness is avoided 
- duality: allows direct and uniform similarity between texts and terms 


### Domain Kernel
Domain Kernel is a similarity function for terms and documents in the domain space. Domain Kernel is a Mercer [Kernel](Kernel), so it can be used in any kernel-based algorithm.

This kernel is represented by a DOmain Model matrix $D$ 
- $K : \mathbb R^n \cup V \to \mathbb R^k$ 
- maps texts $t \in \mathbb R^n$  and terms $w \in V$ into Domain Space: $t' \in \mathbb R^k$ and $w' \in \mathbb R^k$


$K$ is defined as 
- $K(w) = w_i'$ if $w = w_i \in V$ 
- $K(w) = \cfrac{\sum_{t \in T} \text{tf}(w, t) \cdot t'} {\|  \sum_{t \in T} \text{tf}(w, t) \cdot t' \- $K(t) = t (I^{text{idf}} D) = t'$ for documents |- $\text{tf}(w, t)$ is a term frequency of $w$ in text $t$ 
- $I^{\text{idf}}$ is a diagonal matrix with IDFs: $I^{\text{idf}}_{ii} = \cfrac{1}

Can compute the similarity using cosine 

$K$ is defined for any term and text
- $K$ is a mercer kernel by construction: it's a dot product, but unlike many other kernels, it reduces the dimensionality instead of increasing it



## Usage
- after that we can use Domain Models for many NLP task
- can use domain model to estimate topic similarity


Domain Kernels can be used for any instance-based algorithm in many NLP applications:
- [Document Classification](Document_Classification)
- [Document Clustering](Document_Clustering)
- [Term Clustering](Term_Clustering)
- can use any [Machine Learning](Machine_Learning) algorithm with this kernel, e.g. [SVM](SVM)




## References
- Leacock, Claudia, et al. "Towards building contextual representations of word senses using statistical models." (1996). [http://anthology.aclweb.org/W/W93/W93-0102.pdf]


## Sources
- http://www.semdom.org/description
- [Semantic Domains in Computational Linguistics (book)](Semantic_Domains_in_Computational_Linguistics_(book))

[Category:Natural Language Processing](Category_Natural_Language_Processing)
[Category:Thesis](Category_Thesis)