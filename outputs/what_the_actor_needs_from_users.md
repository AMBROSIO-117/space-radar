# What The Actor Needs From Users

## The Simple Version

The Actor needs four things:

| Input | Example | Why It Matters |
| --- | --- | --- |
| Analyst prompt | Find DACH space-tech companies likely to need thermal vacuum testing soon | Tells the Actor what job to do |
| Niche need | thermal vacuum testing | Keeps the search specific |
| Region | Germany DACH | Localizes the search |
| Optional webhook | n8n URL | Sends the result into a workflow |

## Best First Prompt

```text
Find DACH space-tech companies likely to need thermal vacuum testing soon. Focus on evidence, urgency, price or budget clues, and next action for a forward deployed analyst.
```

## What The Actor Does

```text
1. Reads the prompt
2. Builds search queries
3. Uses Tavily to browse/search public web information
4. Scores each source for procurement pressure
5. Prints insights into REPORT.md / INSIGHTS.md
6. Saves lead rows to the Apify Dataset
7. Optionally posts the result to n8n
```

## What Counts As Success

The Actor is useful if it answers:

```text
Who should I look at first?
Why now?
What evidence supports that?
Is there a price or budget clue?
What should I do next?
```

## What Not To Expect

It is not a magic CRM.

It will not perfectly know who is buying. It creates source-backed hypotheses for a human analyst to verify.

## Dry Run Input

Use this first:

```json
{
  "analystPrompt": "Find DACH space-tech companies likely to need thermal vacuum testing soon. Focus on evidence, urgency, price or budget clues, and next action for a forward deployed analyst.",
  "nicheNeed": "thermal vacuum testing",
  "region": "Germany DACH",
  "dryRun": true
}
```

## Live Tavily Input

Use this after dry run works:

```json
{
  "analystPrompt": "Find DACH space-tech companies likely to need thermal vacuum testing soon. Focus on evidence, urgency, price or budget clues, and next action for a forward deployed analyst.",
  "nicheNeed": "thermal vacuum testing",
  "region": "Germany DACH",
  "maxResultsPerQuery": 5,
  "maxLeads": 10,
  "searchDepth": "basic",
  "dryRun": false
}
```

