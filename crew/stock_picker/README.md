# Stock Picker

A [CrewAI](https://crewai.com) crew that discovers trending companies in a sector via web search, researches them, then picks one investment recommendation. The orchestration layer uses a **hierarchical** process with a **manager** agent.

## What it does

1. **Find trending companies** — `SerperDevTool` finds 2–3 companies trending in the news for the given sector (`output/trending_companies.json`, structured as `TrendingCompanyList`).
2. **Research each candidate** — deep dive per company (`output/research_report.json`, structured as `TrendingCompanyResearchList`).
3. **Pick the best company** — final rationale in `output/decision.md`. The picker agent may call **`PushNotificationTool`** to send a Pushover notification (decision + one-sentence rationale).

Configuration lives under `src/stock_picker/config/` (`agents.yaml`, `tasks.yaml`). Orchestration is in `src/stock_picker/crew.py` (`StockPicker` crew class).

## Requirements

- Python `>=3.10,<3.14` (see `pyproject.toml`)
- Dependencies managed with **[uv](https://docs.astral.sh/uv/)**

Install dependencies from this directory:

```bash
uv sync
```

## Environment

Create a `.env` in the project directory (same level as `pyproject.toml`):

| Variable | Purpose |
|---------|---------|
| `OPENAI_API_KEY` | LLM calls (agents use OpenAI-compatible models via CrewAI). |
| `SERPER_API_KEY` | Required for **Serper** search (`SerperDevTool`) on finder and researcher agents. |
| `PUSHOVER_USER`, `PUSHOVER_TOKEN` | Optional but needed for Pushover notifications from `pick_best_company`. |

## Running

From this project directory (`crew/stock_picker`):

```bash
crewai run
```

Alternatively, after sync:

```bash
uv run stock_picker
# or
uv run run_crew
```

Inputs are defined in `src/stock_picker/main.py`: by default **`sector`** is `'Technology'` and **`current_date`** is the runtime timestamp.

## Customizing behavior

- **Agents and wording** — `src/stock_picker/config/agents.yaml`
- **Tasks and output paths** — `src/stock_picker/config/tasks.yaml`
- **Crew wiring (agents, tasks, pydantic outputs, hierarchical manager)** — `src/stock_picker/crew.py`
- **Kickoff inputs and printing** — `src/stock_picker/main.py`
- **Push notifications** — `src/stock_picker/tools/push_tool.py`

## Outputs

| File | Task |
|------|------|
| `output/trending_companies.json` | `find_trending_companies` |
| `output/research_report.json` | `research_trending_companies` |
| `output/decision.md` | `pick_best_company` |

For CrewAI tooling and versioning notes, see `AGENTS.md`.
