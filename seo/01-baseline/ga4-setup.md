# GA4 Setup

## Goal

Start collecting first-party site usage data for mlwiki.org.

GA4 cannot reconstruct historical traffic before tracking is installed.

## Create the property

Create:

```
Property: mlwiki.org
Website: https://mlwiki.org
Timezone: Europe/Berlin
```

Create a Web Data Stream and obtain a Measurement ID:

```
G-XXXXXXXXXX
```

## Recommended repository configuration

Put the measurement ID in `_config.yml`:

```yaml
google_analytics: "G-XXXXXXXXXX"
```

In `_layouts/default.html`, immediately after `<head>`:

```html
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

## Verification

After deployment:

1. Open https://mlwiki.org
2. Navigate across several pages
3. Open GA4 → Realtime
4. Confirm that a user and page views appear

Definition of done:

```
Realtime shows traffic from a live browser session.
```

## Baseline reports to use later

### Daily organic traffic

Dimension:

```
Date
```

Metrics:

```
Sessions
Active users
Engaged sessions
Views
```

Filter:

```
Session default channel group = Organic Search
```

### Organic landing pages

Dimension:

```
Landing page + query string
```

Metrics:

```
Sessions
Active users
Engaged sessions
Engagement rate
Views
```

Filter:

```
Session default channel group = Organic Search
```

### Organic source / medium

Dimension:

```
Session source / medium
```

Metrics:

```
Sessions
Active users
Engaged sessions
```

This helps distinguish Google, Bing, and other organic sources.

## Baseline note

Record the exact first date on which GA4 was verified:

```
GA4 tracking started: YYYY-MM-DD
```
