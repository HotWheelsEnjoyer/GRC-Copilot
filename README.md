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
## Getting Started

### Prerequisites

- Python 3.10+
- Git
- An OpenAI API key

### Clone the repository

```bash
git clone https://github.com/HotWheelsEnjoyer/GRC-Copilot.git
cd GRC-Copilot
```

### Create a virtual environment

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file in the project root and add:

```env
OPENAI_API_KEY=your_api_key_here
```

If your project requires additional variables (database settings, LangSmith keys, etc.), add them here as well.

### Apply database migrations

```bash
cd backend
python manage.py migrate
```

### (Optional) Load sample data

If you have fixtures:

```bash
python manage.py loaddata sample_data.json
```

or run your custom seed script.

### Start the Django server

```bash
python manage.py runserver
```

Open your browser and navigate to:

```
http://127.0.0.1:8000/
```

Log in with one of the sample user accounts and start chatting with the assistant.

---

## Example Prompts

- Show me all active Security policies.
- Who owns the Password Policy?
- List all controls for the IT department.
- Show me all evidence assigned to John.
- Who are the tech leads?

---

## Future Improvements

- Vector search for semantic retrieval
- Streaming responses
- Multi-agent workflows
- Tool execution tracing
- Hybrid RAG with document retrieval
- Docker deployment

---
