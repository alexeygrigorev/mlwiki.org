# Baseline Checklist

Execute in this order.

## 1. Install and verify GA4

- [ ] Create GA4 account/property if needed
- [ ] Create Web Data Stream for https://mlwiki.org
- [ ] Set timezone to Europe/Berlin
- [ ] Record Measurement ID `G-XXXXXXXXXX`
- [ ] Add GA4 to the Jekyll default layout
- [ ] Deploy
- [ ] Visit 2–3 pages
- [ ] Confirm traffic in GA4 Realtime
- [ ] Record tracking start date

Do this first because historical GA4 data cannot be reconstructed later.

## 2. Capture Google Search Console baseline

Performance → Search results.

Use:

```text
Search type: Web
Country: All
Device: All
```

Capture:

- [ ] Last 28 days
- [ ] Last 3 months
- [ ] Longest available daily history

Export:

- [ ] Queries
- [ ] Pages
- [ ] Dates
- [ ] Countries
- [ ] Devices

Also record:

- [ ] Total clicks
- [ ] Total impressions
- [ ] Average CTR
- [ ] Average position

## 3. Capture Search Console indexing state

Indexing → Pages:

- [ ] Indexed
- [ ] Not indexed
- [ ] Reasons for exclusion
- [ ] Counts by reason

Pay attention to:

- Crawled - currently not indexed
- Discovered - currently not indexed
- Duplicate
- Alternate page with proper canonical
- Excluded by noindex
- Not found (404)
- Page with redirect

Do not fix everything yet. Capture first.

## 4. Capture Search Console sitemap state

- [ ] Confirm https://mlwiki.org/sitemap.xml is submitted
- [ ] Record status
- [ ] Record discovered pages
- [ ] Record last read date

## 5. Capture Core Web Vitals state

Record counts/status for:

- [ ] Good
- [ ] Needs improvement
- [ ] Poor

Do not optimize solely for a Lighthouse score at this stage.

## 6. Run Ahrefs Site Audit

Crawl:

```text
https://mlwiki.org/
```

Record:

- [ ] URLs crawled
- [ ] Health Score
- [ ] Errors
- [ ] Warnings
- [ ] Notices

Export URL/issues data including when available:

- [ ] URL
- [ ] HTTP status
- [ ] Indexability
- [ ] Canonical
- [ ] Title
- [ ] Meta description
- [ ] H1
- [ ] Incoming internal links
- [ ] Outgoing internal links
- [ ] Crawl depth
- [ ] Redirects
- [ ] Broken links
- [ ] Duplicate titles
- [ ] Duplicate descriptions

## 7. Capture Ahrefs Site Explorer baseline

Export/save:

### Organic keywords

- [ ] keyword
- [ ] position
- [ ] URL
- [ ] volume
- [ ] estimated traffic
- [ ] country

### Top pages

- [ ] URL
- [ ] estimated traffic
- [ ] keywords
- [ ] top keyword

### Backlinks / referring domains

- [ ] referring domain
- [ ] source URL
- [ ] target URL
- [ ] Ahrefs authority metric if available
- [ ] anchor
- [ ] dofollow/nofollow

Top-level values:

- [ ] referring domains
- [ ] backlinks

## 8. Capture Ubersuggest baseline

Export/save:

### Keywords by Traffic

- [ ] keyword
- [ ] position
- [ ] volume
- [ ] estimated visits
- [ ] URL

### Top Pages by Traffic

- [ ] URL
- [ ] estimated visits
- [ ] keywords
- [ ] backlinks

### Site Audit

Run once as a secondary opinion:

- [ ] pages discovered
- [ ] critical errors
- [ ] warnings
- [ ] notable disagreements with Ahrefs

Do not export huge keyword-idea datasets yet.

## 9. Build the URL master baseline

Use `url-baseline-template.csv`.

One row = one canonical target URL.

Join where possible:

- crawler/Ahrefs technical fields
- Search Console page metrics
- Ahrefs page/keyword estimates
- later: GA4 organic landing-page sessions

GA4 will initially be blank because tracking starts now.

## 10. Segment pages

Create diagnostic groups such as:

### Existing winners

Pages with meaningful impressions/clicks and useful rankings.

### Opportunity

Pages with many impressions but few clicks.

### Near winners

Pages with meaningful impressions and positions roughly in the 5–20 range.

### Invisible

Indexable pages with almost no impressions.

### Technical problems

Pages with broken status, redirects, bad canonical/indexability, broken links, or weak internal discovery.

These are diagnostic groups, not automatic recommendations.

## 11. Choose one topic cluster

Do not research the whole site at once.

Choose one cluster, for example:

- machine learning evaluation metrics
- information retrieval
- linear algebra for machine learning

Then combine:

- existing GSC queries
- Ahrefs keywords
- Ubersuggest keyword ideas
- observed SERPs

Build:

```text
query → intent → cluster → existing page → action
```

## 12. Select the first experiment

Choose only 5–10 URLs.

Prefer pages that:

- are indexable
- already receive meaningful impressions
- have plausible upside
- can be materially improved
- can be measured before/after

Fill in `experiment-template.md`.

## 13. Make the changes

For every changed URL record:

- date
- URL
- change
- experiment ID
- Git commit

Use `change-log-template.csv`.

## 14. Measure

Compare matched periods, for example:

```text
28 days before
vs
28 days after
```

Use:

- GSC impressions
- GSC clicks
- GSC query composition
- GA4 Organic Search sessions

Do not judge the experiment from average position alone.

## 15. Decide

For each experiment:

- keep
- iterate
- revert
- inconclusive

Record the reason and evidence.
