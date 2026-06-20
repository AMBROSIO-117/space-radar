# Space Procurement Signal Radar

This Actor finds DACH space-tech procurement pressure signals for a specific niche product or service.

Default use case:

```text
Find small Germany/DACH space-tech companies likely to need thermal vacuum testing soon.
```

It uses Tavily Search for live web discovery, scores each result for procurement pressure, writes ranked leads to the Apify Dataset, stores a Markdown report, and can optionally POST the result to an n8n webhook.

Simple mental model:

```text
Analyst prompt -> web discovery -> signal scoring -> insights/report -> optional workflow handoff
```

## Inputs

- `analystPrompt`: plain-English task for the forward deployed analyst.
- `nicheNeed`: the specific product/service to sell, for example `thermal vacuum testing`.
- `region`: geographic focus, for example `Germany DACH`.
- `queries`: optional custom search queries.
- `tavilyApiKey`: Tavily API key, or set `TAVILY_API_KEY` as a secret/environment variable.
- `n8nWebhookUrl`: optional n8n Webhook node URL.
- `dryRun`: run with fixture data if you do not have a Tavily key yet.

## Outputs

Each Dataset item is one scored lead with:

- company/source name
- likely need
- score
- evidence snippet
- urgency reason
- price/budget clue
- seller angle
- source URL

The Actor also stores:

```text
OUTPUT
REPORT.md
INSIGHTS.md
```

Open `REPORT.md` first if you want the human-readable answer.

## n8n

Create an n8n workflow with:

```text
Webhook Trigger -> Set/Summarize/AI/Notion/Google Sheets/Email
```

Use `POST` and paste the webhook URL into `n8nWebhookUrl`.
