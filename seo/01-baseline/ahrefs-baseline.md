# Ahrefs Baseline

Use Ahrefs as a diagnostic and external SEO dataset.

Do **not** use Ahrefs Estimated Traffic as the primary traffic KPI. GA4 is the source of truth for actual site sessions.

## Site Audit

Run a crawl of:

```
https://mlwiki.org/
```

Capture top-level values:

```
URLs crawled
Health Score
Errors
Warnings
Notices
```

Health Score is diagnostic, not the project goal.

## URL-level fields to export

Prefer fields such as:

```
URL
HTTP status
indexability
canonical
title
meta description
H1
incoming internal links
outgoing internal links
crawl depth
redirects
broken links
duplicate titles
duplicate descriptions
```

## Organic Keywords

Export where available:

```
keyword
position
URL
volume
estimated traffic
country
```

## Top Pages

Export:

```
URL
estimated traffic
keywords
top keyword
```

## Backlinks / Referring Domains

Export:

```
referring domain
source URL
target URL
DR / equivalent metric
anchor
dofollow / nofollow
```

Record baseline totals:

```
referring domains
backlinks
```

Treat these as Ahrefs-observed values, not absolute counts of every link on the web.
