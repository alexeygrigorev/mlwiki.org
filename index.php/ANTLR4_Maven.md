---
title: ANTLR4 Maven
layout: default
permalink: /index.php/ANTLR4_Maven
---

# ANTLR4 Maven


== pom.xml == 

```genshi
<dependencies>
  <dependency>
    <groupId>org.antlr</groupId>
    <artifactId>antlr4</artifactId>
    <version>4.1</version>
  </dependency>
</dependencies>  

<build>
  <plugins>
    <plugin>
      <groupId>org.antlr</groupId>
      <artifactId>antlr4-maven-plugin</artifactId>
      <version>4.1</version>
      <configuration>
        <visitor>true</visitor>
        <sourceDirectory>${basedir}/src/main/resources/</sourceDirectory>
      </configuration>
      <executions>
        <execution>
          <goals>
            <goal>antlr4</goal>
          </goals>
        </execution>
      </executions>
    </plugin>

    <plugin>
      <groupId>org.codehaus.mojo</groupId>
      <artifactId>build-helper-maven-plugin</artifactId>
      <version>1.8</version>
      <executions>
        <execution>
          <id>add-source</id>
          <phase>generate-sources</phase>
          <goals>
            <goal>add-source</goal>
          </goals>
          <configuration>
            <sources>
              <source>target/generated-sources/antlr4</source>
            </sources>
          </configuration>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
<pluginManagement>
  <plugins>
    <plugin>
      <groupId>org.eclipse.m2e</groupId>
      <artifactId>lifecycle-mapping</artifactId>
      <version>1.0.0</version>
      <configuration>
        <lifecycleMappingMetadata>
          <pluginExecutions>
            <pluginExecution>
              <pluginExecutionFilter>
                <groupId>org.antlr</groupId>
                <artifactId>antlr4-maven-plugin</artifactId>
                <versionRange>[4.0,)</versionRange>
                <goals>
                  <goal>antlr4</goal>
                </goals>
              </pluginExecutionFilter>
              <action>
                <ignore></ignore>
              </action>
            </pluginExecution>
          </pluginExecutions>
        </lifecycleMappingMetadata>
      </configuration>
    </plugin>
  </plugins>
</pluginManagement>
```


## Ссылки
- https://gist.github.com/sharwell/4979017

- https://github.com/miho/antlr-4-playground/blob/master/experiments/expr/src/eu/mihosoft/antlr/experiments
- https://github.com/miho/antlr-4-playground/blob/master/experiments/expr/src/eu/mihosoft/antlr/experiments/Main.java

- https://github.com/antlr/grammars-v4

- http://stackoverflow.com/questions/6487593/what-does-fragment-means-in-antlr
- http://stackoverflow.com/questions/17720608/curbing-antlr4-greediness-building-antlr4-grammar-for-existing-dsl


[Category:Java](Category_Java) [Category:Maven](Category_Maven) [Category:Programming](Category_Programming)