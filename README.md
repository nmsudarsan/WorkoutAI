# 🏋️‍♂️ WorkoutAI – Your Personal Fitness Assistant

WorkoutAI is an AI-powered personal fitness and nutrition assistant built with **Streamlit**, **Langflow**, and **AstraDB**. It helps users manage their fitness goals, generate macro plans using AI, and receive customized workout advice based on their personal profile and notes.

---

## 🚀 Features

- ✅ Collect personal details (age, weight, height, gender, activity level)
- 🎯 Set fitness goals (Muscle Gain, Fat Loss, Stay Active)
- 🍱 Auto-generate nutrition macros (Calories, Protein, Fat, Carbs)
- 📝 Add personal notes (e.g., injuries, preferences)
- 🤖 Ask AI for workout advice using profile + notes
- 💾 Data stored and retrieved from **AstraDB**
- 🔐 Includes request guardrails and retry logic

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io)
- **Backend**: [FastAPI (optional with Uvicorn)](https://fastapi.tiangolo.com/)
- **LLM Orchestration**: [Langflow](https://github.com/langflow-ai/langflow)
- **Database**: [DataStax AstraDB](https://www.datastax.com/astra)
- **Vector Store**: Astra Vector Search (via `$vectorize`)

---

## 📦 Installation

```bash
git clone https://github.com/nmsudarsan/WorkoutAI.git
cd WorkoutAI
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🚨 Environment Variables

Create a `.env` file in the root with:

```env
LANGFLOW_TOKEN=your_langflow_api_key
ASTRA_DB_ID=your_astra_db_id
ASTRA_DB_REGION=your_region
ASTRA_DB_APPLICATION_TOKEN=your_app_token
```

---

## ▶️ Running the App

To start the Streamlit UI:

```bash
streamlit run main.py
```

To run Langflow locally (optional, if needed for timeout handling):

```bash
uvicorn main_uvicorn:app --reload
```

---

## 🧠 How it Works

1. Users enter their profile & goals in the Streamlit UI.
2. Notes are stored and vectorized in AstraDB.
3. On "Ask AI", profile + goals + vectorized notes are sent to Langflow.
4. Langflow parses everything and returns a personalized workout suggestion.
5. The response is shown in the UI.

---

## 🧾 License

This project is licensed under the MIT License.

---

## 🙋‍♂️ Maintainer

Built by [@nmsudarsan](https://github.com/nmsudarsan). Contributions welcome!