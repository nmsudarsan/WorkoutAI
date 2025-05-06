
# 🧠 WorkoutAI

Personal Fitness & Nutrition Assistant powered by Langflow, Streamlit, and AstraDB.

## 🚀 Features
- Save personal fitness profiles
- Set goals and generate macros using AI
- Store and search notes
- Ask AI custom questions about fitness

## 🛠️ Stack
- **Frontend**: Streamlit
- **Backend**: Python
- **Langflow**: AI agent orchestration
- **Database**: AstraDB
- **LLM**: Gemini/OpenRouter/OpenAI via Langflow

## 📦 Installation
```bash
git clone https://github.com/nmsudarsan/WorkoutAI.git
cd WorkoutAI
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
```

## 📂 Folder Structure
- `main.py`: Streamlit UI
- `ai.py`: Langflow calls
- `form_submit.py`: DB update logic
- `profiles.py`: Profile + notes logic
- `.env`: Add your `LANGFLOW_TOKEN`

## 💡 Notes
- Langflow flows should be deployed and accessible via API
- Use `.env` for your API keys

## 🧪 Run the App
```bash
streamlit run main.py
```

---

Built with ❤️ by NMS
