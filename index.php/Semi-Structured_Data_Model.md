---
layout: default
permalink: /index.php/Semi-Structured_Data_Model
tags:
- data-models
- xml
title: Semi-Structured Data Model
---
## Semi-Structured [Data Model](Data_Model)
This is a [Data Model](Data_Model) that is based on [Graphs](Graphs) 
- for representing both regular and irregular data


Main Ideas:
- Data is Self-Describing
- Flexible Data Typing
- Serialized Forms


### Data is Self-Describing
The content comes with it's own description
- (In contract to [Relational Data Model](Relational_Data_Model) where the schema and the data are stored separately)

Starting point: 
- associations list: a collection of key-value pairs

For example, a record:
- <code>name : Alan, </code>
- <code>tel : 32190, </code>
- <code>email : alan@aol.ru</code>

But values themselves can be collections
- <code>name : </code>
  - <code>first : Alan,</code>
  - <code>last : Black </code>
- <code>tel : 32190, </code>
- <code>tel : 32191,</code>
- <code>email : alan@aol.ru</code>


And some labels may repeat


Graphical representation
- can graphically represent as [Tree](Tree)s
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/ufrt/xml/semi-structured-ex1.png" alt="Image">
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/ufrt/xml/semi-structured-ex2.png" alt="Image">
- the [XML](XML) Data Model adopts this representation


### Flexible Data Typing
- there can be no typing at all
- but data may be typed


### There's a serialized form
- The serialized representation of a such graph 
- [XML](XML)
- JSON 
- etc


## Links
- http://en.wikipedia.org/wiki/Semi-structured_data
- http://www.dcs.bbk.ac.uk/~ptw/teaching/ssd/notes.html

## Sources
- [XML and Web Technologies (UFRT)](XML_and_Web_Technologies_(UFRT))
