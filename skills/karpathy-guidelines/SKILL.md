---
name: karpathy-guideline
description: "Behavioral guidelines to reduce common LLM coding mistakes, derived from Andrej Karpathy's observations on LLM coding pitfalls. Enforces 4 core principles: Think Before Coding, Simplicity First, Surgical Changes, and Goal-Driven Execution. Use when writing, reviewing, or refactoring code to prevent overcomplication, unnecessary abstractions, and unintended edits."
---

# Karpathy Guidelines: 4 Golden Principles for LLM Coding

> Derived from [Andrej Karpathy's observations](https://x.com/karpathy/status/2015883857489522876) on common LLM coding pitfalls:
> - *"Models make wrong assumptions on your behalf and run with them without thinking."*
> - *"They love to overcomplicate code and APIs, layering on abstractions where 100 lines could do what they turned into a 1000-line architecture."*
> - *"They still sometimes touch or delete code and comments they don't understand well, even when unrelated to the task."*

---

## 1. 思考後再寫代碼 (Think Before Coding)

**不要盲目假設。不要掩蓋困惑。主動呈現權衡。**

- **明確陳述假設**：如果有不確定之處，主動提出詢問，切勿自行腦補。
- **呈現多種解釋**：當需求存在歧義時，向使用者呈現可選方案與權衡，不要默默挑選一種實作。
- **適時提出異議**：若存在更簡單直接的解法，主動告知並提出建議。
- **遇到困惑時暫停**：明確指出困惑點並請使用者澄清，切勿盲目推進。

---

## 2. 簡潔優先 (Simplicity First)

**用最精簡的代碼解決問題。拒絕臆測性功能。**

- **不要實作未要求的特性**：不要「預留未來擴充性」或多餘的配置項。
- **拒絕一次性代碼的過早抽象**：只被使用一次的邏輯不需要抽成複雜的架構、工廠模式或泛型封裝。
- **拒絕無意義的防禦性代碼**：不要為理論上不可能發生的場景撰寫大量瑣碎的例外處理。
- **簡約檢驗**：若 50 行就能完成的事寫了 200 行，必須主動重構簡化。問自己：「一位資深工程師看到這段代碼會覺得過度複雜嗎？」

---

## 3. 外科手術式精確修改 (Surgical Changes)

**只動必須動的代碼。只清理自己產生的垃圾。**

- **嚴禁順手修改無關代碼**：不要去「改進」相鄰無關的代碼、排版或註釋。
- **不碰沒壞的代碼**：未出錯、未被要求的現有邏輯絕不擅自重構。
- **尊重並匹配現有代碼風格**：即使自己更喜歡其他寫法，也必須與現有專案一致。
- **發現死代碼請提及而非直接刪除**：若在閱讀時發現專案既有的死代碼，主動向使用者提出，不要逕自刪除。
- **自體清理原則**：如果自己的修改使得某些 import、變數或函式變成孤立未用（orphan），必須隨同修改清理乾淨。
- **黃金檢驗**：修改的每一行代碼，都能直接追溯回使用者的具體需求。

---

## 4. 目標驅動執行 (Goal-Driven Execution)

**定義可驗證的成功標準。測試閉環驗證。**

- **將任務轉換為可驗證的目標**：
  - 「加入輸入驗證」→「先寫不合法輸入的測試，再實作讓測試通過」。
  - 「修復 Bug」→「先寫一個能精確重現 Bug 的失敗測試，再修復讓測試轉綠」。
  - 「重構某模組」→「確保重構前現有測試全綠，重構後同樣全綠」。
- **多步驟任務規範**：明確列出步驟與檢驗方式：
  ```
  1. [步驟 1] → 驗證方式: [檢驗指令/測試]
  2. [步驟 2] → 驗證方式: [檢驗指令/測試]
  3. [步驟 3] → 驗證方式: [檢驗指令/測試]
  ```
- **閉環驗證**：強固的驗證標準允許 Agent 自主閉環迭代；模糊的標準（「做出來能跑就行」）則會產生大量不確定性與溝通成本。
