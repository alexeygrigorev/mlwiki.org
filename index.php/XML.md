---
title: XML
layout: default
permalink: /index.php/XML
---

# XML

## XML
XML is a [Semi-Structured Data Model](Semi-Structured_Data_Model) for many applications

XML 
- it is a superset of HTML
- XML is a generic data format
- for machine-to-machine communication and data exchange 
- especially widely used for [Data Integration](Data_Integration)
- there are ways to impose some constraints via schema: [DTD](DTD), [XML Schema](XML_Schema)
- there are many tools


## Representations
### [Tree](Tree) Representation
In XML Trees,
- values are always at the leaf level 
- all other nodes contain information about these nodes 

Examples:
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/ufrt/xml/semi-structured-ex1.png" alt="Image">
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/ufrt/xml/semi-structured-ex2.png" alt="Image">


Object-oriented model of these trees:
- DOM  or [Document Object Model](Document_Object_Model)


### Serialized Form
The following are the serialized forms of these trees:
```xml
<r>
  <name>Alan</name>
  <tel>32190</tel>
  <email>alan@aol.ru</email>
</r>
```

```xml
<r>
  <name>
    <first>Alan</first>
    <last>Black</last>
  </name>
  <tel>32190</tel>
  <email>alan@aol.ru</email>
</r>
```

So this the serialized form is
- it's a textual, linear representation of the tree


=== Examples === 
```text only
<document />
```

```xml
<document> Hello World|   </document>
``` | |```xml
<document>
  <salutation> Hello World|   </salutation> |</document> |
```

```xml
<?xml version="1.0" encoding="utf-8" ?>
<document>
  <salutation color="blue"> Hello World|   </salutation> |</document> |
```

<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/ufrt/xml/xml-trees-ex.png" alt="Image">


Bigger Example:

```xml
<solar_system>
  <star>
    <name>Sun</name>
    <spectral_type>G2</spectral_type>
    <age unit="billions years">5</age>
  </star>
  <planet type="telluric">
    <name>Earth</name>
    <distance unit="km">149600000</distance>
    <mass unit="kg">5.98e24</mass>
    <diameter unit="km">12756</diameter>
    <satellite number="1"/>
  </planet>
  <planet ring="yes" type="gaseous">
    <name>Saturn</name>
    <distance unit="UA">5.2</distance>
    <mass unit="Earth mass">95</mass>
    <diameter unit="Earth diameter">9.4</diameter>
    <satellite number="18"/>
  </planet>
  <planet ring="yes" type="gaseous">
    <name>Uranus</name>
    <distance unit="UA">19.2</distance>
    <mass unit="Earth mass">14.5</mass>
    <diameter unit="Earth diameter">4</diameter>
    <satellite number="15"/>
  </planet>
</solar_system>
```

<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/ufrt/xml/xml-solar-system.png" alt="Image">
- note that digits under nodes signify the positions 
- ''positions'' is a way of identifying nodes 
- to denote the position of the root we use $\epsilon$



## Working with XML
### Parsing
For applications 
- typically an application parses a serialized form and produces a tree 
- it works with it: accesses parts of the document, reorganizes it, etc
- after finishing, it serializes it back to XML 

<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/ufrt/xml/xml-apps.png" alt="Image">


Parsers 
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/ufrt/xml/xml-apps-2.png" alt="Image">
- a parser takes a serialized form an produces a tree form (for example, [DOM](DOM))
- validation
  - first of all it checks if the document is well-formed
  - using schemas, the parser checks if the document is valid


### Schemas
Schemas are used to
- specify constraints for XML documents: order of elements, structure, data types
- augment documents: default values, white space processing, etc
- give some semantics to the documents you want to design
- to reuse and document your decisions 
- designing contracts for web services 

There are 3 ways of doing it:
- [DTD](DTD) - based
- [XML Schema](XML_Schema)
- Relax NG

Schemas are build on top of [Tree Automata](Tree_Automata) and [Regular Expressions](Regular_Expressions) theory
- Validation of a document = a run of a tree automaton


### Attributes vs Elements
Consider the following XML documents :
```xml
<university>
  <teacher subject="math" students="180">M. Durant</teacher>
  <teacher subject="CS" students="130">M. Smith</teacher>
  <teacher subject="CS" students="150">Mme. Martin</teacher>
</university>
```

```xml
<university>
  <teacher>
    <name>M. Durant</name>
    <subject>Math</subject>
    <students>180</students>
  </teacher>
  <teacher>
    <name>M. Smith</name>
    <subject>CS</subject>
    <students>130</students>
  </teacher>
  <teacher>
    <name>Mme. Martin</name>
    <subject>Math</subject>
    <students>150</students>
  </teacher>
</university>
```

Which representation is better? 
- it depends 
- attributes should rather be used for metadata (like units of measure, etc)
- also attributes must be used only for simple types - not for complex values|   | |```text only
<note date="10/01/2008" />
```

Better:
```xml
<note>
  <date>
    <day>10</day>
    <month>01</month>
    <year>2008</year>
  </date>
</note>
```


### Namespaces
Suppose we have two tags with the same name, but different meaning

For example, consider a tag <code><title></code>
- it can be an HTML title 
- a description of a book
- the title of a person

How to avoid naming conflicts? 
- use namespaces: add prefixes to the names 
- this way it's possible to give unique names 
- each namespace prefix is uniquely identified with some URI

 |  |
```xml
<h:table>
  <h:tr>
    <h:td>Apples</h:td>
    <h:td>Bananas</h:td>
  </h:tr>
</h:table>
```

 |  |
```xml
<t:table>
  <t:name>African Coffee</t:name>
  <t:width>80</t:width>
  <t:lenght>120</t:lenght>
</t:table>
```


```xml
<root>
  <h:table xmlns:h="http://www.w3.org/TR/html4/">
    <h:tr>
      <h:td>Apples</h:td>
      <h:td>Bananas</h:td>
    </h:tr>
  </h:table>
  <t:table xmlns:t="http://www.foo.fr/furniture">
    <t:name>African Coffee</t:name>
    <t:width>80</t:width>
    <t:lenght>120</t:lenght>
  </t:table>
</root>
```
- Note that in this case <code>h</code> is defined in the element prefixed with <code>h:</code> it is possible


Default namespace
- for some element we can define a default namespace
- so we don't have to prefix anything down the tree: the default namespace is assumed
- another element down the tree can redefine the default namespace for all its children


```xml
<chapter xmlns="http://www.mydescription.com">
  <paragraph>
  ...
  </paragraph>
</chapter>
```

```xml
<chapter xmlns="http://www.mydescription.com/">
  <paragraph xmlns="http://www.foo.fr/">
  ...
  </paragraph>
</chapter>
```


Several namespaces
- it's also possible to attach several namespaces to one element

```xml
<root xmlns:h="http://www.w3.org/TR/html4/" xmlns:t="http://www.foo.fr/furniture">
  <h:table>
    <h:tr>
      <h:td>Apples</h:td>
      <h:td>Bananas</h:td>
    </h:tr>
  </h:table>
  <t:table>
    <t:name>African Coffee</t:name>
    <t:width>80</t:width>
    <t:lenght>120</t:lenght>
  </t:table>
</root>
```


## Sources
- [XML and Web Technologies (UFRT)](XML_and_Web_Technologies_(UFRT))

[Category:XML](Category_XML)