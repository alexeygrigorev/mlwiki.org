---
title: SPARQL
layout: default
permalink: /index.php/SPARQL
---

# SPARQL

## SPARQL
In [Semantic Web](Semantic_Web), SPARQL is a query language for getting information from [RDF](RDF) graphs
- SPARQL = SPARQL Protocol and RDF Query Language
- matches graph patterns - so also a graph matching language 
- it's a variant of [Turtle](Turtle) adapted for querying
- variables denoted by <code>?</code>

Formal foundation
- e.g. [SQL](SQL) is based on [Relational Algebra](Relational_Algebra)
- SPARQL is based on Predicate Calculus
  - [First Order Logic](First_Order_Logic)
  - in most cases can be expressed as [Conjunctive Queries](Conjunctive_Query)


### Versions
SPARQL 1.0
- Basic Things

SPARQL 1.1
- Aggregations
- Negations
- Nested Queries 
- Transitive Properties 


### Query Types
There are 4 types
- SELECT query
- : results are in a table format.
- CONSTRUCT query
- : results are translated into valid RDF
- ASK query
- : Just TRUE/FALSE 
- DESCRIBE query
- : results are RDF graphs

All of them take <code>WHERE</code> clause


## Structure of a query
Generally, each query follows this structure
- Prefix declarations, for abbreviating URIs
  - <code>PREFIX foo: http://example.com/resources/...</code>
- Dataset definition, stating what RDF graph to query
  - <code>FROM ... </code>
- Result clause, identifying what information to return from the query
  - <code>SELECT ... </code>, <code>ASK ...</code>, <code>CONSTRUCT ...</code> or <code>DESCRIBE ...</code>
- Query pattern, specifying what to query for, in the underlying dataset
  - <code>WHERE { ... } </code>
- Query modifiers, slicing, ordering, and otherwise rearranging query results
  - <code>ORDER BY</code>, etc


Formally,
- A SPARQL query is a tuple $\langle P, G, D, S, R \rangle$: 
- $P$ stands for the prefix declarations ection 
- $G$ is a graph pattern (pattern of the query) 
- $D$ is a set of RDF data ("dataset" : database) 
- $S$ is a "result transformer": Projection,  Distinct, Order, Limit, Offset 
- $R$ is the type of the result: SELECT, CONSTRUCT, DESCRIBE, ASK 


## Select Queries
### Example 1
An example with prefix

 |  |
```turtle
PREFIX foaf: <http://xmlns.com/foaf/0.1/> 
SELECT ?name WHERE { 
  ?x foaf:name ?name
}
```

 |  |
result $\to$

 |  |
       |   name |        | Bob |        |  Alice |     

### Example 2
Consider this RDF graph [http://cs-www.cs.yale.edu/homes/dna/papers/sw-graph-scale.pdf]
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/ufrt/xml/sw/rdf-graph-ex3-sparql.png" alt="Image">

```verilog
SELECT ?player ?club
WHERE {
  ?player :position :striker .
  ?player :playsFor ?club .
  ?club :region :Barcelona 
}
```


the query itself is also a graph
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/ufrt/xml/sw/rdf-graph-ex3-q.png" alt="Image">
- now we match this graph with the data graph
- this query will select only Messi, because he's a striker 


In SQL it would be 

```verilog
SELECT
  A.subject, A.object
FROM
  triples AS A, triples AS B, triples AS C
WHERE
  B.predicate = "position" AND B.object = "striker"
  AND B.subject = A.subject AND A.predicate = "playsFor"
  AND A.object = C.subject AND C.predicate = "region"
  AND C.object = "Barcelona";
```


Also, this query can be translated to the following [Conjunctive Query](Conjunctive_Query)
- $\text{query}(p, c) \equiv \text{Position}(p, \text{``striker''}), \text{PlaysFor}(p, c), Region(c, \text{``Barcelona''})$


### Querying for Property
Can also query for a predicate 
- e.g. what do we know about James Dean? 

```text only
SELECT ?property ?value 
WHERE {
  :JamesDean ?property ?value
}
```

Also can use <code>DISTICNT</code> keyword

```text only
SELECT DISTINCT ?property 
WHERE {
  :JamesDean ?property ?value
}
```

Suppose we want to know anything about a class <code>Actor</code>

```text only
SELECT DISTINCT ?property 
WHERE 
  q0 a :Actor . 
  ?q0 ?property ?object .
}
```


## Where part
In this part matching happens 
- Generally, the same idea as in [Conjunctive Queries](Conjunctive_Query)
- There are ''existential variables'' (not from the head of the query)
  - they are matched with some data in the database and assigned some value
- as saw, here a graph is constructed and matched with 


### Filter: Value constraints
Boolean tests - not graph patterns
- Logical: <code>|  </code>, <code>&&</code>, <code> | </code>  |- Arithmetic: <code>+</code>, <code>-</code>, <code>*</code>, <code>/</code>  |- Comparison: <code>=</code>, <code>|  =</code>, <code>></code>, <code><</code>, ...  |- SPARQL tests: <code>isURI</code>, <code>isBlank</code>, <code>isLiteral</code>, <code>bound</code> |- SPARQL accessors: <code>str</code>, <code>lang</code>, <code>datatype</code>
- Other: <code>sameTerm</code>, <code>langMatches</code>, <code>regex</code> ...


Examples: 

```turtle
PREFIX dc: <http://purl.org/dc/elements/1.1/> 
PREFIX ns: <http://example.org/ns#> 
SELECT ?title ?price 
WHERE { 
  ?x ns:price ?price . 
  FILTER ?price < 30 . 
  ?x dc:title ?title . 
}
```


```text only
SELECT ?actor 
WHERE { 
  ?actor :playedIn :Giant . 
  ?actor :diedOn ?deathdate . 
  FILTER(?deathdate > "1961-11-24"^^xsd:date)
}
```


We can also have several filters
```text only
SELECT ?person 
WHERE{
  ?person a :Person . 
  ?person :bornOn ?birthday . 
  FILTER(?birthday > "Jan 1, 1960"^^xsd:date) 
  FILTER(?birthday < "Dec 31, 1969"^^xsd:date)
}
```


### Optional
When we don't want a query to fail if there is no data for something

Example:
- if price exists, filter on it; otherwise just include it

```turtle
PREFIX dc: <http://purl.org/dc/elements/1.1/> 
PREFIX ns: <http://example.org/ns#> 
SELECT ?title ?price 
WHERE { 
  ?x dc:title ?title . 
  OPTIONAL { 
    ?x ns:price?price . 
     FILTER ?price < 30 
  }
}
```

Also, can have several optionals 

```turtle
PREFIX foaf: <http://xmlns.com/foaf/0.1/> 
SELECT ?name ?mbox ?hpage
WHERE { 
  ?x foaf:name?name . 
  OPTIONAL { ?x foaf:mbox ?mbox } . 
  OPTIONAL { ?x foaf:homepage ?hpage} 
}
```


### Union
```turtle
PREFIX dc10: <http://purl.org/dc/elements/1.0/> 
PREFIX dc11: <http://purl.org/dc/elements/1.1/> 
SELECT ?x ?y 
WHERE {
  { ?book dc10:title ?x } 
  UNION
  { ?book dc11:title ?y } 
}
```

Can have several unions:

```text only
CONSTRUCT { ?s :hasParent ?o } 
WHERE { 
  { ?s :hasMother ?o } 
  UNION
  { ?s :hasFather ?o } 
  UNION
  { ?o :hasSon ?s } 
  UNION 
  { ?o :hasDaughter ?s }
}
```



### Negation (SPARQL 1.1)
Negation is achieved with a keyword <code>UNSAID</code>
- it introduces a subgraph 
- the overall graph pattern will match if the UNSAID pattern does not match.

This query will return all actors with no <code>:diedOn</code> record who played in "Giant"
```text only
SELECT ?actor 
WHERE {
  ?actor :playedIn :Giant . 
  UNSAID { ?actor :diedOn ?deathdate .} 
}
```


### Transitive Queries
Suppose we want to select Joe's children
- and then children of his children

```text only
SELECT ?member 
WHERE { ?member :hasParent :Joe } 

SELECT ?member 
WHERE {
  ?c :hasParent :Joe . 
  ?member :hasParent ?c .
}
```

<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/ufrt/xml/sw/sparql-transitive-1.png" alt="Image">

But what if we want to follow <code>:hasParent</code> as long as it's there?
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/ufrt/xml/sw/sparql-transitive-2.png" alt="Image">
- use <code>*</code> for that (only SPARQL 1.1)

```scdoc
SELECT ?member 
WHERE { ?member :hasParent* :Joe .}
```

But in this case it will also include <code>:Joe</code>
- i.e. it includes zero-length chains as well
- to avoid it, use <code>+</code> instead (like in [Regular Expressions](Regular_Expressions))

```text only
SELECT ?member 
WHERE { ?member :hasParent+ :Joe .}
```


### Ordering (SPARQL 1.1)
```googlesql
SELECT ?title ?date 
WHERE {
  :JamesDean :playedIn ?movie. 
  ?movie rdfs:label ?title . 
  ?movie dc:date ?date . 
} ORDER BY ?date

-- with limit
SELECT ?title 
WHERE {
  :JamesDean :playedIn ?m. 
  ?m rdfs:label ?title . 
  ?m dc:date ?date . 
} ORDER BY ?date 
LIMIT1 

-- inverse order
SELECT ?last 
WHERE { 
  ?who :playedIn :RebelWithoutaCause .
  ?who rdfs:label ?last . 
  ?who :diedOn ?date
} ORDER BY DESC(?date) 
LIMIT 1
```


### Aggregating and Grouping (SPARQL 1.1)
```googlesql
SELECT (COUNT(?movie) AS ?howmany) 
WHERE {:JamesDean ?playedIn ?movie .}

SELECT (SUM (?val) AS ?total)
WHERE {
  ?s a :Sale . 
  ?s :amount ?val 
}

SELECT ?year (SUM (?val) AS ?total)
WHERE {
  ?s a :Sale . 
  ?s :amount ?val . 
  ?s :year ?year 
} GROUP BY ?year


SELECT ?year ?company (SUM(?val) AS ?total) 
WHERE {
  ?s a :Sale . 
  ?s :amount ?val . 
  ?s :year ?year . 
  ?s :company ?company . 
} GROUP BY ?year ?company 

-- with filtering 
SELECT ?year ?company (SUM(?val) AS ?total) 
WHERE {
  ?s a :Sale . 
  ?s :amount ?val . 
  ?s :year ?year . 
  ?s :company ?company . 
} GROUP BY ?year ?company HAVING (?total > 5000)
```


### Subqueries (SPARQL 1.1)
```googlesql
SELECT ?company 
WHERE { 
  {
    SELECT ?company ((SUM(?val)) AS ?total09) 
    WHERE { 
      ?s a :Sale . 
      ?s :amount ?val . 
      ?s :company ?company . 
      ?s :year 2009 . 
    } GROUP BY ?company 
  } . 
  {
    SELECT ?company ((SUM(?val)) AS?total10) 
    WHERE { 
      ?s a :Sale . 
      ?s :amount ?val . 
      ?s :company ?company . 
      ?s :year 2010 .
    } GROUP BY ?company 
  } . 
  FILTER(?total10 > ?total09) . 
}
```


## Other Types of Queries
### Yes/No Queries
Use when we need just TRUE/FALSE

Example: do we have any <code>:diedOn</code> record for <code>:ElizabethTaylor</code>?
```text only
ASK WHERE {:ElizabethTaylor :diedOn ?any}
```

Or can use negation for that:
- e.g. is <code>:ElizabethTaylor</code> still alive?
```text only
ASK WHERE { UNSAID {:ElizabethTaylor :diedOn ?any} }
```


### <code>CONSTRUCT</code> Queries
"Select" queries 
- are run on a RDF graph, but return a table
- have no closure property 
- want to construct a valid RDF graph from the result 

```carbon
CONSTRUCT {
  ?d rdf:type :Director . 
  ?d rdfs:label ?name . 
}
WHERE {
  ?any :directedBy ?d . 
  ?d rdfs:label ?name . 
}
```

<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/ufrt/xml/sw/sparql-construct-ex1.png" alt="Image">


Can use these queries for 
- insert it back into this RDF store / another RDF store
- serialize to [XML/RDF](XML_RDF)


#### Rules
Construct queries provide a convenient way of specifying rules
- based on patterns found in your RDF graph - i.e. facts stored in the database 

Examples:
- from the previous example: if something is directed by <code>?d</code>, then <code>?d</code> must be a <code>:Director</code>
- these rules say "whenever you see this, conclude that"
- can be used to express inference rules in [Inference in Semantic Web](Inference_in_Semantic_Web)

Types of Rules
- completeness rules
  - John's father is Joe $\to$ Joe's son is John
- logical rules 
  - Socrates is a man, all men are mortal $\to$ Socrates is mortal
- definitions
  - Ted's sister is Maria's mother $\to$ Ted is Maria's uncle 
- business rules 
  - customers spent > 5000 USD are preferred customers 

```text only
CONSTRUCT{ ?q1 :hasSon :q2 .} 
WHERE {
  ?q2 a :Man . 
  ?q2 :hasFather ?q1
} 

CONSTRUCT { ?q1 a :Mortal } 
WHERE { ?q1 a :Man } 

CONSTRUCT { ?q1 :hasUncle ?q2 } 
WHERE {
  ?q2 :hasSibling ?parent . 
  ?q2 a :Man . 
  ?q1 :hasParent ?parent 
} 

CONSTRUCT { ?c a :PreferredCustomer } 
WHERE {
  ?c :totalBusiness ?tb . 
  FILTER(?tb > 5000) 
}
```


## Protocol
SPARQL is not only a query language, but also a protocol
- so a query engine can be a web service 

SPARQL endpoints
- received SPARQL queries and send a response - web services
- http://dbpedia.org/sparql


## Implementations
- Jena [http://jena.apache.org/] 
- Sesame [http://www.openrdf.org/]
- Many others: http://en.wikipedia.org/wiki/SPARQL#SPARQL_implementations


## Sources
- [Semantic Web for the Working Ontologist (book)](Semantic_Web_for_the_Working_Ontologist_(book))
- [XML and Web Technologies (UFRT)](XML_and_Web_Technologies_(UFRT))
- http://en.wikipedia.org/wiki/SPARQL

[Category:Semantic Web](Category_Semantic_Web)
[Category:Query Languages](Category_Query_Languages)