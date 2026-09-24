# Data Sources and Exports

## Google Analytics 4

Purpose: measure actual site visits and post-click behavior.

Primary KPI source.

### Daily organic trend

Dimension:

```text
Date
```

Metrics:

```text
Sessions
Active users
Engaged sessions
Views
```

Filter:

```text
Session default channel group = Organic Search
```

Desired table:

```text
date
sessions
active_users
engaged_sessions
views
```

### Organic landing pages

Dimension:

```text
Landing page + query string
```

Metrics:

```text
Sessions
Active users
Engaged sessions
Engagement rate
Views
```

Filter:

```text
Session default channel group = Organic Search
```

### Traffic sources

Dimension:

```text
Session source / medium
```

Metrics:

```text
Sessions
Active users
Engaged sessions
```

Use this later to observe sources such as Google/Bing organic and referrals from AI assistants when available.

---

## Google Search Console

Purpose: measure Google search visibility and clicks.

### Performance exports

#### Queries

```text
query
clicks
impressions
CTR
position
```

#### Pages

```text
page
clicks
impressions
CTR
position
```

#### Dates

```text
date
clicks
impressions
CTR
position
```

#### Countries

```text
country
clicks
impressions
CTR
position
```

#### Devices

```text
device
clicks
impressions
CTR
position
```

Suggested filenames:

```text
gsc_queries_YYYY-MM-DD_3m.csv
gsc_pages_YYYY-MM-DD_3m.csv
gsc_daily_YYYY-MM-DD_longest.csv
gsc_countries_YYYY-MM-DD_3m.csv
gsc_devices_YYYY-MM-DD_3m.csv
```

### Indexing

Record:

```text
status_or_reason
page_count
capture_date
```

### Sitemap

Record:

```text
sitemap_url
status
discovered_pages
last_read
capture_date
```

---

## Ahrefs Site Audit

Purpose: technical crawling and internal-site diagnostics.

Capture URL-level fields when available:

```text
url
http_status
indexable
canonical
title
meta_description
h1
incoming_internal_links
outgoing_internal_links
crawl_depth
redirect_target
broken_links
issues
```

Top-level snapshot:

```text
capture_date
urls_crawled
health_score
errors
warnings
notices
```

Health Score is diagnostic, not a project KPI.

---

## Ahrefs Site Explorer

Purpose: external SEO view and opportunity discovery.

### Organic keywords

```text
keyword
position
url
volume
estimated_traffic
country
```

### Top pages

```text
url
estimated_traffic
keywords
top_keyword
```

### Backlinks/referring domains

```text
referring_domain
source_url
target_url
authority_metric
anchor
link_type
```

Ahrefs traffic is estimated data and must not replace GA4 as the project traffic KPI.

---

## Ubersuggest

Purpose: supplementary keyword/competitor research and second-opinion audit data.

### Keywords by Traffic

```text
keyword
position
volume
estimated_visits
url
```

### Top Pages by Traffic

```text
url
estimated_visits
keywords
backlinks
```

### Keyword Ideas (use after choosing a topic cluster)

```text
keyword
volume
seo_difficulty
cpc
serp_information
```

### Site Audit

Use as a second opinion against Ahrefs, especially when tools disagree.

Do not treat Ubersuggest estimated visits as actual traffic.

---

## Private raw-data layout

Recommended local/private structure:

```text
mlwiki-seo-private/
  01_raw/
    YYYY-MM-DD/
      gsc/
      ga4/
      ahrefs/
      ubersuggest/
      crawl/
  02_processed/
  03_experiments/
  04_reports/
```

Raw exports may contain query/page/account information and should not be committed to this public repository.
