import os
from google import genai

def get_client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is missing. Add it to the .env file.")
    return genai.Client(api_key=api_key)

def get_model():
    return os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

def get_learning_recommendations(
    subject: str,
    level: str = "College",
    goal: str = "Exam preparation",
    days: int = 7,
) -> str:
    client = get_client()
    model = get_model()

    prompt = f"""
Create a {days}-day learning plan for a {level} student.

Subject: {subject}
Goal: {goal}

For each day include:
- Topic
- Concepts to learn
- Practice activity
- Revision activity
- Suggested study time

Finish with:
- Learning Strategy
- Revision Strategy
- Final Review
"""
    response = client.models.generate_content(model=model, contents=prompt)
    return response.text or "No learning path was generated."
