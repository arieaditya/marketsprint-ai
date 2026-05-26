from datetime import datetime
from typing import List, Dict


def render_report(topic: str, matrix: List[Dict[str, str]]) -> str:
    lines = [
        f"# Competitive Report: {topic}",
        f"Generated: {datetime.utcnow().isoformat()}Z",
        "",
        "## Executive Summary",
        "MarketSprint AI helps product designers do fast competitor scans and turn them into actionable briefs.",
        "",
        "## Competitor Matrix",
    ]
    for row in matrix:
        lines += [
            f"### {row['name']}",
            f"- Positioning: {row['positioning']}",
            f"- Risk: {row['risk']}",
            f"- Opportunity: {row['opportunity']}",
            "",
        ]
    lines += [
        "## Recommendations",
        "1. Focus on speed-to-insight UX for designers",
        "2. Add side-by-side competitor snapshot",
        "3. Ship weekly trend digest",
    ]
    return "\n".join(lines)
