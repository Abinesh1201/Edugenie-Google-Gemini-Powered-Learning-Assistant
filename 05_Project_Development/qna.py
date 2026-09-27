import os
from google import genai

def get_client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is missing. Add it to the .env file.")
    return genai.Client(api_key=api_key)

def get_model():
    return os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

def answer_question(question: str) -> str:
    client = get_client()
    model = get_model()

    prompt = f"""
You are EduGenie, an educational AI tutor.
Answer the student's question clearly and accurately.

Student question:
{question}

Rules:
- Explain in simple language.
- Use headings and bullet points when useful.
- Show steps for calculations.
- For programming questions, explain the logic clearly.
- Do not invent facts.
"""
    response = client.models.generate_content(model=model, contents=prompt)
    return response.text or "No answer was generated."
