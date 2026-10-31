---
name: project-report-doctomd
description: Converts all research project documents (proposals, interim reports, final reports, results, shortnotes, PowerPoint presentations) into structured Markdown documents and extracts figure images. Use when user wants to convert project documents (PDF/PPT/Word) to Markdown reports.
---

# Project Report DocToMD (研究計畫文件全方位轉 .md 紀錄)

This skill provides a comprehensive workflow for converting research project documents (Word, PDF, PowerPoint) into clean, structured Markdown (`.md`) reports based on template architecture, automatically extracting and accurately naming figures (`圖.編號`) and tables.

## Supported Document Types
- **提案報告 (Proposal)**: Template `提案樣板.md`
- **期中報告 (Interim Report)**: Template `期中樣板.md`
- **結案報告 (Final Report)**: Template `結案樣板.md`
- **成果 (Results)**: Template `成果樣板.md` (or standard results structure)
- **Shortnote**: Template `Shortnote樣板.md`
- **PowerPoint / PPT-derived PDFs**: Converted into `投影片.md` with slide-by-slide headings (`## 投影片 P.X`).

---

## Phase 1: Pre-conversion Confirmation Protocol (Mandatory)

Before executing any file conversion, the agent **MUST** list the detected parameters and ask the user to confirm.

### Detection Heuristics
1. **Report Type (報告類型)**:
   - File contains `(提)` or `提案`: `提案報告`
   - File contains `(期中)` or `期中`: `期中報告`
   - File contains `(結)` or `結案`: `結案報告`
   - File contains `(成)` or `成果`: `成果`
   - File contains `ShortNote` or `Shortnote`: `Shortnote`
   - *If uncertain*: Ask user to select.
2. **Research Area (研究主題)**:
   - Infer from filename or directory path history (e.g., `熱軋產線`).
3. **Research Topic (研究題目)**:
   - Infer project title from file name (e.g., `熱軋捲形量測系統開發與資訊整合平台建置`).
4. **Source Format (文件格式性質)**:
   - Check if source is a Word-like document vs a PowerPoint / PPT-derived PDF.

### Confirmation Table Format
Present the following summary table to the user and request confirmation:

```markdown
| 項目 | 自動判讀結果 | 請確認/修正 |
| --- | --- | --- |
| **報告類型** | 結案報告 | [提案報告 / 期中報告 / 結案報告 / 成果 / ShortNote] |
| **研究主題** | 熱軋產線 | [例如: 熱軋產線 / 冷軋產線 ...] |
| **研究題目** | 熱軋捲形量測系統開發與資訊整合平台建置 | [專案名稱] |
| **文件性質** | Word-like 文件 / PowerPoint 簡報檔 | [Word-like / PPT] |
| **預計輸出目錄** | `研究領域/{研究主題}/{研究題目}/{報告類型}/` | |
| **預計輸出檔名** | `結案樣板.md` (或 `投影片.md`) | |
```

---

## Phase 2: Conversion Workflow

### Approach A: Word-like Document Conversion

1. **Text Extraction & Full Content Integrity**:
   - Extract full text without summarization or truncation.
   - Use `markitdown` or `fitz` for general text extraction.

2. **Table Extraction (Preventing Vertical Alignment Corruption)**:
   - **CRITICAL**: Do NOT rely on raw text line extraction for PDF tables. Narrow vertical-header cells (e.g. `技\n術`) will break into vertical single-character lists.
   - Use `pdfplumber` (or PyMuPDF `page.find_tables()`) to extract PDF table matrices.
   - Convert table matrices into clean GitHub Flavored Markdown (GFM) tables:
     ```python
     def table_to_gfm(table_data):
         clean_table = []
         for row in table_data:
             if not row: continue
             clean_row = [str(c).strip().replace('\n', '<br>') if c is not None else "" for c in row]
             if any(clean_row): clean_table.append(clean_row)
         if not clean_table: return ""
         num_cols = max(len(r) for r in clean_table)
         lines = ["| " + " | ".join(clean_table[0]) + " |", "| " + " | ".join(["---"]*num_cols) + " |"]
         for r in clean_table[1:]: lines.append("| " + " | ".join(r) + " |")
         return "\n".join(lines)
     ```

3. **Page-Clipped Image Extraction & Precise Figure Naming**:
   - **CRITICAL**: Do NOT extract raw XObject streams blindly, as composite figures/drawing objects will split into fragments like `-3.jpeg` or fallback to `圖_p1_1.png`.
   - Scan page text for figure captions (`圖 1`, `圖 2`, `圖 3`...).
   - Match captions with page image bounding boxes (searching BOTH above and below captions within 300pt).
   - Render page clips using `page.get_pixmap(clip=crop_box, dpi=200)` and save strictly named after the figure caption: `圖1.png`, `圖2.png`, `圖3.png`.

   ```python
   import fitz, re, os

   def extract_figures_clean(pdf_path, output_dir):
       os.makedirs(output_dir, exist_ok=True)
       doc = fitz.open(pdf_path)
       extracted = {}
       for page_idx, page in enumerate(doc):
           blocks = page.get_text("dict")["blocks"]
           captions = []
           for b in blocks:
               if b.get("type") == 0:
                   for line in b.get("lines", []):
                       txt = "".join([s.get("text", "") for s in line.get("spans", [])]).strip()
                       m = re.match(r'^(圖)\s*(\d+[a-zA-Z\(\)]*)[\s\:\：\.\s]*(.*)', txt)
                       if m:
                           captions.append({"num": m.group(2), "bbox": fitz.Rect(line["bbox"])})
           img_rects = [r for img in page.get_images() for r in page.get_image_rects(img[0])]
           for c in captions:
               fig_key = f"圖{c['num']}"
               if fig_key in extracted: continue
               target_rect, min_dist = None, 9999
               for r in img_rects:
                   dist = abs(c['bbox'].y0 - r.y1) if r.y1 <= c['bbox'].y0 else (abs(r.y0 - c['bbox'].y1) if r.y0 >= c['bbox'].y1 else 0)
                   if dist < min_dist: min_dist, target_rect = dist, r
               crop_box = fitz.Rect(max(0, target_rect.x0-5), max(0, target_rect.y0-5), min(page.rect.width, target_rect.x1+5), min(page.rect.height, target_rect.y1+5)) if (target_rect and min_dist < 300) else fitz.Rect(max(0, c['bbox'].x0-200), max(0, c['bbox'].y0-250), min(page.rect.width, c['bbox'].x1+200), max(0, c['bbox'].y0-5))
               pix = page.get_pixmap(clip=crop_box, dpi=200)
               img_path = os.path.join(output_dir, f"{fig_key}.png")
               pix.save(img_path)
               extracted[fig_key] = f"{fig_key}.png"
       return extracted
   ```

4. **Precise Image Link Embedding in Markdown**:
   - Do NOT use naive `str.replace("圖1", ...)` on text, which corrupts inline text citations like `(如圖1所示)`.
   - Replace only standalone Figure Title lines (`圖 1 相機配置圖`) with `![圖1 相機配置圖](圖片/圖1.png)`.

5. **Template Alignment**:
   - Fill in frontmatter, `# 結案摘要`, `# 目標達成情形`, `# 單頁報告`, and `# 結案內文`.
   - Overwrite target template file in destination folder.

---

### Approach B: PowerPoint / PPT-derived PDF Conversion

When the source document is identified as a PowerPoint presentation or a PDF converted from PPT:

1. **Output File Name**: `投影片.md` (saved inside the target report folder).
2. **Page-by-Page Structure**:
   Each slide is mapped to a section heading:
   ```markdown
   ## 投影片 P.1
   [Slide 1 Text Content / Notes]
   ![投影片 P.1 截圖](圖片/投影片_P1.png)

   ## 投影片 P.2
   [Slide 2 Text Content / Notes]
   ![投影片 P.2 截圖](圖片/投影片_P2.png)
   ```
3. **Slide Image Export**:
   Export each slide page as a high-resolution image (`投影片_P1.png`, `投影片_P2.png`, etc.) using PyMuPDF `page.get_pixmap()` so that the visual presentation of every slide is completely preserved alongside the extracted text.

---

## Phase 3: Cleanup

Always clean up temporary files (`temp_extracted.md`, helper python scripts) after conversion completes.
