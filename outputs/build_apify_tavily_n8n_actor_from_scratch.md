# Build From Scratch: Apify + Tavily + n8n

## Goal

Create a very simple Apify Actor:

```text
Input: niche thing to sell + region
Live data: Tavily search
Processing: score procurement pressure
Output: Apify Dataset + Markdown report
Optional automation: POST results to n8n webhook
```

Project:

```text
Space Procurement Signal Radar
```

Default question:

```text
Which Germany/DACH space-tech companies look most likely to need thermal vacuum testing soon?
```

## What Each Tool Does

| Tool | Role |
| --- | --- |
| Apify Actor | The runnable hackathon product. It receives input, runs the workflow, stores output, and can be published. |
| Tavily | Live web-search discovery layer. It finds public pages, company signals, tenders, and ecosystem clues. |
| n8n | Optional automation layer. It receives the finished brief and routes it to Notion, Sheets, Slack, email, or another workflow. |

## Files Created

```text
actor-space-procurement-radar/
  package.json
  Dockerfile
  .env.example
  .actor/
    actor.json
    INPUT_SCHEMA.json
    README.md
  src/
    main.js
```

## Beginner Build Steps

### 1. Run Dry Mode First

Use dry mode when you have no Tavily key yet.

In Apify Console input:

```json
{
  "nicheNeed": "thermal vacuum testing",
  "region": "Germany DACH",
  "dryRun": true
}
```

Expected output:

```text
Dataset rows: scored seed leads
Key-value store: OUTPUT and REPORT.md
```

### 2. Run With Tavily

Add your Tavily API key as an Apify secret/environment variable:

```text
TAVILY_API_KEY=tvly-your-key
```

Input:

```json
{
  "nicheNeed": "thermal vacuum testing",
  "region": "Germany DACH",
  "maxResultsPerQuery": 5,
  "maxLeads": 10,
  "searchDepth": "basic",
  "dryRun": false
}
```

### 3. Add n8n

In n8n:

```text
Webhook node
Method: POST
Path: space-procurement-radar
```

Then add any next step:

```text
Set -> Notion
Set -> Google Sheets
Set -> Email
Set -> Slack
```

Paste the n8n webhook URL into Actor input:

```json
{
  "n8nWebhookUrl": "https://your-n8n-domain/webhook/space-procurement-radar"
}
```

## Demo Script

```text
I built a custom Apify Actor from scratch. It takes a niche procurement need, here thermal vacuum testing for DACH space-tech companies, uses Tavily to discover live web signals, scores each source for procurement pressure, writes ranked leads to Apify Dataset, and optionally sends the result to n8n.
```

## What To Show Judges

1. Actor input screen.
2. Run log.
3. Dataset rows.
4. `REPORT.md` from the key-value store.
5. n8n webhook execution if connected.

## Minimum Working Submission

This is enough:

```text
Custom Apify Actor + dry run + Tavily live mode ready + report output
```

Better:

```text
Custom Apify Actor + Tavily live search + Dataset rows + n8n webhook
```

Best:

```text
Custom Apify Actor + Tavily live search + n8n -> Notion lead database
```

## Safety Boundary

This is not legal, investment, or procurement advice. It produces source-backed hypotheses for human review.
