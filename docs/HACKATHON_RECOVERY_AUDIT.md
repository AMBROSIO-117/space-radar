# Apify Hackathon Recovery Audit

Audit date: 2026-09-08. The owner recalls an Apify hackathon in July; the exact event identity, July dates, and participation status remain unverified pending the email search below.

## Purpose and evidence boundary

This audit answers three different questions:

1. **What was built?** Answerable from repository files and Git history.
2. **Was it truly run and submitted to the July Apify hackathon?** Not proven by this repository.
3. **What can be salvaged into a credible hackathon project?** Answerable as a recommendation, then testable through a real build and demo.

An artifact labeled “submission,” “live,” or “hackathon” is evidence of intent, not proof that an external submission, deployed Actor, judging entry, or live-data run occurred.

## Repository evidence reviewed

| Evidence | What it establishes | What it cannot establish |
| --- | --- | --- |
| `SUBMISSION.md` | A project description and two-minute demo script were drafted | That the form was sent or accepted |
| `actor-space-procurement-radar/src/main.js` | A custom Actor implementation exists | That this exact version was deployed or judged |
| `.actor/actor.json`, `INPUT_SCHEMA.json`, and `Dockerfile` | The Actor has Apify packaging, UI input schema, and a container recipe | That an Apify cloud build succeeded |
| Fixture data and `dryRun` | A deterministic credential-free demonstration path exists | Live collection or current evidence |
| Tavily integration | A live search path is implemented | A successful run, because no run ID/output is committed |
| n8n webhook integration | Optional delivery code exists | That an n8n workflow or Notion database exists |
| `presentation/` and `SUBMISSION.md` | Pitch assets exist | A recorded demo, attendee status, or organizer receipt |
| Git history | The initial project snapshot and later documentation commit exist | The full development timeline or July participation |

The repository has only two commits at this audit. The initial commit is dated June 20, 2026, and no Git remote is configured. No committed Apify Actor ID, build ID, run ID, Dataset URL, public Store URL, hackathon submission URL, organizer confirmation, or July email export was found.

## Complete change and artifact inventory

### Runtime product — strongest salvage value

| Entry | Purpose | Keep? | Required improvement |
| --- | --- | --- | --- |
| `actor-space-procurement-radar/src/main.js` | Builds queries, calls Tavily or fixtures, scores results, writes reports, optionally posts to n8n | Yes | Add automated tests; separate extraction from scoring; preserve source dates and claim provenance |
| `.actor/INPUT_SCHEMA.json` | Generates the Actor input form and validates basic types/ranges | Yes | Add examples and align defaults with tested demo behavior |
| `.actor/actor.json` | Declares Actor name, version, Dockerfile, README, and schema | Yes | Add the deployed Actor identity after a real deployment |
| `Dockerfile` | Builds the Node 20 Actor image | Yes | Verify with a clean container/cloud build |
| `package.json` | Defines Node requirement, Apify dependency, and start command | Yes | Pin/review dependencies and add test/lint scripts |
| `.env.example` | Documents secret names | Yes | Keep placeholders only; never add real credentials |

### Data and analytical method — valuable but incomplete

| Entry | Purpose | Keep? | Required improvement |
| --- | --- | --- | --- |
| `data/space_procurement_business_ontology.json` | Represents sellers, needs, buyers, signals, evidence, and actions | Yes | Validate concepts and keywords with domain practitioners |
| Keyword scoring in `src/main.js` | Produces an explainable 0–100 priority score | Yes, as baseline | Rename it a heuristic score; test false positives and avoid equating score with purchase probability |
| Fixture companies/sources | Makes the demo repeatable | Yes, clearly labeled | Capture expected output and explain that fixtures are hypotheses, not verified leads |
| Evidence/source ledger documentation | Encourages provenance and cost tracking | Yes | Make fields mandatory in runtime output, including publication/retrieval dates |

### Legacy prototypes — archive, do not market as one product

| Entry | Original exploration | Salvage |
| --- | --- | --- |
| `app/main.py` and `data/sample_sources.json` | Actor selection / paid-data decision radar | Salvage the value-ledger idea: why a source was purchased and whether it changed a decision |
| `app/vix_learning_radar.py` and `data/vix_fixture.json` | VIX education using Cboe context | Salvage only reusable parsing/report patterns; keep financial content outside this product |
| `outputs/` | Many brainstorming paths, templates, and generated reports | Treat as archive/research notebook; promote only current decisions into `docs/` |
| `presentation/` | Long and short pitch narratives | Rebuild after the deployed demo and evidence contract are real |

### Previous documentation change

The latest documentation commit added the analyst guide and linked it from the README. That guide contributed the data-to-intelligence model, repository map, technology roles, Codex workflow, Fraunhofer caveat, validation sprint, and proposed intelligence record. The present change deepens Codex mechanics, expands Git collaboration/recovery, and adds this evidence-based hackathon audit.

## Theme fit: participant-grade versus leisure-grade

Repository notes identify the event concept as **“Agents that Pay.”** A credible submission should therefore demonstrate an agent making or recommending an economic data-acquisition decision—not merely call an API inside an Actor.

### Current claim that is defensible

> A custom Apify Actor turns a narrow procurement question into ranked, source-linked hypotheses and stores reusable outputs.

### Current gaps that judges could expose

1. Live discovery uses Tavily, while Apify mainly hosts the custom program and stores results.
2. The “payment” or source-value decision is more explicit in the abandoned Actor Idea Radar than in the current procurement Actor.
3. Keyword occurrence can create confident-looking false positives.
4. Search snippets are treated as evidence without deeper retrieval or primary-source verification.
5. No automated test, deployed run identifier, public Actor URL, or recorded demo proves reproducibility.
6. The product names a seller but does not show a real participant interview or outcome.

### Strong salvage thesis

Combine only the best two ideas:

> **Procurement Evidence Radar** is an Apify Actor for a niche industrial seller. It chooses whether a candidate source is worth acquiring/crawling, records source cost and expected value, extracts dated evidence, and ranks hypotheses for human verification. Its ledger shows what data was used, why it was worth using, and whether it changed the next action.

This preserves the current DACH space-procurement use case and restores the “agent pays for useful data” mechanism. Do not add VIX, generic job search, broad “singularity,” or institutional themes to the demo.

## Participant-grade recovery plan

### Gate 0 — reconstruct the event facts before making claims

Recover and record:

- official event name, host, venue, and dates;
- challenge/theme wording and judging criteria;
- registration or acceptance confirmation;
- team name and participants;
- submission deadline and submission receipt;
- original repo, Actor, Dataset, slide, and video links;
- sponsor credits and their expiration/terms;
- organizer feedback, judging result, or follow-up.

Unknown facts must remain `UNKNOWN`; do not fill them from memory.

### Gate 1 — prove the artifact

- Add automated unit tests for query construction, deduplication, every score band, and report output.
- Run a clean Docker/Apify cloud build.
- Perform one fixture run and one controlled live run.
- Save non-secret proof: Actor URL/ID, build ID, run ID, timestamp, input, sanitized log, Dataset URL/export, and report output.
- Confirm a fresh clone can reproduce the fixture demo.

### Gate 2 — prove the intelligence method

- Retrieve full primary pages rather than relying only on search snippets.
- Store publisher, publication date, retrieval date, supported fact, inference, and contradiction.
- Ask a reviewer to audit five results without seeing the score first.
- Publish precision-at-five and the false-positive log; do not call it “accuracy” without labeled ground truth.

### Gate 3 — prove participant relevance

- Show the official criterion and the exact demo moment satisfying it.
- Explain why the Actor abstraction, Dataset, and key-value store are necessary.
- If “Agents that Pay” is confirmed, show a budget, a source-selection decision, recorded cost, information gain, and stop condition.
- Name one domain user and the decision they are trying to make.

### Gate 4 — prepare a truthful two-minute demo

```text
0:00–0:20  User and expensive decision
0:20–0:40  Why ordinary search results are not enough
0:40–1:10  Live Actor input and run
1:10–1:35  One evidence chain: source -> fact -> inference -> score -> next step
1:35–1:50  Data-cost/value ledger and human safeguard
1:50–2:00  Measured result, limitation, and next experiment
```

Use “prototype,” “heuristic,” and “candidate” where appropriate. Never imply real customers, live data, paid acquisition, submission, or judging if the proof is absent.

## Outlook recovery procedure

This coding environment has no configured Outlook/Microsoft mail connector, so it cannot inspect the inbox directly. The repository exposes an Outlook author address in Git metadata, but that provides no access to the mailbox.

Search Outlook yourself using several narrow searches rather than one broad keyword. Outlook search syntax varies by client, so use the available filters for sender, recipient, date, attachments, and subject together with these term groups:

```text
Apify
"Agents that Pay"
hackathon AND (Apify OR juggleHUB)
(registration OR registered OR ticket OR acceptance) AND Apify
(submission OR submitted OR deadline OR Devpost) AND Apify
(credit OR coupon OR voucher OR token) AND Apify
(winner OR judging OR feedback OR mentor) AND Apify
```

Focus the date window on June through August of the relevant year, then widen it if the year itself is uncertain. Check Inbox, Archive, Sent, Deleted Items, Junk Email, and conversation attachments. Sent mail may contain the only copy of a form response or project link.

For each relevant message, add one row to a private recovery ledger:

| Field | Example |
| --- | --- |
| Message date/time and timezone | `YYYY-MM-DD HH:MM UTC+02:00` |
| Direction | received / sent |
| From and to | organizer and participant addresses |
| Subject | exact subject |
| Evidence category | registration / acceptance / deadline / submission / credit / feedback |
| Factual claim supported | “Registration was accepted” |
| IDs or links | event, form receipt, Actor, Dataset, repository, video |
| Attachment saved | filename and private storage location |
| Repository-safe? | yes / no / sanitized-only |

Do not commit full `.pst`/`.ost` mailboxes, access tokens, magic login links, private attendee lists, QR tickets, coupon codes, or messages containing personal data. For repository proof, prefer a redacted text record containing the minimum fact, date, message subject, and a private evidence reference. Preserve the original privately.

After completing this search, replace each `UNKNOWN` event fact with either a cited record or `NOT FOUND AFTER SEARCH`. The latter is stronger and more honest than silently assuming participation. If a mail connector is later authorized, request a read-only search first and require confirmation before moving, deleting, replying to, or forwarding messages.

## Present-state verdict

**Salvageable prototype: yes. Proven July hackathon submission: no evidence in the repository. Participant-grade release: not yet.**

The fastest honest route is to recover event evidence, deploy and record one real Apify run, strengthen provenance, reintroduce the source-value ledger, test the heuristic, and demonstrate one user decision. Everything else is secondary.
