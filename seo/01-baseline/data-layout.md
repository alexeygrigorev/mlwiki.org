# Baseline Data Layout

The mlwiki.org repository is public.

**Do not commit real Search Console, GA4, Ahrefs, or Ubersuggest exports here.**

Use a private workspace such as:

```
mlwiki-seo/
  00_project/
  01_raw/
  02_processed/
  03_experiments/
  04_reports/
```

Recommended raw layout:

```
01_raw/
  2026-09-24/
    gsc/
    ga4/
    ahrefs/
    ubersuggest/
    crawl/
```

Example filenames:

```
01_raw/2026-09-24/gsc/gsc_queries_3m.csv
01_raw/2026-09-24/gsc/gsc_pages_3m.csv
01_raw/2026-09-24/gsc/gsc_daily.csv

01_raw/2026-09-24/ahrefs/site_audit.csv
01_raw/2026-09-24/ahrefs/organic_keywords.csv
01_raw/2026-09-24/ahrefs/top_pages.csv
01_raw/2026-09-24/ahrefs/backlinks.csv

01_raw/2026-09-24/ubersuggest/keywords_by_traffic.csv
01_raw/2026-09-24/ubersuggest/top_pages.csv
```

## Measurement metadata

Keep a private baseline metadata file with:

```
Site: https://mlwiki.org
Baseline date: 2026-09-24
Primary KPI: 50,000 Organic Search sessions / calendar month
Target date: September 2027
GA4 timezone: Europe/Berlin
GSC search type: Web
GSC geography: All
GSC device: All
GA4 tracking started: YYYY-MM-DD
```

## Unified URL table

The main processed baseline artifact should be one row per canonical URL.

Suggested columns:

```
url
http_status
indexable
canonical
title
h1
meta_description
crawl_depth
internal_links_in
internal_links_out
gsc_clicks
gsc_impressions
gsc_ctr
gsc_position
ahrefs_keywords
ahrefs_estimated_traffic
referring_domains
ga4_organic_sessions
diagnostic_group
notes
```

Initially, GA4 fields may be empty because measurement starts only after installation.
