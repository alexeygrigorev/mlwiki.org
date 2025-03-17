---
title: "My bat file"
layout: default
permalink: /index.php/My_bat_file
---

# My bat file


## Командная строка с PATH

command_line.bat:
```bash
echo off
cls

cmd /K C:\Dev\bin\bootstrap.bat
```

bootstrap.bat:
```bash
@echo off

set NODE_JS_PATH=C:\Program Files (x86)\nodejs
set PYTHON_PATH=C:\Users\Alexey Grigorev\Documents\Portable Python 2.7.3.1\App
set DOT=C:\Users\Alexey Grigorev\Documents\soft\graphviz-2.34\release\bin;C:\Program Files\gs9.06\bin
set UNIX=C:\cygwin\bin
set JAVA_HOME=C:\Program Files\Java\jdk1.7.0_25
set GRAILS_HOME=C:\Users\Alexey Grigorev\Documents\soft\grails-2.3.5
set GRAILS=%GRAILS_HOME%\bin
set PATH=%PATH%;%UNIX%;%NODE_JS_PATH%;%PYTHON_PATH%;%DOT%;%GRAILS%

cmd
cls
```

## Передаём параметры
```scdoc
python C:\UBS\dev\portablepython\App\Scripts\uncompyle2 %*
```

%* передаёт все переданные параметры 


[Category:Scripts](Category_Scripts)
[Category:Snippets](Category_Snippets)