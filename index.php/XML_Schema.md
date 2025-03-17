---
title: "XML Schema"
layout: default
permalink: /index.php/XML_Schema
---

# XML Schema

## XML Schema
This is a better alternative to [DTD](DTD) for validating [XML](XML) documents 
- it is XML itself
- it can express complex types
- it supports namespaces



## Types
### Predefined Primitives
There are a lot of predefined primitives


|   Type  |   Example of Value  |  <code>string</code>  |  <code>any Unicode string </code> ||  <code>boolean</code>  |  <code>true, false, 1, 0 </code> ||  <code>decimal</code>  |  <code>3.1415 </code> ||  <code>float</code>  |  <code>6.02214199E23 </code> ||  <code>double</code>  |  <code>42E970 </code> ||  <code>dateTime</code>  |  <code>2004-09-26T16:29:00-05:00 </code> ||  <code>time</code>  |  <code>16:29:00-05:00 </code> ||  <code>date</code>  |  <code>2004-09-26 </code> ||  <code>hexBinary</code>  |  <code>48656c6c6f0a </code> ||  <code>base64Binary</code>  |  <code>SGVsbG8K </code> ||  <code>anyURI</code>  |  <code>http://0agr.ru/wiki/ </code> ||  <code>QName</code>  |  <code>rcp:recipe, recipe </code> |


```xml
<simpleType name="integerList"> 
  <list itemType="integer"/> 
</simpleType>
```


### Simple Types: Constrains
We also can add additional constraints with so-called facets

- <code>length </code>
- <code>minLength </code>
- <code>maxLength </code>
- <code>pattern </code>
- <code>enumeration </code>
- <code>whiteSpace</code>

|  |
- <code>maxInclusive </code>
- <code>maxExclusive </code>
- <code>minInclusive </code>
- <code>minExclusive </code>
- <code>totalDigits </code>
- <code>fractionDigits </code>



```xml
<simpleType name="score_from_0_to_100"> 
  <restrictionbase="integer"> 
    <minInclusivevalue="0"/> 
    <maxInclusivevalue="100"/> 
  </restriction> 
</simpleType> 

<simpleType name="percentage"> 
  <restriction base="string"> 
    <patternvalue="([0-9]| [1-9][0-9]|100)%"/>  |  </restriction> 
</simpleType>
```


So as you see it's also possible to use [Regular Expressions](Regular_Expressions)
- to define constraints, etc


### Derived Simple Types
We can derive a simple type from two simple types:

```xml
<simpleType name="boolean_or_decimal"> 
  <union> 
    <simpleType> 
  <restriction base="boolean"/> 
  </simpleType> 
  <simpleType> 
    <restriction base="decimal"/> 
  </simpleType> 
  </union> 
</simpleType>
```

There are some built-in derived types
- normalizedString 
- unsignedLong 
- ... 


### Complex Types
Elements:
- reference to already defined element: <code><element ref="name" /> </code>


We can use [Regular Expressions](Regular_Expressions) for restricting sequences of tags we can have:

|  Concatenation   |  <code><sequence> ...</sequence> </code> ||  Union     |  <code><choice> ...</choice> </code> ||  All    |  <code><all> ...</all></code> ||  Element wildcard  |  <code><any /> </code> ||  ?  |  minOccurs="0" maxOccurs="1" ||  +  |  minOccurs="1" maxOccurs="unbounded" ||  *  |  minOccurs="0" maxOccurs="unbounded" |

Attributes
- also can refer to already defined attributes
  - <code><attribute ref="r:class"/></code>

### Extensions
Suppose we want to have an integer with a parameter
- we can extend from integer and add an attribute

```xml
<complexType name="category"> 
  <simpleContent> 
    <extension base="integer"> 
      <attribute ref="r:class"/>
    </extension> 
  </simpleContent> 
</complexType>
```


Same way we can extend one more time
- and add another attribute

```xml
<complexType name="extended_category"> 
  <simpleContent> 
    <extension base="n:category"> 
      <attribute ref="r:kind"/> 
    </extension> 
  </simpleContent> 
</complexType>
```


Also we can restrict some class
- adding a restriction is a little bit different from extension 

```carbon
<complexType name="restricted_category"> 
  <simpleContent> 
    <restriction base="n:category"> 
      <totalDigits value="3"/> 
      <attribute ref="r:class" use="required"/> 
    </restriction> 
  </simpleContent> 
</complexType>
```


### Local vs Global Declaration
Usually we define an element and reference it
- this is called ''global declaration''

However it's possible to describe an element with an anonymous type
```carbon
<element name="card"> 
  <complexType> 
    <sequence> 
      <element name="name" type="string"/> 
      ... 
    </sequence> 
  </complexType> 
</element>
```

Note that it can cause some problems
- locally defined elements must belong to the namespace - but they don't
- they are ''unqualified'' by default (no namespace is associated)
- such elements belong to the element they're associated with
- so we have to set <code>elementFormDefault="qualified"</code>
- some links: [and [http://www.w3.org/TR/xmlschema-0/#NS](http://stackoverflow.com/questions/1463138/what-does-elementformdefault-do-for-xml-when-is-it-used])


## Examples
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


Here's the XML schema for it

```scdoc
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified" 
  targetNamespace="http://foo.fr/solar_system" xmlns:s="http://foo.fr/solar_system">

  <xs:element name="solar_system">
    <xs:complexType>
      <xs:sequence>
        <xs:element ref="s:star"/>
        <xs:element maxOccurs="unbounded" ref="s:planet"/>
      </xs:sequence>
    </xs:complexType>
  </xs:element>

  <xs:element name="star">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="name" type="xs:NCName"/>
        <xs:element name="spectral_type" type="xs:NCName"/>
        <xs:element name="age" type="s:measure_type"/>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
  <xs:element name="planet">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="name" type="xs:NCName"/>
        <xs:element name="distance" type="s:measure_type"/>
        <xs:element name="mass" type="s:measure_type"/>
        <xs:element name="diameter" type="s:measure_type"/>
        <xs:element ref="s:satellite"/>
      </xs:sequence>
      <xs:attribute name="ring" type="xs:NCName"/>
      <xs:attribute name="type" use="required" type="xs:NCName"/>
    </xs:complexType>
  </xs:element>

  <xs:complexType name="measure_type">
    <xs:simpleContent>
      <xs:extension base="xs:float">
        <xs:attribute name="unit" use="required" type="xs:NCName"/>
      </xs:extension>
    </xs:simpleContent>
  </xs:complexType>
  <xs:element name="satellite">
    <xs:complexType>
      <xs:attribute name="number" use="required" type="xs:integer"/>
    </xs:complexType>
  </xs:element>
  
</xs:schema>
```


Note the usage of <code>xs:NCName</code>
- it is like string but doesn't allow certain characters 
- see more here: [http://stackoverflow.com/questions/1631396/what-is-an-xsncname-type-and-when-should-it-be-used]


## See Also
- [XML](XML)
- [DTD](DTD)
- [Tree Automata](Tree_Automata)


## Sources
- [XML and Web Technologies (UFRT)](XML_and_Web_Technologies_(UFRT))

[Category:XML](Category_XML)