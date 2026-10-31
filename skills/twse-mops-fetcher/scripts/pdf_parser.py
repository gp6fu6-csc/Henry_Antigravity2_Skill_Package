import os
import re
import pdfplumber
import pandas as pd
from typing import List, Dict, Tuple

def parse_inventory_and_tables(pdf_path: str) -> Tuple[List[Dict], str]:
    """
    從 PDF 財報中搜尋並解析附註與表格（特別針對存貨明細）。
    回傳 (解析到的結構化資料列, 提取到的關鍵內文摘要)
    """
    extracted_rows = []
    extracted_text_blocks = []
    
    if not os.path.exists(pdf_path):
        print(f"[ERROR] 檔案不存在: {pdf_path}")
        return [], ""
        
    print(f"[*] 正在解析 PDF: {os.path.basename(pdf_path)}...")
    
    with pdfplumber.open(pdf_path) as pdf:
        total_pages = len(pdf.pages)
        for idx, page in enumerate(pdf.pages):
            page_num = idx + 1
            text = page.extract_text() or ""
            
            # Check if page contains inventory keywords
            if any(kw in text for kw in ["存貨", "原物料", "商品存貨", "在製品"]):
                extracted_text_blocks.append(f"=== Page {page_num} ===\n" + text)
                lines = text.split("\n")
                
                for line in lines:
                    # Match inventory lines like: "原 物 料 $ 41,314 $ 41,158 $ 27,189" or "商品存貨 145,131 82,129 33,915"
                    clean_line = re.sub(r'\s+', ' ', line.strip())
                    if any(item in clean_line for item in ["原物料", "原 物 料", "商品存貨", "在製品", "在 製 品", "在途存貨", "在 途 存 貨"]):
                        parts = clean_line.split(" ")
                        extracted_rows.append({
                            "頁碼": page_num,
                            "原始行內文": clean_line,
                            "項目": parts[0] if len(parts) > 0 else clean_line,
                            "內容": " ".join(parts[1:]) if len(parts) > 1 else ""
                        })
                        
    return extracted_rows, "\n\n".join(extracted_text_blocks)

def export_extracted_tables(pdf_path: str, output_excel_path: Optional[str] = None) -> Optional[str]:
    """
    將提取的表格資料匯出為 Excel 檔案。
    """
    rows, text_summary = parse_inventory_and_tables(pdf_path)
    if not rows and not text_summary:
        print(f"[INFO] 在 {os.path.basename(pdf_path)} 中未找到存貨細項。")
        return None
        
    if output_excel_path is None:
        base_no_ext = os.path.splitext(pdf_path)[0]
        output_excel_path = f"{base_no_ext}_存貨及表格資料.xlsx"
        
    df = pd.DataFrame(rows)
    df.to_excel(output_excel_path, index=False)
    print(f"[SUCCESS] 已匯出表格資料至: {output_excel_path}")
    return output_excel_path

if __name__ == "__main__":
    import sys
    test_pdf = sys.argv[1] if len(sys.argv) > 1 else "g:/我的雲端硬碟/股市研究/4195/財務報告書/4195_114年_202502_4195_AI1.pdf"
    export_extracted_tables(test_pdf)
