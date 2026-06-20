import argparse
import json
from pathlib import Path


SIGNAL_TYPES = {
    "actor_choice_gap": "Hard to know which Actor is worth running",
    "llm_context_need": "Source is useful for LLM/RAG or agent context",
    "marketplace_signal": "Source indicates marketplace supply or demand",
    "pricing_signal": "Source clarifies paid access or usage model",
    "proof_artifact": "Source points toward something buildable",
}


def score_signal(signal):
    fields = ["relevance", "freshness", "credibility", "actionability"]
    return sum(int(signal.get(field, 0)) for field in fields)


def band(score):
    if score >= 16:
        return "very useful"
    if score >= 11:
        return "useful"
    if score >= 6:
        return "weak"
    return "discard"


def summarize_source(source):
    signals = source.get("signals", [])
    if not signals:
        return 0, "discard"
    best = max(score_signal(signal) for signal in signals)
    return best, band(best)


def render_table(headers, rows):
    header_line = "| " + " | ".join(headers) + " |"
    sep_line = "| " + " | ".join(["---"] * len(headers)) + " |"
    row_lines = ["| " + " | ".join(str(cell).replace("\n", " ") for cell in row) + " |" for row in rows]
    return "\n".join([header_line, sep_line, *row_lines])


def generate_report(data):
    question = data["question"]
    arena = data["arena"]
    sources = data["sources"]
    ledger = data["ledger"]

    source_rows = []
    best_signals = []
    for source in sources:
        best_score, best_band = summarize_source(source)
        source_rows.append([
            source["title"],
            source["url"],
            source["actor"],
            best_score,
            best_band,
        ])
        for signal in source.get("signals", []):
            signal_score = score_signal(signal)
            best_signals.append((signal_score, source, signal))

    best_signals.sort(key=lambda item: item[0], reverse=True)

    signal_rows = []
    for signal_score, source, signal in best_signals[:5]:
        signal_rows.append([
            signal["type"],
            signal["text"],
            source["title"],
            signal_score,
            band(signal_score),
        ])

    ledger_rows = []
    for entry in ledger:
        ledger_rows.append([
            entry["actor"],
            entry["reason"],
            entry["input"],
            entry["output"],
            entry["cost_proxy"],
            entry["signal_value"],
        ])

    top_signal = best_signals[0][2] if best_signals else None
    top_source = best_signals[0][1] if best_signals else None

    executive_answer = (
        "The buildable opportunity is not another scraper. It is a small decision layer "
        "that helps an agent choose which Actor is worth paying for, then records whether "
        "the returned evidence changed the decision."
    )

    if top_signal and top_source:
        executive_answer += (
            f" The strongest signal came from `{top_source['title']}`: "
            f"{top_signal['text']}"
        )

    report = f"""# Apify Actor Idea Radar - Demo Report

## Question

{question}

## Arena

{arena}

## Executive Answer

{executive_answer}

## Evidence Table

{render_table(["Source", "URL", "Actor", "Best score", "Usefulness"], source_rows)}

## Top Signals

{render_table(["Type", "Signal", "Source", "Score", "Usefulness"], signal_rows)}

## Paid-Data Ledger

{render_table(["Actor", "Reason", "Input", "Output", "Cost proxy", "Signal value"], ledger_rows)}

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
"""
    return report


def main():
    parser = argparse.ArgumentParser(description="Generate an Apify Actor Idea Radar report.")
    parser.add_argument("--input", default="data/sample_sources.json", help="Path to source JSON")
    parser.add_argument("--output", default="outputs/apify_actor_idea_radar_report.md", help="Markdown output path")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    data = json.loads(input_path.read_text())
    report = generate_report(data)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report)
    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
