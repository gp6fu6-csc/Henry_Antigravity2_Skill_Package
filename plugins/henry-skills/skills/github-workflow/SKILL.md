---
name: github-workflow
description: Guide for secure, automated local Git operations (clone, commit, push, branching) under Windows. Instructs the AI on how to utilize the user's native credentials transparently.
---

# GitHub local Workflow Guide (Windows)

This skill guides the AI on how to manage local repository synchronization with GitHub.

## 🤝 Native Credential Inheritance

*   **Rule**: Never ask the user for their GitHub username, password, or Personal Access Tokens (PATs) in the chat.
*   **Execution**: All Git commands executed by the AI (via `run_command`) run directly within the user's local Windows shell session. This means they automatically inherit the user's:
    *   Windows Credential Manager entries (HTTPS)
    *   SSH Agent keys (SSH)
    *   Local `.gitconfig` settings

If a push or pull fails due to `Authentication failed` or `Permission denied (publickey)`, instruct the user to run `git push` manually once in their terminal to trigger their system's interactive credential helper, then report back.

## 📥 Downloading (Cloning & Pulling)

*   **Cloning**: Use `git clone <repository> <destination>` to fetch remote repositories. Always verify that target directories do not overlap with existing project structures.
*   **Pulling**: Run `git pull origin <branch>` to fetch and integrate remote updates before starting substantial work.

## 📤 Uploading (Committing & Pushing)

When the user requests to save progress or upload changes to GitHub:

1.  **State check**: Run `rtk git status` (utilizing RTK) to verify modified files.
2.  **Surgical Staging**: Stage only the relevant files that correspond to the requested changes. Avoid staging unrelated config files or system caches.
3.  **Descriptive Commits**: Write concise, professional commit messages.
    *   *Example*: `git commit -m "feat: integrate RTK token compression for powershell"`
4.  **Safe Push**: Run `git push origin <branch>` to upload the changes.
