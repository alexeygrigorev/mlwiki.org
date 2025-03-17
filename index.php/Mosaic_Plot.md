---
title: Mosaic Plot
layout: default
permalink: /index.php/Mosaic_Plot
---

# Mosaic Plot

## Mosaic Plot
This is a [Plot](Plot)
- it's a visualization of information from [Contingency Table](Contingency_Table)s
- it's similar to a [Bar Chart](Bar_Chart), but shows more information
- uses areas to represent this information


### [R](R)
Add data

```carbon
library(openintro)
data(email)
```

One variable

```text only
tab1 = table(email$number)
mosaicplot(tab1, col=c('yellow2', 'skyblue2', 'red'),
           main='Numbers in emails')
```

<img src="http://habrastorage.org/files/5d6/3a9/1dd/5d63a91dd2be45e499aeacedb579328e.png" alt="Image">


```text only
tab2 = table(email$number, email$spam)
mosaicplot(tab2, col=c('yellow2', 'skyblue2'),
           main='Numbers in emails vs spam/not spam')
```

<img src="http://habrastorage.org/files/afd/8ce/0b7/afd8ce0b7f3d4f71ad86a07b56d3a098.png" alt="Image">


## Sources
- [OpenIntro Statistics (book)](OpenIntro_Statistics_(book))

[Category:Plots](Category_Plots)
[Category:R](Category_R)