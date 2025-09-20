---
layout: default
permalink: /index.php/OWL
tags:
- knowledge-representation
- semantic-web
title: OWL
---
## OWL
OWL - Web Ontology Language

Several languages 
- OWL-Full - No limits, but some things can be undecidable
- OWL-DL - [Descriptive Logic](Descriptive_Logic)
- OWL-Lite - [RDFS-Plus](RDFS-Plus), DL-Lite
- for logical semantics behind there expressions see [Semantic Web Logic](Semantic_Web_Logic)



## <code>owl:Restriction</code>: Restrictions
Allows to describe classes in terms of other things we already modeled 
- a Restriction in OWL is a Class defined by describing the individuals it contains
- <code>owl:Restriction rdfs:subClassOf owl:Class</code>


### Kinds of Restrictions
- <code>owl:someValuesFrom</code>
  - all individuals form which at least one value of the property $P$ comes from some class $C$ 
  - e.g. <code>:AllStarPlayer</code> is a <code>:Player</code> for which at least one value of <code>:playsFor</code> comes from the class <code>:AllStarTeam</code>
  - <code>[a owl:Restiction; owl:onProperty :playsFor; owl:someValuesFrom :AllStarTeam]</code>
  - if at least one team of this guy is of the class <code>:AllStarTeam</code> $\Rightarrow$ he is an <code>:AllStarPlayer</code>
- <code>owl:allValuesFrom</code> 
  - individuals for which all values of property $P$ come from class $C$
  - if there are any members, they all must have the same property
- <code>owl:hasValue</code>
  - all individuals that have some specific value $a$ for the property $P$ 
  - e.g. :JapanTeams - the set of all baseball <code>:Team</code>s <code>:from :Japan</code> 
  - e.g. Suppose we have a property <code>:orbitsAround</code>
    - then everything that <code>:orbitsAround :TheSun</code> belongs to the <code>:SolarSystem</code>
    - <code>[a owl:Restriction; owl:onProperty :orbitsAround; owl:hasValue :TheSun]</code>

Best way to use these restrictions:
- <code>rdfs:subClassOf</code>
- <code>owl:equivalentClass</code>


### Example: Questionnaire
- a questionnaire contains a number of questions 
- each question has some possible answers
- in contrast to a quiz there is no "right" answer
- the selection of some answers precludes other questions

Schema (namespace <code>q</code>):
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/ufrt/xml/sw/owl-rest-quest1.png" alt="Image">

```actionscript 3
q:optionOf a owl:ObjectProperty; 
    rdfs:domain q:Answer; 
    rdfs:range q:Question; 
    owl:inverseOf q:hasOption. 
q:hasOption a owl:ObjectProperty. 
q:answerText a owl:DatatypeProperty; 
    rdfs:domain q:Answer; 
    rdfs:range xsd:string. 
q:questionText a owl:FunctionalProperty, owl:DatatypeProperty;
    rdfs:domain q:Question; 
    rdfs:range xsd:string. 
q:Answer a owl:Class. 
q:Question a owl:Class.
```


Data (namespace <code>d</code>): 
```actionscript 3
d:WhatProblem a q:Question; 
    q:hasOption d:STV, d:SInternet, d:SBoth; 
    q:questionText "What system are you having trouble with?".
    d:STV a q:Answer; 
    q:answerText "Cable TV". 
d:SInternet a q:Answer; 
    q:answerText "High-speed Internet". 
d:SBoth a q:Answer;
    q:answerText "Both". 
    d:TVsymptom a q:Question; 
    q:questionText "What television symptoms are you having?";
    q:hasOption d:TVSnothing, d:TVSnosound, d:TVStiling, d:TVSreception.
d:TVSnothing a q:Answer; 
    q:answerText "No Picture". 
d:TVSnosound a q:Answer; 
    q:answerText "No Sound". 
d:TVStiling a q:Answer; 
    q:answerText "Tiling". 
    d:TVSreception a q:Answer; 
    q:answerText "Bad reception".
```


#### <code>owl:someValuesFrom</code>: Answered questions
For each question need to know what's selected 
- for that first define a special property <code>q:hasSelectedOption</code>:
  - <code>q:hasSelectedOption a owl:ObjectProperty; rdfs:subPropertyOf q:hasOption.</code>
- suppose that for <code>d:WhatProblem</code> the selected option is <code>d:STV</code>
  - <code>d:WhatProblem q:hasSelectedOption d:STV</code>
- a question is answered if it has a selected option (e.g. <code>d:WhatProblem</code> is answered)

```objective-c
q:AnsweredQuestion owl:equivalentClass 
    [a owl:Resrtiction; 
       owl:onProperty q:hasSelectedOption;
       owl:someValuesFrom q:Answer].
```


#### <code>owl:allValuesFrom</code>: Next Questions
Next questions should depend of what's been asked and answered
- first, define all answers that were selected 
- <code>q:SelectedAnswer a owl:Class; rdfs:subClassOf q:Answer</code>
- to make sure that any option that was selected will appear in this class: 
  - <code>q:SelectedAnswer rdfs:range q:SelectedAnswer</code>
  - e.g. <code>d:WhatProblem q:hasSelectedOption d:STV</code> $\Rightarrow$
  - <code>d:STV a q:SelectedAnswer</code>

now define questions that can be asked: <code>q:EnabledQuestion a owl:Class</code>
- when some answer is selected, we want to infer that some dependent questions become enabled
- each answer potentially makes some other questions enabled
- define property <code>q:enablesCandidate</code> for that

```actionscript 3
q:enablesCandidate a owl:ObjectProperty;
    rdfs:domain q:Asnwer;
    rdfs:range q:Question.

d:STV q:enablesCandidate d:TVsymptom. 
d:SBoth q:enablesCandidate d:TVsymptom.
```

Restriction:
- we want that only answers that were selected enforce this property
- so use <code>owl:allValuesFrom</code> and <code>rdfs:subClassOf</code>

```objective-c
q:SelectedAnswer rdfs:subClassOf [a owl:Restriction; 
    owl:onProperty q:enablesCandidate; 
    owl:allValuesFrom q:EnabledQuestion]
```


Inference example
- assume <code>d:STV</code> is selected: <code>d:STV a q:SelectedAnswer</code>
- infer that <code>d:STV a [a owl:Restriction; owl:onProperty q:enablesCandidate; owl:allValuesFrom q:EnabledQuestion]</code>
- any individuals related to it by <code>q:enablesCandidate</code> must be members of <code>q:EnabledQuestion</code>
- since <code>d:STV q:enablesCandidate d:TVsymptom</code> infer that <code>d:TVsymptom a q:EnabledQuestion</code>


## Sets and Counting
### Union and Intersection
- <code>U a owl:Class; owl:unionOf (ns:A ns:B ...) .</code>
- <code>I a owl:Class; owl:intersectionOf (ns:A ns:B ...) .</code>

Example:
- suppose we want to know what are enabled high-priority questions
```objective-c
q:CandidateQuestions owl:equivalentClass [
    a owl:Class;
      owl:intersectionOf(q:EnabledQuestion q:HighPriorityQuestion)]
```


### Set Enumeration: Closing the World
Recall the Open World Assumption (see [Semantic Web#Main Assumptions](Semantic_Web#Main_Assumptions))
- we can't be sure that if we don't have a record about some fact then it doesn't exist: 
- it can exist, but maybe we just don't know about it
- sometimes we need to "close the world": assume we know everything

<code>owl:oneOf</code>
- we assume that we can enumerate all the elements of some class 
- so we put a limit on the AAA slogan: now nobody can say something additional about this topic
- so handle it with care
- Example:
```actionscript 3
ss:SolarPlanet rdf:type owl:Class; 
    owl:oneOf (ss:Mercury ss:Venus  ss:Earth  ss:Mars
               ss:Jupiter ss:Saturn ss:Uranus ss:Neptune).
```


### Cardinality Restrictions
- to express constants on the # of individuals who can participate in some restriction class
- for example, a baseball team can have only 9 players 

```json
[a owl:Restriction;
   owl:onProperty :hasPlayer;
   owl:cardinality 9]
```

Also can use:
- <code>owl:minCardinality</code> - lower bound
- <code>owl:maxCardinality</code> - upper bound


### Set Compliment
<code>ex:ClassA owl:complimentOf ex:ClassB</code>
- ''compliment'' - another class whose members are things that don't belong to this ''complimented'' class
- $A = \Omega - B$

But it includes <u>everything</u> that is not in the complimented class
- e.g. <code>bb:MinorLeaguePlayer owl:complimentOf bb:MajorLeaguePlayer</code>
- this will include everything else in the universe: players, managers, fans, planets, etc
- solution: combine with intersection

```objective-c
bb:MinorLeaguePlayer owl:intersectionOf (
    [a owl:Class; owl:complimentOf bb:MajorLeaguePlayer]
    bb:Player)
```
- so <code>bb:MinorLeaguePlayer</code>s are <code>bb:Player</code>s who's not in Major League


### Disjoint Sets
<code>:Man owl:disjointSet :Woman</code>
- <code>:Irene a :Woman </code>
- <code>:Ralph a :Man</code>
- infer that <code>:Irene owl:differentFRom :Ralph</code>


## Links
Protégé 
- http://protege.stanford.edu/download/download.html
- useful tool for building OWL models
- good tutorial: http://owl.cs.manchester.ac.uk/tutorials/protegeowltutorial/


## See Also
- [RDFS and OWL Summary](RDFS_and_OWL_Summary)
- [Semantic Web](Semantic_Web)
- [RDF](RDF)
- [RDFS](RDFS)
- [RDFS-Plus](RDFS-Plus) - a subset of OWL and an extension of [RDFS](RDFS) with more inferencing capabilities
- [Inference in Semantic Web](Inference_in_Semantic_Web)
- [Semantic Web Logics](Semantic_Web_Logics)

## Sources
- [Semantic Web for the Working Ontologist (book)](Semantic_Web_for_the_Working_Ontologist_(book))
- [XML and Web Technologies (UFRT)](XML_and_Web_Technologies_(UFRT))
