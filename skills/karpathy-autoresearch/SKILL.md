---
name: karpathy-autoresearch
description: "Autonomous LLM research and self-directed experimentation framework by Andrej Karpathy. Directs an AI agent to autonomously iterate on neural network training (modifying model architecture, optimizer, hyperparameters in train.py), running fixed 5-minute training experiments, evaluating validation bits per byte (val_bpb), recording results in results.tsv, and keeping or discarding changes. Use when running autonomous ML/LLM research, self-improving training loops, or when the user mentions karpathy-autoresearch or autoresearch."
---

# karpathy-autoresearch: Autonomous LLM Research Framework

> *"Give an AI agent a small but real LLM training setup and let it experiment autonomously overnight. It modifies the code, trains for 5 minutes, checks if the result improved, keeps or discards, and repeats. You wake up in the morning to a log of experiments and (hopefully) a better model."* — Andrej Karpathy

`karpathy-autoresearch` is an autonomous experimentation harness designed for single-GPU LLM training and iterative neural architecture / hyperparameter optimization.

---

## 1. Core Architecture & File Roles

The system is centered around three primary files:

| File | Role | Modifiable by Agent? | Description |
| :--- | :--- | :---: | :--- |
| **`prepare.py`** | Foundation & Harness | ❌ **No (Immutable)** | Fixed constants, one-time data downloading, BPE tokenizer training, dataloader, and ground-truth evaluation (`val_bpb`). |
| **`train.py`** | Research Target | ✅ **Yes (Sole Target)** | Contains the full GPT model architecture, optimizer (Muon + AdamW), hyperparameters, batch sizing, and training loop. |
| **`program.md`** | Agent Guidelines | 👤 **Human Edited** | Ground rules, constraints, and instructions for the agent's research loop. |
| **`results.tsv`** | Experiment Log | 🤖 **Agent Logged** | Tab-separated experiment history logging commits, metrics, parameter counts, and keep/discard decisions. |

---

## 2. Evaluation Metric & Ground Rules

1. **Primary Metric: `val_bpb` (Validation Bits Per Byte)**
   - **Lower is better.**
   - Vocab-size independent, ensuring architectural and tokenization changes are fairly evaluated.
2. **Fixed Time Budget: Exactly 5 Minutes**
   - Training runs for a strict 5-minute wall-clock budget (excluding initial startup and PyTorch compilation).
   - Prevents compute drift; speed optimizations translate directly into processing more tokens.
3. **Simplicity Criterion**:
   - Simpler is better. A marginal improvement ($< 0.001$ `val_bpb`) that introduces complex or brittle code should be rejected.
   - Code deletion or simplification that maintains equal performance is a major win.
4. **VRAM Constraints**:
   - Soft constraint: Memory usage must fit within the host GPU without Out-Of-Memory (OOM) errors.

---

## 3. Autonomous Experimentation Lifecycle

```
[Start Session]
       │
       ▼
1. Agreement & Setup: Propose run tag (e.g. `mar5`), checkout `autoresearch/<tag>`
       │
       ▼
2. Verification: Verify data in `~/.cache/autoresearch/` (run `uv run prepare.py` if missing)
       │
       ▼
3. Baseline Run: Execute unedited `uv run train.py` (~5 min) ──► Record in `results.tsv`
       │
       ├─────────────────────────────────────────────────────────────┐
       ▼                                                             │
4. Formulate Hypothesis (Architecture, Hyperparams, Optimizer, etc.) │
       │                                                             │
       ▼                                                             │
5. Edit `train.py`                                                   │
       │                                                             │
       ▼                                                             │
6. Execute Experiment: `uv run train.py` (5-min budget)              │
       │                                                             │
       ▼                                                             │
7. Evaluate Result (`val_bpb`):                                      │
   ├── Improved? ──► Commit (`git commit`), keep, log to `results.tsv`│
   └── Degraded / Crash? ──► Revert (`git reset --hard HEAD~1`), log  │
       │                                                             │
       └───────────────────────── Repeat ────────────────────────────┘
```

---

## 4. `results.tsv` Format

Record every run with the following columns:

```tsv
commit	val_bpb	training_seconds	total_seconds	peak_vram_mb	num_params_M	status	description
base001	0.997900	300.1	325.9	45060.2	50.3	keep	baseline unedited train.py
exp0002	0.994210	300.2	326.1	45110.0	51.2	keep	switched activation to SwiGLU
exp0003	1.002100	300.1	325.8	45050.0	50.3	discard	increased learning rate to 0.01
```

---

## 5. Execution Commands

```bash
# Setup dependencies
uv sync

# One-time dataset preparation & BPE tokenizer training (~2 min)
uv run prepare.py

# Launch training run (~5 min fixed budget)
uv run train.py
```
