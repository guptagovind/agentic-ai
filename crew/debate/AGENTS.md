# AGENTS.md — `debate` (this repo)

This file describes **this package only**. For full CrewAI patterns and long-form reference, use [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) and [docs.crewai.com](https://docs.crewai.com).

---

## Pinned facts (from this tree)

| Item | Value |
|------|--------|
| Package / module | `debate` |
| Crew class | **`Debate`** — `src/debate/crew.py`, `@CrewBase` |
| Config | `config/agents.yaml`, `config/tasks.yaml` |
| Crew | `Process.sequential`, `verbose=True` (no `tracing=` in `Crew(...)`) |
| Agents | `debater`, `judge`; LLM strings in YAML (`openai/gpt-4o-mini`) |
| Tasks | `propose`, `oppose`, `decide` — outputs under **`output/*.md`** per `tasks.yaml` |
| `main.py` | **`run()`** only; kickoff `inputs` include **`motion`** |
| Dependency | `crewai[tools]==1.10.1` in `pyproject.toml` |
| Scripts | `run_crew` / `debate` → `main:run`. **`train` / `replay` / `test` / `run_with_trigger`** in `pyproject.toml` **not implemented** in `main.py` unless added |

## Layout

```
src/debate/
  main.py
  crew.py
  config/
    agents.yaml
    tasks.yaml
  tools/
    custom_tool.py   # unused in crew.py
knowledge/
  user_preference.txt
output/              # task outputs (often gitignored)
```

YAML method names on **`Debate`** must match keys: **`debater`**, **`judge`**, **`propose`**, **`oppose`**, **`decide`**.
