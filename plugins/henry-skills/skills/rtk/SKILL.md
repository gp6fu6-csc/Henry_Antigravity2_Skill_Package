---
name: rtk
description: Token-optimized CLI proxy for shell commands on Windows. Instructs the AI agent to always prefix Windows terminal commands with 'rtk' to save 60-90% tokens on terminal outputs.
---

# RTK (Rust Token Killer) Windows Guide

> [!IMPORTANT]
> **WINDOWS PATH**: On this system, RTK is installed globally.
> If the environment PATH has not refreshed yet in the current session, call it using its absolute path: `C:\Users\gp6fu\.rtk\rtk.exe`. Otherwise, use `rtk` directly.

When executing shell commands via terminal tools (like `run_command`), always prefix the command with `rtk` to minimize token consumption.

## Command Prefix Rules

Always translate raw commands into RTK-prefixed commands:

| Raw Windows Command | RTK Windows Command |
| :--- | :--- |
| `git status` | `rtk git status` |
| `git diff` | `rtk git diff` |
| `npm run test` | `rtk npm run test` |
| `npm run build` | `rtk npm run build` |
| `cargo test` | `rtk cargo test` |
| `dir` or `ls` | `rtk ls` (Note: prefer `list_dir` tool unless shell listing is required) |

## Meta Commands

Use these commands directly to monitor performance:
*   `rtk gain` - Show cumulative token savings.
*   `rtk gain --history` - Show command history with exact token savings.

## Why

RTK acts as a CLI proxy that filters, groups, truncates, and summarizes command outputs, removing noise (e.g. repetitive build progress logs, long compiler stacks) while keeping only what the LLM needs to know.
