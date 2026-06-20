# Demo Runbook

## First Demo: Dry Run

Use this when you need a reliable demo without API keys.

```json
{
  "analystPrompt": "Find DACH space-tech companies likely to need thermal vacuum testing soon. Focus on evidence, urgency, price or budget clues, and next action for a forward deployed analyst.",
  "nicheNeed": "thermal vacuum testing",
  "region": "Germany DACH",
  "maxLeads": 5,
  "dryRun": true
}
```

Check:

```text
Dataset -> lead rows
Storage -> Key-value store -> REPORT.md
Storage -> Key-value store -> INSIGHTS.md
```

## Live Demo: Tavily

Set:

```text
TAVILY_API_KEY=tvly-your-key
```

Use:

```json
{
  "analystPrompt": "Find 1-5 DACH space-tech companies likely to need thermal vacuum testing soon. Report score, evidence, source link, contact info if available, and an engagement email.",
  "nicheNeed": "thermal vacuum testing",
  "region": "Germany DACH",
  "maxResultsPerQuery": 5,
  "maxLeads": 5,
  "searchDepth": "basic",
  "dryRun": false
}
```

## Optional n8n Demo

Create:

```text
Webhook -> Respond to Webhook
```

Paste the test webhook URL into:

```json
{
  "n8nWebhookUrl": "https://your-n8n-url/webhook-test/space-procurement-radar"
}
```

## What To Show

1. Plain-language Actor input.
2. Dataset rows.
3. `REPORT.md`.
4. Source URLs and evidence.
5. Optional n8n receiving the payload.

## Recovery If Live Search Fails

Switch back to:

```json
{
  "dryRun": true
}
```

Say:

```text
The dry run proves the Actor workflow. Live search is the same flow with Tavily credentials enabled.
```

