# Cboe Data Without Credentials or Spend - Beginner Path

Date: 2026-06-20
Goal: Connect the hackathon idea to Cboe/volatility data without paid APIs, broker credentials, Robinhood, Betfair, or trading execution.

## 1. Start With The Safe Dataset

Use **Cboe VIX historical daily data**.

Why:

- Free public page
- No account needed
- No broker connection
- No live trading or execution
- Enough data to build a useful educational/proof artifact

Cboe page:

https://www.cboe.com/tradable-products/vix/vix-historical-data

Direct CSV commonly exposed from that page:

https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv

If the direct CSV link ever changes, go to the historical data page and click:

**VIX Index data for 1990 to present (Updated Daily)**

## 2. What Not To Use Yet

Avoid for now:

- Robinhood API idea
- Betfair API idea
- Broker APIs
- Unofficial trading APIs
- Real-time option chain feeds
- Paid Cboe DataShop products
- LiveVol or analytics platforms
- Anything requiring login, payment, or trading account access

Reason:

You are not building a trading tool. You are building a **market-structure learning and signal artifact**.

## 3. The Beginner Project

Build:

**VIX Learning Radar**

One-liner:

> A tiny tool that loads free Cboe VIX history, finds volatility regimes and spike events, and generates an educational brief about what changed.

This avoids financial advice. It explains market structure and volatility behavior.

## 4. MVP Output

The tool should generate:

1. Latest available VIX close
2. 30-day average VIX
3. Highest VIX days in the dataset
4. Recent spike dates
5. Simple volatility regime labels
6. Short educational brief
7. Data ledger

Example regime labels:

- `calm`: VIX below 15
- `normal`: VIX 15-20
- `stressed`: VIX 20-30
- `crisis`: VIX above 30

Do not say:

- "Buy"
- "Sell"
- "Trade this"
- "Prediction"
- "Signal to enter"

Say:

- "Historical regime"
- "Observed volatility"
- "Educational context"
- "Not investment advice"

## 5. No-Code Version

1. Open the Cboe historical data page.
2. Download the VIX history CSV.
3. Open in Numbers, Excel, or Google Sheets.
4. Create columns:
   - date
   - close
   - 30-day moving average
   - regime label
5. Sort by close descending.
6. Write a short brief:
   - What were the biggest spikes?
   - How often did VIX exceed 30?
   - What does the latest close look like compared with history?

## 6. Python Beginner Version

```python
import pandas as pd

url = "https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv"

df = pd.read_csv(url)
print(df.head())
print(df.tail())
print(df.columns)
```

Then inspect the column names. Cboe CSV files often use columns like:

- `DATE`
- `OPEN`
- `HIGH`
- `LOW`
- `CLOSE`

Then:

```python
df["DATE"] = pd.to_datetime(df["DATE"])
df["MA_30"] = df["CLOSE"].rolling(30).mean()

def regime(vix):
    if vix < 15:
        return "calm"
    if vix < 20:
        return "normal"
    if vix < 30:
        return "stressed"
    return "crisis"

df["REGIME"] = df["CLOSE"].apply(regime)

print(df.tail(10))
print(df.sort_values("CLOSE", ascending=False).head(10))
```

## 7. Apify Connection

If you want to keep the hackathon "agents that pay" angle:

Use Apify for **context pages**, not for the CSV at first.

Suggested sources:

- Cboe VIX overview page
- Cboe VIX historical data page
- Cboe VIX FAQ
- Cboe VIX methodology or whitepaper pages

Use:

- `apify/website-content-crawler` to crawl Cboe educational pages
- Manual CSV download for the actual VIX time series

Ledger example:

```json
{
  "source": "Cboe VIX historical data CSV",
  "access": "free public download",
  "credentials": "none",
  "cost": "0",
  "reason": "Use official historical VIX closes for educational regime analysis",
  "signal_value": 5
}
```

## 8. Demo Question

Use this:

> "Using only free public Cboe data, what does VIX history show about volatility regimes, and what educational artifact would help beginners understand the difference between volatility observation and trading advice?"

Output:

> "The recommended proof artifact is a VIX regime explainer dashboard: it labels historical VIX periods as calm, normal, stressed, or crisis, shows spike dates, and explains that VIX is an observed market-implied volatility index, not a trading recommendation."

## 9. How This Connects To Your Bigger Thesis

This is not "options trading."

It is:

> Decision literacy around regulated market infrastructure.

That is serious and safe:

- Cboe is a real market infrastructure operator.
- VIX is a public volatility index.
- You can study market structure without trading.
- The output can be educational and evidence-backed.

## 10. First Build

Build a script:

```text
app/cboe_vix_beginner.py
```

It should:

1. Load the free VIX CSV.
2. Compute 30-day average.
3. Label regimes.
4. Find top 10 VIX closes.
5. Generate Markdown report.
6. Add a data ledger.

That is enough.

