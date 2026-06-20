# Apify Actor Build Coach Checklist

## Goal

Build and run:

```text
Space Procurement Signal Radar
```

It should:

1. Accept an input like `thermal vacuum testing`.
2. Run in Apify as a custom Actor.
3. Produce ranked lead rows in the Apify Dataset.
4. Save a `REPORT.md`.
5. Optionally send results to n8n.

## Fastest Path

Use Apify Console first. Do not start with CLI unless mentors require it.

## Step 1 - Open The Actor Source Folder

Source folder:

```text
actor-space-procurement-radar/
```

Files to copy into Apify:

```text
package.json
Dockerfile
.actor/actor.json
.actor/INPUT_SCHEMA.json
.actor/README.md
src/main.js
```

## Step 2 - Create Actor In Apify

In Apify Console:

```text
Actors -> Create new Actor
```

Choose:

```text
Node.js / JavaScript Actor
```

Name:

```text
space-procurement-signal-radar
```

## Step 3 - Add Files

In the Actor source editor, make the file tree match:

```text
package.json
Dockerfile
.actor/
  actor.json
  INPUT_SCHEMA.json
  README.md
src/
  main.js
```

Copy/paste the local file contents into matching Apify files.

## Step 4 - Build

Click:

```text
Save -> Build
```

If build fails:

1. Open build log.
2. Check that `package.json` exists.
3. Check that `Dockerfile` exists.
4. Check that `src/main.js` exists.
5. Check that `package.json` contains `"type": "module"`.

## Step 5 - First Run: Dry Mode

Use this input:

```json
{
  "nicheNeed": "thermal vacuum testing",
  "region": "Germany DACH",
  "dryRun": true
}
```

Expected:

```text
Run succeeds
Dataset contains rows
Key-value store contains OUTPUT and REPORT.md
```

If this works, the Actor is real.

## Step 6 - Add Tavily

In Apify Actor settings or secrets, add:

```text
TAVILY_API_KEY=tvly-your-key
```

Then run:

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

Expected:

```text
Dataset contains live source URLs
Scores vary
REPORT.md includes lead table
```

## Step 7 - Add n8n

In n8n create:

```text
Webhook
Method: POST
Path: space-procurement-radar
```

Click:

```text
Listen for test event
```

Copy the test webhook URL into Actor input:

```json
{
  "nicheNeed": "thermal vacuum testing",
  "region": "Germany DACH",
  "dryRun": true,
  "n8nWebhookUrl": "https://your-n8n-url/webhook-test/space-procurement-radar"
}
```

Expected:

```text
n8n receives JSON with leads and ledger
```

## Step 8 - What To Demo

Demo in this order:

1. Actor input form.
2. Run log.
3. Dataset rows.
4. `REPORT.md`.
5. n8n webhook receipt if connected.

## Demo Line

```text
I built a custom Apify Actor that acts like a forward deployed analyst for a niche aerospace supplier. It takes a thing to sell, finds live market/procurement signals with Tavily, scores the evidence, writes a ranked lead brief to Apify, and can push the workflow into n8n.
```

