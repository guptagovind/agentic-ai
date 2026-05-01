# EngineeringTeam Crew

A [crewAI](https://crewai.com) project that turns plain-English software
requirements into a working Python module with a Gradio demo UI and a unit-test
suite. It is configured to build a small **trading-simulation account
management** module (`accounts.py`) end-to-end.

## What this crew does

Given a `requirements` string, a `module_name` and a `class_name`, the crew
runs four agents in sequence and writes everything to the `output/` folder:

| # | Agent              | Task            | Output                         |
|---|--------------------|-----------------|--------------------------------|
| 1 | `engineering_lead` | `design_task`   | `output/<module_name>_design.md` (markdown design) |
| 2 | `backend_engineer` | `code_task`     | `output/<module_name>` (Python module — runs sandboxed code execution) |
| 3 | `frontend_engineer`| `frontend_task` | `output/app.py` (Gradio UI on top of the module) |
| 4 | `test_engineer`    | `test_task`     | `output/test_<module_name>` (unittest suite — runs sandboxed code execution) |

The default inputs in `src/engineering_team/main.py` produce
`output/accounts.py` (an `Account` class), `output/app.py` (a Gradio frontend),
and `output/test_accounts.py` (a `unittest` suite). Change the `requirements`,
`module_name`, or `class_name` constants in `main.py` to target a different
project.

## Project layout

```
engineering_team/
├── src/engineering_team/
│   ├── config/
│   │   ├── agents.yaml       # engineering_lead, backend_engineer, frontend_engineer, test_engineer
│   │   └── tasks.yaml        # design_task, code_task, frontend_task, test_task
│   ├── tools/
│   │   └── custom_tool.py    # Stub BaseTool (not wired in by default)
│   ├── crew.py               # @CrewBase class wiring agents + tasks
│   └── main.py               # Entry point: defines requirements, calls crew().kickoff()
├── knowledge/
│   └── user_preference.txt
├── output/                   # Generated artifacts (design doc, module, UI, tests)
├── pyproject.toml
└── uv.lock
```

## Requirements

- Python `>=3.10, <3.14`
- [`uv`](https://docs.astral.sh/uv/) for dependency management
- An OpenAI API key (the YAML configs use `gpt-4o-mini`)
- Docker, because the `backend_engineer` and `test_engineer` run with
  `allow_code_execution=True` and `code_execution_mode="safe"`, which executes
  generated code inside a Docker sandbox

## Installation

```bash
pip install uv          # if you don't already have it
crewai install          # syncs the env from pyproject.toml / uv.lock
```

Create a `.env` file in this directory with at least:

```
OPENAI_API_KEY=sk-...
# Optional: override the default model for any agent that doesn't pin one
# MODEL=gpt-4o-mini
```

## Running the crew

From `crew/engineering_team/`:

```bash
crewai run
```

`pyproject.toml` also exposes these scripts (defined under `[project.scripts]`,
some of which currently point to functions that aren't yet implemented in
`main.py` — `crewai run` / `engineering_team` is the supported entry point):

| Script             | Purpose                              |
|--------------------|--------------------------------------|
| `engineering_team` | Same as `run_crew`; runs the crew    |
| `run_crew`         | Calls `engineering_team.main:run`    |
| `train`            | Reserved (not implemented in `main.py`) |
| `replay`           | Reserved (not implemented in `main.py`) |
| `test`             | Reserved (not implemented in `main.py`) |

A successful run prints the final task output and writes the four files listed
in the table above into `output/`.

## Trying the generated app

Once the crew has produced `output/accounts.py`, `output/app.py`, and
`output/test_accounts.py`:

```bash
cd output
python app.py            # launches the Gradio UI
python -m unittest test_accounts.py
```

The Gradio UI exposes tabs for: Account Creation, Deposit, Withdraw, Buy
Shares, Sell Shares, Portfolio Value, Profit/Loss, Holdings, and Transactions.
The `Account` class enforces basic rules (positive deposit/withdraw, no
negative balance, can't sell shares you don't hold), and `get_share_price`
returns fixed prices for `AAPL`, `TSLA`, `GOOGL`.

## Customising

- Edit `src/engineering_team/main.py` to change `requirements`, `module_name`,
  or `class_name`.
- Edit `src/engineering_team/config/agents.yaml` to change agent roles, goals,
  or per-agent LLM (defaults to `gpt-4o-mini`).
- Edit `src/engineering_team/config/tasks.yaml` to change task descriptions or
  output paths.
- Edit `src/engineering_team/crew.py` to add agents/tasks, change the process
  (currently `Process.sequential`), enable memory, etc.
- Sandboxed-execution agents (`backend_engineer`, `test_engineer`) are tuned
  with `max_execution_time=240` and `max_retry_limit=5`; adjust as needed.

## Support

- crewAI [documentation](https://docs.crewai.com)
- crewAI [GitHub](https://github.com/crewAIInc/crewAI)
- [Discord](https://discord.com/invite/X4JWnZnxPb)
