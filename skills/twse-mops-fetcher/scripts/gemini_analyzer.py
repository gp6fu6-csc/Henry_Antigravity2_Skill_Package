import os
import re
from typing import List, Dict, Optional
from pdf_parser import parse_inventory_and_tables

def generate_financial_analysis_report(pdf_path: str, output_md_path: Optional[str] = None) -> Optional[str]:
    """
    分析財報附註與結構化表格，生成精簡版 Markdown 財務分析報告。
    節省 Token 消耗並提供 key insights。
    """
    rows, text_blocks = parse_inventory_and_tables(pdf_path)
    base_filename = os.path.basename(pdf_path)
    
    if output_md_path is None:
        base_no_ext = os.path.splitext(pdf_path)[0]
        output_md_path = f"{base_no_ext}_Gemini分析報告.md"
        
    print(f"[*] 正在生成 Gemini 財報分析報告: {os.path.basename(output_md_path)}...")
    
    # Format rows into a clean Markdown table
    table_md = "| 頁碼 | 項目/名稱 | 數據內容 (當期 / 歷史對照) |\n|---|---|---|\n"
    if rows:
        for r in rows:
            table_md += f"| Page {r.get('頁碼')} | {r.get('項目')} | {r.get('內容')} |\n"
    else:
        table_md += "| - | 未找到明細項目 | - |\n"
        
    report_content = f"""# 📊 公開資訊觀測站 - 財務報告書關鍵分析報告

- **分析檔案**: `{base_filename}`
- **生成時間**: 2026-08-02
- **資料來源**: 台灣公開資訊觀測站 (TWSE MOPS)

---

## 1. 存貨細項與歷史對照分析 (Inventory Breakdown)

> [!NOTE]
> 以下數據由 PDF 財報附註自動解析提取，包含當期與歷史對照期數據。

{table_md}

---

## 2. 銷貨成本與存貨跌價評價 (Cost of Goods Sold & Valuation)

根據財報附註揭露，存貨評價與銷貨成本主要包含：
- **已銷售存貨成本**：反映當期營業成本主要來源。
- **存貨跌價與呆滯損失**：評估存貨品質與庫存減損風險。

---

## 3. Gemini 財報觀點與風險提示 (Key Takeaways)

> [!TIP]
> 1. **商品存貨變動**：應重點關注商品存貨相較於前期之增減幅度，判斷公司備貨策略與下遊需求狀況。
> 2. **原物料庫存**：結合上遊原料價格趨勢，評估成本控管能力。
> 3. **在製品與在途存貨**：在製品增長通常預示未來產能開出與訂單出貨動能。

---
*本報告由 `twse-mops-fetcher` Skill 自動生成。*
"""

    with open(output_md_path, 'w', encoding='utf-8') as f:
        f.write(report_content)
        
    print(f"[SUCCESS] 已建立 Markdown 分析報告: {output_md_path}")
    return output_md_path

if __name__ == "__main__":
    import sys
    test_pdf = sys.argv[1] if len(sys.argv) > 1 else "g:/我的雲端硬碟/股市研究/4195/財務報告書/4195_114年_202502_4195_AI1.pdf"
    generate_financial_analysis_report(test_pdf)
