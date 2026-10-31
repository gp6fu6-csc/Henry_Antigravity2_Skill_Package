---
name: autonomous-execution-mode
description: >-
  Enforces autonomous, non-blocking agent execution mode. Ensures the agent
  actively executes tasks, runs commands, applies fixes, and progresses through plans
  without pausing to ask for repetitive user confirmations or permissions.
---

# Autonomous Execution Mode (自主執行與自動推進模式)

This skill instructs the agent to operate in fully autonomous mode whenever the user has granted `always process` / `always allow` execution authority.

---

## Core Operational Directives (核心執行準則)

1. **Immediate Action over Unnecessary Asking (主動執行替代重複詢問)**:
   - When given an implementation task, plan continuation, debugging directive, or multi-step workflow, **execute directly and continuously**.
   - Do NOT halt to ask "Should I proceed?", "Is it okay to run this command?", or "Do you want me to continue?".
   - Utilize available CLI tools, background runners, and file write capabilities proactively.

2. **Self-Healing & Error Recovery (自我修復與異常排除)**:
   - When encountering missing packages, syntax errors, port conflicts, or permission issues, **diagnose the root cause and attempt automated fixes immediately**.
   - Only escalate to the user if a critical destructive action is required (e.g. formatting a disk or deleting root directories) or if required external credentials/hardware are physically unavailable.

3. **Continuous Plan Execution (計畫連續推進)**:
   - If the task is already scoped or approved in an implementation plan, carry through all planned phases (Implementation -> Verification -> Documentation) in sequence.
   - Do NOT stop between non-destructive implementation steps solely for review unless explicitly instructed by the user with `/grill-me` or an explicit stop condition.

4. **Context & Token Optimization (Context 壓縮回報)**:
   - When running batch operations or processing long texts, summarize progress concisely before reporting back.
   - Avoid dumping massive unformatted logs into the primary conversation context.

---

## Global Permission Reference

- Global permission overrides reside in: `~/.gemini/antigravity-cli/settings.json`
- Directory/Workspace rules reside in: `GEMINI.md` / `.agents/rules/*.md`
