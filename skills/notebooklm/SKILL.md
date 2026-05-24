---
name: notebooklm
description: Guide to securely connect, query, and troubleshoot NotebookLM MCP servers under Windows. Addresses credential expiration, manual authentication, and Chrome profile privacy considerations.
---

# NotebookLM MCP Integration & Troubleshooting (Windows)

This skill guides the AI on how to interact with the NotebookLM MCP server and resolve authentication/permission errors.

## 🔑 Authentication & Token Management

If any NotebookLM MCP tool returns an authentication error (e.g., `RPC Error 16: Authentication expired`):

1.  **Call `refresh_auth` first**: Try running the `refresh_auth` tool to reload tokens from the disk cache.
2.  **Request User Authentication**: If the token reload still returns an error, do NOT attempt to bypass it automatically. Instead, instruct the user to run the authentication CLI tool on their host Windows terminal:
    ```powershell
    notebooklm-mcp-auth
    ```
3.  **Wait for User confirmation**: Once the user completes the browser login, call `refresh_auth` again to load the fresh session tokens.

## 🚨 Security & Privacy Rules

*   **Chrome Profile Isolation**: The `refresh_auth` tool may attempt to read cookies from the user's Chrome profile folder to automatically authenticate.
    *   **AI Precaution**: Explicitly advise the user to use a **dedicated, isolated Chrome Profile** for NotebookLM, rather than their main personal/business profile, to avoid exposing sensitive personal session cookies to local scripts.
*   **Data Sensitivity**: NotebookLM documents and RAG queries are processed remotely. Do NOT upload highly confidential data (such as proprietary algorithms, raw database exports, or unencrypted keys) unless the user explicitly commands it.

## 📂 Key Capabilities

The NotebookLM MCP server enables:
*   Listing notebooks: `notebook_list`
*   Creating notebooks: `notebook_create`
*   Querying notebook contexts: `notebook_query`
*   Adding Web URLs or Drive sources: `notebook_add_url`, `notebook_add_drive`
*   Creating studio artifacts: `audio_overview_create`, `mind_map_create`
