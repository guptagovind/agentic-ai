# Debate Crew

CrewAI project: class **`Debate`** in `src/debate/crew.py` loads **`config/agents.yaml`** and **`config/tasks.yaml`**, runs **`Process.sequential`**.

## What the code does

| Piece | Behavior |
|--------|-----------|
| **`Debate` crew** | Agents: `debater`, `judge`. Tasks (in order): `propose` → `oppose` → `decide`. |
| **`agents.yaml`** | Both agents use `openai/gpt-4o-mini`. Role/goal/backstory reference `{motion}`. |
| **`tasks.yaml`** | Task outputs: `output/propose.md`, `output/oppose.md`, `output/decide.md`. |
| **`main.py`** | Defines only **`run()`**. Builds `inputs = {"motion": "There needs to be strict laws to regulate LLMs"}` and calls `Debate().crew().kickoff(inputs=inputs)`. Imports `datetime` but does not use it. |
| **`tools/custom_tool.py`** | Example `MyCustomTool`; **not** referenced in `crew.py` (no tools on agents). |
| **`knowledge/user_preference.txt`** | Sample text only; **not** wired into the crew in code. |

## Prerequisites

- Python `>=3.10,<3.14` (`pyproject.toml`)
- Dependency: `crewai[tools]==1.10.1`

## Setup

Run from **`crew/debate/`** (where this `pyproject.toml` lives):

```bash
cd crew/debate
uv sync
# or: crewai install
```

Set `OPENAI_API_KEY` in `.env` (or use your environment).

## Run

```bash
crewai run
```

Equivalent: `uv run run_crew` or `uv run debate` (both call `debate.main:run`).

## Changing the motion

Edit the `inputs` dict inside **`run()`** in `src/debate/main.py`. That is the only kickoff input the YAML expects (`{motion}`).

## `pyproject.toml` vs `main.py`

`[project.scripts]` also defines **`train`**, **`replay`**, **`test`**, and **`run_with_trigger`** pointing at `debate.main`. Those functions **are not defined** in `src/debate/main.py` right now, so commands like `uv run train` or `crewai train` will fail until you add matching functions to `main.py`.

## Support

- [CrewAI documentation](https://docs.crewai.com)
- [CrewAI on GitHub](https://github.com/joaomdmoura/crewai)
