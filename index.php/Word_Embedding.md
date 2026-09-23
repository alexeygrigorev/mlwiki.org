---
layout: default
permalink: /Word_Embedding
tags:
- nlp
- machine-learning
title: Word Embedding
---

## Word Embedding

https://en.m.wikipedia.org/wiki/Distributional_semantics#Distributional_Hypothesis
https://en.m.wikipedia.org/wiki/Semantic_memory#Hyperspace_Analogue_to_Language_.28HAL.29
https://en.m.wikipedia.org/wiki/Semantic_similarity
https://en.m.wikipedia.org/wiki/Random_indexing
https://en.m.wikipedia.org/wiki/Second-order_co-occurrence_pointwise_mutual_information

Word Embeddings / Distributed Word Representation

A word embedding W:words→RnW:words→Rn is a paramaterized function mapping words in some language to high-dimensional vectors (perhaps 200 to 500 dimensions). For example, we might find:

## Usual
VSM LSI HAL
LDA

## Neural Networks
http://colah.github.io/posts/2014-07-NLP-RNNs-Representations

In the proposed approach one learns simultaneously (1) a distributed representation
for each word (i.e. a similarity between words) 

1.1 Fighting the Curse of Dimensionality with its Own Weapons
In a nutshell, the idea of the proposed approach can be summarized as follows:
1. associate with each word in the vocabulary a distributed “feature vector” (a realvalued
vector in Rm), thereby creating a notion of similarity between words,
2. express the joint probability function of word sequences in terms of the feature
vectors of these words in the sequence, and
3. learn simultaneously the word feature vectors and the parameters of that function.

The feature vector represents different aspects of a word: each word is associated with a
point in a vector space. The number of features (e.g. m  30 60 100
in the experiments)
is much smaller than the size of the vocabulary.

Why does it work? In the previous example, if we knew that dog and cat played similar
roles (semantically and syntactically), and similarly for (the,a), (bedroom,room),
(is,was), (running,walking), we could naturally generalize from The cat is
walking in the bedroom to A dog was running in a room and likewise
to many other combinations. In the proposed model, it will so generalize because “similar”
words should have a similar feature vector

]. Learning a clustering of
words [10, 1] is also a way to discover similarities between words. In the model proposed
here, instead of characterizing the similarity with a discrete random or deterministic variable
(which corresponds to a soft or hard partition of the set of words), we use a continuous
real-vector for each word, i.e. a distributed feature vector, to indirectly represent similarity
between words. The idea of using a vector-space representation for words has been well
exploited in the area of information retrieval (for example see [12]), where vectorial feature
vectors for words are learned on the basis of their probability of co-occurring in the
same documents (Latent Semantic Indexing [4]). An important difference is that here we
look for a representation for words that is helpful in representing compactly the probability
distribution of word sequences from natural language text. 

Experiments indicate that
learning jointly the representation (word features) and the model makes a big difference in
performance.

http://www.iro.umontreal.ca/~lisa/publications2/index.php/attachments/single/74

### word2vec

Many different types of models were proposed for estimating continuous representations of words,
including the well-known Latent Semantic Analysis (LSA) and Latent Dirichlet Allocation (LDA).
In this paper, we focus on distributed representations of words learned by neural networks, as it was
previously shown that they perform significantly better than LSA for preserving linear regularities
among words [20, 31]; LDA moreover becomes computationally very expensive on large data sets

3.1 Continuous Bag-of-Words Model

given context around predict the word

3.2 Continuous Skip-gram Model

given word predict context around

## Algebraic Relations
special properties ,see w2v

http://arxiv.org/pdf/1301.3781.pdf
https://code.google.com/p/word2vec/
