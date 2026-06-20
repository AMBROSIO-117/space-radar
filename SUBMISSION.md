# Hackathon Submission

Project name:

```text
Space Procurement Signal Radar
```

## What It Does

Space Procurement Signal Radar is an Apify Actor that acts like a forward deployed analyst for a niche seller.

The user gives it a prompt like:

```text
Find 1-5 DACH space-tech companies likely to need thermal vacuum testing soon.
```

The Actor discovers/searches public evidence, scores each lead with a procurement ontology, and prints a one-page brief with:

- company/source
- region
- likely need
- score
- evidence snippet
- source URL
- price/budget clue
- suggested seller angle

## Challenge Fit

| Requirement | Fit |
| --- | --- |
| Working demo | Actor runs in dry mode and live Tavily mode |
| At least one Apify Actor | Custom Actor in `actor-space-procurement-radar/` |
| Public repo/project link | This folder is prepared for GitHub |
| 2-minute demo | Use `presentation/space_radar_5_slide_live_pitch.md` |

## Demo Input

```json
{
  "analystPrompt": "Find DACH space-tech companies likely to need thermal vacuum testing soon. Focus on evidence, urgency, price or budget clues, and next action for a forward deployed analyst.",
  "nicheNeed": "thermal vacuum testing",
  "region": "Germany DACH",
  "maxLeads": 5,
  "dryRun": true
}
```

## 2-Minute Demo Script

**0:00-0:20 - Problem**

"Most sales tools produce generic lead lists. I wanted something more like a forward deployed analyst: take a niche seller problem and find procurement pressure with evidence."

**0:20-0:45 - Product**

"The user gives the Actor a plain-language prompt, like finding DACH space-tech companies that may need thermal vacuum testing. The Actor searches public sources, scores evidence with a procurement ontology, and writes a ranked brief."

**0:45-1:20 - Demo**

"Here is the Actor input. Here is the run. Here are the Dataset rows. Here is `REPORT.md`, with the ranked leads, evidence, score, and next action."

**1:20-1:45 - Why Apify Matters**

"Apify turns this into a reusable Actor with inputs, runs, Dataset output, and report storage. It is not just a script; it is a repeatable workflow."

**1:45-2:00 - Close**

"The output is not a generic scraped list. It is a ranked action list a seller can use to decide who to investigate first."

## Optional Upgrades

- Tavily live search.
- n8n webhook handoff.
- Notion/CRM lead database.
- Apify Website Content Crawler for deeper source extraction.

## Safety Boundary

This is source-backed procurement intelligence for human review. It does not claim certainty, send emails automatically, or make legal/procurement decisions.

