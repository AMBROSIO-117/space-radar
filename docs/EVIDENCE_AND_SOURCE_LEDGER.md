# Evidence And Source Ledger

## Project Decision Trail

The project began as a broader OSINT / proof-of-work radar concept and moved through several possible directions:

1. Job/proof-of-work radar.
2. Zero-to-one / institutional bottleneck radar.
3. VIX Learning Radar using Cboe data.
4. Final direction: Space Procurement Signal Radar.

The final direction was chosen because it is:

- Concrete.
- Sales/procurement-oriented.
- Demoable with 1-5 leads.
- Compatible with Apify Actor requirements.
- Useful for a forward deployed analyst workflow.

## Current Main Artifacts

| Artifact | Path |
| --- | --- |
| Actor source | `actor-space-procurement-radar/` |
| Single source of truth | `docs/SINGLE_SOURCE_OF_TRUTH.md` |
| Demo runbook | `docs/DEMO_RUNBOOK.md` |
| Business ontology | `outputs/space_radar_business_ontology.md` |
| Technical ontology | `outputs/space_radar_technical_ontology.md` |
| Machine-readable ontology | `data/space_procurement_business_ontology.json` |
| Full presentation source | `presentation/space_radar_full_presentation.md` |
| 5-slide pitch | `presentation/space_radar_5_slide_live_pitch.md` |

## External Technologies

| Technology | Use |
| --- | --- |
| Apify | Actor runtime, dataset, key-value store |
| Tavily | Optional live web search API |
| n8n | Optional workflow handoff to Notion/CRM/email |
| Notion | Optional human-facing lead database |
| LLM | Helps transform plain-language seller prompt into Actor input |

## Legacy Artifacts

These remain useful background but are not the current submission:

| Artifact | Path |
| --- | --- |
| VIX Learning Radar | `app/vix_learning_radar.py` |
| VIX objective note | `outputs/vix_learning_objectives_live_vs_trailing.md` |
| Apify actor idea radar | `app/main.py` |
| OSINT/proof-of-work context | `outputs/proof_of_work_radar_context.md` |

