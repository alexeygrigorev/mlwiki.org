---
layout: default
title: All Articles
---
This is a complete list of all articles in the ML Wiki.

{% assign sorted_pages = site.pages | where_exp: "page", "page.path contains 'index.php/'" | where_exp: "page", "page.path contains '.md'" | sort: "title" %}

<div style="columns: 3; column-gap: 2rem; margin-top: 2rem;">
{% for page in sorted_pages %}
  {% if page.title and page.title != "" and page.title != "All Articles" %}
    <div style="break-inside: avoid; margin-bottom: 0.5rem;">
      <a href="{{ page.url | relative_url }}">{{ page.title }}</a>
    </div>
  {% endif %}
{% endfor %}
</div>

---

**Total Articles**: {{ sorted_pages | where_exp: "page", "page.title != 'All Articles'" | size }}