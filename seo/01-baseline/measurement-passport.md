# Measurement Passport

## Project

Site: https://mlwiki.org

Baseline date: 2026-09-24

Primary market: English-language search

Project type: educational SEO experiment site

## Outcome goal

Reach **50,000 GA4 Organic Search sessions per calendar month by September 2027**.

## Learning goal

Learn and repeatedly practice:

- crawling and indexing
- technical SEO
- keyword research
- topic research
- search intent
- content design
- information architecture
- internal linking
- on-page SEO
- Search Console analysis
- GA4 analysis
- SEO experimentation
- AI search / citation visibility

## Primary KPI

### Monthly Organic Search sessions

Source: GA4

Definition:

```text
Metric: Sessions
Filter: Session default channel group = Organic Search
Period: calendar month
Timezone: Europe/Berlin
```

Operational view:

```text
Organic Search sessions
rolling 28 days
```

## Diagnostic metrics

### GA4

- Sessions
- Active users
- Engaged sessions
- Engagement rate
- Views
- Organic landing pages
- Session source / medium

### Google Search Console

- Clicks
- Impressions
- CTR
- Average position
- Queries
- Pages
- Countries
- Devices
- Indexed pages
- Not indexed pages
- Sitemap status
- Core Web Vitals status

### Ahrefs

- URLs crawled
- Site Audit Health Score
- Errors
- Warnings
- Notices
- HTTP status
- Indexability
- Canonical
- Title
- Meta description
- H1
- Incoming internal links
- Outgoing internal links
- Crawl depth
- Redirects
- Broken links
- Duplicate titles/descriptions
- Organic keywords
- Top pages
- Backlinks
- Referring domains

### Ubersuggest

- Keywords by Traffic
- Top Pages by Traffic
- Keyword Ideas
- Search volume
- SEO Difficulty
- SERP data
- Backlinks
- Site Audit (secondary opinion)

## Metric rules

1. GA4 sessions are the primary traffic KPI.
2. GSC clicks are a separate search-performance metric.
3. Ahrefs/Ubersuggest traffic is modeled/estimated data.
4. Never compare metrics across different date ranges without noting the difference.
5. Always record filters, country, device, search type, and timezone.
6. Treat unknown values as unknown; do not infer missing measurements.
7. Compare experiments using matching before/after windows when possible.

## Search Console baseline settings

```text
Property: mlwiki.org (record exact property name)
Search type: Web
Country: All
Device: All
```

Recommended baseline windows:

- last 28 days
- last 3 months
- longest available history for daily trend

## GA4 setup

Create:

```text
Property: mlwiki.org
Web stream: https://mlwiki.org
Timezone: Europe/Berlin
```

Tracking start date should be recorded once GA4 is deployed.

GA4 will not reconstruct historical site visits from before installation.

## GA4 implementation location

The main Jekyll layout is:

```text
_layouts/default.html
```

Recommended configuration:

`_config.yml`

```yaml
google_analytics: "G-XXXXXXXXXX"
```

`_layouts/default.html`

```html
<head>
    {% if site.google_analytics %}
    <script async src="https://www.googletagmanager.com/gtag/js?id={{ site.google_analytics }}"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', '{{ site.google_analytics }}');
    </script>
    {% endif %}
```

Definition of done:

- production deployment completed
- GA4 Realtime shows visits to mlwiki.org
- page views are recorded on several URLs
