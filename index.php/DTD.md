---
title: DTD
layout: default
permalink: /index.php/DTD
---

# DTD

## DTD
DTD, or Document Type Definition, is a language for defining schemas for [XML](XML)
- to validate the content of XML documents
- it uses [Regular Expressions](Regular_Expressions) for validation
- it is an integral part of XML specification


### Regular Expression
The following defines the valid content of <code>table</code> element in XTML
- <code>caption? ( col* |  colgroup* ) thead? tfoot? ( tbody+ | tr+ )</code> |- with this expression, the following is a minimal possible word that matches it
- <code>tbody tr</code>


## Schema Definition
### Declaration
To declare schema
- add <code><|  DOCTYPE {name} SYSTEM "http://{uri}.dtd"></code> to the beginning of an XML document | |<?xml version="1.1"?> 
<|  DOCTYPE collection SYSTEM "http://foo.fr/example.dtd"> |<collection>  |... 
</collection> 


### |  ELEMENT |The declaration for elements (tags or titles in our XML documents) is the following  |- <|  ELEMENT {name} {content_mode}> where |- name - a name of some tag from the document |- content_mode <code>EMPTY</code>, <code>ANY</code> or 
- <code>#PCDATA</code> "parsed character data", only one text element is allowed in the content
- some regular expression over the tag names


Example:
- <code><|  ELEMENT table (caption?,(col*|colgroup*),thead?,tfoot?,(tbody+|tr+)) ></code> |- colon (<code>,</code>) is used to express concatenation, pipe (<code>|</code>) - to express union |


### <code>|  ATTLIST</code> |Also we need to declare attributes for elements |- syntax: <code><|  ATTLIST {tag} {attribute} {type} {#REQUIRED|#IMPLIED}></code>  | |
```f#
<|  ATTLIST input maxlength CDATA #REQUIRED  |                tabindex CDATA #IMPLIED> |
```
- <code>#IMPLIED</code> = optional, <code>#REQUIRED</code>  = not optional
- CDATA: any value

```f#
<|  ATTLIST p align (left|center|right|justify) #IMPLIED>
``` |- here we enumerate possible values of attributes |- for optional attributes can also put the default value 

```f#
<|  ATTLIST form method (get|post) "get">
``` |- the default value of this attribute is <code>get</code> |

## Example
### Solar System
Consider the following XML:

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


DTD-schema for this examples is:
```carbon
<|  ELEMENT solar_system (star,planet+)> | |<|  ELEMENT star (name,spectral_type,age)> | |<|  ELEMENT name (#PCDATA)> |<| ELEMENT spectral_type (#PCDATA)> |<| ELEMENT age (#PCDATA)> |<| ATTLIST age unit CDATA #REQUIRED> | |<|  ELEMENT planet (name,distance,mass,diameter,satellite?)> |<| ATTLIST planet ring CDATA #IMPLIED> |<| ATTLIST planet type CDATA #REQUIRED> | |<|  ELEMENT distance (#PCDATA)> |<| ATTLIST distance unit CDATA #REQUIRED> | |<|  ELEMENT mass (#PCDATA)> |<| ATTLIST mass unit CDATA #REQUIRED> | |<|  ELEMENT diameter (#PCDATA)> |<| ATTLIST diameter unit CDATA #REQUIRED> | |<|  ELEMENT satellite EMPTY> |<| ATTLIST satellite number CDATA #REQUIRED> |
``` |
Note the limitation:
- we cannot have two different <code>name</code> elements
- i.e. can have only one definition per one name


For example, the following is not possible to validate with DTD

```xml
<planet>
  <name language="English">Earth</name>
</planet>

<star>
  <name>Sum</name>
</star>
```


## Limitations
- Specification of attribute values is too limited 
- Element and attribute declarations are context insensitive 
- Character data cannot be combined with the regular expression content model 
- It does not itself use an XML syntax 
- No support for namespaces 


### [XML Schema](XML_Schema)
- More expressive 
- XML itself
- support namespaces
- many other things


## Links
- http://en.wikipedia.org/wiki/Document_type_definition

## See Also
- [Tree Automata](Tree_Automata)
- [XML](XML)
- [XML Schema](XML_Schema)

## Sources
- [XML and Web Technologies (UFRT)](XML_and_Web_Technologies_(UFRT))

[Category:XML](Category_XML)