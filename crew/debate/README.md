# debate

CrewAI crew: **`Debate`** in `src/debate/crew.py` loads **`config/agents.yaml`** and **`config/tasks.yaml`**, runs **`Process.sequential`** (no explicit `tracing=` in code).

## What it does

| Piece | Details |
|--------|--------|
| **Agents** | `debater`, `judge`. **`openai/gpt-4o-mini`** in YAML. **`{motion}`** in roles/goals/tasks. |
| **Tasks** | `propose` → `oppose` → `decide`; files **`output/propose.md`**, **`oppose.md`**, **`decide.md`**. |
| **main.py** | **`run()`** only: `inputs = {"motion": "..."}`, `kickoff` inside `try`/`except`. Imports **`sys`** and **`datetime`**; **`datetime` is unused**. |
| **tools/** | **`custom_tool.py`** scaffold; **not** used in `crew.py`. |
| **knowledge/** | **`user_preference.txt`**; **not** wired in `crew.py` or YAML. |

## Requirements

- Python **>=3.10,<3.14**
- **`crewai[tools]==1.10.1`**
- **`.env`**: **`OPENAI_API_KEY`** (and any keys your agents need).

## Setup & run

From **`crew/debate/`**:

```bash
cd crew/debate
uv sync
crewai run
```

Change the motion in **`src/debate/main.py`** (`inputs` in **`run()`**).

## pyproject scripts

**`train`**, **`replay`**, **`test`**, **`run_with_trigger`** are listed but **`main.py` only defines `run()`** — add those functions before using `crewai train` / etc.

## References

- [CrewAI docs](https://docs.crewai.com)
- Assistant-oriented notes: **`AGENTS.md`**
