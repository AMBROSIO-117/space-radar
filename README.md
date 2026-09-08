# Space Procurement Signal Radar

An Apify Actor that acts like a **forward deployed analyst** for niche B2B sellers.

It takes a plain-language seller prompt, discovers public web evidence, scores prospective buyers with a procurement ontology, and prints a one-page lead brief.

```text
User prompt -> web/search discovery -> score evidence -> print insights -> save report
```

## Default Use Case

```text
Find 1-5 DACH space-tech companies likely to need thermal vacuum testing soon.
For each company, report score, evidence, source link, contact info if available,
and a short engagement email.
```

## Why It Matters

As a seller in a concentrated buyer market, a generic company list is not enough.

The useful question is:

```text
Who should I investigate first, why now, and what evidence supports it?
```

This project turns scattered public web signals into a ranked procurement action list.

## Current Hackathon Build

Main Actor source:

```text
actor-space-procurement-radar/
```

The Actor:

- Accepts an analyst prompt, niche need, region, and max lead count.
- Runs in dry mode with fixture data.
- Runs live mode with Tavily Search API.
- Scores evidence using a simple procurement ontology.
- Writes rows to Apify Dataset.
- Saves `OUTPUT`, `REPORT.md`, and `INSIGHTS.md`.
- Can optionally POST the result to n8n.

## Source Of Truth

Start here:

- [Analyst coding and Codex 101](docs/ANALYST_CODING_AND_CODEX_101.md)
- [Apify hackathon recovery audit](docs/HACKATHON_RECOVERY_AUDIT.md)
- [Single source of truth](docs/SINGLE_SOURCE_OF_TRUTH.md)
- [Demo runbook](docs/DEMO_RUNBOOK.md)
- [GitHub push guide](docs/GITHUB_PUSH.md)
- [Evidence/source ledger](docs/EVIDENCE_AND_SOURCE_LEDGER.md)

Presentation source:

- [5-slide live pitch](presentation/space_radar_5_slide_live_pitch.md)
- [Full presentation source](outputs/space_radar_prompt_to_insights_presentation.md)

## Actor Input: Dry Run

Use this first. It does not need API keys.

```json
{
  "analystPrompt": "Find DACH space-tech companies likely to need thermal vacuum testing soon. Focus on evidence, urgency, price or budget clues, and next action for a forward deployed analyst.",
  "nicheNeed": "thermal vacuum testing",
  "region": "Germany DACH",
  "maxLeads": 5,
  "dryRun": true
}
```

Expected output:

```text
Apify Dataset rows
Key-value store -> OUTPUT
Key-value store -> REPORT.md
Key-value store -> INSIGHTS.md
```

## Actor Input: Live Tavily Mode

Set `TAVILY_API_KEY` as an Apify secret/environment variable, then run:

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

## Optional n8n Handoff

Create an n8n workflow:

```text
Webhook -> Set -> Notion/Sheets/Email
```

Then add the webhook URL to the Actor input:

```json
{
  "n8nWebhookUrl": "https://your-n8n-url/webhook/space-procurement-radar"
}
```

## Tech Stack

| Tool | Role |
| --- | --- |
| Apify | Actor runtime, Dataset, key-value report storage |
| JavaScript | Actor implementation |
| Tavily | Optional live web search |
| n8n | Optional workflow automation |
| Notion | Optional lead database |
| LLM | Helps convert seller intent into Actor input |

## Repo Map

```text
actor-space-procurement-radar/   Custom Apify Actor
data/                            Ontology and fixtures
docs/                            Canonical project docs
presentation/                    Presentation source
outputs/                         Working notes, templates, generated artifacts
app/                             Legacy prototypes
```

## Legacy Exploration

Earlier explorations are kept for context, including VIX Learning Radar and Apify Actor Idea Radar. They are not the current submission direction.
