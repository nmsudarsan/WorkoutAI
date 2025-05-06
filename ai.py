# ai.py (with guardrails)
import os
import json
import requests
import time
from dotenv import load_dotenv
from profiles import get_notes

load_dotenv()

APPLICATION_TOKEN = os.getenv("LANGFLOW_TOKEN")

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {APPLICATION_TOKEN}"
}

PROJECT_ID = "e2beeb5e-6d49-4f17-adad-b99784180dbd"
ASK_AI_FLOW_ID = "e7e80611-0b09-4b6e-b4e6-ce66142e8bec"
MACROS_FLOW_ID = "014e9a62-a65e-46c4-aaa8-2bdbf99e8a77"
BASE_URL = f"https://api.langflow.astra.datastax.com/lf/{PROJECT_ID}/api/v1/run"


def dict_to_string(obj, level=0):
    strings = []
    indent = "  " * level
    if isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(value, (dict, list)):
                nested = dict_to_string(value, level + 1)
                strings.append(f"{indent}{key}: {nested}")
            else:
                strings.append(f"{indent}{key}: {value}")
    elif isinstance(obj, list):
        for idx, item in enumerate(obj):
            nested = dict_to_string(item, level + 1)
            strings.append(f"{indent}Item {idx + 1}: {nested}")
    else:
        strings.append(f"{indent}{obj}")
    return ", ".join(strings)


# -------------------------- GUARDRAILS --------------------------
def is_valid_question(question):
    if not question or len(question.strip()) < 3:
        return False
    return True

def is_safe_response(text):
    red_flags = ["kill", "harm", "illegal", "suicide", "violence"]
    lowered = text.lower()
    return not any(flag in lowered for flag in red_flags)


def ask_ai(profile, question, retries=3, delay=10):
    if not is_valid_question(question):
        return "❌ Please enter a valid question."

    url = f"{BASE_URL}/{ASK_AI_FLOW_ID}"
    profile_string = dict_to_string(profile)

    payload = {
        "output_type": "text",
        "input_type": "text",
        "tweaks": {
            "TextInput-sK8H9": {"input_value": profile_string},
            "TextInput-DDpIM": {"input_value": question}
        }
    }

    print("🧠 Sending request to Langflow...")

    for attempt in range(retries):
        try:
            start = time.time()
            response = requests.post(url, json=payload, headers=HEADERS)
            duration = round(time.time() - start, 2)
            print(f"✅ Langflow responded in {duration} seconds")

            response.raise_for_status()

            answer = response.json()["outputs"][0]["outputs"][0]["results"]["text"]["data"]["text"]

            if not is_safe_response(answer):
                return "⚠️ The AI response was flagged as unsafe."

            return answer

        except requests.exceptions.HTTPError as err:
            print(f"❌ Attempt {attempt+1}: {err}")
            if attempt == retries - 1:
                raise
            else:
                print(f"⏳ Retrying in {delay} sec...")
                time.sleep(delay)

    return "❌ Failed to get a safe response from Langflow."


def ask_ai_with_fallback(profile, question):
    try:
        return ask_ai(profile, question)
    except Exception as e:
        print("🔥 Fallback triggered:", str(e))
        return "Sorry, the AI is taking too long to respond. Please try again later."


def get_macros(profile, goals):
    url = f"{BASE_URL}/{MACROS_FLOW_ID}"
    print("GOALS:", goals)
    print("PROFILE:", dict_to_string(profile))

    payload = {
        "output_type": "text",
        "input_type": "text",
        "tweaks": {
            "TextInput-UJewc": {"input_value": ", ".join(goals)},
            "TextInput-Avs0K": {"input_value": dict_to_string(profile)}
        }
    }

    response = requests.post(url, json=payload, headers=HEADERS)
    response.raise_for_status()

    raw_output = response.json()["outputs"][0]["outputs"][0]["results"]["text"]["data"]["text"]
    print("🔍 RAW LANGFLOW OUTPUT:\n", raw_output)

    cleaned_output = raw_output.strip().strip("```").strip("json").strip()

    try:
        return json.loads(cleaned_output)
    except json.JSONDecodeError as e:
        print("❌ JSON parsing failed:", e)
        return {
            "protein": 0,
            "calories": 0,
            "fat": 0,
            "carbs": 0
        }
