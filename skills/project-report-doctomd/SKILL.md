---
name: project-report-doctomd
description: Converts all research project documents (proposals, interim reports, final reports, results, shortnotes, PowerPoint presentations) into structured Markdown documents and extracts figure images. Use when user wants to convert project documents (PDF/PPT/Word) to Markdown reports.
---

# Project Report DocToMD (研究計畫文件全方位轉 .md 紀錄)

This skill provides a comprehensive workflow for converting research project documents (Word, PDF, PowerPoint) into clean, structured Markdown (`.md`) reports based on template architecture, automatically extracting and accurately naming figures (`圖.編號`).

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

1. **Text Extraction**:
   ```bash
   uv tool run --with "markitdown[all]" markitdown "path/to/document.pdf" -o "temp_extracted.md"
   ```

2. **Image Extraction & Caption Matching**:
   Use PyMuPDF (`fitz`) to extract embedded images and match captions (`圖 1`, `圖 2`, `圖 1(a)`):
   ```python
   import fitz, os, re
   
   pdf_path = "path/to/document.pdf"
   output_dir = "path/to/圖片"
   os.makedirs(output_dir, exist_ok=True)
   
   doc = fitz.open(pdf_path)
   for page_index in range(len(doc)):
       page = doc[page_index]
       image_list = page.get_images(full=True)
       blocks = page.get_text("dict")["blocks"]
       text_blocks = [b for b in blocks if b["type"] == 0]
   
       for img_index, img in enumerate(image_list):
           xref = img[0]
           base_image = doc.extract_image(xref)
           image_bytes = base_image["image"]
           image_ext = base_image["ext"]
           rects = page.get_image_rects(xref)
           if not rects: continue
           img_rect = rects[0]
   
           caption = f"圖_p{page_index+1}_{img_index+1}"
           min_dist = 9999
           for b in text_blocks:
               bbox = fitz.Rect(b["bbox"])
               if bbox.y0 >= img_rect.y1:
                   dist = bbox.y0 - img_rect.y1
                   if dist < 120 and dist < min_dist:
                       text = "".join([l["spans"][0]["text"] for l in b["lines"]]).strip()
                       match = re.search(r'圖\s*(\d+[a-zA-Z\(\)]*|-\d+)', text)
                       if match:
                           caption = f"圖{match.group(1)}"
                           min_dist = dist
   
           safe_caption = re.sub(r'[\\/*?:"<>|]', '_', caption)
           image_path = os.path.join(output_dir, f"{safe_caption}.{image_ext}")
           with open(image_path, "wb") as f:
               f.write(image_bytes)
   ```

3. **Template Formatting**:
   - Align content with target template (`提案樣板.md`, `期中樣板.md`, `結案樣板.md`, etc.).
   - Embed relative image links `![圖1 ...](圖片/圖1.jpeg)`.
   - Overwrite or write to the target template file in the destination folder.

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
