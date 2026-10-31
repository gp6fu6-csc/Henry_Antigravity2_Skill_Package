---
name: generic-research-workflow
description: Automatically conducts literature and patent searches, decomposes topics, drafts research proposals and presentation slides based on the project configuration. Triggers when the user wants to run a research workflow, generate proposals/slides for academic or patent topics, or needs a structured research report.
version: 1.0.0
metadata:
  openclaw:
    homepage: https://github.com/JimLiu/baoyu-skills#generic-research-workflow
    requires:
      anyBins:
        - python
---

# Generic Research Proposal & Literature/Patent Search Workflow

本技能可協助 AI 代理人自動執行全套的科研主題文獻與專利檢索，並直接產出高品質的書面提案報告與簡報投影片。

## 適用場景

當用戶提出以下需求時，應觸發並使用本 Skill：
* 針對特定技術主題（例如：「鋼捲邊緣缺陷檢測」）進行專利或學術論文檢索。
* 需要撰寫研究提案（Research Proposal）或技術分析報告。
* 需要自動生成技術簡報（Presentation Slides）。
* 需要建立一個結構化的科研專案目錄以存放原始論文、圖片與摘要。

## 運作原理

本 Skill 的核心由兩個 Python 腳本驅動：
1. `scripts/patent_literature_crawler.py`：負責串接學術與專利 API 進行檢索，並具有離線生成 fallback 功能。
2. `scripts/run_workflow.py`：工作流的核心引擎，負責讀取 `project_config.yaml`，調用爬蟲，將抓取回來的 raw data 進行兩階段精煉，在 `workspace/patent_academic_survey/` 目錄下建立獨立子資料夾存放原始文件、代表性圖片與摘要檔，並最終拼裝成符合 APA 7th 格式的 Proposal 書面與 Slides 簡報。

## 執行流程與 AI 引導指南

身為執行此技能的 AI，請遵循以下步驟：

### 步驟 1：初始化專案目錄與配置

在用戶指定的研究工作區（以下簡稱 `{project_path}`）中，建立或確認存在 `project_config.yaml` 檔案。

#### `project_config.yaml` 格式範例
```yaml
project_name: "基於高精度鋼捲側緣三維掃描的缺陷檢測與分析技術"
template: "steel_coil"  # 若為鋼捲相關主題使用 steel_coil，其他主題使用 generic
keywords:
  - "3D Steel Coil Edge Scan"
  - "Coil Protrusion Baseline Fitting"
  - "Overlap Defect Detection AI"
stages:
  1_提案準備:
    output_dir: "workspace/patent_academic_survey/drafts"
    paper_name: "paper_proposal.md"
    slides_name: "slides_proposal.md"
```

### 步驟 2：執行工作流引擎

使用系統的 terminal 工具，執行以下指令啟動工作流：

```powershell
python "{baseDir}/scripts/run_workflow.py" "{project_path}"
```
*(註：`{baseDir}` 為此 `SKILL.md` 所在的絕對路徑；`{project_path}` 為科研專案工作區目錄的絕對路徑。)*

### 步驟 3：產出驗證與歸檔

工作流會自動在 `{project_path}/workspace/patent_academic_survey/` 下生成以下架構：
* `papers/paper_themeX_YY/` 及 `patents/patent_branchX_YY/`：內含原始 PDF/Word、代表圖與摘要。
* `results/`：包含最終產出成果（`final_report.md` 與 `slides_report.md`）。

作為執行此技能的 AI，在執行完工作流後，請巡檢產出的檔案，確認提案書及簡報的完整性，並在此對齊用戶的具體需求（例如特定缺陷標準或定量指標）。
