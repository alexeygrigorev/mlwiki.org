---
title: "Smoothing for Language Models"
layout: default
permalink: /index.php/Smoothing_for_Language_Models
---

# Smoothing for Language Models

## Smoothing for Language Models
It's a form of [Regularization](Regularization) for [Statistical Language Models](Statistical_Language_Models)


## Parameter Estimation
Suppose $\theta$ is a Unigram [Statistical Language Model](Statistical_Language_Model)
- so $\theta$ follows [Multinomial Distribution](Multinomial_Distribution)
- $D$ is a document consisting of words: $D = \{w_1, \ ... \ , w_m \}$
- $V$ is the vocabulary of the model: $V = \{ w_1, \ ... \ , w_M \}$
- By the unigram model, each word is independent, so
- $P(D \mid \theta) = \prod_i P(w_i \mid \theta) = \prod_{w \in V} P(w \mid \theta)^{c(w, D)}$
- where $c(w, D)$ is the term frequency: how many times $w$ occurs in $D$ (see also [TF-IDF](TF-IDF))
- how do we estimate $P(w \mid \theta)$?

With MLE, we have:

$\hat p_\text{ML} (w \mid \theta) = \cfrac{c(w, D)}{\sum_{w \in V} c(w, D)} = \cfrac{c(w, D)}
No smoothing



[Smoothing](Smoothing)
- MLE may [overfit](Overfitting) the data: it will assign 0 probabilities to words it hasn't seen 
- What to do with it? 
- [Bayesian Parameter Estimation](Bayesian_Parameter_Estimation) can both maximize the data likelihood and incorporate the prior belief to "smooth" the estimate
- use MAP: [Maximum A Posteriori Estimation](Maximum_A_Posteriori_Estimation):
- $\hat \theta = \operatorname{arg max}_{\theta} P(\theta \mid D) = \operatorname{arg max}_{\theta} P(D \mid \theta) \, P(\theta)$
- so we can define some prior $P(\theta)$, and depending on the choice of prior, we'd have different estimators
- if the prior prefers models that don't assign 0 probability to any $w$, then at the end we won't have 0 entries 
- adjusting MLE to avoid 0 probability is called "smoothing" - it's a form of regularization



## Interpolation Smoothing
Discount some probability mass of seen words 
- then discounted probability is shared between all words: seen and unseen
- so it's some sort of interpolation between LME probabilities and prior/collection model


=== Additive Smoothing === 
[Laplace Smoothing](Laplace_Smoothing) (or Additive Smoothing):
- $\hat p_\lambda (w \mid \theta) = \cfrac{c(w, D) + \lambda}{\sum_{w \in V} c(w, D)} = \cfrac{c(w, D)}- so it gives the same probability mass $\cfrac{\lambda}
If $\lambda = 1$ then we have "+1 Smoothing"


### Collection Smoothing
- Additive smoothing gives the same probability mass $\cfrac{\lambda}- it may not be what we want: maybe we want to give more or less weight to certain words
- so the idea is to have some reference language model 
- if we have a corpus, then we can use this corpus to learn the LM on the entire corpus
- such corpus LM is called "Collection LM" or "Background LM"


#### Collection LM
There are two ways of building the Collection LM:
- let $P(w \mid C)$ denote the collection LM


1) Each word contributes equally
- $P(w \mid C) = \cfrac{\sum_{D \in C} c(w, D)}{ \sum_{D \in C} | D- it's the same as if we concatenated all documents in $C$ into one |- "Macro-averaging"


2) Each document contribute equally
- $P(w \mid C) = \cfrac{1}{N} \sum_{D \in C} \cfrac{c(w, D)}{ | D- average contribution of each doc |- "Micro-averaging"

Approach (1) is more popular than (2)


#### Smoothing with Collection LM
Once we learned the Collection LM, we can use it to smooth the probabilities:

$$P(w \mid \hat \theta) = \begin{cases}
P_{\lambda} (w \mid \theta) & \text{ if } w \in D\\ 
\alpha \cdot P(w \mid C) & \text{ else }
\end{cases}$$


Where
- $P_{\lambda} (w \mid \theta)$ smoothed probabilities (with Laplace Smoothing)
- $\alpha$ coefficient that controls how much prob. mass is assigned to unseen words
- One way: $\alpha = \cfrac{1 - \sum_{w : \ c(w, D) > 0} P_{\lambda}(w \mid \theta) }{1 - \sum_{w : \ c(w, D) > 0} P(w \mid \theta)}$
- When we're doing Laplace smoothing, we take some probability mass from each seen words and re-distribute it evenly 
- here we distribute it according to Collection LM


### Jelinek-Mercer Smoothing
Or "Fixed Coefficient Interpolation"

Interpolate MLE with the collection LM
- use some coefficient of interpolation $\beta$ 
- $P_\beta(w \mid \hat \theta) = (1 - \beta) \, \cfrac{c(w, D)}

### Dirichlet Prior Smoothing
It's a Bayesian Smoothing with special prior: [Dirichlet Distribution](Dirichlet_Distribution)
- $\text{Dir}(\theta \mid \boldsymbol \alpha) = \cfrac{\Gamma \left( \sum_{i} \alpha_i \right)}{\prod_i  \Gamma(\alpha_1)} \cdot \prod_i \theta_{i}^{\alpha_i - 1}$
- params: $\boldsymbol \alpha = (\alpha_1, \ ... \ , \alpha_- let $\alpha_i = \mu \cdot P(w_i \mid C)$, $\mu$ - param, $P(w_i \mid C)$


Dirichlet is a [Conjugate Prior](Conjugate_Prior) for [Multinomial Distribution](Multinomial_Distribution)
- it means that the prior has the same functional form as the likelihood


Posterior:
- $P(\theta \mid D) \propto \prod_{w \in V} P(w \mid \theta)^{c(w, D) + \mu \, P(w \mid C) - 1}$ 
- posterior is also Dirichlet distribution with $\alpha_i = c(w_i, D) + \mu \, P(w \mid C)$


Dirichlet Smoothing:
- $P_\mu(w \mid \hat \theta) = \cfrac{c(w, D) + \mu \, P(w \mid C)}- Compare with Jelinek-Mercer: same if $\beta = \cfrac{\mu}{\mu + | D |
"Eventually, data overrides the prior":
- for a fixed $\mu$ longer documents will get less smoothing
- as $| D| \to \infty$, smoothing $\to 0$ |

Notes: 
- the smoothing adds a pseudo count $\mu P(w \mid C)$ to each word
- thus Additive Smoothing is a special case of Dirichlet smoothing with uniform Collection LM


### Absolute Discounting Smoothing
- $P_\delta (w \mid \hat \theta) = \cfrac{\max \big( c(w, D) - \delta, 0 \big) }{\sum_{w' \in V} c(w', D)} + \sigma \, P(w \mid C)$
- $\delta \in [0, 1]$ discounting factor
- $\sigma = \delta \cfrac


## Backoff
Interpolation:
- discount some probability mass from seen words, reassing it to both seen and unseen
- problem with this approach: some words may end up with counts even higher than the original
- for example, if a word is frequent in the collection LM 


Alternative Strategy: ''Back Off''
- trust MLE for high count words
- but discount and redistribute probability mass for less common terms
- popular in [Speech Recognition](Speech_Recognition), but less popular in [Information Retrieval](Information_Retrieval)


## Other Smoothing Methods
### Good-Turing  Smoothing
Idea:
- # of unseen events = # of "singletons": words that occur only once 
- let $\hat{c}(w, D)$ be the adjusted count of $w$ 
- then $P(w \mid \hat \theta) = \cfrac{\hat{c}(w, D)}

What is  $\hat{c}(w, D)$?
- let $n_r$ denote # of words that occur $r$ times in $D$ 
- then the adjusted is done via:
- $\hat{c}(w, D) \, n_{c(w, D)} = \big(c(w, D) + 1\big) \, n_{c(w, D) + 1}$


Intuition
- let's pretend that none of the singletones were observed 
- use this to estimate the total # of unseen words


Improvements:
- Gale, William, and Geoffrey Sampson. "Good-Turing smoothing without tears." 1995. [https://faculty.cs.byu.edu/~ringger/CS479/papers/Gale-SimpleGoodTuring.pdf]



## Smoothing vs [TF-IDF](TF-IDF)
Smoothing and TF-IDF are connected
- also see probabilistic justification for TF-IDF in 
  - Hiemstra, Djoerd. "A probabilistic justification for using tf× idf term weighting in information retrieval." 2000. [http://doc.utwente.nl/66959/1/ijodl.pdf]



Let's derive a query retrieval function using the smoothed log likelihood:
- $Q$ is a query
- assuming the general smoothing scheme: (comparing $Q$ with each $D$)
- $\log P(Q \mid \theta) = \sum_{w \in V} c(w, Q) \, \log P(w \mid \theta) = \sum_{w \in D} c(w, Q) \, \log P_S(w \mid \theta) + \sum_{w \not \in D} c(w, Q) \, \alpha \log P(w \mid \theta)$
- $\sum_{w \not \in D} c(w, Q) \, \alpha \log P(w \mid \theta) = \sum_{w \in V} c(w, Q) \, \alpha \log P(w \mid \theta) - \sum_{w \in D} c(w, Q) \, \alpha \log P(w \mid \theta)$: 
  - words that are not in the document = all words - words that are in the document
- let's regroup it:
- $\log P(Q \mid \theta) = \sum_{w \in D} c(w, Q) \, \log \cfrac{P_S (w \mid \theta) }{\alpha \, P(w \mid C)} + | Q| \, \log \alpha + \sum_{w \in V} c(w, Q) \, \alpha \log P(w \mid \theta) = \ ...$ |- can ignore the last term $\sum_{w \in V} c(w, Q) \, \alpha \log P(w \mid \theta)$ because it will not affect the ranking 
- thus we're left with 
- $\log P(Q \mid \theta) \mathop{=}\limits^{\text{rank}} \sum_{w \in D} c(w, Q) \, \log \cfrac{P_S (w \mid \theta) }{\alpha \, P(w \mid C)} + | Q| \, \log \alpha$   |

Observe:
- form of this smoothed retrieval function is similar to TF-IDF:
- first term: $\sum_{w \in D} c(w, Q) \, \log \cfrac{P_S (w \mid \theta) }{\alpha \, P(w \mid C)}$
- it sums over all matched terms - ones with $c(w, Q) > 0$ 
- $P_S (w \mid \theta)$ would be larger for words with high TF ($\approx$ TF heuristic)
- frequent items in collection would have high $P(w \mid C)$ and thus smaller overall weight ($\approx$ IDF heuristic)


## Other Smoothing Ideas
### Clustering / KNN Smoothing
Smoothing all documents from $C$ with the same collection LM may be not the most optimal approach
- maybe need to try more "individual" approaches


Can try:
- cluster all documents prior indexing, build a cluster LM for each cluster, and then smooth documents using their associated cluster LM
- find [KNN](KNN) docs, and then smooth using them 




## References
- Chen, Stanley F., and Joshua Goodman. "An empirical study of smoothing techniques for language modeling." 1996 [and 1999 [http://u.cs.biu.ac.il/~yogo/courses/mt2013/papers/chen-goodman-99.pdf](http://arxiv.org/pdf/cmp-lg/9606011.pdf]).


## Sources
- Zhai, ChengXiang. "Statistical language models for information retrieval." 2008.


[Category:NLP](Category_NLP)
[Category:Information Retrieval](Category_Information_Retrieval)
[Category:Regularization](Category_Regularization)