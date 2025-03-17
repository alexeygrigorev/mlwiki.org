---
title: Downloading coursera previews
layout: default
permalink: /index.php/Downloading_coursera_previews
---

# Downloading coursera previews

Скрипт выдёргивает все ссылки на видео из превью для курсеры и складывает их в файл

```python
import urllib
import re

outputhtml = open('course-download.html' ,'w')

mainpage = urllib.urlopen("https://class.coursera.org/algo2-2012-001/lecture/preview");
mainpage_contents = mainpage.read()

allvideos = re.findall('(".*?lecture_id.*?")', mainpage_contents)

for vid_each in allvideos:
    vid = vid_each[1:-1]
    vidcontent = urllib.urlopen(vid).read()

    vidtitle = re.findall('<div id="lecture_title" class="hidden">(.*?)</div>', vidcontent)
    if (len(vidtitle) > 0):
        vidtitle = vidtitle[0]
    else:
        continue

    vidurl = re.findall('"([^"]*?\.mp4)"', vidcontent)
    if (len(vidurl) > 0):
        vidurl = vidurl[0]
    else:
        continue

    vidsub = re.findall('src="(.*?subtitles.*?_en)"', vidcontent)
    if (len(vidsub) > 0):
        vidsub = vidsub[0]
    else:
        vidsub = ''

    outputhtml.write(vidurl + ' ' + vidsub + '\n')
    print vidtitle

outputhtml.close()
```

Оригинал: [http://crossplatform.net/download-coursera-videos-with-your-favorite-download-manager/]

[Category:Coursera](Category_Coursera)
[Category:Scripts](Category_Scripts)
[Category:Python](Category_Python)