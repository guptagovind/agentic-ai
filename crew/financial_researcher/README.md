# financial_researcher

CrewAI crew: **`ResearchCrew`** in `src/financial_researcher/crew.py` loads **`config/agents.yaml`** and **`config/tasks.yaml`**, runs **`Process.sequential`** with **`tracing=False`**.

## What it does

| Piece | Details |
|--------|--------|
| **Agents** | `researcher` (with **SerperDevTool**), `analyst`. Both use **`openai/gpt-4o-mini`** per YAML. |
| **Tasks** | `research_task` → `analysis_task` (`context` = research). Analyst writes **`output/report.md`**. |
| **Inputs** | `{company}` everywhere in YAML. Default in **`main.py`**: `Newgen Software Technologies Ltd.` |
| **main.py** | **`run()`** only: `set_suppress_tracing_messages(True)`, `kickoff`, prints `result.raw`. |
| **Tools** | **`tools/custom_tool.py`** is a scaffold; **not** wired in `crew.py`. |
| **knowledge/** | `user_preference.txt` exists; **not** referenced in `crew.py` or YAML. |

## Requirements

- Python **>=3.10,<3.14** (`pyproject.toml`)
- **`crewai[litellm,tools]==1.10.1`**
- **`.env`**: at least **`OPENAI_API_KEY`**. **`SERPER_API_KEY`** for `SerperDevTool`.

## Setup & run

From **`crew/financial_researcher/`** (where this `pyproject.toml` lives):

```bash
cd crew/financial_researcher
uv sync
# or: crewai install
crewai run
```

Use a **local** `.env` or export keys; `crewai run` invokes **`uv run run_crew`** → `financial_researcher.main:run`.

Change the company by editing the **`inputs`** dict in **`src/financial_researcher/main.py`**.

## pyproject scripts

`[project.scripts]` also lists **`train`**, **`replay`**, **`test`**, **`run_with_trigger`**. **`main.py` only defines `run()`** — those entry points will fail until you add matching functions.

## References

- [CrewAI docs](https://docs.crewai.com)
- Project notes for assistants: **`AGENTS.md`**
