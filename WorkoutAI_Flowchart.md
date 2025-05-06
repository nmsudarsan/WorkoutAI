
#  GenAI Fitness Assistant – Workflow Flowchart

```
+---------------------------+
|     User Interacts via   |
|     Streamlit Frontend   |
+------------+-------------+
             |
             v
+---------------------------+
|      Form Inputs:         |
|  - Personal Data Form     |
|  - Goals Selection        |
|  - Notes Submission       |
+------------+-------------+
             |
             v
+---------------------------+
| Streamlit Session State  |
|   Stores:                |
|   - Profile (ID: 1)      |
|   - Notes (from DB)      |
+------------+-------------+
             |
             v
+---------------------------+
|        MongoDB / AstraDB |
|  Database "workout"      |
|  ├── Collection: notes   |
|  └── Collection: personal|
|      _data               |
+------------+-------------+
             |
             v
+---------------------------+
|     Add / Update Notes   |
|  - New notes saved       |
|  - Timestamp added       |
|  - Stored with user_id   |
+------------+-------------+
             |
             v
+---------------------------+
|     Langflow Flow Trigger|
|     (via Langflow API)   |
+------------+-------------+
             |
             v
+---------------------------+
|       Data Preprocessing |
|  - Profile Dict → String |
|  - Notes → Text          |
|  - Question = User Input |
+------------+-------------+
             |
             v
+---------------------------+
|     Langflow Prompt Flow |
|  ┌─ Prompt Node 1        |
|  │  - Injects Profile    |
|  │  - Injects Notes      |
|  │                       |
|  └─ Prompt Node 2        |
|     - Adds Question      |
|     - LLM Processes All  |
+------------+-------------+
             |
             v
+---------------------------+
|     Langflow Uses LLM    |
|  - Gemini/OpenRouter     |
|  - Analyzes Context      |
|  - Generates Guidance    |
+------------+-------------+
             |
             v
+---------------------------+
|     Response Sent Back   |
|  to Python `ask_ai()`    |
+------------+-------------+
             |
             v
+---------------------------+
|     Output Rendered      |
|   in Streamlit           |
|   - AI Advice Shown      |
|   - Macros Suggested     |
+---------------------------+
```

---

🧠 Core Technologies

Category	Tool / Library	Purpose
LLM Platform	Langflow (w/ Groq backend)	Visual orchestration of multi-agent LLM workflows
LLM Provider	Gemini (via Langflow)	AI text generation & reasoning
Vector DB	Astra DB (DataStax)	Stores notes & vector embeddings for retrieval
API Orchestration	FastAPI + Uvicorn	Local API serving of Langflow flows without timeouts
Frontend	Streamlit	Interactive web UI for users
Backend Logic	Python 3.11+	All business logic, orchestration, and API calls

🧾 Data Management

Tool / Library	Purpose
MongoDB (via Astra)	Stores user profile, goals, nutrition, and notes
Langflow Tweaks	Dynamic flow inputs from Python via tweaks
Notes Vectorization	Notes stored and auto-vectorized for context

🧰 Python Libraries Used

Library	Purpose
requests	For calling Langflow APIs
uvicorn	ASGI server for serving FastAPI
fastapi	Expose Langflow as a local API
streamlit	Build the user interface
python-dotenv	Securely manage environment variables
datetime	Timestamp note metadata
json	Encode/decode Langflow payloads
os	Manage paths, secrets
time	Timeout handling and retries

🌐 Deployment & Dev Tools

Tool	Purpose
GitHub	Project version control and hosting
.env file	Stores secure API tokens like Langflow’s bearer token
VS Code	IDE for development
Langflow Playground	Build and debug flow logic visually

🧩 Langflow Nodes Used

Node Type	Function
TextInput	Accepts user profile and questions
Astra DB Collection	Retrieves notes
Lambda Filter	Filters and extracts just the text field
Parser	Converts extracted notes to clean text
PromptTemplate	Final prompt template using all variables
