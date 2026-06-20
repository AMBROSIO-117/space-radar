# Apify Actor Use / Improve Plan

Date: 2026-06-20
Goal: Use or improve an existing Apify Actor for the Agents that Pay hackathon without drifting into job search or generic scraping.

## 1. Recommended Direction

Build a wrapper/meta-Actor around existing Apify Actors:

**Paid Data Decision Ledger**

It does not compete with Google Search Scraper or Website Content Crawler. It improves how an agent chooses, runs, evaluates, and explains paid/live data calls.

Core question:

> "When should an agent pay for this data source, and what signal value did it get back?"

This fits the hackathon because the core demo is not just data extraction. It is an agent making an economic decision about data.

## 2. Existing Actors To Use

### Primary Actor 1: Google Search Results Scraper

Use for:

- Discovering candidate sources
- Finding consensus around a thesis
- Finding competing tools/pages
- Capturing public search evidence

Why:

- Search is the "FIND" phase.
- It creates a visible source-selection trail.
- It gives the agent options before it pays/crawls deeper.

### Primary Actor 2: Website Content Crawler

Use for:

- Crawling selected pages
- Extracting clean Markdown/text
- Feeding the text into analysis
- Producing source-backed evidence tables

Why:

- The Actor is maintained by Apify.
- It is designed for LLM/RAG contexts.
- It can output clean content from docs, blogs, help pages, and sites.

## 3. What You Improve

Do not improve the crawler itself today. Improve the *operating layer* around it.

Add:

- Source reason: why this Actor was selected
- Expected signal: what the agent hoped to learn
- Cost proxy: pay-per-use or pay-per-result estimate
- Evidence yield: what useful information came back
- Signal-value score: did this source change the decision?
- Next action: crawl more, stop, compare, or build proof artifact

This becomes your unique layer:

> Actors retrieve data. Your agent judges whether that data was worth buying.

## 4. MVP Name

Use one:

- Paid Data Decision Ledger
- Actor Buyer Conscience
- Source Value Ledger
- Zero-to-One Data Buyer

Recommendation: **Paid Data Decision Ledger**. It is clear and demo-friendly.

## 5. Demo Flow

Input:

```json
{
  "question": "Is there evidence that agents need a data-buying judgment layer?",
  "arena": "paid web data and Apify Actors",
  "budget_usd": 1.00,
  "max_sources": 5
}
```

Flow:

1. Run Google Search Results Scraper for discovery.
2. Rank result URLs by likely signal value.
3. Select 2-3 pages to crawl.
4. Run Website Content Crawler.
5. Extract claims, signals, contradictions, and gaps.
6. Score each source:
   - relevance
   - freshness
   - credibility
   - novelty
   - actionability
7. Produce:
   - decision brief
   - paid-data ledger
   - proof artifact recommendation

## 6. Ledger Schema

```json
{
  "actor": "apify/google-search-scraper",
  "reason": "Discover candidate public sources for the thesis",
  "input_summary": "query='agents paid web data source selection'",
  "output_summary": "10 results, 4 relevant, 2 selected for crawl",
  "cost_proxy": "pay-per-use / platform usage",
  "signal_value": 4,
  "decision_impact": "Identified that most pages discuss tool access, fewer discuss purchase judgment"
}
```

## 7. Signal-Value Scoring

Score 1-5:

- `1`: no useful signal
- `2`: generic background only
- `3`: confirms known consensus
- `4`: reveals useful gap or contradiction
- `5`: changes the decision or directly defines the proof artifact

Weighted score:

```text
signal_value = relevance + credibility + novelty + actionability - cost_penalty
```

Keep it simple for the demo. Judges need to see the behavior, not a perfect model.

## 8. Output Report

Use this structure:

1. Executive answer
2. Sources bought/retrieved
3. Consensus map
4. Overlooked angle
5. Evidence table
6. Paid-data ledger
7. Recommended proof artifact
8. Caveats

## 9. Why This Is Better Than "Just Scraping"

A normal scraper says:

> "Here is the data."

Your improved agent says:

> "Here is why I paid for this data, what I learned, whether it was worth it, and what to build next."

That is closer to the event theme: agents that pay.

## 10. Connection To Apify Ideas Guidance

Apify's Actor ideas guidance suggests several suitable Actor categories:

- Web scrapers and crawlers
- SaaS API wrappers
- Open-source library wrappers
- MCP servers and AI tools
- AI agents

It also says suitable Actor jobs are background tasks with well-defined input/output, or request-response tools in standby mode.

This plan fits as an AI agent / MCP-style tool:

- Well-defined input: question, arena, budget
- Background execution: source discovery and crawling
- Well-defined output: brief, ledger, scored source list
- Clear user value: helps agents decide what data is worth buying

## 11. Build Order

### Version 0: Manual chain

- Run Google Search Scraper manually.
- Copy result URLs.
- Run Website Content Crawler manually.
- Paste outputs into analysis script.
- Generate ledger/report.

Fastest demo if Apify API setup is slow.

### Version 1: Python CLI wrapper

Files:

```text
app/main.py
app/apify_runs.py
app/source_scoring.py
app/report.py
sql/schema.sql
outputs/report.md
.env.example
```

### Version 2: Publish as Actor

Actor input:

```json
{
  "question": "string",
  "arena": "string",
  "budgetUsd": 1,
  "maxSources": 5,
  "seedUrls": []
}
```

Actor output:

```json
{
  "decisionBrief": "...",
  "ledger": [],
  "sourceScores": [],
  "proofArtifact": {}
}
```

## 12. Concrete Demo Script

Say:

> "I started with Apify's own Actor ecosystem. The obvious move is to chain Search and Website Content Crawler. But the missing piece is judgment. If agents are going to pay for data, they need to explain why they paid, what signal they got, and whether the purchase changed the decision. So I built a ledger-first wrapper: it discovers sources, buys/crawls evidence, scores signal value, and recommends the next proof artifact."

## 13. Safe Boundaries

Do:

- Public sources
- Official docs
- Marketplace pages
- Product pages
- Public articles
- Aggregate signals

Do not:

- Scrape private people
- Harvest contacts
- Use credential exports
- Make financial recommendations
- Claim surveillance or defense use
- Frame this as recruiting/job search

## 14. Immediate Next Step

Pick one of these build modes:

1. Manual chain for fastest demo.
2. Python CLI wrapper for strongest hackathon prototype.
3. Published Actor if mentors push for Actor creation.

Recommendation: **Python CLI wrapper first**, then publish only if time remains.

