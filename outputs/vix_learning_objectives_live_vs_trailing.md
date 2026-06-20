# VIX Learning Radar - Objective

## One-Sentence Goal

Help a beginner answer: **What volatility regime are we in, how unusual is it versus trailing VIX history, and which official context explains what that means?**

## What The Agent Gets Done

The agent turns a scary market-data topic into a beginner-safe learning brief.

It does not predict markets, recommend trades, connect to a broker, or require paid Cboe credentials.

## Live Data

Live data means the agent pulls current web context during the demo.

For the hackathon, the required live-data step is:

```text
Apify Actor: apify/website-content-crawler
Target pages:
- https://www.cboe.com/tradable-products/vix/
- https://www.cboe.com/tradable-products/vix/vix-historical-data
```

This gives the demo a real Apify Actor run and a source trail.

## Trailing Data

Trailing data means historical observations used to compare today's/latest available value against the past.

For this project:

```text
Cboe VIX historical CSV:
https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv
```

The script labels simple regimes:

| VIX close | Label |
| --- | --- |
| Under 15 | calm |
| 15 to under 20 | normal |
| 20 to under 30 | stressed |
| 30 and above | crisis |

## Where Tavily Fits

Tavily can be used by a beginner in both directions:

| Use | Role |
| --- | --- |
| Live context | Search for current VIX explanations, official references, and recent educational sources |
| Trailing context | Find pages that explain historical VIX spikes, volatility regimes, and how to interpret Cboe data |

Tavily should be treated as optional discovery. Apify remains the hackathon-required live web-data source.

## Demo Commands

Dry run:

```bash
python3 app/vix_learning_radar.py
```

Live Apify run:

```bash
export APIFY_API_TOKEN=your_token_here
python3 app/vix_learning_radar.py --live
```

Live Apify plus Tavily:

```bash
export APIFY_API_TOKEN=your_token_here
export TAVILY_API_KEY=your_tavily_token_here
python3 app/vix_learning_radar.py --live --tavily
```

## Demo Claim

"VIX Learning Radar uses one live Apify Actor and one trailing public Cboe dataset to produce a beginner-safe volatility learning brief. Tavily can optionally help discover context, but the core demo already works with Apify plus Cboe."
