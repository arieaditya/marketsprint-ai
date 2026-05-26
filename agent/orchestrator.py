import argparse
from pathlib import Path
from research import run_research
from analysis import build_matrix
from report import render_report


def main(topic: str):
    facts = run_research(topic)
    matrix = build_matrix(facts)
    report = render_report(topic, matrix)
    out = Path(__file__).resolve().parents[1] / "output" / "indonesia-fintech-competitive-report.md"
    out.write_text(report)
    print(f"Report generated: {out}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", default="indonesia fintech")
    args = parser.parse_args()
    main(args.topic)
