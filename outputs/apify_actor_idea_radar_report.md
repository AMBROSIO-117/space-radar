# Apify Actor Idea Radar - Demo Report

## Question

What public signals suggest builders need better ways to decide which Apify Actor is worth paying for?

## Arena

Apify Actor marketplace and paid web data

## Executive Answer

The buildable opportunity is not another scraper. It is a small decision layer that helps an agent choose which Actor is worth paying for, then records whether the returned evidence changed the decision. The strongest signal came from `Website Content Crawler`: The Actor retrieves useful content, but it does not decide whether the crawl was worth paying for.

## Evidence Table

| Source | URL | Actor | Best score | Usefulness |
| --- | --- | --- | --- | --- |
| Apify Actor Ideas | https://apify.com/ideas | provided-context/manual-source | 19 | very useful |
| Website Content Crawler | https://apify.com/apify/website-content-crawler | apify/website-content-crawler | 20 | very useful |
| Google Search Scraper | https://apify.com/apify/google-search-scraper | apify/google-search-scraper | 19 | very useful |

## Top Signals

| Type | Signal | Source | Score | Usefulness |
| --- | --- | --- | --- | --- |
| actor_choice_gap | The Actor retrieves useful content, but it does not decide whether the crawl was worth paying for. | Website Content Crawler | 20 | very useful |
| marketplace_signal | There are many possible Actor categories, which creates a source-selection problem for builders. | Apify Actor Ideas | 19 | very useful |
| llm_context_need | The Actor is already positioned for feeding AI models, which makes it a strong candidate for evidence collection. | Website Content Crawler | 19 | very useful |
| actor_choice_gap | Search discovery produces candidate sources, but the agent still needs a ranking method for what to crawl next. | Google Search Scraper | 19 | very useful |
| proof_artifact | A useful meta-tool would help builders choose an Actor idea and explain why it is worth building or running. | Apify Actor Ideas | 18 | very useful |

## Paid-Data Ledger

| Actor | Reason | Input | Output | Cost proxy | Signal value |
| --- | --- | --- | --- | --- | --- |
| provided-context/manual-source | Seed the demo with known Apify idea context before API wiring | Apify Actor ideas page | Actor categories and idea framing | free provided context | 4 |
| apify/website-content-crawler | Representative crawler for source extraction in LLM workflows | https://apify.com/apify/website-content-crawler | Crawler capability and LLM/RAG positioning | pay per usage when run on Apify | 5 |
| apify/google-search-scraper | Representative discovery Actor for finding candidate sources | query about Apify Actor selection and paid data | Candidate sources to rank and crawl | pay per usage when run on Apify | 4 |

## Recommended Proof Artifact

Build a **Paid Data Decision Ledger**:

- User enters a question.
- Agent discovers possible sources.
- Agent chooses one or two Apify Actors.
- Agent records why each Actor was used.
- Agent scores source value by relevance, freshness, credibility, and actionability.
- Agent generates a short decision brief with caveats.

## Caveats

- This demo uses seeded source records so it can run without an Apify token.
- The next step is to replace `data/sample_sources.json` with real Actor outputs.
- This does not recommend trades, scrape private people, or make background-check claims.
