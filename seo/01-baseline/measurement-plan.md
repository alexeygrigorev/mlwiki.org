# Measurement Plan

## Primary KPI

**50,000 Organic Search sessions per calendar month by September 2027.**

Definition:

```
Platform: Google Analytics 4
Metric: Sessions
Filter: Session default channel group = Organic Search
Reporting timezone: Europe/Berlin
```

## Diagnostic metrics

### GA4

Track:

- Organic Search sessions
- Active users
- Engaged sessions
- Engagement rate
- Views
- Organic landing pages
- Session source / medium

Recommended daily export shape:

```
date
sessions
active_users
engaged_sessions
views
```

Recommended landing-page export shape:

```
landing_page
sessions
active_users
engaged_sessions
engagement_rate
views
```

Filter:

```
Session default channel group = Organic Search
```

## Google Search Console

Track:

- clicks
- impressions
- CTR
- average position
- queries
- pages
- countries
- devices
- indexed pages
- excluded / not indexed pages
- sitemap state

Do not treat:

- average position as the primary success metric
- GSC clicks as identical to GA4 sessions

## Ahrefs

Use Ahrefs as a diagnostic / external-data system, not as the primary traffic source of truth.

Track:

- Site Audit crawl results
- HTTP status
- indexability
- canonical
- title
- meta description
- H1
- internal links
- crawl depth
- redirects
- broken links
- organic keywords
- estimated traffic
- top pages
- backlinks
- referring domains

## Ubersuggest

Use mainly for:

- keyword research
- Keywords by Traffic
- Top Pages
- Site Audit as a second opinion
- keyword ideas
- search volume
- SEO difficulty
- SERP observations

## Measurement rules

Every reported metric should include:

- source
- exact metric definition
- date range
- filters
- geography
- device scope where relevant
- extraction date

Never compare unlike periods without explicitly noting the difference.

For experiments, prefer equal before/after windows (for example 28 days vs 28 days) and keep external confounders in mind.
