---
layout: default
permalink: /index.php/Sublime_Tricks
title: Sublime Tricks
---
## Новые горячии клавиши

Например, 

### оборачивание тегом math

preferences - key binding (user)

 [
  { "keys": ["alt+shift+m"], "command": "insert_snippet", "args": { "name": "Packages/mediawiki/math-tag.sublime-snippet" } }
 ]

Packages/mediawiki/math-tag.sublime-snippet:

 &lt;snippet&gt;
     &lt;content&gt;&lt;|  [CDATA[&lt;math&gt;${2:$SELECTION}&lt;/math&gt;]]&gt;&lt;/content&gt; |     &lt;scope&gt;math&lt;/scope&gt; |     &lt;description&gt;Math Tag&lt;/description&gt;
 &lt;/snippet&gt;