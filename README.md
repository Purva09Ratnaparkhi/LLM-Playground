
# 🧠 LLM Playground → Agentic AI Systems

> A step-by-step journey from a basic LLM API to a **production-ready, agentic AI system**.

This repository demonstrates how to **build real AI systems**, not just prompt an LLM.  
It focuses on **architecture, robustness, memory, and agentic behavior**.

---

## 🚀 Project Overview

This project starts as a simple **LLM API backend** and gradually evolves into an **agent-ready AI system**.

The goal is to:
- Understand how LLMs work **in real systems**
- Build reliable, scalable AI backends
- Progress naturally toward **Agentic AI**

---

## 🧩 Tech Stack

- **Python**
- **FastAPI** – API backend
- **OpenRouter** – LLM gateway
- **Async / HTTPX** – non-blocking LLM calls
- **LangGraph** – agent orchestration (Phase 4+)
- **Free LLM models** – cost-safe experimentation

---

## 📂 Repository Structure

```
llm-playground/
│
├── app/                 # Core LLM backend (Phases 1–3)
│   ├── main.py          # FastAPI entry point
│   ├── llm_client.py    # LLM calling + retries
│   ├── memory.py        # Conversation memory
│   ├── schemas.py       # Request/response models
│   └── config.py        # Environment config
│
├── agent/               # Agentic AI (Phase 4+)
│   ├── state.py
│   ├── nodes.py
│   ├── graph.py
│   └── run.py
│
├── README.md
└── .gitignore
```

---

## 🧠 PHASED ROADMAP

### 🟦 Phase 1 — LLM API Basics
- Built a FastAPI `/chat` endpoint
- Integrated with OpenRouter
- Used async calls for scalability
- Learned how LLM APIs actually work

📌 *Outcome:* Stateless LLM backend

---

### 🟩 Phase 2 — Conversation Memory
- Added `session_id` based memory
- Stored conversations on the server
- Enabled multi-turn chats
- Learned that **LLMs don’t remember — systems do**

📌 *Outcome:* Stateful conversational system

---

### 🟨 Phase 3 — Production Hardening
- Memory trimming (sliding window)
- Retry logic with exponential backoff
- Timeouts & safe error handling
- Free-tier cost safety
- Model fallback readiness

📌 *Outcome:* Production-style, agent-ready backend

---

### 🟥 Phase 4 — Agentic AI (In Progress)
- LangGraph-based agents
- Explicit agent state
- Reasoning nodes
- Agent execution graphs

📌 *Outcome:* Real agents, not chatbots

---

### 🟪 Phase 5 — Agent Intelligence (Planned)
- Agent loops (think → act → observe)
- Tool calling
- Decision making
- Planning vs execution

---

### 🟫 Phase 6 — Knowledge & Long-Term Memory (Planned)
- RAG (Retrieval-Augmented Generation)
- Vector databases
- Persistent memory

---

### 🟥 Phase 7 — Multi-Agent Systems (Planned)
- Multiple agents with roles
- Task orchestration
- Collaboration patterns

---

### 🟦 Phase 8 — Flagship Project (Planned)
- **Jarvis-style AI assistant**
- Automation + tools
- End-to-end demo

---

## 🔐 Environment Setup

Create a `.env` file (never commit it):

```env
OPENROUTER_API_KEY=your_api_key_here
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the API:

```bash
uvicorn app.main:app --reload
```

Open API docs:

```
http://127.0.0.1:8000/docs
```

---

## 🧠 Key Learnings So Far

- LLMs are **stateless**
- Memory must be **system-managed**
- Async enables scalable AI backends
- External APIs **will fail** → retries are mandatory
- Agents are **state machines**, not prompts

---
