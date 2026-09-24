# Google Search Console Baseline

Search Console is the primary source for what happens in Google Search **before the visit**.

## Standard filters

Use:

```
Search type: Web
Country: All
Device: All
```

Capture:

- last 28 days
- last 3 months
- longest useful historical date range for trend analysis

## Export 1 — Queries

Columns:

```
query
clicks
impressions
CTR
position
```

Suggested filename:

```
gsc_queries_2026-09-24_last-3-months.csv
```

## Export 2 — Pages

Columns:

```
page
clicks
impressions
CTR
position
```

Suggested filename:

```
gsc_pages_2026-09-24_last-3-months.csv
```

## Export 3 — Dates

Columns:

```
date
clicks
impressions
CTR
position
```

Suggested filename:

```
gsc_daily_2026-09-24_longest-available.csv
```

## Export 4 — Devices

Columns:

```
device
clicks
impressions
CTR
position
```

## Export 5 — Countries

Columns:

```
country
clicks
impressions
CTR
position
```

## Indexing baseline

Open Indexing → Pages and record:

```
Indexed
Not indexed
```

Capture the reason groups, especially:

```
Crawled - currently not indexed
Discovered - currently not indexed
Duplicate
Alternate page with proper canonical
Excluded by noindex
404
Redirect
```

Do not fix everything immediately. First record the baseline.

## Sitemap baseline

Verify:

```
https://mlwiki.org/sitemap.xml
```

Record:

```
Submitted sitemap
Status
Discovered pages
Last read
```

The repository already contains `sitemap.xml` and `robots.txt`, and robots.txt references the sitemap.

## Core Web Vitals baseline

Record only:

```
Good
Needs improvement
Poor
```

Do not optimize solely to improve a score before identifying whether the issue affects meaningful pages.

## Automation later

Search Console API can later be used to retrieve dimensions such as:

```
date
query
page
country
device
searchAppearance
```

Manual export is useful for understanding the workflow; automation should come after the baseline is understood.
