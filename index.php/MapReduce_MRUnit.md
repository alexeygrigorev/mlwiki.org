---
title: MapReduce/MRUnit
layout: default
permalink: /index.php/MapReduce_MRUnit
---

# MapReduce/MRUnit

## MapReduce MRUnit
MR Unit is a library for unit-testing [Hadoop MapReduce](Hadoop_MapReduce) jobs
- https://mrunit.apache.org/


## Example
### Maven Dependency
For Hadoop2: 

 <dependency>
   <groupId>org.apache.mrunit</groupId>
   <artifactId>mrunit</artifactId>
   <version>1.1.0</version>
   <classifier>hadoop2</classifier> 
   <scope>test</scope>
 </dependency>

Use classifier <code>hadoop1</code> for Hadoop1 

This version works well with Hadoop <code>2.6.0-cdh5.4.7</code>


### Mapper Test
Steps:
- You wrap your mapper in <code>MapDriver.newMapDriver</code>
- Feed some input data
- Provide expected output 
- Run

 mapper = MapDriver.newMapDriver(new YourMapper());
 
 // input
 mapper.addInput(key1, value1);
 mapper.addInput(key2, value2);
 mapper.addInput(key3, value3);
 
 // expected output
 mapper.addOutput(outKey1, outValue1);
 mapper.addOutput(outKey2, outValue2);
 mapper.addOutput(outKey3, outValue3);
 
 mapper.runTest();

### Reducer Test
Same as for Mapper:
- Wrap your reducer in <code>ReduceDriver.newReduceDriver</code>
- Provide input and expected output 
- Run

 reducer = ReduceDriver.newReduceDriver(new YourReducer());
 
 reducer.addInput(key1, value1);
 reducer.addInput(key2, value2);
 
 reducer.addOutput(outKey1, outValue1);
 reducer.addOutput(outKey2, outValue2);
 
 reducer.runTest();


### Configuration
Changing some configuration parameters is easy
- use <code>driver.getConfiguration()</code>

E.g.:

 reducer.getConfiguration().setInt("app.name.param1", 4);


### Distributed Cache
Faking a file from "Distribute Cache":

 URL resource = this.getClass().getResource("test-resource-file.txt");
 Path link = Paths.get("symlink");
 Path target = Paths.get(resource.toURI());
 if (link.toFile().exists()) {
     link.toFile().delete();
 }
 
 Files.createSymbolicLink(link, target);
 
 try {
     // test goes here
 } finally {
     link.toFile().delete();
 }



[Category:Hadoop](Category_Hadoop)
[Category:Java](Category_Java)
[Category:Snippets](Category_Snippets)