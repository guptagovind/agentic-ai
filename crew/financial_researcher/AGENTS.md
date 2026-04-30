# AGENTS.md — `financial_researcher` (this repo)

This file describes **this package only**. For full CrewAI patterns, API churn, and long-form assistant reference, use the upstream file from [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) (`templates/crew/AGENTS.md` or equivalent) and [docs.crewai.com](https://docs.crewai.com).

---

## Pinned facts (from this tree)

| Item | Value |
|------|--------|
| Package name | `financial_researcher` |
| Crew class | **`ResearchCrew`** — `src/financial_researcher/crew.py`, `@CrewBase` |
| Config | `config/agents.yaml`, `config/tasks.yaml` (paths relative to package dir) |
| Crew | `Process.sequential`, `verbose=True`, **`tracing=False`** |
| Researcher | **`SerperDevTool()`** on the agent |
| Analyst report | **`output/report.md`** (`analysis_task` in YAML) |
| `main.py` | **`run()`** only; `inputs = {"company": "..."}`; **`set_suppress_tracing_messages(True)`** before kickoff |
| Dependencies | `crewai[litellm,tools]==1.10.1` in `pyproject.toml` |
| Scripts | `run_crew` / `financial_researcher` → `main:run`. **`train` / `replay` / `test` / `run_with_trigger`** listed in `pyproject.toml` but **not implemented** in `main.py` unless you add them |

## Layout

```
src/financial_researcher/
  main.py          # entry: run()
  crew.py          # ResearchCrew
  config/
    agents.yaml
    tasks.yaml
  tools/
    custom_tool.py # unused in crew.py
knowledge/
  user_preference.txt  # not wired into crew
output/
  report.md        # generated (gitignore if you prefer)
```

When editing CrewAI code here, match **`ResearchCrew`** and the YAML keys (`researcher`, `analyst`, `research_task`, `analysis_task`) exactly.
