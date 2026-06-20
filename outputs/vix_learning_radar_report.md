# VIX Learning Radar - Demo Report

Generated: 2026-06-20T08:49:52Z

Mode: `dry-run-fixture`

## Demo Question

Using public Cboe data and at least one Apify Actor, what can a beginner learn about VIX volatility regimes without broker credentials or paid market-data subscriptions?

## Clear Objective

Help a beginner answer: **"What volatility regime are we in, how unusual is it versus trailing VIX history, and which official context explains what that means?"**

The agent should produce an educational brief, not a trade recommendation.

## Executive Answer

The useful beginner artifact is not a trading signal. It is a **VIX Learning Radar**: a small educational agent that pulls Cboe context pages with Apify, reads free public VIX history, labels volatility regimes, and explains what changed without recommending trades.

Latest available VIX close in the dataset: **16.4** on **2026-06-18**, labeled **normal**. The 30-day average is **19.69**.

## Cboe Context Signals From Apify Crawl

| Signal type | Source | Evidence | Score |
| --- | --- | --- | --- |
| risk_clarity | Cboe Volatility Index | Found terms: risk, portfolio, unique characteristics | 5 |
| market_structure | Cboe Volatility Index | Found terms: futures, options, index, methodology | 5 |
| market_structure | Historical Data for Cboe VIX Index | Found terms: futures, options, index | 5 |
| data_access | Historical Data for Cboe VIX Index | Found terms: historical data, datashop, updated daily | 5 |
| education_need | Cboe Volatility Index | Found terms: education, faq | 4 |

## Largest Historical VIX Closes

| Date | Close | Regime |
| --- | --- | --- |
| 2020-03-16 | 82.69 | crisis |
| 2020-03-18 | 76.45 | crisis |
| 2020-03-17 | 75.91 | crisis |
| 2025-04-07 | 46.98 | crisis |
| 2024-08-05 | 38.57 | crisis |
| 2026-05-22 | 20.02 | stressed |
| 2026-05-26 | 19.78 | normal |
| 2026-06-12 | 19.44 | normal |
| 2026-05-21 | 19.2 | normal |
| 2026-06-11 | 18.91 | normal |

## Optional Tavily Discovery

Not used in this run. Add `--tavily` with `TAVILY_API_KEY` to include search discovery.

## Paid / Live Data Ledger

| Data source | Reason | Input | Output | Cost proxy | Signal value |
| --- | --- | --- | --- | --- | --- |
| apify/website-content-crawler | Pull live Cboe educational/context pages | https://www.cboe.com/tradable-products/vix/, https://www.cboe.com/tradable-products/vix/vix-historical-data | 2 crawled items | Apify usage / hackathon credits | Provides source-backed context for the report |
| Cboe public CSV | Load free historical VIX closes | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv | 33 daily rows | $0, no credentials | Provides the numeric regime evidence |

## What This Gets Done

- Gives a beginner a safe starting point for Cboe data.
- Separates education from trading advice.
- Demonstrates an Apify Actor pulling live web context.
- Produces a concrete report and ledger in under two minutes.

## Caveats

- This is not investment advice.
- This does not place trades or connect to a broker.
- The VIX CSV is public historical data and may be delayed or revised by Cboe.
- For live options/futures analytics, Cboe DataShop, LiveVol, or licensed market-data products may require payment or credentials.
