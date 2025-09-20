---
title: "Hadoop MapReduce"
layout: default
permalink: /index.php/Hadoop_MapReduce
---

# Hadoop MapReduce

## Hadoop MapReduce
This is a [Hadoop](Hadoop) data processing tool on top of [HDFS](HDFS)
- it's a batch query processing tool that goes over '''all''' available data
- best for off-line use
- it's a part of [Hadoop](Hadoop)


## [MapReduce](MapReduce) Jobs
### Jobs
''Job'' is a specification that should be run on the cluster by [Hadoop](Hadoop)/[YARN](YARN)
- it's a unit of work
- contains: paths to input data, the MapReduce program (Map and Reduce UDFs) and configuration
- a job can have several input paths, and one output path

Job packaging: 
- when we run the code on a cluster, we package it to a set of jar files 
- we need to tell the cluster which is our jar 
- done via <code>job.setJarByClass(MyJob.class)</code>, so Hadoop can figure out which jar to use
- job is submitted via <code>job.waitForCompletion(true)</code>


### Data Locality Principle
- programs don't pull data from storage 
- instead, programs (jobs and tasks) are sent as close to data as possible 


### Tasks
Each job consists of tasks:
- there are two types of tasks: '''map tasks''' and '''reduce tasks'''
- tasks are scheduled by [YARN](YARN) and run on different nodes 
- if a task fails, it's rescheduled on a different node

Map tasks:
- the input files are split into fixed-size pieces - ''input splits''
- then Hadoop creates a map task for each input split
- and then the task applies the map function to each record of that split
- map tasks write their results to local disks, not HDFS - their output is intermediate results and can be thrown away, when reducers are done 

Reducer tasks:
- we specify the number of reducers for the job
- reducers cannot use the data locality principle, because input of Reducers is the output from all the mappers
- output of reducer is typically stored on hdfs
- it's possible to have 0 reducers, then such a job is called "Map Only" and writes the output directly to HDFS 


Users can set mappers, reducers and combiners

 job.setMapperClass(MyMapper.class);
 job.setCombinerClass(MyCombiner.class);
 job.setReducerClass(MyReducer.class);

Map only tasks

 job.setMapperClass(MyMapper.class);
 job.setNumReduceTasks(0);



## MapReduce Job Execution
General flow:
- input files are split into input splits
- '''map phase''': master picks some idle workers and assigns them a map task
- mappers write their results to their disks
- '''reduce phase''': once they finish, reducers take the results and process

<img src="https://raw.github.com/alexeygrigorev/ulb-adb-project-couchbd/master/report/images/map-reduce2.png" alt="Image">


'''map phase'''
- each input split is assigned to a map worker
- it applies the [map function](MapReduce#Map_Function) to each record
- results are written to $R$ partitions, where $R$ is the number of reducers
- wait until '''all''' map tasks are completed


'''shuffle phase''' (sorting)
- the master assigns reduce task to workers
- the intermediate results are shuffled and assigned to reducers
- if there's a combiner function, it is applied to each partition
- each reduces pulls its partition from mappers' disks
- each record is assigned to only one reduces


<img src="https://habrastorage.org/files/29b/802/f87/29b802f87a734694b9e5fcf16fd016e9.png" alt="Image"> <!-- Image: map-to-reduce.png -->
'''reduce phase'''
- Reducers ask the Application Master where the mappers are located
- and then they start pulling files from mappers as soon as mappers complete
- now apply the [reduce function](MapReduce#Reduce_Function) to each group
- output is typically stored on [HDFS](HDFS)


Hadoop in one picture: 

<img src="https://raw.github.com/alexeygrigorev/ulb-adb-project-couchbd/master/report/images/hadoop.png" alt="Image">

(Figure source: Huy Vo, NYU Poly and [http://escience.washington.edu/get-help-now/what-hadoop])


### Shuffling Details
- Hadoop is often referred as "Big [Distributed Merge Sort](External_Merge_Sort)"
- Hadoop guarantees that the that the input to reducers is sorted by key 
- ''Shuffle'' is the process of sorting and transferring map output to the reducers
- The output of mappers is not just written to disk, Hadoop does some pre-sorting 

<img src="https://habrastorage.org/files/9f3/a16/024/9f3a16024acb42d98c8aeb320b370d1e.png" alt="Image"> <!-- Image: shuffling.png -->

For tuning MapReduce jobs, it may be useful to know how the shuffling is performed
- Each mapper has ~100 mb buffer (buffer size is configured in <code>mapreduce.task.io.sort.mb</code>)
- when it's 80% full (set in <code>mapreduce.map.sort.spill.percent</code>), a background thread starts to ''spill'' the content on disk (while the buffers are still being populated)
- it's written to disk in the [Round Robin](Round_Robin) fashion to <code>mapreduce.cluster.local.dir</code> directory into a job-specific subdirectory 
- before writing to disk, the output is subdivided into partitions, and within each partition records are sorted by key
- if there's a combiner function, it's applied 
- then all spills are merged 
- if there are multiple spills (at least 3, specified in <code>mapreduce.map.combine.minspills</code>), then combiner is run again
- by default the output of mapper is not compressed, but you can turn it on with <code>mapreduce.map.output.compress=true</code> and the compression library is set with <code>mapreduce.map.output.compress.codec</code>
- then each reducer can download its partition


Sorting at the Reducer side
- as soon as mappers complete, reducers start pulling the data from their local disks
- each reducer gets its own partitions and merge-sort them 
- also, reducer is fed data at the last merge phase to save one iteration of merge sort


### Runtime Scheduling Scheme
- see [YARN](YARN) for details how it's scheduled
- For job execution MapReduce component doesn't build any execution plan beforehand
- Result: no communication costs
- MR tasks are done without communication between tasks

### Failures and Fault-Tolerance
There are different types of failures:
- Task Failure (e.g. task JVM crushed). 
  - It a task attempt fails, it's rescheduled on a different node
  - If the attempt fails 4 times (configured in <code>mapreduce.map| reduce.maxattempts</code>), it's not rescheduled |- Application Master failure 
- Cluster Failure (not recoverable)


Fault tolerance is achieved naturally in this execution scheme
- detect failures and re-assigns tasks of failed nodes to others in the cluster
- also leads to (some) load balancing 


## Execution
### The Tool Interface
<code>Tool</code> is a helper class for executing Hadoop MR jobs 
- so you can implement the <code>Tool</code> interface and run it with the <code>ToolRunner</code> 
- it knows where to look for config files and already parses some parameter
- e.g. if you pass <code>-conf</code> parameter, it knows that it needs to load <code>Configuration</code> from there
- Usually you have something like YouJob extends Configured implements Tool {


### Unit Testing
[MapReduce/MRUnit](MapReduce_MRUnit)
- MRUnit is a library for testing MapReduce jobs
- uses a mock job runner, collect the output and compares it with the expected output



### Running Locally
- You can also run your files locally for testing, before submitting the job to a real cluster
- the default mode is local, and MR jobs are run with <code>LocalJobRunner</code>
- it runs on a single JVM and can be run from IDE 
- The local mode is the default one: <code>mapreduce.framework.name=local</code> by default 
- You can also have a local YARN cluster - see <code>MiniYARNCluster</code>


### Running on Cluster
Jobs must be packaged to jar files 
- easiest way: <code>mvn clean package </code>
- or <code>mvn clean package -DskipTests</code>

''client'' - the driver class that submits the job, usually it implements the <code>Tool</code> interface

Client classpath:
- job jar
- jar files in the <code>lib/</code> directory inside the jar
- classpath defined by <code>HADOOP_CLASSPATH</code>

Task classpath
- it runs on a separate JVM, not on the same as the client|   |- not controlled by <code>HADOOP_CLASSPATH</code> - it's only for the client |- the job jar and its <code>lib/</code> directory
- files in the distributed cache (submitted via <code>-libjars</code>)

Task classpath precedence 
- for client: <code>HADOOP_USER_CLASSPATH_FIRST=true</code>
- for configuration: <code>mapreduce.job.user.classpath.first=true</code>

Results: 
- <code>part-r-0001</code> (or <code>part-m-0001</code> if job is map only)
- you can merge the result 
- just merge - see snippets 
- order - see [MapReduce Patters](MapReduce_Patters)


### Problem Decomposition
- Problems rarely can be expressed with a single MapReduce job
- usually need a few of them 

Hadoop solution: <code>JobControl</code> class
- linear chain of jobs:

 JobClient.runJob(conf1);
 JobClient.runJob(conf2);

- the job control creates a graph of jobs to be run on the cluster 
- the jobs are submitted to the cluster specified in configuration 
- but the <code>JobClient</code> class is run on the client machine 


Other tools for running worflows
- [Apache Oozie](Oozie) - for running workflows 
- [Luigi](Luigi)



## Hadoop MapReduce Features
### Compression
Output of reducers (and mappers) can be compressed 

For example, to use [GZip](GZip) compression, use

 TextOutputFormat.setCompressOutput(job, true);
 TextOutputFormat.setOutputCompressorClass(job, GzipCodec.class);

Hadoop can recognize gzipped files automatically when reading


### Writables
Objects in Hadoop should implement the <code>Writable</code> interface
- by implementing it, you're telling Hadoop how the files should be de-serialized
- the Java default serialization mechanism is not effective to be used in Hadoop

<code>Writable</code> interface has two methods:
- <code>void write(DataOutput out)</code>
- <code>void readFields(DataInput in)</code>

Implementation is usually easy:

 @Override
 public void write(DataOutput out) throws IOException {
     Text.writeString(out, language);
     Text.writeString(out, token);
     out.writeLong(hash);
 }
 
 @Override
 public void readFields(DataInput in) throws IOException {
     language = Text.readString(in);
     token = Text.readString(in);
     hash = in.readLong();
 }

<code>WritableComparator</code> 
- is another interface to be used for keys 
- it's a <code>Writable</code> and <code>Comparable</code>
- so there's <code>int compareTo()</code> method


<code>RawComparator</code>
- We also can have a raw comparator - to compare directly on bytes without depersonalization 
- it's very good for speed because it avoids serialization/de-serialization
- the method to implement is <code>int compare(byte[] b1, int s1, int l1, byte[] b2, int s2, int l2)</code>
- <code>WritableComparator</code> already implements this method



### Counters
Counters is a good way to count things
- for example, to count how many records are processed 
- how mane records are processed with exceptions

Usage:

 try {
     process(record, context);
     context.getCounter(Counters.DOCUMENTS).increment(1);
 } catch (Exception ex) {
     LOGGER.error("Caught Exception", ex);
     context.getCounter(Counters.EXCEPTIONS).increment(1);
 }


### Secondary Sort
- Typically the output of mappers is sorted by key only - there's no specific order for values 
- Sometimes we need to make sure that the values are also sorted
- to do it, we create a custom <code>Writable</code> that is composed of both key and value 
- and use <code>NullWritable</code> to output the value 
- See [MapReduce/Secondary Sort](MapReduce_Secondary_Sort)


### Distributed Cache
Distributed cache is a service for copying files to task nodes 

<code>Tool</code> interface:
- If you implement the <code>Tool</code> interface, can specify files with the <code>-files</code> option
- e.g. <code>-files some/path/to/file.txt</code>
- and then you can read this file from the working directory just with <code>new File("file.txt")</code>
- use the <code>setup</code> method in mapper or reducer for this
- these files are first copied to HDFS, and then pulled to local machines before the task is executed

In Java API you'd use this: 

 Job job = Job.getInstance(getConf());
 job.addCacheFile(new URI(path.toUri() + "#symlink-name"));

- you can also specify a symlink name by appending <code>"#symlink-name"</code>
- then you can read the file with 

 FileUtils.openInputStream(new File("./symlink-name"));



## MapReduce vs RDBMS
[RDBMS](Relational_Databases) 
- Declarative query language
- Schemas
- [Indexing](Indexing_(databases)) 
- [Logical Query Plan Optimization](Logical_Query_Plan_Optimization) 
- [Caching](Caching)
- [View Materialization](View_Materialization) 
- [ACID](ACID) and transactions 

MapReduce
- High Scalability 
- Fault-tolerance


## Advantages
[MapReduce](MapReduce) is simple and expressive
- computing aggregation is easy
- flexible
  - no dependency on [Data Model](Data_Model) or schema
  - especially good for unstructured data
  - cannot do that in [Database](Database)s
- can write in any programming language
- fault-tolerance: detect failures and re-assigns tasks of failed nodes to others in the cluster
- high scalability
- even though not in the most efficient way
- cheap: runs on commodity hardware
- open source


## Disadvantages
### No Query Language
No high-level declarative language as SQL
- [MapReduce](MapReduce) is very low level - need to know programming languages 
- programs are expensive to write and to maintain
- programmers that can do that are expensive
- for [Data Warehousing](Data_Warehousing): [OLAP](OLAP) is not that good in MapReduce

Possible solutions: 
- [Pig](Pig), [Hive](Hive), [Tez](Tez), [Impala](Impala), [Spark](Spark), [Flink](Flink)


### Performance
Performance issues:
- no schema, no index, need to parse each input
  - may cause performance degradation
- not tuned for multidimensional queries
- possible solutions: [HBase](HBase), [Hive](Hive)
- because of fault-tolerance and scalability - it's not always optimized for I/O cost
  - all intermediate results are materialized (no [Pipelining](Pipelining))
  - triple replication
- low latency
  - big overhead for small queries (job start time + jvm start time)


Map and Reduce are Blocking
- a transition from Map phase to Reduce phase cannot be made while Map tasks are still running
  - reason for it is that relies on [External Merge Sort](External_Merge_Sort) for grouping intermediate results
  - [Pipelining](Pipelining) is not possible
- latency problems from this blocking processing nature
- causes performance degradation - bad for [on-line processing](OLAP)


Solutions for I/O optimization
- [HBase](HBase)
  - [Column-Oriented Database](Column-Oriented_Databases) that has index structures
  - data compression (easier for Column-Oriented Databases)
- Hadoop++ [https://infosys.uni-saarland.de/projects/hadoop.php]
  - HAIL (Hadoop Aggressive Indexing Library) as an enhancement for HDFS 
  - structured file format
  - 20x improvement in Hadoop performance
- [Spark](Spark) and [Flink](Flink) can do pipelining
- Incremental MapReduce (like in [CouchDB](CouchDB) [[http://eagain.net/articles/incremental-mapreduce/](http://stackoverflow.com/questions/11236676/why-is-mapreduce-in-couchdb-called-incremental]))


## Sources
- Lee et al, Parallel Data Processing with MapReduce: A Survey [http://www.cs.arizona.edu/~bkmoon/papers/sigmodrec11.pdf]
- Ordonez et al, Relational versus non-relational database systems for data warehousing [http://www2.cs.uh.edu/~ordonez/w-2010-DOLAP-relnonrel.pdf]
- Paper by Cloudera and Teradata, Awadallah and Graham, Hadoop and the Data Warehouse: When to Use Which. [http://www.teradata.com/white-papers/Hadoop-and-the-Data-Warehouse-When-to-Use-Which/]
- [Introduction to Data Science (coursera)](Introduction_to_Data_Science_(coursera))
- [Hadoop: The Definitive Guide (book)](Hadoop__The_Definitive_Guide_(book))

[Category:Hadoop](Category_Hadoop)
[Category:Distributed Systems](Category_Distributed_Systems)
[Category:MapReduce](Category_MapReduce)
[Category:Improve Images](Category_Improve_Images)