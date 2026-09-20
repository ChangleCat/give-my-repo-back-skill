# Give My Repo Back!

**Let AI write the tasks. Do the engineering yourself. Take your repository back.**

English | [简体中文](README.zh-CN.md)

[![Validate skill](https://github.com/ChangleCat/give-my-repo-back-skill/actions/workflows/validate.yml/badge.svg)](https://github.com/ChangleCat/give-my-repo-back-skill/actions/workflows/validate.yml)

Vibe coding can leave you with a working project whose internals you cannot explain. The AI chose the architecture, wrote the code, and fixed the failures. Now you want to put it on your résumé—and answer questions about it with confidence.

Give My Repo Back! turns that situation into a learning workflow. The agent investigates your repository, documents a real need, and designs atomic tasks for **you** to complete. You read, predict, investigate, implement, test, and explain. The agent coaches and reviews your work.

Skill ID: `give-my-repo-back-skill`

## What you get

- A repository brief grounded in files, symbols, and observed behavior.
- A requirement document with acceptance scenarios and decisions for you to investigate.
- A dependency-aware roadmap and actionable task cards, with one card active at a time.
- Graduated hints when you get stuck.
- Review of both your result and your understanding.
- A record of demonstrated capabilities, AI assistance, and remaining learning gaps.
- Interview practice based on work you actually performed.
- A proactive start menu when you load the skill without a prepared requirement.
- A zero-knowledge route from running the project to tracing and changing one observable path.
- Human-made, evidence-backed runtime flow maps for learning bounded system slices.
- A rough effort estimate and a concrete first-five-minutes action on each active card.

All generated learning documents follow your language. Ask in Simplified Chinese and the agent writes Chinese titles, instructions, tables, hints, and review feedback. Code identifiers, paths, and machine-readable keys stay intact.

## Install

### With the Skills CLI

Requires Node.js/npm with `npx`. Run from the repository you want to study.

```sh
npx skills add ChangleCat/give-my-repo-back-skill --skill give-my-repo-back-skill
```

Choose your agent and installation scope in the installer. For a global OpenCode installation:

```sh
npx skills add ChangleCat/give-my-repo-back-skill --skill give-my-repo-back-skill --agent opencode --global
```

For a local checkout, use its absolute path:

```sh
npx skills add /absolute/path/to/give-my-repo-back-skill --skill give-my-repo-back-skill
```

Inspect, update, or remove an installation:

```sh
npx skills list
npx skills update give-my-repo-back-skill
npx skills remove give-my-repo-back-skill
```

Use `--global` for global removal. For a manually copied installation, replace or remove only its dedicated skill folder. CLI syntax and supported agent IDs are documented in the [Skills CLI README](https://github.com/vercel-labs/skills#readme).

### Manual installation

Download this repository's ZIP from GitHub or clone it, then copy `SKILL.md` and the entire `references/` directory into a folder named `give-my-repo-back-skill` under your harness's documented skill directory. Include `LICENSE` when redistributing. `agents/` is optional; README and example files are not required at runtime.

For example, OpenCode documents `.opencode/skills/` for project skills and `~/.config/opencode/skills/` for user skills. A project installation looks like this; see [OpenCode's skill documentation](https://opencode.ai/docs/skills/).

```text
your-project/
└── .opencode/skills/give-my-repo-back-skill/
    ├── SKILL.md
    ├── LICENSE
    └── references/
        ├── artifacts.md
        ├── coaching-and-review.md
        └── system-map.md
```

Other harnesses may use different directories or activation rules. Follow their documentation instead of assuming one path works everywhere. Reload skills or start a new session as required by your harness.

### Without native skill support

Keep the skill folder somewhere the agent can read and ask:

```text
Read /absolute/path/to/give-my-repo-back-skill/SKILL.md and follow its
referenced instructions. Apply this workflow to my current project.
You design the tasks; I will investigate and implement them.
```

If the interface cannot read files, provide `SKILL.md` and the referenced documents as context, then share the relevant project files as needed. The agent must identify evidence it cannot inspect.

## Start your first session

Open the project you want to understand and name the skill in your request. A portable starting prompt is:

```text
Use give-my-repo-back-skill on this repository. Find a small, useful
improvement that will help me understand its request flow. Write the
requirements and task cards in English under docs/repo-ownership/.
Give me the first card and let me do the implementation.
```

If you already have a need:

```text
Use give-my-repo-back-skill. I want to add pagination to the task list
myself. Investigate the current behavior, document the requirement,
and break it into atomic cards. Let me make the design decisions.
```

For interview preparation:

```text
Use give-my-repo-back-skill to help me understand the authentication
subsystem. Assign practical investigation and change tasks, then ask
me interview questions about what I actually did.
```

Native invocation syntax varies by harness. Naming the skill or explicitly pointing to its file avoids depending on a particular slash command or UI.

If you load the skill without a detailed request, the agent should proactively offer four ways to begin: bring your own need, let it scout the repository, choose an area to learn, or resume earlier work. You can simply choose the recommended repository scan when you are unsure.

## How a session works

1. **Choose a target.** Bring a requirement, choose a subsystem, or ask the agent to find useful work.
2. **Read the brief and requirement.** Understand the current behavior, intended outcome, and open decisions.
3. **Take one card.** Predict what will happen and form a plan before editing.
4. **Do the work.** Inspect, implement, and validate; request a hint when needed.
5. **Bring evidence.** Submit your diff, output, trace, or observations with the repository revision and applicable scope. Checks are recorded as `pass`, `fail`, or `not_run`; `not_run` does not prove that the code is correct.
6. **Explain it.** Defend the flow, decision, and a failure mode or alternative.
7. **Continue.** The agent records evidence and adapts the next card.

A working change alone does not close a card. You also need to explain the part it teaches. When the agent supplies implementation at your request, it records that assistance and proposes a recovery exercise.

If you start with little or no repository knowledge, the first cards should help you run one documented check, locate an entry point, trace one path, draw a small system map, and make a low-risk observable change. The default map is a numbered runtime flow plus an evidence index: you draw the prediction, revise it from repository evidence, and explain it back. Mermaid is convenient but not required. You do not need to choose a feature before you can begin.

See a [complete example card](examples/atomic-task-card.md) or its [Simplified Chinese version](examples/atomic-task-card.zh-CN.md). These use a fictional repository to show the format; real cards must cite your repository.

## Documents and resuming work

When requested, learning artifacts are written inside the project being studied:

```text
docs/repo-ownership/
├── ownership-brief.md
├── requirements.md
├── roadmap.md
├── ledger.md
├── maps/
│   └── GMRB-002-create-task.md
└── cards/
    └── GMRB-001.md
```

These ordinary Markdown files carry progress between sessions and harnesses. Ask a new agent to load the skill and resume from this directory. It should check repository changes, reuse existing IDs and notes, and continue from the recorded next action. Evidence remains part of the learning history, but a material change to the behavior or inputs it covered changes its validity from `current` to `needs_recheck`; unrelated changes leave it alone. Discussion-only sessions can keep artifacts in the conversation.

The optional `maps/` directory is created only when a system-map card benefits from a persistent artifact. A small session does not need it.

## Harness compatibility

The core uses the [Agent Skills file structure](https://agentskills.io/specification): `SKILL.md` plus relative reference files. It requires no Codex APIs, MCP server, vendor-specific task manager, or runtime package. `agents/openai.yaml` only supplies optional Codex display metadata; other tools can ignore it.

The design targets open-source and other coding harnesses that can load instructions and inspect repository files. Native discovery is harness-specific; explicit file loading is the fallback. **Cross-harness execution has not been tested.** Format portability is a design goal, not a claim that every agent follows the coaching contract correctly.

Repository source, comments, logs, and ordinary documentation are treated as evidence during investigation. Instructions embedded in that content cannot authorize secret disclosure, external uploads, destructive operations, or unrelated scope expansion.

## Validation

GitHub Actions validates every push and pull request with version `0.1.1` of the Agent Skills reference validator. Run the same check locally with an absolute path:

```sh
uvx --from skills-ref==0.1.1 agentskills validate /absolute/path/to/give-my-repo-back-skill
python /absolute/path/to/give-my-repo-back-skill/scripts/validate_project.py
```

The second command checks local Markdown links and verifies that the English and Simplified Chinese READMEs retain the same essential sections and installation markers.

## Project contents

| Path | Purpose |
| --- | --- |
| [SKILL.md](SKILL.md) | Portable agent instructions and workflow |
| [references/](references/) | Artifact templates, human-made system-map protocol, and coaching/review protocol |
| [examples/](examples/) | English and Chinese example task cards |
| [scripts/validate_project.py](scripts/validate_project.py) | Local link and bilingual README checks used by CI |
| [agents/openai.yaml](agents/openai.yaml) | Optional Codex display metadata |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Contribution and review guidance |
| [LICENSE](LICENSE) | MIT license |

## Contribute

Useful contributions include better task design, clearer multilingual output, and concrete reports of where an agent took over human work. Read [CONTRIBUTING.md](CONTRIBUTING.md). Please distinguish observed behavior from untested compatibility claims.

When publishing a fork, update the installation addresses in both READMEs to point to your repository. There is no build step or package registry publish step: the repository itself is the skill source.

## License

[MIT](LICENSE).
