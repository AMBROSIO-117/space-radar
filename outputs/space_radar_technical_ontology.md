# Space Procurement Signal Radar - Technical Ontology

## System Components

| Component | Type | Responsibility |
| --- | --- | --- |
| Apify Actor | Runtime/product | Runs the workflow and stores outputs |
| Actor input schema | JSON schema | Defines the form in Apify Console |
| Tavily Search API | External data/search API | Finds live web sources |
| Scoring engine | JavaScript functions | Converts text signals into ranked leads |
| Apify Dataset | Storage | Stores one row per lead |
| Apify key-value store | Storage | Stores `OUTPUT` JSON and `REPORT.md` |
| n8n Webhook | Automation trigger | Receives finished result |
| Notion database | Optional dashboard | Stores leads and source ledger |

## Data Flow

```mermaid
sequenceDiagram
    participant User
    participant Actor as Apify Actor
    participant Tavily
    participant Dataset as Apify Dataset
    participant KV as Apify KV Store
    participant N8N as n8n Webhook

    User->>Actor: nicheNeed, region, dryRun/search settings
    Actor->>Tavily: POST /search for each query
    Tavily-->>Actor: results with title, url, content
    Actor->>Actor: dedupe, score, rank
    Actor->>Dataset: pushData(leads)
    Actor->>KV: setValue(OUTPUT, REPORT.md)
    Actor-->>N8N: optional POST ranked brief
```

## Actor Input Contract

| Field | Type | Purpose |
| --- | --- | --- |
| `nicheNeed` | string | Specific thing to sell |
| `region` | string | Geography to focus |
| `queries` | string[] | Optional custom search queries |
| `maxResultsPerQuery` | integer | Tavily results per query |
| `maxLeads` | integer | Number of ranked leads to keep |
| `searchDepth` | enum | Tavily cost/depth choice |
| `tavilyApiKey` | secret string | Tavily credential |
| `n8nWebhookUrl` | string | Optional n8n webhook |
| `dryRun` | boolean | Run without live API |

## Lead Output Contract

| Field | Meaning |
| --- | --- |
| `companyOrSource` | Name/title from source result |
| `region` | Region input |
| `likelyNeed` | Need inferred from text |
| `score` | 0-100 procurement pressure score |
| `confidence` | Low/Medium/High |
| `urgencyReason` | Explanation for timing signal |
| `priceBudgetClue` | Direct or proxy budget signal |
| `sellerAngle` | Suggested sales angle |
| `evidence` | Source snippet |
| `sourceUrl` | Evidence URL |
| `query` | Query that found the source |
| `matchedSignals` | Scoring dimensions that matched |

## Current Code Map

| Function | File | Purpose |
| --- | --- | --- |
| `tavilySearch` | `src/main.js` | Calls Tavily Search API |
| `scoreResult` | `src/main.js` | Scores one result into a lead |
| `dedupeByUrl` | `src/main.js` | Removes duplicate URLs |
| `buildReport` | `src/main.js` | Creates Markdown report |
| `postToN8n` | `src/main.js` | Sends finished output to n8n |

## Minimum Viable Build

```text
Actor receives input
Actor runs dryRun or Tavily search
Actor scores leads
Actor writes Dataset rows
Actor writes REPORT.md
```

That is enough for a working demo.

## Stronger Build

```text
Actor also sends payload to n8n
n8n writes the top lead to Notion
```

That proves operational workflow.

## Future Build

```text
Tavily discovery -> Apify Website Content Crawler for deeper source pages -> LLM extraction -> Notion/CRM
```

Do this only after the simple Actor works.

## Failure Modes

| Failure | Fix |
| --- | --- |
| Too many generic results | Add negative scoring and tighter queries |
| No price clues | Search tender/award/funding queries separately |
| n8n does not receive data | Use test webhook URL and press "Listen for test event" |
| Notion blocks write | Ask workspace owner to share database with integration |
| Scores look fake | Show matched signals and low confidence honestly |

