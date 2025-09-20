---
layout: default
permalink: /index.php/Hadoop_Pseudo_Distributed_Mode
tags:
- hadoop
- mapreduce
title: Hadoop Pseudo Distributed Mode
---
## Hadoop Pseudo Distributed Mode
[Hadoop](Hadoop) cluster can be emulated with "pseudo-distributed mode"
- all Hadoop demons run, and applications feel like tHey are being executed on a real cluster 
- good for testing [Hadoop MapReduce](Hadoop_MapReduce) jobs before running them on a fully distributed cluster


## Setting Up Locally
### Preparation
- install Hadoop from binaries, put e.g. to <code>~/soft/hadoop-2.6.0/</code>
- point <code>HADOOP_CONF_DIR</code> to some directory with config, e.g. <code>~/conf/hadoop-local</code>

You need to export the following env variables:

 #|  /bin/bash |  | export HADOOP_HOME=~/soft/hadoop-2.6.0
 export HADOOP_BIN=$HADOOP_HOME/bin
 
 export HADOOP_CONF_DIR=~/conf/hadoop-cluster
 export YARN_CONF_DIR=$HADOOP_CONF_DIR
 
 export PATH=$HADOOP_BIN:$HADOOP_HOME/sbin:$PATH


Also, if you don't have a java on your PATH, you need to create <code>hadoop-env.sh</code> in <code>HADOOP_CONF_DIR</code> and add (replace)

 export JAVA_HOME=/home/user/soft/jdk1.8.0_60/
 export HADOOP_CONF_DIR=${HADOOP_CONF_DIR:-"/etc/hadoop"}


### Properties

Hadoop in "Pseudo-distributed mode" should have properties similar to these:

 cat core-site.xml
 <?xml version="1.0"?>
 <configuration>
   <property>
     <name>fs.defaultFS</name>
     <value>hdfs://localhost/</value>
   </property>
   <property>
     <name>hadoop.tmp.dir</name>
     <value>/home/agrigorev/tmp/hadoop/</value>
   </property>
 </configuration>

 cat hdfs-site.xml 
 <?xml version="1.0"?>
 <configuration>
   <property>
     <name>dfs.replication</name>
     <value>1</value>
   </property>
 </configuration>

 cat mapred-site.xml 
 <?xml version="1.0"?>
 <configuration>
   <property>
     <name>mapreduce.framework.name</name>
     <value>yarn</value>
   </property>
 </configuration>

 cat yarn-site.xml 
 <?xml version="1.0"?>
 <configuration>
   <property>
     <name>yarn.resourcemanager.hostname</name>
     <value>localhost</value>
   </property>
   <property>
     <name>yarn.nodemanager.aux-services</name>
     <value>mapreduce_shuffle</value>
   </property>
 </configuration>


### File System
- Once the configuration is set, format the filesystem
- <code>hdfs namenode -format</code>
- if <code>hadoop.tmp.dir</code> is not specified, it'll use <code>/tmp/hadoop-${user.name}</code>, which is cleaned after each reboot 


### Setting SSH Access
- Application master and workers on the cluster communicate via ssh 
- it's the same for pseudodistributed mode - except that the master and all the workers are located on the same machine
- but they still need to use ssh for that 
- so make sure you can do <code>ssh localhost</code>
- if not - check if ssh service and <code>ssh-agent</code> are running 


### Starting Daemons
To start, use

 start-dfs.sh
 start-yarn.sh
 mr-jobhistory-daemon.sh start historyserver


make sure namenode started:

 telnet localhost 8020


If namenode doesn't start in local mode, do [http://stackoverflow.com/questions/8076439/namenode-not-getting-started]: 
- delete all contents from the hadoop temporary folder: <code>rm -Rf tmp_dir</code>
- format the namenode: <code>hadoop namenode -format</code>
- start the namenode again: <code>start-dfs.sh</code>

Starting datanodes
- <code>hadoop-daemon.sh start datanode</code>
- to check if it works:

 hadoop fs -put somefile /home/username/
 hadoop fs -ls /home/username/ 


Troubleshooting:
- if datanode doesn't start [http://stackoverflow.com/questions/16725804/]
- if yarn resourcemanager doesn't start 
  - "Queue configuration missing child queue names for root" [http://stackoverflow.com/questions/28357130/unable-to-start-resourcemanager-capacity-scheduler-xml-not-found-hadoop-2-6-0]
  - copy [capacity-scheduler.xml](http://svn.apache.org/viewvc/hadoop/common/trunk/hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-tests/src/test/resources/capacity-scheduler.xml?view=co&revision=1495684&content-type=text%2Fplain) to <code>HADOOP_CONF_DIR</code>

### Jobs Monitoring

 yarn application -list
 yarn application -kill application_1445857836386_0002



## Links
- [note on Evernote](http://www.evernote.com/shard/s344/sh/21cdb658-ed50-40e7-809c-4a6418d3c10b/1912d438d4abb05617d31caa7609ffdd)

## Sources
- [Hadoop: The Definitive Guide (book)](Hadoop__The_Definitive_Guide_(book))
