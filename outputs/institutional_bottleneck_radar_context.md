# Institutional Bottleneck Radar - Non-Job-Search Hackathon Context

Date: 2026-06-20
Event: Agents that pay hackathon, juggleHUB Berlin
Pivot note: This version intentionally avoids CVs, job search, recruiting, role matching, and candidate evaluation.

## 1. Working Thesis

Build an agent that pays for live web data to detect institutional bottlenecks and turn noisy public evidence into a concrete proof-of-need brief.

The agent takes:

- A sector, institution, or operational domain
- A decision question
- Optional seed URLs or keywords

It retrieves paid/live web data through Apify Actors, extracts signals of friction or demand, clusters them into bottleneck themes, and outputs:

- A bottleneck map
- Evidence table
- Data-source and payment ledger
- One recommended proof artifact or pilot to build next

This is professional/civic decision support. It is not surveillance, personal profiling, financial advice, cyber reconnaissance, or sensitive defense analysis.

## 2. One-Sentence Demo

"Give the agent a public-service or business-process domain; it buys live web evidence, identifies repeated operational bottlenecks, and recommends the smallest proof artifact that could validate the problem."

## 3. Best Hackathon Scope

Pick one narrow, public, non-sensitive domain. Good options:

- **Berlin coworking/event venue operations:** identify demand signals around hackathons, AI events, coworking pain points, venue discovery, and service gaps.
- **EU startup support infrastructure:** find recurring bottlenecks in grant discovery, accelerator applications, founder services, and market-entry support.
- **LATAM digital public-service infrastructure:** use only public pages, reports, and news to identify citizen-service friction, procurement gaps, or digitization bottlenecks.
- **Apify paid-web marketplace intelligence:** analyze Actor Store categories, pricing models, use cases, and gaps in agent-ready paid data.
- **Data-team operating infrastructure:** identify common bottlenecks in data documentation, metric ownership, process mining, and orchestration from public case studies and docs.

Recommendation for today: **Apify paid-web marketplace intelligence** or **Berlin AI event/coworking bottleneck radar**. Both are safe, demo-friendly, event-relevant, and easy to ground with live web data.

## 4. Strong Demo Concept

### Paid-Web Actor Opportunity Radar

Question:

"Where are there repeated demand signals for paid web data agents, but weak existing Actor coverage or unclear pricing?"

Inputs:

- Apify Store category pages
- Actor pages for search/crawling/social/maps/jobs/company data, excluding personal-contact harvesting
- Public event description from Agents that Pay
- Optional founder/community pages or Apify docs

Output:

- Top 5 underserved agent/data opportunities
- Evidence table showing source URL, demand signal, existing actor coverage, pricing model, and gap
- Recommended Actor or chained-agent prototype to build
- Ledger of paid/live calls

Why this fits the hackathon:

- It directly studies the paid web.
- It uses Apify as both source and infrastructure.
- It avoids job search and personal profiling.
- It can be demoed even if no private data is available.

## 5. OSINT Framework Adaptation

Use OSINT as disciplined public-source mapping, not as personal investigation.

### Requirement

Define the decision:

- "Which bottleneck is worth prototyping?"
- "Which market has repeated paid-data demand?"
- "Which public-service workflow shows visible friction?"
- "Which dataset would an agent rationally pay for?"

### Sources

Use public, non-sensitive sources:

- Official websites
- Public documentation
- Public marketplaces
- Public event pages
- News and industry pages
- Reviews only in aggregate, not for individual profiling
- Public reports and case studies
- Public forums only for theme extraction, not personal identification

Avoid:

- Scraping private individuals
- Contact harvesting
- Credential/account exports
- Sensitive defense data
- Financial/investment recommendations
- Anything framed as background checking

### Collection

Useful Apify Actors:

- Google Search Results Scraper: discover relevant pages.
- Website Content Crawler: crawl official pages, docs, and case studies.
- Google Maps Scraper: only for aggregate venue/service patterns, not individual people.
- Apify Store pages / Actor metadata extraction: map paid-data offerings and pricing models.
- Reddit/X/social actors only if used for aggregate public sentiment and with careful scope.

### Processing

Extract:

- Bottleneck statements
- Affected stakeholder
- Evidence source
- Frequency or recurrence signal
- Existing solution/data availability
- Pricing or access model
- Confidence and caveats

### Analysis

Rank bottlenecks by:

- Evidence strength
- Repetition across sources
- Freshness
- Data availability
- Paid-web fit
- Demo feasibility
- Ethical/safety risk

### Output

The report should answer:

- What public evidence indicates a bottleneck?
- Why would an agent pay for this data?
- Which sources were used?
- What is the smallest useful prototype?
- What are the caveats and non-claims?

## 6. Minimal Ontology

Core entities:

- `Domain`: sector or operating area under review
- `Institution`: public body, company, platform, or service ecosystem
- `Source`: URL, title, date, actor run, credibility, freshness
- `Signal`: public evidence of demand, friction, cost, delay, confusion, or unmet need
- `Bottleneck`: clustered signal group with root-cause hypothesis
- `DatasetNeed`: data an agent would retrieve or pay for
- `PaidAccess`: actor, pricing model, cost proxy, run limit
- `ProofArtifact`: prototype, dashboard, dataset, brief, workflow, or actor spec
- `DecisionBrief`: final human-readable output
- `LedgerEntry`: what was retrieved, why, cost proxy, and signal value

## 7. Minimal SQL Model

Use SQLite or DuckDB.

```sql
domains(id, name, question, created_at)
actor_runs(id, actor, input_json, cost_usd, status, started_at, ended_at)
sources(id, url, title, run_id, retrieved_at, credibility, freshness)
signals(id, domain_id, source_id, signal_text, stakeholder, signal_type, confidence)
bottlenecks(id, domain_id, name, hypothesis, severity, evidence_count)
signal_bottlenecks(signal_id, bottleneck_id)
dataset_needs(id, bottleneck_id, data_needed, access_path, paid_web_fit)
ledger_entries(id, run_id, actor, reason, input_summary, output_summary, cost_proxy, signal_value)
artifacts(id, bottleneck_id, artifact_type, spec, priority)
```

## 8. Demo Flow

1. User enters a domain and question.
2. Agent runs discovery search.
3. Agent crawls 2-5 selected pages.
4. Agent extracts signals into structured JSON.
5. Agent clusters signals into bottlenecks.
6. Agent maps bottlenecks to paid dataset needs.
7. Agent recommends one proof artifact.
8. Agent prints a ledger of every Actor/data call.
9. Agent generates Markdown report.

## 9. Recommended First Demo

### Demo: Apify Actor Opportunity Radar

Question:

"What paid-web data opportunity should a builder prototype today for agents that need to buy data?"

Data sources:

- Apify Store
- Apify pricing model docs
- Apify Actor pages for Google Search, Website Content Crawler, Maps, social, company/data categories
- Event description

Output:

- Existing paid-data categories
- Gaps where agents need better source discovery, evaluation, or ledgering
- Prototype recommendation: an "Actor buyer agent" that chooses, runs, and records paid data calls
- Evidence and ledger

Possible winning angle:

"Instead of building one more scraper, we build the agent that decides what data is worth paying for."

## 10. Alternative Demo: Berlin AI Event Infrastructure Radar

Question:

"What operational bottlenecks do Berlin AI/community events face, and what paid/live data would help organizers solve them?"

Data sources:

- Public event listings
- Venue pages
- Google Maps venue data
- Public community calendars
- Event descriptions and agenda pages

Output:

- Bottlenecks: venue discovery, agenda fit, sponsor matching, attendee skill mix, follow-up workflows
- Dataset needs: venue capacity, event categories, organizer contact pages, schedule density, public attendance signals
- Proof artifact: event intelligence dashboard for organizers

This option is event-relevant and highly demoable, but it should avoid scraping personal attendee data.

## 11. Positioning From Your Existing Materials

Keep:

- Ontology and semantic-layer framing
- Value engineering method: elicit, structure, translate, verify, adopt
- "Own the orchestration layer" from the n8n story
- Paid-data ledger from the directive PDF
- Institutional bottleneck radar as long-term thesis

Remove:

- CV/profile claim comparison
- Target role matching
- Job search scoring
- Cover-letter/application workflows
- Candidate credibility evaluation
- Palantir recruiting/interview framing

Safe positioning:

"This is an agentic analyst for public operational bottlenecks. It pays for live data, shows its ledger, and recommends the smallest proof artifact that would validate whether the bottleneck is real."

## 12. Hackathon Pitch

"Agents will not just browse the web. They will decide when data is worth paying for. Institutional Bottleneck Radar is a small agent that starts with a domain question, buys live web evidence through Apify, clusters repeated friction signals, and recommends the smallest proof artifact to validate the opportunity. The key feature is not only the answer; it is the ledger showing what the agent paid for, why it paid, and what signal value it got back."

## 13. Build Decision

Build the chained Actor MVP, not a brand-new scraper.

Best stack:

- Python CLI
- Apify API/client calls
- SQLite or DuckDB
- Markdown report
- Mermaid architecture diagram
- `.env.example` only

## 14. Needed From You

To proceed without job-search context, provide:

1. The domain you want to investigate:
   - Apify Actor opportunity radar
   - Berlin AI event infrastructure
   - LATAM public-service bottleneck
   - Data-team operating infrastructure
   - Other
2. One decision question.
3. Any seed URLs you want included.
4. Apify API token or confirmation that Actor calls will be run manually.
5. Paid-data budget for the demo.
6. Preferred output: Markdown report, PDF, CLI demo, or small web app.

Do not upload passwords, credential exports, bank files, private identity documents, or anything that would make the demo about a person rather than an institution or public domain.

