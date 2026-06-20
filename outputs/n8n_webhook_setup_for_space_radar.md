# n8n Webhook Setup For Space Procurement Signal Radar

## Simple Workflow

Create a new n8n workflow:

```text
Webhook -> Set -> Respond to Webhook
```

## Webhook Node

Use:

```text
HTTP Method: POST
Path: space-procurement-radar
```

n8n gives you two URLs:

```text
Test URL: use while you are editing and listening for a test event
Production URL: use after activating/publishing the workflow
```

Paste the URL into the Actor input field:

```text
n8nWebhookUrl
```

## Payload Shape From The Actor

The Actor sends:

```json
{
  "project": "Space Procurement Signal Radar",
  "nicheNeed": "thermal vacuum testing",
  "region": "Germany DACH",
  "generatedAt": "2026-06-20T...",
  "leads": [],
  "ledger": []
}
```

## Notion Next Step

After the Webhook node, add a Notion node:

```text
Resource: Database Page
Operation: Create
Database: Lead Radar
```

Map fields:

| Notion Field | Actor Payload |
| --- | --- |
| Company | `leads[0].companyOrSource` |
| Region | `region` |
| Likely Need | `leads[0].likelyNeed` |
| Score | `leads[0].score` |
| Evidence URL | `leads[0].sourceUrl` |
| Price Clue | `leads[0].priceBudgetClue` |
| Seller Angle | `leads[0].sellerAngle` |

For a hackathon demo, it is acceptable to send only the top lead first. Looping over all leads is a nice upgrade if time remains.
