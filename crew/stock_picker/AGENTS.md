# AGENTS.md — stock_picker

Context for AI coding assistants working on this repository. Prefer the **installed** CrewAI APIs and patterns used in `src/stock_picker/` over stale examples from the web.

## Project layout

```
crew/stock_picker/
├── pyproject.toml
├── src/stock_picker/
│   ├── main.py              # kickoff inputs: sector, current_date
│   ├── crew.py              # StockPicker class, agents, tasks, Crew
│   ├── config/
│   │   ├── agents.yaml      # trending_company_finder, financial_researcher, stock_picker, manager
│   │   └── tasks.yaml       # find_trending_companies → research → pick_best_company
│   └── tools/
│       └── push_tool.py      # PushNotificationTool (Pushover)
└── output/                   # JSON + decision.md produced at runtime
```

## Crew overview

- **Class**: `StockPicker` in `crew.py`, decorated with `@CrewBase`.
- **YAML**: `agents_config`, `tasks_config` point at `config/agents.yaml` and `config/tasks.yaml`.
- **Process**: `Process.hierarchical` with a dedicated **manager** agent (`agents.yaml` → `manager`, `manager_agent=manager` on `Crew`).
- **Agents**:
  - `trending_company_finder` — `SerperDevTool()`
  - `financial_researcher` — `SerperDevTool()`
  - `stock_picker` — `PushNotificationTool()` only (no Serper on this agent).
- **Tasks** (sequential delegation under hierarchy):
  1. `find_trending_companies` → `TrendingCompanyList` (`output_pydantic`).
  2. `research_trending_companies` → depends on prior via YAML `context`, `TrendingCompanyResearchList`.
  3. `pick_best_company` → final prose to `output/decision.md`; should use push tool per task description.

Structured outputs are modeled in `crew.py` with **Pydantic** (`TrendingCompany`, `TrendingCompanyList`, etc.) passed as `output_pydantic` on tasks.

## Environment

- **`OPENAI_API_KEY`** — required for LLMs (YAML uses `openai/gpt-4o-mini` for specialists, `openai/gpt-4o` for manager unless changed).
- **`SERPER_API_KEY`** — needed for Serper-backed search tools.
- **`PUSHOVER_USER`** / **`PUSHOVER_TOKEN`** — Pushover (`push_tool.py` posts to `https://api.pushover.net/1/messages.json`).

When changing CrewAI APIs or decorators, verify against live docs (`https://docs.crewai.com`) and the pinned `crewai[tools]` version in `pyproject.toml`.

## CLI and entrypoints

Typical workflow: **`crewai run`** from `crew/stock_picker`.

`pyproject.toml` declares `[tool.crewai] type = "crew"` and console scripts targeting `stock_picker.main:run`. If scripts reference helpers not implemented in `main.py`, align either the script table or implementation.

## Conventions when editing code

- Keep YAML keys and `@agent` / `@task` method names in `crew.py` aligned with YAML keys (`trending_company_finder`, `find_trending_companies`, etc.).
- After changing prompts or flows, rerun the crew to refresh `output/` fixtures if they are tracked.
