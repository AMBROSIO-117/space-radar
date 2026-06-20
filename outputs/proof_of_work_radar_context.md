# Proof-of-Work Radar - Hackathon Context Brief

Date: 2026-06-20
Event: Agents that pay hackathon, juggleHUB Berlin
Primary directive: `/Users/nutri-012/Downloads/proof_of_work_radar_codex_directive.pdf`

## 1. Working Thesis

Build a narrow agent that turns professional profile claims into a defensible proof-of-work plan.

The agent takes:

- A CV or LinkedIn/profile text
- A target role, company, or sector
- Optional personal artifacts such as project writeups, public repos, dashboards, notes, and application material

It retrieves paid or live web data through Apify Actors, extracts what the market actually asks for, compares that against the profile claims, and produces:

- A credibility-gap report
- A next proof artifact to build
- An evidence table
- A paid-data ledger showing actor, reason, input, output, cost proxy, and signal value

This should be framed as professional decision support, not as defense intelligence, surveillance, background checking, financial advice, or sensitive targeting.

## 2. One-Sentence Demo

"Paste a CV and a target role; the agent buys or retrieves live role/company/sector data, identifies which claims are under-proven, and recommends the single best proof artifact to build next."

## 3. Best Hackathon Scope

Use one target and one profile:

- Profile: Henry Galindo CV from `/Users/nutri-012/Downloads/memory/CV_Henry_Galindo_1.pdf`
- Target option A: Junior Value Engineer / Ontology Builder / Forward Deployed role
- Target option B: Junior Data Engineer - Energy Transition, from the saved Data Berlin HTML
- Target option C: n8n AI PM / data automation role, using the existing DACH Job Search OS and n8n story

Recommendation: choose target option A only if you have a concrete job URL today. Otherwise choose target option B or n8n because your local files already provide role/application context.

## 4. What the Local Files Add

### Directive PDF

The PDF defines the ontology, SQL model, build order, and success criteria. The core build order is:

1. Hard-code one target.
2. Paste CV text and extract claims into JSON.
3. Call one or two Apify Actors for job/company/source pages.
4. Extract demand signals.
5. Compare claims versus demand.
6. Generate a report plus ledger.

### CV

Strong extractable claims:

- Junior value engineer / business analyst positioning
- Data Value Chain framework at KWS
- Ontology-driven team wiki / single source of truth
- SQL, CTEs, window functions, Power BI, DAX, Power Query
- SAP S/4HANA, Celonis object-centric process mining, SAP Analytics Cloud
- Stakeholder delivery across Scout24 data and AI teams
- Product ownership, Jira backlog, generative search benchmarking
- n8n, dbt, LLM workflow, API scripting, semantic-layer thinking

Likely credibility gaps:

- "Ontology" claim needs a public artifact, not only CV language.
- "LLM-driven automation" needs a concrete workflow or repo.
- "Value measurement framework" needs a reproducible sample scorecard.
- SQL/Python skill needs an inspectable project with input, query/code, output, and explanation.
- Palantir/Value Engineer positioning needs role-specific evidence from live demand data.

### DACH Job Search OS

This is useful because it already defines a reusable F2T2EA-style job pipeline:

- FIND: score role fit
- FIX: draft application material
- TRACK: update tracker
- TARGET: complete form package
- ENGAGE: submit
- ASSESS: evaluate outcome

For the hackathon, do not over-index on the military wording. Use it as a civilian decision workflow: discover, constrain, observe, prioritize, act, evaluate.

### n8n Story

Best proof narrative:

"Own the orchestration layer, not just the data inside it."

This can become the proof artifact recommendation if the target role asks for automation, data operations, process mapping, or AI workflow ownership.

Suggested artifact:

- A small public workflow report showing: input job URL -> scraped job facts -> extracted demand signals -> CV claim comparison -> recommended proof artifact.

### PLTR Files

Useful positioning themes:

- Value Engineering: elicit, structure, translate, verify, adopt
- Ontology thinking: object, property, link, source, owner, workflow
- Interview prep: real problems, clarifying questions, trade-offs, existing systems, pragmatic working solutions

Use this as language and structure, not as the hackathon's subject matter. Keep the MVP civilian and professional.

### Strategy Package / Meridian Vault

Most of this is personal operating doctrine, account organization, and compartmentalization. It is not core hackathon material.

Useful constraints only:

- Keep secrets out of the repo.
- Use `.env.example` for keys, never real tokens.
- Preserve a ledger of paid data calls.
- Keep professional/public identity separate from private account-security material.

I intentionally did not read or use credential-like exports such as the Proton Pass CSV.

## 5. OSINT Framework Adaptation

Use OSINT as a disciplined source map, not as "find everything about a person."

### Requirement

What decision are we trying to support?

Example: "What proof artifact should Henry build next to credibly target a Junior Value Engineer role?"

### Sources

Use public, role-relevant, non-sensitive sources:

- Job postings
- Company career pages
- Company product pages
- Public case studies
- Public documentation
- Public GitHub/repo/project artifacts from the candidate if provided
- Optional sector pages and market reports

Avoid:

- Private social scraping of individuals
- Contact harvesting
- Credential/account files
- Sensitive defense data
- Unverified claims from random blogs when official pages are available

### Collection

Use Apify Actors for paid/live data:

- Google Search Results Scraper for discovering role/company pages
- Website Content Crawler for company pages, career pages, and documentation
- LinkedIn Jobs Scraper only if needed and compliant with the event/tool setup
- Optional Reddit/X/social actors only for aggregate market signal, not personal surveillance

### Processing

Extract:

- Role demand: required skills, preferred skills, domain language, seniority signals
- Company demand: product vocabulary, buyer problems, operating principles
- Sector demand: repeated concepts across multiple pages
- Candidate claims: skills, domain claims, achievements, evidence type

### Analysis

Compare each claim against demand:

- Matched and evidenced
- Matched but weakly evidenced
- Overstated
- Missing
- Adjacent but needs translation

### Output

The report should answer:

- What does the target market actually ask for?
- Which profile claims are credible?
- Which claims need proof?
- What one artifact should be built next?
- Which paid/live data calls were used and why?

## 6. MVP Data Model

Use SQLite or DuckDB.

Tables:

- `profiles(id, source, raw_text, created_at)`
- `targets(id, target_type, target_name, question)`
- `actor_runs(id, actor, input_json, cost_usd, status, started_at, ended_at)`
- `sources(id, url, title, run_id, retrieved_at, credibility, freshness)`
- `claims(id, profile_id, claim, skill, evidence_strength, evidence_text)`
- `demands(id, target_id, demand, skill, source_id, importance)`
- `gaps(id, claim_id, demand_id, severity, reason)`
- `artifacts(id, gap_id, project_spec, priority)`

## 7. Demo Flow

### CLI or notebook flow

1. Load sample CV text.
2. Load target prompt:
   - `target_type = role`
   - `target_name = Junior Value Engineer`
   - `question = What proof artifact should this candidate build next?`
3. Run Actor 1:
   - Google Search Results Scraper query: `"Junior Value Engineer" data ontology AI role requirements`
4. Run Actor 2:
   - Website Content Crawler over one selected role/company/career page
5. Extract demand signals into JSON.
6. Extract CV claims into JSON.
7. Compare and rank gaps.
8. Generate Markdown report.
9. Print ledger table.

### Demo report structure

- Executive answer
- Target demand summary
- Candidate claim map
- Gap matrix
- Recommended proof artifact
- Evidence table
- Paid-data ledger
- Caveats

## 8. Suggested First Proof Artifact

Recommended artifact:

**"Ontology-backed Job Fit Radar"**

Build a small public demo that:

- Takes one job post and one CV
- Extracts claims and demands
- Stores both in SQLite
- Produces a gap matrix
- Recommends a next artifact
- Shows the data lineage and cost ledger

Why this is strong:

- It proves the exact skill claimed: semantic-layer thinking.
- It uses live web data.
- It has a clean paid-web ledger.
- It is easy to demo in under three minutes.
- It avoids sensitive data.

## 9. Hackathon Pitch

"Most career tools rewrite your CV. That is cheap. Proof-of-Work Radar asks what your target market actually demands, compares it to the claims you are making, and tells you what proof to build next. It uses paid/live web data as an external benchmark, keeps a ledger of every data call, and produces a defensible evidence map rather than generic advice."

## 10. Files Reviewed or Inventoried

Reviewed directly:

- `proof_of_work_radar_codex_directive.pdf`
- `CV_Henry_Galindo_1.pdf`
- `DACH_JobSearch_OS.md`
- `n8n_Story_KWS_Interview.md`
- `Operator_Foundation_PLTR_DefTech_Archive.docx`
- `PLTR Early Careers.pdf`
- Strategy package README, thesis, playbook, execution checklist
- Strategy package CSV inventories
- Downloads file inventory and PLTR filename search

Inventoried but not deeply used:

- Cover letters and recommendation letters
- `moneyball-2011.pdf`
- media files and zip archives
- duplicate vault files
- account/security exports

## 11. Information Still Needed From You

Upload or paste these, in priority order:

1. One target job URL or saved job post text for the actual demo.
2. Your preferred demo target: Palantir/Value Engineer, n8n/AI PM, Data Engineer, or another role.
3. Apify API token or confirmation that you will run the paid Actor calls manually in your account.
4. A public artifact you want the agent to evaluate, such as GitHub repo, Notion page, dashboard screenshot, workflow JSON, or project writeup.
5. The exact judge-facing demo story: career proof radar, company/role radar, or broader institutional bottleneck radar.
6. Any budget constraint for paid Actor runs.
7. Whether the final output should be Markdown only, PDF, or a tiny web app.

Do not upload passwords, credential exports, private account ledgers, bank documents, or anything you would not want in a hackathon repo.

## 12. Immediate Build Decision

Build the chained Actor MVP, not a brand-new Actor, unless mentors strongly push otherwise.

Reason:

- The event rewards a working demo.
- The directive is already an orchestration and comparison problem.
- The differentiated part is the ontology, ledger, and proof artifact recommendation, not scraper engineering.

Best stack:

- Python CLI
- Apify API/client calls
- SQLite or DuckDB
- Markdown report
- Mermaid architecture diagram
- `.env.example` only

## 13. External Sources Checked

- OSINT Framework: https://osintframework.com/
- Apify Store: https://apify.com/store
- Apify Actor pricing models: https://docs.apify.com/platform/actors/running/actors-in-store
- Apify Python SDK overview: https://docs.apify.com/sdk/python/docs/overview
- Apify MCP integration docs: https://docs.apify.com/platform/integrations/mcp

