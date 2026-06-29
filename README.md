# 🤖 GRC Copilot

An agentic AI assistant built with Django and LangChain that answers governance, risk, and compliance (GRC) questions by invoking custom tools to retrieve live data from a database instead of relying solely on LLM knowledge.

## Overview

Traditional chatbots rely on pre-trained knowledge and can hallucinate when answering domain-specific questions. This project addresses that by equipping an LLM with a set of backend tools that query a Django database in real time.

The assistant can answer questions about:

- 👥 Users
- 📋 Policies
- 🛡️ Controls
- 📁 Evidence

using structured database queries while enforcing role-based access control.

---

## Features

- 🧠 Agentic AI workflow
- 🛠️ LLM tool/function calling
- 💬 Conversational interface
- 🔍 Live database retrieval using Django ORM
- 🔐 Role-based access control
- 📚 Conversation history
- ⚡ Modular tool architecture

---

## How it Works

```text
                User
                  │
                  ▼
           Django Chat UI
                  │
                  ▼
             AI Agent (LLM)
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
   get_users  get_policies  get_controls
                  │
                  ▼
            Django ORM
                  │
                  ▼
             SQLite Database
```

Instead of answering from its own knowledge, the LLM decides which tool to invoke based on the user's request. Each tool performs the appropriate database query and returns structured information back to the model to generate a grounded response.

---

## Tech Stack

- Python
- Django
- LangChain
- OpenAI GPT
- SQLite
- Django ORM

---

## Example Questions

```
Who owns the Password Policy?

Show me all active Security policies.

Which controls belong to the Compliance department?

Who are the tech leads?

List all evidence assigned to John.
```

---

## Project Structure

```
RAG_PROJ/
│
├── ai/
│   ├── agent/
│   └── tools/
│
├── backend/
│   ├── chat/
│   ├── grc/
│   └── manage.py
│
└── README.md
```

---

## Key Concepts Demonstrated

- Agentic AI
- LLM Tool Calling
- Database Grounding
- Role-Based Authorization
- Django ORM
- Modular Backend Design

---

## Future Improvements

- Vector search for semantic retrieval
- Streaming responses
- Multi-agent workflows
- Tool execution tracing
- Hybrid RAG with document retrieval
- Docker deployment

---
