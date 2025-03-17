---
title: "Java interview questions"
layout: default
permalink: /index.php/Java_interview_questions
---

# Java interview questions

## Java basics
- Meaning of keywords: static, final, transient
- Contract between equals() and hashCode()
- Rules to create equals method (stability, transitivity, reflectivity etc)
- Access modifiers in Java
- Explain strictfp, volatile, transient?
- Purpose, types and creation of nested classes
- What does it mean that an object or a class is mutable or immutable?
- How to make class immutable?
- Besides “string” do you know any other immutable classes?
- How can we replace multi-inheritance pattern in Java
- Can interface inherit from different interface
- Regular vs. static initialization blocks

Also
- Length in bytes for primitive types
- '''this''' and '''super''' keywords
- What different between StringBuffer and StringBuilder? 
- Difference between overriding and overloading


## Exceptions
- Checked vs. unchecked exceptions. Why would one use former or later?
- Difference in handling of Error and Exception
- Could we have only try and finally withouth catch
- Cases when the finally block isn't executed
- What is exception handling mechanism
- Java Exceptions API
- How to avoid catch block?


## Collections
- General collection interfaces (Collection, Set, Map, List, Queue, SortedSet, SortedMap)
- Interfaces extending Collection. Is Map part of Collection interface?
- Difference between ArrayList and LinkedList
- Difference between Stack and Queue
- TreeSet vs LinkedHashSet
- Internal structure of HashMap/Hashtable
- Requirements for implementation of hashCode to achieve best performance
- Definition and ways of resolving collisions in hash tables
- Differences between Hashtable and ConcurrentHashMap
- Special versions of collections. EnumSet, EnumMap, WeakHaskMap, IdentityHashMap.
- Implementation details of about ConcurrentHashMap. Synchronization.
- Iterator and modification of a List. ConcurentModificationException. Collections with safe iterators (CopyOnWriteArrayList/CopyOnWriteArraySet)


## Java 5+ Specifics
- What is a parameterized or generic type?
- Can we use parameterized types in exception handling?
- Liskov substitution principle
- What is a wildcard parameterized type?
- What is Autoboxing and what are its advantages/pitfalls?
- Problems Enum type solves (comparing to "public static int" enum pattern)
- Can we add something to List<?> ?
- What are Annotations and which predefined by the language specification does one know (@Deprecated, @Override, @SuppressWarnings)



## Multithreading
- Thread vs Runnable, run() vs start()
- Synchronization of java blocks and methods
- Explain usage of the couple wait()/notify()
- Difference between sleep and wait
- Atomic operations
- What does it mean Volatile keyword?
- java.util.concurrent.*, what utils do you know?
- Thread local, what for are they needed?
- Does child thread see the value of parent thread local?
- Deadlock definition plus example
- Livelock definition plus example
- Starvation definition plus example
- Race condition definition plus example
- Garbage definition plus example
- Execution order
- Atomicity of long and double assignment operations
- Lock-free operations, how to create lock-free implementation of field reassignment


How to interrupt a thread
- http://javatalks.ru/topics/36538
- http://stackoverflow.com/questions/2020992/is-thread-interrupt-evil


## Java NIO
- What is NIO
- What is Channel
- What is Buffer
- What is Charset
- What is Selector
- How to lock file?
- what is NIO2 ?


## Memory & GC
- Memory model in JVM
- How does virtual space divided in Java?
- What difference between float and BigDecimal. How they store the data?
- Java object references
- What is deep copy of a Java object?
- Disadvantages of setting heap size too high
- What are utilities for JVM monitoring? What is Jconsole?
- How to force GC be executed?
- Garbage collection principles
- What are memory leaks?
- Are memory leaks a problem in Java?
- What is variable shadowing
- How would you monitor JVM
- How would you monitor how GC behaves during program execution
- Name few GC implementations (Serial, Parallel, ParallelOld, ConcarentMarkAndSweep, G1) describe major  differences



## Unit testing
- Libraries that help to writing unit tests
- EasyMock and Mockito usage
- Junit. What is this tool for?
- What are features of Junit? Please explain Junit Theories


## Some Links
- http://www.itshared.org/2015/10/java-interview-questions.html
- [115 Java Interview Questions and Answers – The ULTIMATE List](http://www.evernote.com/shard/s344/sh/0a9befd7-507d-4a9b-be08-fb5e39876219/2718ba3054cec6ef43edba0b19606277)

[Category:Interviews](Category_Interviews)
[Category:Java](Category_Java)