# Coder crew

Minimal [CrewAI](https://crewai.com) project: one **Python Developer** agent runs **code** for an `assignment`, writes **code plus program output** to a file under `output/`, and streams the crew result to stdout.

Python **3.10–3.13** (`requires-python` in `pyproject.toml`). Dependencies use **[uv](https://docs.astral.sh/uv/)**.

## Prerequisites

- **uv** and a virtualenv synced from `pyproject.toml` / `uv.lock`
- **`OPENAI_API_KEY`** in a `.env` file at this project root (see `.gitignore`; never commit secrets)
- **Docker Engine** running and reachable by the user that runs `crewai run`, because the agent uses **`allow_code_execution=True`** with **`code_execution_mode="safe"`** (`src/coder/crew.py`): the bundled `CodeInterpreterTool` runs code in Docker in safe mode.

## Setup

From this directory (`crew/coder/`, next to `pyproject.toml`):

```bash
uv sync
```

Create `.env` with at least:

```bash
OPENAI_API_KEY=sk-...
```

## What the code does

| Piece | Purpose |
|--------|--------|
| `src/coder/crew.py` | **`Coder`** crew: sequential process, coder agent with code execution (**safe** / Docker), `max_execution_time=120`, `max_retry_limit=3`. |
| `src/coder/main.py` | Ensures **`output/`** exists, sets `assignment` text, **`kickoff(inputs={"assignment": ...})`**, **`print(result.raw)`**. |
| `src/coder/config/agents.yaml` | Agent **`coder`**: Python Developer, **`gpt-4o-mini`**. |
| `src/coder/config/tasks.yaml` | Task **`coding_task`**: fulfill `{assignment}`; **`expected_output`** is code + captured output in a text file; **`output_file: output/code_and_output.txt`**. |
| `src/coder/tools/custom_tool.py` | Example **`MyCustomTool`** stub — **not** registered on the agent until you wire it in `crew.py`. |
| `knowledge/` | Optional knowledge files (e.g. `user_preference.txt`); not required for the default task. |

## Run

```bash
crewai run
```

Equivalent:

```bash
uv run run_crew
# or
uv run coder
```

On success you should get **`output/code_and_output.txt`** (from the task’s `output_file`) and the final narrative in the terminal via `print(result.raw)`.

## Configure

- Change the problem string: **`assignment`** in `src/coder/main.py`.
- Change role/goal/model: **`src/coder/config/agents.yaml`**.
- Change deliverable / path: **`src/coder/config/tasks.yaml`** (`expected_output`, `output_file`).
- Execution mode / timeouts: **`src/coder/crew.py`** (`code_execution_mode`, `max_execution_time`, `max_retry_limit`).

**Note:** `pyproject.toml` defines console scripts `train`, `replay`, `test`, and `run_with_trigger` pointing at `coder.main`, but **`main.py` currently only implements `run`**. Use `crewai run` until those functions are added if you need them.

## Troubleshooting (short)

- **Docker errors:** Install/start Docker; ensure `docker info` works for the same user as the crew (e.g. `docker` group).
- **Task timeout:** Long agent loops or many tool calls can hit `max_execution_time`; increase it in `crew.py` or simplify `expected_output` / assignment.
- **`unsafe` code execution:** If you switch to `code_execution_mode="unsafe"`, the stock `CodeInterpreterTool` returns the **`result`** variable from `exec`, not `print()` output — align generated code or stay on **safe** + Docker.

## Links

- [CrewAI docs](https://docs.crewai.com)
- [CrewAI GitHub](https://github.com/crewAIInc/crewAI)

See **`AGENTS.md`** in this folder for broader CrewAI patterns; the top **“This codebase”** section there matches **this** project.
