# ai_service.py
import os
import re
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)
AI_MODEL = "llama-3.3-70b-versatile" 

def ask_ai(message, user):
    """Chatbot helper with personality."""
    try:
        response = client.chat.completions.create(
            model=AI_MODEL,
            messages=[
                {
                    "role": "system", 
                    "content": (
                        "You are a friendly career advisor for StudPath. "
                        f"Student: {user.name}, Course: {user.course}. "
                        "Provide practical, encouraging advice for the Indian tech market."
                    )
                },
                {"role": "user", "content": message}
            ],
            max_tokens=600
        )
        return response.choices[0].message.content
    except Exception as e:
        print("AI ERROR:", e)
        return "AI error occurred."

def generate_ai_roadmap(career_name, user_info):
    """Dynamic roadmap generator."""
    prompt = f"Generate a 4-phase learning roadmap for a {career_name} for student {user_info['name']}. Return ONLY JSON."
    try:
        response = client.chat.completions.create(
            model=AI_MODEL,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2500,
            temperature=0.6
        )
        raw = response.choices[0].message.content.strip()
        raw = re.sub(r"```json\s*|\s*```", "", raw).strip()
        return json.loads(raw)
    except Exception as e:
        print(f"Roadmap AI Error: {e}")
        return {}
    
def ask_ai_roadmap_chat(message, career_name, user):
    """Context-aware chatbot for the roadmap sidebar."""
    try:
        response = client.chat.completions.create(
            model=AI_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": (
                        f"You are an expert career advisor for StudPath. "
                        f"The student is currently viewing their '{career_name}' roadmap.\n\n"
                        f"Student profile:\n"
                        f"Name: {user.name}\n"
                        f"Course: {user.course}\n\n"
                        "Answer questions about this specific career path with actionable, concise advice. Use markdown for formatting."
                    )
                },
                {"role": "user", "content": message}
            ],
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        print("Roadmap Chat AI Error:", e)
        return "⚠️ Sorry, I encountered an error connecting to my brain."