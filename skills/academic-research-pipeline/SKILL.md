---
name: academic-research-pipeline
description: An advanced multi-agent collaborative pipeline (Professor, Patent Engineer, SPM) for deep academic/patent research utilizing specialized search tools (OpenAlex, arXiv, PubMed, Google Patents, Lens, Espacenet, WIPO), NotebookLM, and seamless direct Google Drive / Gemini Web export integration.
---

# Academic & Patent Multi-Agent Research Pipeline (Windows)

This skill guides the AI to orchestrate a collaborative multi-agent simulation (**University Professor**, **Global Patent Engineer**, and **Senior Product Manager**) to conduct deep literature and patent research. It incorporates specialized search APIs, NotebookLM RAG, and **direct integrations with pre-existing NotebookLM notebooks and Gemini Web exports (saved as Google Docs in Google Drive)**.

---

## 🛠️ Folder & File Structure

The pipeline operates strictly within the workspace folders and produces standardized deliverables:

```
./workspace/drafts/
├── Global_Review.md                     # Master Technical Report (Ch 1-3)
├── References.md                        # Master Bibliography (APA 7th Edition)
├── slides_review.md                     # Slide Deck (Marp Markdown format)
├── academic_review/                     # Academic reviews and images
│   ├── paper_[主題編號]_[文章編號].md
│   └── paper_[主題編號]_[文章編號]_architecture.jpg (or Mermaid diagrams)
└── patent_review/                       # Patent reviews and diagrams
    ├── patent_keywords.json             # Multilingual keyword mappings
    ├── patent_[技術分支編號]_[專利號].md
    └── patent_[技術分支編號]_[專利號]_diagram.jpg (or Mermaid diagrams)
```

---

## 📋 Multi-Stage Pipeline Execution

The AI MUST execute the workflow sequentially, acting as the designated specialist agent at each stage:

### 1. Stage 0: Automated Existing Assets Ingestion (Roles: All Agents)
At the very beginning of the session, the AI **MUST actively prompt the user** to prevent them from forgetting to leverage pre-existing research.
*   **The AI Prompt**: The AI must output a clean, interactive greeting asking:
    1.  *"Do you have any existing NotebookLM notebooks for this topic?"*
    2.  *"Do you have any Gemini Web research exported directly to Google Docs in your Google Drive?"*
*   **Direct NotebookLM Integration**:
    *   If the user has an existing notebook, the AI MUST call `notebook_list` to list all notebooks, let the user select one, and set it as the active research workspace.
*   **Direct Gemini Web (Google Docs) Integration**:
    *   Gemini Web allows users to click **"Export to Docs" (匯出至 Google 文件)** at the bottom of any response.
    *   To avoid manual copy-pasting, the AI **MUST call `source_list_drive`** to list files in the user's Google Drive.
    *   The AI will present a list of recent Google Docs and let the user select their exported Gemini Web research file.
    *   Once selected, the AI will pull the document content or directly link it to the research notebook using `notebook_add_drive`.

### 2. Stage 1: Topic Decomposition & Strategy (Role: Senior Product Manager)
*   **Action**: Create `implementation_plan.md` in the artifacts directory.
*   **Task**:
    *   Decompose the research topic into **`N` core technical sub-topics**.
    *   **Merge the pre-existing Gemini/NotebookLM findings** into the sub-topics, ensuring previously collected data acts as the baseline knowledge.
    *   Outline new search queries to fill any technical gaps.
*   **Gate**: Wait for **explicit user approval** on the sub-topic architecture before proceeding.

### 3. Stage 2: Parallel Literature & Patent Retrieval (Roles: Professor & Patent Engineer)
The AI assumes these roles to perform deep retrieval for each of the `N` sub-topics:

#### 📚 Academic Review (Role: University Professor)
*   **Rule**: Follow the **N * 10 Rule** (Retrieve at least 10 core papers from the last 10 years per sub-topic).
*   **Specialized Search Tools**:
    *   🌟 **OpenAlex**: Global open academic knowledge graph for cross-disciplinary discovery.
    *   🌟 **arXiv**: Computer science, AI, physics, and math preprints.
    *   🌟 **PubMed / Europe PMC**: Biomedical and life sciences database.
*   **Deliverables** (per paper):
    *   **Markdown Summary**: `./workspace/drafts/academic_review/paper_[主題編號]_[文章編號].md`
        *   Contains: Research purpose, method, core technology, pros/cons.
        *   Must include a `### 引用資訊` section with the full BibTeX and perfect **APA 7th Edition** citation.
    *   **Architecture Diagram**: `./workspace/drafts/academic_review/paper_[主題編號]_[文章編號]_architecture.jpg` (or a Mermaid.js diagram embedded in the MD file).

#### 🛡️ Patent Review (Role: Global Patent Engineer)
*   **Rule**: Follow the **N * 10 Rule** (Retrieve at least 10 core patents from the last 10 years per sub-topic, covering the top 10 technological jurisdictions: US, EP, CN, JP, KR, GB, IL, RU, AU, TW).
*   **Patent Search Tools**:
    *   🌟 **Google Patents**: Global语义 search, CPC/IPC filter, and translation comparison.
    *   🌟 **Lens.org (The Lens)**: Academic-to-patent citation link analysis.
    *   🌟 **Espacenet (EPO)**: Tracking patent families and European technical state-of-the-art.
    *   🌟 **WIPO PATENTSCOPE**: Direct lookup of PCT international patent filings.
    *   🌟 **USPTO Patent Public Search**: Rigorous US patent full-text search.
*   **Deliverables**:
    *   **Keyword Matrix**: Save multilingual translated keywords to `./workspace/drafts/patent_review/patent_keywords.json`.
    *   **Markdown Summary**: `./workspace/drafts/patent_review/patent_[技術分支編號]_[專利號].md`
        *   Contains: Patent purpose, implementation method, core claims (Claims), pros/cons, and FTO notes.
        *   Must include a `### 引用資訊` section with the perfect **APA 7th Edition** patent citation.
    *   **Patent Diagram**: `./workspace/drafts/patent_review/patent_[技術分支編號]_[專利號]_diagram.jpg` (or a Mermaid.js diagram).

### 4. Stage 3: NotebookLM Ingestion & Deep RAG (Role: Research Coordinator)
*   **Action**: Use the NotebookLM MCP tools.
*   **Task**:
    *   If a new notebook is created: Call `notebook_create`, import all retrieved summaries, papers, and the selected Google Docs from Drive.
    *   If an existing notebook is selected: Query it directly using `notebook_query` and add the new Stage 2 findings + selected Google Docs to it using `notebook_add_drive` or `notebook_add_text` / `notebook_add_url`.
    *   Perform multi-dimensional querying to extract core technological comparisons, identify white spaces, discover patent wall gaps, and compile performance metrics.

### 5. Stage 4: Strategic Report & Slides Synthesis (Role: Senior Product Manager)
Synthesize the reviews into the three final deliverables. Compile them **chapter-by-chapter** to bypass output token limits:

#### 📄 Deliverable 1: Master Technical Report (`./workspace/drafts/Global_Review.md`)
*   **Chapter 1: Global Review & Mapping**: Systematic summary of academic and patent reviews (incorporating both pre-existing and newly searched assets).
    *   Must embed illustrations with **correct relative paths** (e.g., `![](./academic_review/...)` or `![](./patent_review/...)`).
    *   All citations MUST use footnote markers (`[^reference]`) referencing the BibTeX keys.
*   **Chapter 2: Gap Analysis**:
    *   Detailed pros/cons comparison tables.
    *   Analysis of existing academic bottlenecks, patent barriers, and unresolved "blind spots".
*   **Chapter 3: Future Roadmap & Patent Defense**:
    *   3-5 highly concrete, actionable future research pathways.
    *   Corresponding patent circumvention and defense-wall building strategies.

#### 📚 Deliverable 2: Reference List (`./workspace/drafts/References.md`)
*   Compile all BibTeX and citation strings from the reviews.
*   Every citation must use the Markdown footnote format: `[^reference]: Citation string` and perfectly align one-to-one with the footnote markers in `Global_Review.md` using the **APA 7th Edition** format.

#### 📊 Deliverable 3: Slide Presentation (`./workspace/drafts/slides_review.md`)
*   Write in clean Markdown (compatible with Marp).
*   **Dynamic Split Rule**: Keep slides clutter-free (one visual anchor + bullet points per slide). If a topic is complex, split it dynamically into consecutive slides rather than cramming text.
*   Embed technical architecture/patent diagrams using correct relative image paths.

---

## 🛡️ Rigorous Validation Rules for the AI Agent
1.  **Zero Hallucinated Citations**: Every footnote must map to a real article retrieved in Stage 2 or extracted from pre-existing research.
2.  **No Text Placeholders**: Every section must be fully written out. Do not write generic placeholders.
3.  **Local Execution**: Prefix all Windows terminal validation or Git sync commands with `rtk` (absolute path: `C:\Users\gp6fu\.rtk\rtk.exe`) to compress terminal token costs.
