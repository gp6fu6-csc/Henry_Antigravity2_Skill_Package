---
name: twse-mops-fetcher
description: 台灣公開資訊觀測站 (TWSE MOPS) 資料擷取與財務報告書 (PDF) 下載、表格解析及 Gemini 分析工具。
---

# TWSE MOPS Fetcher & Financial Report Analysis Skill

本 Skill 能讓使用者決定要從「台灣公開資訊觀測站 (TWSE MOPS)」獲取哪一種類型的資料（預設「財務報告書 (PDF)」），並自動建立結構化資料夾下載至電腦指定路徑，同時支援 PDF 附註表格（如存貨明細）解析與 Gemini 財報摘要報告生成。

---

## 🛠️ 目錄與檔案結構規範

下載檔案與分析結果將自動組織為：
```text
<指定儲存路徑>/
└── <股票代號>/
    └── <資料種類>/
        ├── <股票代號>_<民國年份>年_<PDF檔名>.pdf          # 原始財報 PDF 檔
        ├── <股票代號>_<民國年份>年_<PDF檔名>_存貨及表格資料.xlsx # 提取之結構化表格
        └── <股票代號>_<民國年份>年_<PDF檔名>_Gemini分析報告.md  # 財報關鍵摘要與分析
```

預設基礎儲存路徑為：`g:/我的雲端硬碟/股市研究`。

---

## 💻 執行方式 (Execution Protocol)

當使用者要求下載 MOPS 資料或分析財報時，執行以下命令：

```powershell
C:\Users\gp6fu\.mops_venv\Scripts\python.exe C:\Users\gp6fu\.gemini\config\skills\twse-mops-fetcher\scripts\main.py --stock <股票代號> --year <民國年份> --outdir "<儲存路徑>" --analyze
```

### 常用參數：
* `--stock`: 股票代號，單檔（例如 `4195`）或多檔逗號分隔（例如 `4195,2330`）。
* `--year`: 民國年份（例如 `114` 代表 2025 年）。
* `--type`: 資料種類（預設 `財務報告書`）。
* `--outdir`: 電腦指定路徑（預設 `g:/我的雲端硬碟/股市研究`）。
* `--analyze`: 加上此旗標可自動對 PDF 進行附註表格 (存貨明細) 提取與 Gemini 摘要報告生成。

---

## 範例指令 (Example Usage)

### 1. 下載基米 (4195) 114 年財務報告書並進行 Gemini 分析
```powershell
C:\Users\gp6fu\.mops_venv\Scripts\python.exe C:\Users\gp6fu\.gemini\config\skills\twse-mops-fetcher\scripts\main.py --stock 4195 --year 114 --outdir "g:/我的雲端硬碟/股市研究" --analyze
```

### 2. 批量下載台積電 (2330) 與鴻海 (2317) 114 年財報 PDF
```powershell
C:\Users\gp6fu\.mops_venv\Scripts\python.exe C:\Users\gp6fu\.gemini\config\skills\twse-mops-fetcher\scripts\main.py --stock 2330,2317 --year 114 --outdir "g:/我的雲端硬碟/股市研究"
```
