---
name: mattpocock-skill
description: "Matt Pocock's complete suite of agent skills for real engineering: includes grill-me / grill-with-docs (interview & stress-test designs), to-spec (spec generation), to-tickets (tracer-bullet issue breakdown), implement & implement-spec (task graph orchestration), tdd (test-driven development), code-review (standards & spec review), diagnosing-bugs, retro, domain-modeling, wayfinder, and triage. Use when the user asks for rigorous software engineering, disciplined planning, test-first development, code review, or mentions Matt Pocock's skills."
---

# Skills For Real Engineers (Matt Pocock Skills Suite)

> "My agent skills that I use every day to do real engineering - not vibe coding. These skills are designed to be small, easy to adapt, and composable. They work with any model. They're based on decades of engineering experience." — Matt Pocock

This skill serves as the central router, orchestrator, and guide for Matt Pocock's entire engineering workflow suite.

---

## 1. The Main Flow: Idea → Ship

The primary route for taking an idea from raw concept to verified production code:

```
[Idea / Request]
       │
       ▼
1. /grill-with-docs (or /grill-me) ────► Need throwaway code? ──► [/prototype + /handoff]
       │                                                                  │
       ├──────────────────────────────────────────────────────────────────┘
       ▼
2. /to-spec (Turn discussion into structured spec with test seams & user stories)
       │
       ▼
3. /to-tickets (Split into tracer-bullet tickets with blocking edges)
       │
       ├─────────────────────────────────┬─────────────────────────────────┐
       ▼                                 ▼                                 ▼
   Single Ticket                   Full Spec Graph                   Direct Feature
  [/implement]                   [/implement-spec]                      [/tdd]
       │                                 │                                 │
       └────────────────► [/tdd] ◄───────┘                                 │
                            │                                              │
                            ▼                                              ▼
                    [/code-review] ◄───────────────────────────────────────┘
                            │
                            ▼
                         [/pr]
                            │
                            ▼
                        [/retro] (Reflect & update environment, lint, standards)
```

### Step 1: Grilling (`/grill-with-docs` or `/grill-me`)
- **`/grill-with-docs`**: The default starting point in a project repository. Conducts a relentless, round-by-round interview to stress-test your design and clarify implicit assumptions. Retains knowledge statefully in `GLOSSARY.md` and Architecture Decision Records (ADRs).
- **`/grill-me`**: The stateless equivalent of `grill-with-docs` when working outside a repository (e.g. brainstorming a standalone proposal or writing).
- **Core Grilling Principle**: The agent finds *facts* (via subagents and repo inspection); the user makes *decisions*.

### Step 2: Prototyping Detour (`/prototype` + `/handoff`)
- When a design question requires executable validation (UI layout, state model, performance check), detour through a prototype.
- Use `/handoff` to bridge between sessions, build the prototype on a `prototype/<name>` branch, and feed lessons back into the main design thread.

### Step 3: Specifying (`/to-spec`)
- Synthesizes the conversation, agreed decisions, and codebase context into a rigorous specification without further interrogation.
- Documents problem statement, user stories, explicit test seams, and implementation decisions.

### Step 4: Ticketing (`/to-tickets`)
- Decomposes the spec into independent, tracer-bullet tickets.
- Explicitly declares blocking dependency edges between tickets.
- Supports GitHub Issues, GitLab Issues, or local markdown files under `.scratch/<feature>/issues/`.

### Step 5: Implementing with TDD (`/implement`, `/implement-spec`, `/tdd`)
- **`/implement`**: Works on a single ticket in a clean context window. Follows test-driven development (`/tdd`) and concludes with a code review.
- **`/implement-spec`**: Builds the entire spec by orchestrating implementer subagents across parallel frontier tickets on an integration branch.
- **`/tdd`**: Enforces strict test-driven red-green-refactor cycles.

### Step 6: Two-Axis Code Review (`/code-review`)
- Reviews changes against two independent criteria in parallel subagents:
  1. **Standards Axis**: Conformance to project `CODING_STANDARDS.md`, `CONTRIBUTING.md`, and Fowler code smell heuristics.
  2. **Spec Axis**: Faithful delivery of originating requirements and user stories.

### Step 7: Pull Request (`/pr`)
- Crafts high-impact PR descriptions highlighting the smallest visual change, before/after evidence, and one-way vs. two-way door decisions.

### Step 8: Retrospective (`/retro`)
- Analyzes the coding session to improve the **agent's environment** (steering rules, deterministic linter rules, test scaffolds, or documentation) rather than just fixing immediate code issues.

---

## 2. On-Ramps & Support Workflows

- **`/triage`**: Triage incoming issues and external PRs through canonical states (`needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`).
- **`/diagnosing-bugs`**: Systematic scientific diagnosis loop for elusive bugs and regressions. Demands a tight reproduction command before theorizing.
- **`/wayfinder`**: Map large, foggy multi-session greenfield initiatives into decision tickets before entering the implementation flow.
- **`/improve-codebase-architecture`**: Periodic maintenance scan for deep-module opportunities and interface thickening.
- **`/domain-modeling`**: Clarifies domain terms, resolves overloaded concepts, and records decisions in `GLOSSARY.md` and ADRs.
- **`/codebase-design`**: Deep-module vocabulary reference (module, depth, interface, seam, adapter, locality).

---

## 3. Standalone Utilities

- **`/wizard`**: Generates interactive shell scripts to walk humans through manual setup steps (tokens, secrets, cloud consoles).
- **`/teach`**: Interactive multi-session curriculum loop to teach a programming concept within the workspace.
- **`/to-questionnaire`**: Formulates targeted questionnaires when external stakeholder feedback is needed.
- **`/wait-what`**: Emergency circuit breaker when an agent's explanation fails to land; prompts a clear, jargon-free re-pitch.
- **`/handoff`**: Compacts session state into a portable handoff document for another agent, human, or fresh window.
- **`/setup-matt-pocock-skills`**: Scaffolds issue tracker, triage labels, and domain doc layout for a repository.

---

## 4. Context Hygiene & Smart Zone

Keep grilling, spec, and tickets in an unbroken context window within the **smart zone** (~150k tokens). Clear or handoff between implementation tickets to keep agent reasoning sharp.
