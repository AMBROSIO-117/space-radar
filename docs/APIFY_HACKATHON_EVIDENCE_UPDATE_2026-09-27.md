# Space Radar: hackathon evidence update (27 September 2026)

This is a dated correction to `docs/HACKATHON_RECOVERY_AUDIT.md`. It separates the recovered implementation, the original event's requirements, and the available external records. The earlier audit remains a useful inventory, but its July date and Outlook-access limitation are superseded here. The final recovery note below supersedes this document's earlier statement that the shared Notion page contents were unavailable.

## What the records establish

- The "Agents that Pay" hackathon took place in Berlin on **20 June 2026**, according to event emails dated 16, 19, and 20 June in the owner's connected Outlook mailbox. The September 8 audit's reference to a July event is incorrect for this event.
- The 20 June organizer email, "Information from the opening talk," asked participants to build an agent that pays for web data and uses **at least one Apify Actor as its live data source**. A working demo, public repository or project link, and two-minute demonstration were submission requirements. The submission cutoff was 15:30 local event time.
- A 20 June Notion notification says Mikel Mangold shared a page named "Hackathon Apify". A separate notification records the import of `space_radar_business_ontology.md`. These are evidence of team materials, not proof of a completed submission.
- The owner's 10 September message, "Reconnecting after the Apify hackathon — Space Radar," describes working with Mikel and explicitly says Mikel **may** have shared a submission through a Notion form; it calls the recovered repository an incomplete prototype. The searched connected Outlook mailbox contains that outbound message but no identified reply from the recipient. This does not establish the state of other accounts or channels.
- The connected Notion account currently opens "Ambrosio's Space" and its ATLAS project. The historic "Hackathon Apify" page remains unavailable to this live connection, but a 27 September Notion HTML/CSV export of that page was subsequently supplied and inspected. Its contents are summarized in the final recovery note below; the event-day state and submission status remain unknown.

**Defensible project description:** "I participated in the June 20 Agents that Pay hackathon in Berlin, worked with a teammate on Space Radar, and preserved a space procurement intelligence prototype and ontology. I am reconstructing its live-data chain and cannot yet verify a final submission or judged demo."

## What the current code does, and what the chart promises

The diagram in `docs/ANALYST_CODING_AND_CODEX_101.md` is a good system map, but its last steps are a proposed review loop, not a verified implementation. In `actor-space-procurement-radar/src/main.js`, `dryRun=true` uses three authored examples. In live mode the Actor calls Tavily's search API; there is no call to a *second* Apify Actor to acquire live data. The code deduplicates exact URL strings, assigns keyword weights, ranks leads, and writes dataset rows and a Markdown report. It can POST the output to an n8n webhook **before** any human review. It does not persist a human review decision, outcome feedback, a primary-source snapshot, or a calibrated confidence measure. `INSIGHTS.md` currently receives the same report as `REPORT.md`.

Running a custom Actor on Apify would demonstrate Apify packaging; by itself it would not prove that the event's "Apify Actor pulling live data" requirement was met. The recovered source cannot rule out an unpreserved event-day version or a different live Actor in the teammate's materials.

## Evidence and decision register

| Claim or asset | Status at this review | What would change the status |
| --- | --- | --- |
| Event was on 20 June | Supported by organizer and registration emails | None needed for ordinary description |
| User worked on Space Radar with Mikel | Supported by the owner's contemporaneous follow-up and Notion share; independent team confirmation not recovered | Shared page or teammate's project records |
| Submission accepted / demo judged / prize awarded | **Unverified** | Form receipt, organizer record, public submission link, demo recording |
| Current Actor has live Apify Actor as its source | **Not supported by recovered code** | Source code and run records showing a live Actor invocation |
| Current Actor runs in dry mode | Previously reported in the September 8 documentation work; not re-run in this evidence update | Reproduce against a fixture and retain the output |
| Live procurement intelligence is reliable | **Unverified** | Dated primary sources, reproducible run, analyst review, outcome validation |
| Shared hackathon Notion page content | **Recovered from an owner-provided Notion HTML/CSV export on 27 September**; the live page remains inaccessible to this connection | Original revision or event-day snapshot, if a date-specific claim is needed |

## Salvage decision

**Keep** the Actor packaging, input/output schemas, ontology, evidence-ledger idea, and the narrow procurement question. **Treat** the keyword scores as a transparent triage baseline, not objective confidence or purchasing likelihood. **Separate** the Python VIX and other unrelated prototypes from the hackathon story. To make a credible participant-grade retrospective, retain an actual live Apify Actor source and its timestamped run ID if recovered, link each lead to a primary source, log facts separately from inferences, record a human review decision, and show one end-to-end two-minute example. If the original event submission cannot be recovered, label the new result as a **post-hackathon continuation**, with its own date.

The owner has decided to stop contacting Apify about the missing response. This record does not send or schedule a follow-up.

## Cross-project boundary

The connected Notion ATLAS page is a **separate** miltech intelligence system, with 8 Sources, 11 Entities, 8 Signals, and 1 Brief at this review. The 8 source rows have no stored raw capture or content hash recorded in Notion. It offers a useful Sources → Entities → Signals → Briefs ontology, but it is not evidence that the hackathon entry contained those records. Keep NYY baseball analysis separate too: it is a new research intake, with no NYY repository accessible in the connected GitHub installation at this review; a GitLab repository may exist outside this connection.

## Source pointers

- Repository: `docs/ANALYST_CODING_AND_CODEX_101.md`, `docs/HACKATHON_RECOVERY_AUDIT.md`, `actor-space-procurement-radar/src/main.js`, `SUBMISSION.md` (a draft).
- Outlook, connected account: 20 June "Information from the opening talk"; 20 June "Page shared with you: Hackathon Apify"; 20 June ontology import notice; 10 September "Reconnecting after the Apify hackathon — Space Radar".
- Notion, current connection: "ATLAS — Miltech Intelligence OS" and its Sources, Entities, Signals, Briefs databases. Historic shared page ID `385bd139-e501-801c-87e3-e887b5a802e8` could not be fetched live; its owner-provided export is preserved separately.

This update summarizes private records without copying email addresses, message bodies, tokens, or event coupon codes into the repository.

## Final recovery note: supplied Notion export (27 September 2026)

The owner supplied `2c159ab4-55a8-46fa-a334-29c2907cf0d5_ExportBlock-d6a863b3-e5c4-4fef-a86e-50e8e1c3d02b.zip` (SHA-256 `ff852f22a5a23b31395678aa563850de022e9cd5620c41e8f339354158198a2d`). The 15-entry export includes the actual "Hackathon Apify" page, `space_radar_business_ontology`, a short government-grants prompt page, and a YouTube-example database with one CSV and 11 record pages (10 videos plus a mistaken header row). The export's ZIP timestamps show the export, **not** when each page section was written. The shared page may have been edited after the event.

Recovered design: a DACH thermal-vacuum-testing lead question; bilingual discovery queries and candidate companies; a **proposed** chain of `apify/google-search-scraper` → `apify/website-content-crawler` → evidence-backed scored lead brief; a 25/20/20/15/10/10 scoring plan; four proposed Notion databases; and a two-minute demo script. It lists an Apify console Actor integrations URL ending in `RlotS7TggwW1eUj3d`, which is a pointer, not an Actor source or run record. The YouTube CSV shows an example collection with 10 actual video rows, and no run ID, crawl receipt, or procurement lead verification. "Submission Fit" and sample lead tables in the page are plans written in the future tense.

**Updated evidence status:** The planning page and ontology are now **recovered and preserved**. The Actor source associated with that console URL, event-day live run, public submission link, and judged demo are **still not recovered**. The existing JavaScript Actor in this repository remains a distinct recovered prototype using Tavily in live mode. Do not claim the proposed two-Actor chain ran or that the draft was submitted. The owner has ended this recovery pass and does not want further contact with Apify. A private canonical archive of the supplied ZIP and its contents is the portable handoff.
