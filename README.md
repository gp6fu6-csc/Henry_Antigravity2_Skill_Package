# Henry_Antigravity2_Skill_Package (Windows Version)

> [!WARNING]
> **ENVIRONMENT SPECIFICATION**: This package is currently designed and optimized exclusively for **Windows (PowerShell)** environments. 
> If you expand this package to macOS or Linux in the future, you MUST explicitly document and label the environment-specific sections and update this warning accordingly.

This is a unified skill and configuration package for Google Antigravity 2.0, curated by Henry. It contains custom global skills and guides for:
1. **Karpathy Guidelines** - Clean code and behavioral standards for LLMs.
2. **RTK (Rust Token Killer) Integration** - Standardized Windows-based token compression for shell commands.
3. **NotebookLM MCP Guide** - Secure management of NotebookLM MCP server and authentication troubleshooting.
4. **GitHub Workflow Guide** - Secure local git operations utilizing native Windows credentials.
5. **Academic Research Pipeline** - A multi-stage pipeline for deep academic, patent, and technical research.
6. **Skill Creator** - Official Anthropic tool to create, modify, and optimize skills.
7. **Frontend Design** - Official frontend design skill for crafting high-quality production-grade UIs.
8. **Find Skills (Skill.sh)** - Discovery and management tool to search/install agent skills via the skills.sh ecosystem.

---

## 📂 Package Structure

```
Henry_Antigravity2_Skill_Package/
├── README.md                  # This file
├── install.ps1                # Automated Windows installer script
├── uninstall.ps1              # Automated Windows uninstaller script
└── skills/
    ├── karpathy-guidelines/
    │   └── SKILL.md           # Karpathy clean coding guidelines
    ├── rtk/
    │   └── SKILL.md           # Windows RTK command integration rules
    ├── notebooklm/
    │   └── SKILL.md           # NotebookLM session and MCP guide
    ├── github-workflow/
    │   └── SKILL.md           # Git download/upload processes
    ├── academic-research-pipeline/
    │   └── SKILL.md           # Multi-stage technical & academic research pipeline
    ├── skill-creator/
    │   └── SKILL.md           # Official skill creation and optimization tool
    ├── frontend-design/
    │   └── SKILL.md           # Official premium UI/UX frontend design skill
    └── find-skills/
        └── SKILL.md           # Global agent skill search & discovery tool (Skill.sh)
```

---

## ⚙️ How to Sync and Install Across Computers (Windows)

Since this package is structured to be version-controlled on GitHub, you can set up a new environment in two simple steps:

### Step 1: Clone the Repository
Clone your GitHub repository to any directory on your new Windows machine:
```powershell
git clone <your-github-repo-url> Henry_Antigravity2_Skill_Package
cd Henry_Antigravity2_Skill_Package
```

### Step 2: Run the Installer
Run the automated installation script inside PowerShell. This will copy the skills globally into your Antigravity plugins directory (`~\.gemini\config\plugins\`):
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\install.ps1
```

To remove the skills at any time, run:
```powershell
.\uninstall.ps1
```

---

## 📋 Environment History and Rules for Future AIs

*   **Current Version**: `v1.0.0`
*   **Target OS**: Windows (PowerShell)
*   **Rule for future AI editors**: If the user asks to adapt this package for **macOS** or **Linux**, you **MUST** create separate folders (e.g., `skills-mac/`, `skills-linux/` or separate OS sections inside the skills) and clearly label the environment at the top of the README.md and the modified SKILL.md files. Do NOT overwrite Windows-specific configurations (like `.exe` paths or PowerShell wrapper scripts) in the main files.
