# MarketSprint AI

Autonomous Competitive Intelligence Agent for Product Designers.

## Structure
- `agent/orchestrator.py` main pipeline
- `agent/research.py` web/data research stage
- `agent/analysis.py` synthesis & competitor matrix
- `agent/report.py` markdown report generation
- `config/agents.yaml` runtime config
- `prompts/system_prompts.py` role prompts
- `output/indonesia-fintech-competitive-report.md` demo report
- `submission/grant-application.md` answers for form #04 & #05
- `submission/usage-proof.md` metrics/evidence

## Run
```bash
python3 agent/orchestrator.py --topic "indonesia fintech"
```
