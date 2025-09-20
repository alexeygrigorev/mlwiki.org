---
layout: default
permalink: /index.php/Groovy_Java_in_Maven
tags:
- groovy
- java
- maven
title: Groovy Java in Maven
---
Смешанный проект с groovy и java используя maven и Groovy-Eclipse compiler

## Groovy-eclipse Compiler

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">

  <modelVersion>4.0.0</modelVersion>

  <groupId>com.alexeygrigorev.groovyjavamix</groupId>
  <artifactId>groovy-java-mix-project</artifactId>
  <version>1.0.0-SNAPSHOT</version>
  <name>Groovy and Java mixed project</name>
  <description>Groovy and Java mixed project</description>

  <properties>
    <javaVersion>1.6</javaVersion>
  </properties>

  <dependencies>
    <dependency>
      <groupId>org.codehaus.groovy</groupId>
      <artifactId>groovy-all</artifactId>
      <version>2.0.4</version>
    </dependency>
  
 
    <|  -- Test --> |    <dependency> |      <groupId>org.hamcrest</groupId>
      <artifactId>hamcrest-all</artifactId>
      <version>1.3</version>
      <scope>test</scope>
    </dependency>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit-dep</artifactId>
      <version>4.8.1</version>
      <scope>test</scope>
      <exclusions>
        <exclusion>
          <groupId>org.hamcrest</groupId>
          <artifactId>hamcrest-core</artifactId>
        </exclusion>
      </exclusions>
    </dependency>

  </dependencies>

  <build>
    <plugins>

      <|  -- Configuration needed for Groovy to work from Eclipse --> |      <plugin> |        <groupId>org.codehaus.mojo</groupId>
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
                <source>src/main/java</source>
                <source>src/main/groovy</source>
              </sources>
               <resources>
                <resource>src/main/resources</resource>
               </resources>
            </configuration>
          </execution>
          <execution>
            <id>add-test-source</id>
            <phase>generate-test-sources</phase>
            <goals>
              <goal>add-test-source</goal>
            </goals>
            <configuration>
              <sources>
                <source>src/test/java</source>
                <source>src/test/groovy</source>
              </sources>
               <resources>
                <resource>src/test/resources</resource>
               </resources>
            </configuration>
          </execution>
        </executions>
      </plugin>

      <plugin>
        <artifactId>maven-compiler-plugin</artifactId>
        <version>3.1</version>
        <configuration>
          <source>${javaVersion}</source>
          <target>${javaVersion}</target>
          <compilerId>groovy-eclipse-compiler</compilerId>
          <compilerArgument>nowarn</compilerArgument>
        </configuration>
        <dependencies>
          <dependency>
            <groupId>org.codehaus.groovy</groupId>
            <artifactId>groovy-eclipse-compiler</artifactId>
            <version>2.5.1-1</version>
          </dependency>
          <dependency>
            <groupId>org.codehaus.groovy</groupId>
            <artifactId>groovy-eclipse-batch</artifactId>
            <version>2.1.5-03</version>
          </dependency>
        </dependencies>
      </plugin>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-eclipse-plugin</artifactId>
        <version>2.8</version>
        <configuration>
          <additionalProjectnatures>
            <projectnature>org.eclipse.jdt.groovy.core.groovyNature</projectnature>
          </additionalProjectnatures>
        </configuration>
      </plugin>

      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-source-plugin</artifactId>
        <executions>
          <execution>
            <id>attach-sources</id>
            <goals>
              <goal>jar</goal>
            </goals>
          </execution>
        </executions>
      </plugin>
    </plugins>

    <pluginManagement>
      <plugins>
        <|  -- Ignore/Execute plugin execution --> |        <plugin> |          <groupId>org.eclipse.m2e</groupId>
          <artifactId>lifecycle-mapping</artifactId>
          <version>1.0.0</version>
          <configuration>
            <lifecycleMappingMetadata>
              <pluginExecutions>
                <|  -- copy-dependency plugin --> |                <pluginExecution> |                  <pluginExecutionFilter>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-dependency-plugin</artifactId>
                    <versionRange>[1.0.0,)</versionRange>
                    <goals>
                      <goal>copy-dependencies</goal>
                      <goal>unpack</goal>
                    </goals>
                  </pluginExecutionFilter>
                  <action>
                    <ignore />
                  </action>
                </pluginExecution>
              </pluginExecutions>
            </lifecycleMappingMetadata>
          </configuration>
        </plugin>
      </plugins>
    </pluginManagement>
  </build>
</project>
```

Для того, чтобы тесты, написанные на Groovy, можно было запускать из Maven, в Surefire нужно добавить следующее

```genshi
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-surefire-plugin</artifactId>
  <version>${surefire.version}</version>
  <configuration>
    <jvm>${jdk16}/bin/java</jvm>
    <argLine>-Xmx512m</argLine>
    <forkMode>once</forkMode>
    <redirectTestOutputToFile>true</redirectTestOutputToFile>
    <includes>
      <include>**/*Test.*</include>
    </includes>
  </configuration>
</plugin>
```

Таким образом Surefire будет запускать не только тесты на Java, а все классы, оканчивающиеся на Test

## GMaven


## Sources
- https://github.com/nickmcdowall/JavaAndGroovy
