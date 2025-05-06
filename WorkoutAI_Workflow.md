
# 🏋️‍♂️ WorkoutAI Project - Workflow Overview

## 1. Project Setup
- Create a virtual environment: `python -m venv venv`
- Activate environment:
  - Windows: `venv\Scripts\activate`
  - Mac/Linux: `source venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt`

## 2. Environment Configuration
- Add a `.env` file:
```
LANGFLOW_TOKEN=your_langflow_token_here
```

## 3. Astra DB
- Set up two collections: `personal_data_collection` and `notes_collection`
- Store and retrieve user profile and notes.

## 4. Langflow Setup
- Create two flows: `get_macros` and `ask_ai`
- Use three input nodes in `ask_ai` flow: `TextInput-sK8H9` (profile), `TextInput-DDpIM` (question), and notes from DB.

## 5. Streamlit UI
- Four fragments:
  - `personal_data_form()`: name, age, height, weight, etc.
  - `goals_form()`: Select fitness goals
  - `macros()`: Fetch and edit macros using Langflow
  - `notes()`: Save and view notes
  - `ask_ai_func()`: Ask questions to AI agent

## 6. Langflow API Integration
- Use `requests.post()` with retries and delays to handle Langflow 504 Gateway Timeout
- Format payload with 3 inputs and send to Langflow
- Parse and display result to user

## 7. Guardrails
- Add simple retry logic with exponential backoff
- Validate response format from Langflow

## 8. Deployment
- Host using Streamlit locally or on Streamlit Cloud
- Can optionally run Langflow locally using Uvicorn (not required if using Astra-hosted Langflow)

## 9. GitHub
- Push all files to your GitHub repo
- Include `requirements.txt` and `README.md`
