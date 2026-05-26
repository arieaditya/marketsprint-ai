from typing import List, Dict
from research import CompetitorFact


def build_matrix(facts: List[CompetitorFact]) -> List[Dict[str, str]]:
    rows = []
    for f in facts:
        rows.append({
            "name": f.name,
            "positioning": f"{f.value_prop} for Indonesia market",
            "risk": "Moat in distribution and compliance",
            "opportunity": "Designer-first intelligence workflow",
        })
    return rows
