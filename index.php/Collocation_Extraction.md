---
layout: default
permalink: /index.php/Collocation_Extraction
tags:
- nlp
- text-mining
title: Collocation Extraction
---
## Collocation Extraction
There's no commonly accepted definition of "collocation", but it's usually a multiple-word token (i.e. an $n$-gram) where
- the words of the ngram co-occur together more often than by chance alone
- usually they mean something collectively, something different from what each word means alone

Other names for collocations:
- compound terms 
- multi-word terms
- $n$-grams

### Types of Collocations
There are two types of collocations:
- Open Compounds 
- Compositional Collocation 

Open Compounds 
- uninterrupted sequences of words that generally function as a single "word" in the text 
- e.g. "stock market", "foreign exchange"

Compositional Collocation 
- a sequence interrupted by preposition or a conjunction 
- e.g. "cure for cancer", "guns and ammunitions"

### Applications
There are following applications for Collocation Extraction 
- [Indexing](Inverted_Index), [Information Retrieval](Information_Retrieval)
- [Language Generation](Language_Generation)
- [Word Sense Disambiguation](Word_Sense_Disambiguation)
- [Document Classification](Document_Classification)
- and many others 

[Information Retrieval](Information_Retrieval)
- in IR these words may represent documents better than unigram tokens
- some tri-grams and higher order $n$-grams may be good for IR, even though they aren't compound term - in the sense of the definitions above. 


### Identification of Collocations
How to find and extract collocations? 
- by "co-occur more often than by chance" we can mean independence 
- so we can test if the words in the collocation are independent or not
- if they aren't - then maybe it's a collocation
- we also can use some measures than quantify the dependence between words - and the higher the measure, the more likely the words form a collocation


## Two Word Collocations
Let us start by considering the bigram collocation case
- suppose the collocation candidate is $(w_1, w_2)$ 
- if both $w_1$ and $w_2$ are frequent, they may co-locate just by chance, even if they don't form a collocation
- we want to test if this collocation occurs significantly more often than by chance
- for that we can compare how often $w_1$ and $w_2$ occur independently, and how often they occur together
- can do [Hypothesis Testing](Hypothesis_Testing) for that

General framework:
- under the Independence hypothesis ($H_0$) we assume that there is no association between $w_1$ and $w_2$, i.e. they are independent 
- let $P(w_1)$ and $P(w_2)$ are probabilities that a random token in a text is $w_1$ and $w_2$ resp.
- and $P(w_1, w_2)$ is the probability that $(w_1, w_2)$ occur together in the text (i.e. one follows another) 
- so under $H_0$, $P(w_1, w_2) = P(w_1)\, P(w_2)$
- we can compute the observed probability of $P(w_1, w_2)$ and compare it with the probability under $H_0$  
- if these probabilities are significantly different from each other, then $(w_1, w_2)$ is a collocation


Ranking candidates 
- if we can measure the degree of dependence, we can rank the candidate collocation
- usually tests have some test statistics which we can use for ranking candidates
- often it is more interesting to look at the top ranking candidates rather than at all of them


Ways to test/rank:
- [$T$-test](T-test)
- Odds Ratio
- [Point-Wise Mutual Information](Point-Wise_Mutual_Information)
- [Chi-Squared Test](Chi-Squared_Test)
- The [Dice Coefficient](Dice_Coefficient) $\text{DICE}(w_1, w_2) = \cfrac{2 \, c(w_1, w_2)}{c(w_1)\, c(w_2)}$
- [Log Likelihood Ratio](Log_Likelihood_Ratio) ([Entropy](Entropy) version): $G^2 = \sum_{ij} O_{ij} \log \cfrac{O_{ij}}{E_{ij}}$
- and others 
- these measures are usually based on frequencies obtained from some corpus


### [$T$-tests](T-test)
$t$-test can also be used for collocation discovery
- it looks at the mean and variance 
- can use $t$-test for proportions: $t = \cfrac{\bar x - \mu}{\sqrt{s^2 / N}}$

The idea:
- The probability of generating a bigram $(w_1, w_2)$ is a [Bernoulli Random Variable](Bernoulli_Random_Variable) with $p= P(w_1, w_2)$ 
- for Bernoulli, $\mu = p$ and $\sigma^2 = p\, (1-p)$
- because $p$ is typically quite small, $\sigma^2 \approx p$ for most bigrams
- then we can calculate the $t$-value and the corresponding critical value ($N$ = number of unigrams)
- and if $t$ is large enough, reject $H_0$ 
- but in this case, it's more useful to rank values by their $t$ rather than just know if a bigram passes a test or not


### Other Tests
Other tests can also be used 
- e.g. [Chi-Squared Test](Chi-Squared_Test) (see [Chi-Squared Test of Independence](Chi-Squared_Test_of_Independence))
- it's a good alternative for t-test

it's applied to 2-by-2 table 
- in essence, it compares observed frequencies to expected frequencies 
- if the difference is large - reject $H_0$ 
- $X^2 = \sum_{ij} \cfrac{(O_{ij} - E_{ij})^2}{E_{ij}}$
- $X^2$ is distributed as $\chi^2$


### [Odds Ratio Test](Odds_Ratio_Test)
To compare $P(w_1, w_2)$ with $P(w_1) \, P(w_2)$ we can use the Odds Ratio:
- [Odds Ratio](Odds_Ratio) is $\cfrac{P(w_1, w_2)}{P(w_1) \, P(w_2)}$
- collocations should have scores higher than 1
- the higher the ratio, the more likely a bigram is a collocation


### [Point-Wise Mutual Information](Point-Wise_Mutual_Information)
[Mutual Information](Mutual_Information):
- it's a measure on how much one word tells about the other 
- In [Information Theory](Information_Theory), Mutual Information is defined between Random Variables, not words (values of RVs)
- which is why we use PMI

Point-Wise Mutual Information (PMI):
- instead of Odds Ratio, can use [Log Odds](Log_Odds):
- $\log \cfrac{P(w_1, w_2)}{P(w_1) \, P(w_2)}$
- then it becomes [Point-Wise Mutual Information](Point-Wise_Mutual_Information)
- $\text{PMI}(w_1, w_2) = \log \cfrac{P(w_1, w_2)}{P(w_1)\, P(w_2)} = \log \cfrac{P(w_1) \, P(w_2 \mid w_1)}{P(w_1)\, P(w_2)} = \log \cfrac{P(w_2 \mid w_1)}{P(w_2)}$


PMI is the amount of information we get when 
- a word $w_1$ occurs at position $i$ 
- and it's followed by $w_2$ at position $i+1$


PMI can generalize to any $n$-grams
- suppose $\mathbf x$ and $\mathbf y$ are vectors (not necessarily of the same dimensions)
- then $\text{PMI}(\mathbf x, \mathbf y) = \log \cfrac{P(\mathbf x, \mathbf y)}{P(\mathbf x)\, P(\mathbf y)}$
- also see the [#$n$-Gram Collocations](#$n$-Gram_Collocations) section


## Estimates

### [Maximum Likelihood Estimator](Maximum_Likelihood_Estimator)
Estimation of $P(w_1)$, $P(w_2)$ and $P(w_1, w_2)$:
- these probabilities are estimated from a corpus 
- typically using [Maximum Likelihood Estimator](Maximum_Likelihood_Estimator)
- No [Smoothing](Smoothing_for_Language_Models) is typically needed because we don't need to generalize to unseen words
- We want to extract collocations from a given corpus, not to build a [Statistical Language Model](Statistical_Language_Model)

[MLE](MLE) of $P(w_1)$ and $P(w_2)$: 
- $\hat P(w) = \cfrac{c(w)}{N}$, where 
- $c(w)$ is the number of times $w_1$ appeared in the corpus, and 
- $N$ is the total number of tokens


[MLE](MLE) of $P(w_1, w_2)$
- $P(w_1, w_2) = P(w_1) \, P(w_2 \mid w_1)$, so 
- $\hat P(w_1, w_2) = \hat P(w_1) \, \hat P(w_2 \mid w_1) = \cfrac{c(w_1)}{N} \cdot \cfrac{c(w_1, w_2)}{c(w_1)} = \cfrac{c(w_1, w_2)}{N}$


so MLE estimate of PMI is 
- $\text{PMI}(w_1, w_2) = \log \cfrac{\hat P(w_2 \mid w_1)}{\hat P(w_2)} = \log \left( \cfrac{c(w_1, w_2)}{c(w_1)} \cdot \cfrac{N}{c(w_2)} \right)$


## $n$-Gram Collocations
For 3-grams:
- treat $(w_1, w_2)$ as a single var
- $\text{PMI}\Big((w_1, w_2), w_3 \Big) = \log \cfrac{P\big((w_1, w_2), w_3\big)}{P(w_1, w_2)\, P(w_3)} = \log \cfrac{P\big(w_1, w_2, w_3\big)}{P(w_1, w_2)\, P(w_3)}$
  - $P(w_1, w_2, w_3) = P(w_1) \, P(w_2 \mid w_1) \, P(w_3 \mid w_1, w_2)$
  - $\hat P(w_1, w_2, w_3) = \cfrac{c(w_1)}{N} \cdot \cfrac{c(w_1, w_2)}{c(w_1)} \cdot \cfrac{c(w_1, w_2, w_3)}{c(w_1, w_2)} = \cfrac{c(w_1, w_2, w_3)}{N}$
- So estimate of $\text{PMI}\big((w_1, w_2), w_3\big)$ is 
  - $\text{PMI}\big((w_1, w_2), w_3\big) = \log \left( \cfrac{c(w_1, w_2, w_3)}{N} \cdot \cfrac{N}{c(w_1, w_2)} \cdot \cfrac{N}{c(w_3)} \right) = \log \cfrac{N \cdot c(w_1, w_2, w_3)}{c(w_1, w_2) \, c(w_3)}$


For $n$-grams:
- $\text{PMI}\big((w_1, \, ... \, , w_n), w_{n+1} \big) = \log \cfrac{P(w_1, \ ... \ , w_{n+1})}{P(w_1, \ ... \ , w_n)\, P(w_{n+1})}$
- Estimate:
- $\text{PMI}\big((w_1, \, ... \, , w_n), w_{n+1} \big) = \log \cfrac{N \cdot c(w_1, \ ... \ , w_{n+1})}{c(w_1, \ ... \ , w_n) \, w(n_{n+1})}$




## References
- McInnes B. T. "Extending the log likelihood measure to improve collocation identification", 2004.
- Boulis C. "Clustering of Cepstrum Coefficients Using Pairwise Mutual Information", 2002.
- Tadić M., Šojat K. "Finding multiword term candidates in Croatian", 2003.
- Gerlof Bouma, "Normalized (Pointwise) Mutual Information in Collocation Extraction" [https://svn.spraakdata.gu.se/repos/gerlof/pub/www/Docs/npmi-pfd.pdf]

## Sources
- De Kok D., Brouwer H. "Natural language processing for the working programmer". 2011. Chapter 3 [[https://web.archive.org/web/20151026194211/http://nlpwp.org/book/chap-ngrams.xhtml archived version version](http://nlpwp.org/book/chap-ngrams.xhtml]), [google scholar](http://scholar.google.com/scholar?cluster=12545221866517295405&as_sdt=0,5)
- Manning C. D., Schütze H. "Foundations of statistical natural language processing", 1999. Chapter 5 [http://nlp.stanford.edu/fsnlp/promo/colloc.pdf]
- Petrović S. et al. "Comparison of collocation extraction measures for document indexing", 2006. [http://bib.irb.hr/datoteka/251298.110-4-157-203.pdf]
