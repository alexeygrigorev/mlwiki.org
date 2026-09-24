# MLWiki SEO Baseline

This folder defines the first SEO stage for [mlwiki.org](https://mlwiki.org).

## Goal

Primary outcome goal:

> Reach **50,000 Organic Search sessions per calendar month by September 2027**.

Learning goal:

> Use mlwiki.org as a practical SEO lab to learn crawling and indexing, keyword and topic research, search intent, information architecture, on-page SEO, internal linking, technical SEO, measurement, experimentation, and visibility in AI-assisted search.

## Baseline stage

The first stage is:

1. Create reliable measurement.
2. Capture the current state before major SEO changes.
3. Collect technical and search-performance diagnostics.
4. Build one URL-level baseline table.
5. Choose one topic cluster.
6. Run a small first experiment on 5–10 URLs.
7. Compare before/after results using the same measurement definitions.

Do **not** optimize the whole site before the baseline is captured.

## Primary metric

The project North Star is:

- **GA4 Organic Search sessions per calendar month**
- GA4 dimension/filter: `Session default channel group = Organic Search`

Operational trend metric:

- **Organic Search sessions, rolling 28 days**

Important:

- Google Search Console clicks are not the same thing as GA4 sessions.
- Ahrefs/Ubersuggest traffic values are estimates, not the primary KPI.
- Search Console describes search visibility and clicks before the visit.
- GA4 describes user activity after the visit.

## Data sources

| Question | Primary source |
|---|---|
| How many organic visits do we get? | GA4 |
| Which Google queries/pages get impressions and clicks? | Google Search Console |
| Which pages are indexed / excluded? | Google Search Console |
| Is sitemap processing healthy? | Google Search Console |
| Which technical crawl issues exist? | Ahrefs Site Audit |
| Which backlinks/referring domains exist according to Ahrefs? | Ahrefs |
| Which keywords/pages appear to have opportunity? | Ahrefs + Ubersuggest |
| What are keyword ideas / volumes / SERPs? | Ubersuggest + Ahrefs |
| What exactly changed on the site? | Git history |

## Current site state already confirmed

The repository already contains:

- `robots.txt`
- `sitemap.xml`
- canonical tags in the default layout
- structured data in the default layout

At baseline creation time, no Google Analytics / GTM / Plausible / Matomo tracking code was found in the repository.

## Files in this folder

- [measurement-passport.md](measurement-passport.md) — definitions and metric contract
- [baseline-checklist.md](baseline-checklist.md) — exact sequence to execute now
- [data-sources.md](data-sources.md) — what to export from each tool
- [url-baseline-template.csv](url-baseline-template.csv) — URL-level master table schema
- [experiment-template.md](experiment-template.md) — first SEO experiment template
- [change-log-template.csv](change-log-template.csv) — record of SEO changes

## Raw data policy

**Do not commit raw GSC, GA4, Ahrefs, or Ubersuggest exports to this public repository.**

Store raw exports privately, for example:

```text
mlwiki-seo-private/
  01_raw/
    2026-09-24/
      gsc/
      ga4/
      ahrefs/
      ubersuggest/
      crawl/
```

This repository should contain methodology, schemas, decisions, experiment definitions, and non-sensitive summaries only.
