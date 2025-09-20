---
layout: default
permalink: /index.php/Math-Aware_POS_Tagging
tags:
- nlp
- thesis
title: Math-Aware POS Tagging
---
## Math-Aware POS Tagging
[POS Tagging](POS_Tagging) is one of the [NLP](NLP)  task, but what about scientific documents with math expressions? 
- can adjust traditional POS Tagging methods to handle formulas 


### Classification
[Penn Treebank POS Scheme](Penn_Treebank_POS_Scheme) doesn't have special classes for mathematics.
What we can do is to add other math-related classes:

- '''ID''' for identifiers (e.g. "... where $E$ stands for energy", $E$ should be tagged as ID)
- '''MATH''' for formulas (e.g. "$E = mc^2$ is the mass-energy equivalence formula", "$E = mc^2$ should be tagged as '''MATH''')


### Text Preprocessing
Mathematical expressions are usually contained within special tags, e.g. inside tag <code>&lt;math&gt;&lt;/math&gt;</code> for wikipedia, or inside <code>$$</code> for latex documents. 

- We find all such mathematical expressions and replace each with a unique single token "'''MATH_mathID'''"
- the mathID could be a randomly generated string or result of some hash function applied to the content of formula. The latter approach is preferred when we want to have consistent strings across several runs. 
- Then we apply traditional [POS Tagging](POS_Tagging) techniques to the textual data. They typically will annotate such "'''MATH_mathID'''" tokens as nouns
- after that we may want to re-annotate all math tokens: if it contains only one identifier, we label it as '''ID''', if several - as '''MATH'''. But in some cases we want to keep original annotation
- after that we can bring the mathematical content back to the document


### Usage
- Can be used in Mathematical NLP
- e.g. in [Mathematical Definition Extraction](Mathematical_Definition_Extraction)


## Sources
- Kristianto, Giovanni Yoko, et al. "Extracting definitions of mathematical expressions in scientific papers." 2012. [https://kaigi.org/jsai/webprogram/2012/pdf/719.pdf]
- Pagael, Robert, and Moritz Schubotz. "Mathematical Language Processing Project." 2014. [http://arxiv.org/pdf/1407.0167]
- Schöneberg, Ulf, and Wolfram Sperber. "POS Tagging and its Applications for Mathematics." 2014. [http://arxiv.org/pdf/1406.2880]
