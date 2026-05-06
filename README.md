# agentic-ai

Workspace for **agentic AI** coursework and experiments—primarily self-contained [CrewAI](https://crewai.com) crews under `crew/`, plus a workspace-level Python environment for broader course dependencies.

The workspace `pyproject.toml` bundles libraries used across the Udemy Agentic AI Engineering-style material ([OpenAI Agents](https://openai.github.io/openai-agents-python/), CrewAI, LangGraph, LangChain, AutoGen, MCP, and related tooling). **`crew/` projects each ship their own `pyproject.toml` and `uv.lock`**; treat them as the canonical place to install and run a specific demo.

## Repository layout

| Path | Purpose |
|------|---------|
| [`crew/coder`](crew/coder/README.md) | Minimal crew: one Python developer agent runs an assignment with safe Docker-backed code execution, writes output under `output/`. |
| [`crew/debate`](crew/debate/README.md) | Sequential debate crew: propose → oppose → decide on a motion; markdown artifacts in `output/`. |
| [`crew/engineering_team`](crew/engineering_team/README.md) | Four-agent pipeline: design → implementation → Gradio frontend → tests (default: trading-style `accounts` module). |
| [`crew/financial_researcher`](crew/financial_researcher/README.md) | Research + analyst crew with web search (**Serper**); produces `output/report.md` for a given company. |
| [`crew/stock_picker`](crew/stock_picker/README.md) | Hierarchical crew: find trending companies in a sector, research them, pick a recommendation; optional Pushover notifications. |
| `.env.example` | Template for API keys (copy to `.env` at the scope where you run code—crew root vs repo root). |
| Root `pyproject.toml` / `uv.lock` | Optional shared environment at the repo root (`requires-python >=3.12`). |

For agent orchestration details, YAML keys, and project-specific prerequisites, open each crew’s **`README.md`** (and **`AGENTS.md`** where present for CrewAI-focused assistant context).

## Quick start (workspace root)

Optional: sync the workspace environment from the repo root:

```bash
uv sync
```

Set secrets using [`.env.example`](.env.example) as a guide (never commit real keys).

## Running a CrewAI project

Every crew is independent. From the crew directory that contains **`pyproject.toml`**:

```bash
cd crew/<project_name>
uv sync          # or: crewai install — per project docs
crewai run       # typical entrypoint; see that project’s README
```

Many crews need **`OPENAI_API_KEY`**; several also need **`SERPER_API_KEY`**, **Docker** (when using safe code execution), or other vars—check the subdirectory README before your first run.
