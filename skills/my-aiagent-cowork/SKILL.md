---
name: my-aiagent-cowork
description: >-
  Antigravity 2.0 與地端 LLM 協同作業核心技能 (Hybrid AI Agent Collaboration Skill)。
  當使用者需要進行 AI Coding、大量文獻/文件檢索解析、長篇報告起草或批次自動化任務時啟用。
  在執行任務前，必須先主動向使用者呈現「雲端大腦與地端模型的工作分工表 (Hybrid Allocation Plan)」，
  說明哪些架構/審查工作維持雲端處理，哪些繁重生成/摘要/向量運算指派給地端 RTX 4060 GPU 執行，以達到極致節省 Token 與高效能產出。
---

# My_AIAgent_Cowork (雲地協同智慧 Agent 技能)

本技能定義 Antigravity 2.0 (雲端高階智商大腦) 與本機地端 LLM (ROG Flow Z13 / RTX 4060 GPU) 之間的協同作業標準流程。

---

## 🎯 核心運作原則 (Operational Directives)

### 1. 任務前置：輸出分工透明化表格 (Pre-task Allocation Declaration)
在接收使用者指派的任何中大型任務時，**在開始呼叫工具執行前，必須先主動輸出「雲地協同分工表」**，向使用者清楚說明任務拆解：

```markdown
### 🤝 雲地協同工作分工規劃 (Hybrid Task Allocation)

| 任務階段 / 子項目 | 運算端點 | 指派模型 / 工具 | 運作目的與 Token 節省效益 |
|---|---|---|---|
| 1. 任務架構拆解與決策規劃 | ☁️ 雲端 AI | Antigravity 2.0 (Gemini 3.7) | 負責整體架構設計、品質標準制定與邏輯引導 |
| 2. 原始代碼/草稿/長文初探 | 💻 本機地端 | 地端專屬模型 (如 phi4 / llama3.1 / gemma4) | 於本機 GPU 生成大量文本/程式碼，**0 雲端 Token 消耗** |
| 3. 跨文獻向量比對 / 資料檢索 | 💻 本機地端 | nomic-embed / DDGS 搜尋 | 本地向量運算與隱私搜尋，原始長文不送雲端 |
| 4. 程式碼驗證、審查與最終交付 | ☁️ 雲端 AI | Antigravity 2.0 | 審查地端產出代碼、修復潛在 Bug、整合排版並交付 |
```

---

## 🤖 地端模型角色對應矩陣 (Local LLM Dispatch Matrix)

| 業務類型 | 地端調度模型 | 調度 API / 腳本 | 特性與參數要求 |
|---|---|---|---|
| **AI 程式編寫 (Coding)** | `phi4:14b-q4_K_M` | `http://127.0.0.1:11434/api/generate` | 邏輯嚴密，適合繁複函式、演算法、單元測試 |
| **長文摘要 / Context 壓縮** | `gemma4:e4b` | `http://127.0.0.1:11434/api/generate` | 4000 字元自動分塊，將長文壓縮為精簡 JSON |
| **文件起草 / 報告撰寫** | `llama3.1:8b-instruct-q5_K_M` | `http://127.0.0.1:11434/api/generate` | 100% GPU 顯存運算，繁中流暢，起草章節段落 |
| **向量嵌入 (Embeddings)** | `nomic-embed-text:v1.5` | `http://127.0.0.1:11434/api/embed` | 768 維本地向量運算，RAG 語意比對 |
| **中文超長文 (隔離模式)** | `qwen3:8b` | `http://127.0.0.1:11434/api/generate` | 務必帶入 `num_predict: 2048` 防止思考鏈死循環 |

---

## 🛠️ 地端模型調用方式 (How to Dispatch Locally)

### 方式 A：透過 Python 腳本調用 (推薦，穩定可靠)
在執行過程中，可直接使用專案虛擬環境的 Python 調用地端 Ollama API：
```python
import requests

response = requests.post(
    "http://127.0.0.1:11434/api/generate",
    json={
        "model": "phi4:14b-q4_K_M",  # 或 llama3.1:8b-instruct-q5_K_M / gemma4:e4b
        "prompt": "<具體任務提示詞>",
        "stream": False
    },
    timeout=180
)
local_result = response.json().get("response", "")
```

### 方式 B：透過自動化批次處理器
若針對 `workspace/uploads/` 中的多份文件：
```powershell
.\.venv\Scripts\python.exe scripts\batch_processor.py
```

---

## 🔄 任務執行標準流程 (Execution Lifecycle)

1. **宣示分工**：主動列出雲端與地端的工作分工表。
2. **地端執行**：調用本機 RTX 4060 GPU 進行重度生成/解析，將原始檔案或草稿留在本地。
3. **雲端精煉**：Antigravity 讀取地端產出的結果，進行邏輯重構、排版潤飾與品質驗收。
4. **成果歸檔**：將最終成品（代碼、Markdown 報告）保存至專案結構或 `workspace/outputs/`。
