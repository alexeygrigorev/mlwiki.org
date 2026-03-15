# ML Wiki

A comprehensive wiki covering machine learning, statistics, probability, data mining, and related topics.

Live site: [mlwiki.org](https://mlwiki.org)

## About

ML Wiki is a collection of articles on machine learning concepts, algorithms, and resources. Originally hosted on MediaWiki, it has been migrated to Jekyll and GitHub Pages.

## Local development

Requires Ruby and Bundler:

```bash
bundle install
bundle exec jekyll serve
```

Then open [http://localhost:4000](http://localhost:4000).

## Contributing

Edit any article and submit a pull request. Articles are Markdown files in `index.php/` with YAML frontmatter:

```yaml
---
layout: default
permalink: /index.php/Article_Name
tags:
- machine-learning
title: Article Name
---
```

LaTeX math is supported via MathJax (`$...$` for inline, `$$...$$` for display).

## Migration tools

The wiki was migrated from MediaWiki using a Python script:

```bash
uv sync
uv run python transfer.py data/wiki-pages.xml
```
