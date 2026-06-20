import argparse
import csv
import json
import os
import statistics
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path


ACTOR_ID = "apify/website-content-crawler"
CBOE_VIX_PAGE = "https://www.cboe.com/tradable-products/vix/"
CBOE_VIX_HISTORY_PAGE = "https://www.cboe.com/tradable-products/vix/vix-historical-data"
CBOE_VIX_CSV = "https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv"
TAVILY_SEARCH_URL = "https://api.tavily.com/search"
DEFAULT_TAVILY_QUERY = "Cboe VIX volatility index historical data beginner explanation"


def post_json(url, payload, timeout=180):
    body = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def post_json_with_auth(url, payload, bearer_token, timeout=30):
    body = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=body,
        headers={
            "Authorization": f"Bearer {bearer_token}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def run_website_content_crawler(token, urls, max_pages):
    actor_path = ACTOR_ID.replace("/", "~")
    endpoint = f"https://api.apify.com/v2/acts/{actor_path}/run-sync-get-dataset-items"
    query = urllib.parse.urlencode({"token": token, "timeout": 180})
    payload = {
        "startUrls": [{"url": url} for url in urls],
        "maxCrawlPages": max_pages,
        "saveMarkdown": True,
        "saveHtml": False,
        "saveFiles": False,
    }
    return post_json(f"{endpoint}?{query}", payload)


def run_tavily_search(api_key, query, max_results=5):
    payload = {
        "query": query,
        "topic": "finance",
        "search_depth": "basic",
        "max_results": max_results,
        "include_answer": True,
        "include_raw_content": False,
    }
    return post_json_with_auth(TAVILY_SEARCH_URL, payload, api_key)


def fetch_vix_history(limit=None):
    with urllib.request.urlopen(CBOE_VIX_CSV, timeout=30) as response:
        text = response.read().decode("utf-8")
    rows = list(csv.DictReader(text.splitlines()))
    parsed = []
    for row in rows:
        date = row.get("DATE") or row.get("Date") or row.get("date")
        close = row.get("CLOSE") or row.get("Close") or row.get("close")
        if not date or not close:
            continue
        parsed.append({"date": date, "close": float(close)})
    return parsed[-limit:] if limit else parsed


def load_fixture(path):
    return json.loads(Path(path).read_text())


def regime(value):
    if value < 15:
        return "calm"
    if value < 20:
        return "normal"
    if value < 30:
        return "stressed"
    return "crisis"


def extract_context_signals(items):
    signals = []
    keywords = {
        "education_need": ["education", "learn", "course", "faq", "glossary", "what is"],
        "risk_clarity": ["risk", "hedge", "portfolio", "volatility risk", "unique characteristics"],
        "market_structure": ["futures", "options", "index", "methodology", "term structure"],
        "data_access": ["historical data", "market data", "datashop", "delayed", "updated daily"],
    }
    for item in items:
        url = item.get("url") or item.get("loadedUrl") or item.get("metadata", {}).get("canonicalUrl", "")
        title = item.get("metadata", {}).get("title") or item.get("title") or url
        text = (item.get("text") or item.get("markdown") or "")[:12000].lower()
        for signal_type, words in keywords.items():
            hits = [word for word in words if word in text]
            if hits:
                signals.append(
                    {
                        "source": title,
                        "url": url,
                        "type": signal_type,
                        "evidence": f"Found terms: {', '.join(hits[:4])}",
                        "score": min(5, 2 + len(hits)),
                    }
                )
    return signals


def analyze_vix(rows):
    closes = [row["close"] for row in rows]
    latest = rows[-1]
    last_30 = closes[-30:] if len(closes) >= 30 else closes
    top = sorted(rows, key=lambda row: row["close"], reverse=True)[:10]
    return {
        "latest_date": latest["date"],
        "latest_close": latest["close"],
        "latest_regime": regime(latest["close"]),
        "ma_30": round(statistics.mean(last_30), 2),
        "top_spikes": top,
    }


def render_table(headers, rows):
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(cell).replace("\n", " ") for cell in row) + " |")
    return "\n".join(lines)


def build_report(context_items, vix_rows, mode, tavily_result=None, tavily_query=None):
    analysis = analyze_vix(vix_rows)
    signals = extract_context_signals(context_items)
    signal_rows = [
        [signal["type"], signal["source"], signal["evidence"], signal["score"]]
        for signal in sorted(signals, key=lambda item: item["score"], reverse=True)
    ]
    spike_rows = [
        [row["date"], row["close"], regime(row["close"])]
        for row in analysis["top_spikes"]
    ]
    ledger_rows = [
        [
            ACTOR_ID,
            "Pull live Cboe educational/context pages",
            f"{CBOE_VIX_PAGE}, {CBOE_VIX_HISTORY_PAGE}",
            f"{len(context_items)} crawled items",
            "Apify usage / hackathon credits",
            "Provides source-backed context for the report",
        ],
        [
            "Cboe public CSV",
            "Load free historical VIX closes",
            CBOE_VIX_CSV,
            f"{len(vix_rows)} daily rows",
            "$0, no credentials",
            "Provides the numeric regime evidence",
        ],
    ]
    tavily_rows = []
    if tavily_result:
        results = tavily_result.get("results", [])
        tavily_rows = [
            [
                item.get("title", "Untitled")[:80],
                item.get("url", ""),
                round(float(item.get("score", 0)), 3) if item.get("score") is not None else "",
                (item.get("content") or "")[:140],
            ]
            for item in results
        ]
        ledger_rows.append(
            [
                "Tavily Search API",
                "Discover recent beginner-friendly context around the VIX question",
                tavily_query or DEFAULT_TAVILY_QUERY,
                f"{len(results)} search results",
                "Tavily API credits",
                "Optional source discovery; Apify remains the required live Actor",
            ]
        )

    tavily_section = "Not used in this run. Add `--tavily` with `TAVILY_API_KEY` to include search discovery."
    if tavily_result:
        tavily_answer = tavily_result.get("answer") or "No direct Tavily answer returned."
        tavily_section = f"""Tavily answer summary:

{tavily_answer}

{render_table(["Title", "URL", "Score", "Snippet"], tavily_rows or [["none", "none", "none", "No Tavily results"]])}"""

    return f"""# VIX Learning Radar - Demo Report

Generated: {datetime.utcnow().isoformat(timespec="seconds")}Z

Mode: `{mode}`

## Demo Question

Using public Cboe data and at least one Apify Actor, what can a beginner learn about VIX volatility regimes without broker credentials or paid market-data subscriptions?

## Clear Objective

Help a beginner answer: **"What volatility regime are we in, how unusual is it versus trailing VIX history, and which official context explains what that means?"**

The agent should produce an educational brief, not a trade recommendation.

## Executive Answer

The useful beginner artifact is not a trading signal. It is a **VIX Learning Radar**: a small educational agent that pulls Cboe context pages with Apify, reads free public VIX history, labels volatility regimes, and explains what changed without recommending trades.

Latest available VIX close in the dataset: **{analysis["latest_close"]}** on **{analysis["latest_date"]}**, labeled **{analysis["latest_regime"]}**. The 30-day average is **{analysis["ma_30"]}**.

## Cboe Context Signals From Apify Crawl

{render_table(["Signal type", "Source", "Evidence", "Score"], signal_rows or [["none", "none", "No signals extracted", 0]])}

## Largest Historical VIX Closes

{render_table(["Date", "Close", "Regime"], spike_rows)}

## Optional Tavily Discovery

{tavily_section}

## Paid / Live Data Ledger

{render_table(["Data source", "Reason", "Input", "Output", "Cost proxy", "Signal value"], ledger_rows)}

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
"""


def main():
    parser = argparse.ArgumentParser(description="VIX Learning Radar demo.")
    parser.add_argument("--live", action="store_true", help="Run Apify Actor and fetch live Cboe CSV")
    parser.add_argument("--fixture", default="data/vix_fixture.json", help="Fixture JSON for dry-run mode")
    parser.add_argument("--output", default="outputs/vix_learning_radar_report.md", help="Markdown report path")
    parser.add_argument("--max-pages", type=int, default=2, help="Max pages for Website Content Crawler")
    parser.add_argument("--tavily", action="store_true", help="Add optional Tavily search discovery")
    parser.add_argument("--tavily-query", default=DEFAULT_TAVILY_QUERY, help="Tavily search query")
    parser.add_argument("--tavily-results", type=int, default=5, help="Max Tavily results")
    args = parser.parse_args()

    if args.live:
        token = os.environ.get("APIFY_API_TOKEN")
        if not token:
            raise SystemExit("Set APIFY_API_TOKEN before running --live.")
        context_items = run_website_content_crawler(
            token,
            [CBOE_VIX_PAGE, CBOE_VIX_HISTORY_PAGE],
            args.max_pages,
        )
        vix_rows = fetch_vix_history()
        mode = "live-apify"
    else:
        fixture = load_fixture(args.fixture)
        context_items = fixture["context_items"]
        vix_rows = fixture["vix_rows"]
        mode = "dry-run-fixture"

    tavily_result = None
    if args.tavily:
        tavily_key = os.environ.get("TAVILY_API_KEY")
        if not tavily_key:
            raise SystemExit("Set TAVILY_API_KEY before running --tavily.")
        tavily_result = run_tavily_search(tavily_key, args.tavily_query, args.tavily_results)
        mode = f"{mode}+tavily"

    report = build_report(context_items, vix_rows, mode, tavily_result, args.tavily_query)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report)
    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
