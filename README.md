# Henry Antigravity 2.0 Skill Package

本儲存庫整合了 Google Antigravity 2.0 所需的高效能 Agent 全域技能（Global Skills）與全域外掛模組（Global Plugins）。包含軟體工程研發規範、逆向工程、精準等角技術繪圖、語意程式碼圖譜、自主 LLM 研究、學術研究流水線、多智能體蜂群調度以及生產力工具。

---

## 📦 技能目錄總覽（共 24 個 Global Skills）

### 1. 軟體工程與逆向分析 (Engineering & Reverse Engineering)
- **`reverse-engineer-anything`** / **`Reverse-Engineer-Anythong`**：跨平台逆向工程利器（REA），支援原生二進位 (PE/ELF/Mach-O)、Electron/ASAR、行動端 APK/IPA、韌體二進位 (Binwalk/Unblob) 與協議逆向還原。
- **`mattpocock-skill`**：Matt Pocock 軟體工程行為準則套件（`/grill-me`, `/to-spec`, `/to-tickets`, `/tdd`, `/code-review`, `/retro` 等 39 個子技能）。
- **`codegraph`**：基於 Rust 內核 + Tree-sitter + SQLite (FTS5) 的 100% 地端語意程式碼圖譜與精確檢索引擎。
- **`karpathy-guideline-12`**：Andrej Karpathy 擴展版 12 條 LLM 與 Coding Agent 研發行為準則。
- **`karpathy-guideline`** / **`karpathy-guidelines`**：Andrej Karpathy 4 項核心編碼準則（思考後再寫代碼、簡潔優先、外科手術式修改、目標驅動執行）。
- **`github-workflow`**：Windows 本地 Git 與 GitHub 操作最佳實踐與憑證繼承。
- **`frontend-design`**：專業級前端 UI/UX 設計標準（Tailwind CSS / shadcn/ui），避免千篇一律的 AI 美學。

### 2. 視覺化、圖表與設計 (Visual, Diagrams & Technical Design)
- **`anatomy`**：極致細節之互動式 Isometric（等角軸測）SVG 技術圖解與儀器級架構圖製作，支援四色著色、實體機構繪製與 WebGL Shader 特效。

### 3. AI 研究與模型實驗 (AI Research & Experimentation)
- **`karpathy-autoresearch`**：Andrej Karpathy 自主 LLM 訓練研究框架（固定 5 分鐘時間預算、Muon 優化器、`val_bpb` 閉環評估）。
- **`academic-research-pipeline`**：進階多角色（教授、專利工程師、領域審稿員）學術與專利研究流水線。
- **`generic-research-workflow`**：自動文獻檢索、專利交叉比對與結構化研究報告生成。
- **`notebooklm`**：Google NotebookLM API / MCP 連接、資料庫查詢與文獻摘要工具。

### 4. 智慧代理與協同運算 (Swarm & Collaborative Compute)
- **`ruflo-swarm-orchestrator`**：多智能體蜂群調度器，支援動態任務分解與併行子 Agent 協作。
- **`my-aiagent-cowork`**：Antigravity 2.0 雲端大腦與地端 RTX 4060 GPU 協同運算配置。
- **`autonomous-execution-mode`**：自主執行模式規範，遇錯自動修復（Self-healing），無須停滯等待。

### 5. 技能管理與效能調校 (Skill Tooling & Performance)
- **`skill-creator`**：Agent Skill 創建、性能基準評估（Eval Viewer）與自動化測試套件。
- **`find-skills`**：Agent 技能探索與安裝指南。
- **`rtk`**：Windows Shell 萬用 Token 最佳化代理 CLI。

### 6. 商業與生產力工具 (Productivity & Financial Tools)
- **`project-report-doctomd`**：研究專案各類報告（Word / PDF / PPT）轉 Markdown 結構化文件與圖表擷取。
- **`officecli`**：微軟 Office 文件（Word、Excel、PowerPoint）檢視、排版檢查與批次編輯工具。
- **`twse-mops-fetcher`**：台灣公開資訊觀測站 (TWSE MOPS) 財報下載、表格解析與分析工具。

---

## 🚀 快速安裝（Windows PowerShell）

在 PowerShell 中執行以下指令即可將全部技能與外掛同步安裝至本機全域設定：

```powershell
.\install.ps1
```

所有技能將自動部署至 `~/.gemini/config/skills/` 與 `~/.gemini/config/plugins/`，在任何專案中皆可直接使用。
