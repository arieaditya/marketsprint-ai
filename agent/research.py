from dataclasses import dataclass
from typing import List

@dataclass
class CompetitorFact:
    name: str
    value_prop: str
    pricing: str
    channels: str


def run_research(topic: str) -> List[CompetitorFact]:
    seed = [
        CompetitorFact("Xendit", "Payment infrastructure", "Custom", "API-first, enterprise sales"),
        CompetitorFact("Midtrans", "Payment gateway", "Tiered", "SMB + enterprise"),
        CompetitorFact("DOKU", "Online payment", "Custom", "Partnership-led"),
    ]
    return seed
