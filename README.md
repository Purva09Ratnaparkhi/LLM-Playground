# 🧠 LLM Playground → Agentic AI Foundations

> A hands-on foundation project that evolves from a basic LLM API into a **working agentic AI system with tools, reasoning loops, and provider abstraction**.

This repository focuses on **how agentic AI systems are built internally**, not just how to prompt an LLM.

---

## 🚀 Project Overview

This project was built to understand and implement:

- How LLM-backed systems actually work
- How to design **agent loops** (think → act → observe → decide)
- How to integrate **tools** into agents
- How to keep systems **cost-safe, debuggable, and provider-agnostic**

It serves as a **foundation project** for more advanced, real-world agentic systems (RAG agents, research agents, automation agents).

---

## 🧩 Tech Stack

- **Python**
- **FastAPI** – LLM API backend
- **LangGraph** – agent orchestration & state machines
- **Gemini 2.5 Flash (free tier)** – primary LLM
- **Ollama (local)** – fallback LLM (cost-safe)
- **HTTPX** – async HTTP calls
- **python-dotenv** – environment management

---

## 📂 Repository Structure

