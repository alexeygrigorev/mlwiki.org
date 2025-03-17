---
title: "Stop Words"
layout: default
permalink: /index.php/Stop_Words
---

# Stop Words

## Stop Words
Stop words are ''function words'':
- stop words are useful syntactically and grammatically, but don't tell anything about the document content 
- and they are topic-neutral: stop words have the same likelihood of occurring in both relevant and non-relevant documents - so not very useful for [Information Retrieval](Information_Retrieval)  
- they are present everywhere: usually most frequent words are stop words
- for example, "the", "a", "an", ...


## Stop Words Removal
In many cases stop words are not needed:
- for example, in [Information Retrieval](Information_Retrieval) or [NLP](NLP)
- they don't have enough descriptive power to distinguish between relevant and not relevant documents: all documents have them|   |- so, before [indexing](Inverted_Index) they are often removed |- it also makes the index much smaller
- it can be seen as a [Dimensionality Reduction](Dimensionality_Reduction) technique for text data


### [NLP Pipeline](NLP_Pipeline)
Stop words removal is a part of the [NLP Pipeline](NLP_Pipeline)
- for building [Inverted Index](Inverted_Index)
- for building [Vector Space Model](Vector_Space_Model)


### Implementing
- English: http://www.ranks.nl/stopwords
- http://www.textfixer.com/resources/common-english-words.txt

Stop words removal in NLTK [http://stackoverflow.com/questions/19130512/stopword-removal-with-nltk]:

```python
>>> from nltk.corpus import stopwords
>>> stop = stopwords.words('english')
>>> sentence = "this is a foo bar sentence"
>>> print [i for i in sentence.split() if i not in stop]
['foo', 'bar', 'sentence']
```


## Stop Words Usage
There are cases when stop words are not removed, and even used 

Examples:
- author identification ("the little words give authors away")
- language detection: languages have very distinctive set of stop words, so they can be used to detect the language of a text (see e.g. here [http://blog.alejandronolla.com/2013/05/15/detecting-text-language-with-python-and-nltk/])


## Stop Words Learning
- Stop words can be learned from the text, usually by looking at top words and manually selecting them 
- But this process can be automated (Wilbur1992):
- use [Term Strength](Term_Strength) for automatically discovering stop words
- Term Strength: given a pair of documents, what's the probability that when a term occurs in one document of the pair, it also occurs in another?  



## Sources
- [Information Retrieval (UFRT)](Information_Retrieval_(UFRT))
- Aggarwal, Charu C., and ChengXiang Zhai. "A survey of text clustering algorithms." Mining Text Data. 2012.
- Wilbur, W. John, "The automatic identification of stop words." 1992. [http://www.researchgate.net/publication/247786801_The_automatic_identification_of_stop_words]

[Category:Feature Selection](Category_Feature_Selection)
[Category:NLP](Category_NLP)
[Category:Information Retrieval](Category_Information_Retrieval)
[Category:Python](Category_Python)