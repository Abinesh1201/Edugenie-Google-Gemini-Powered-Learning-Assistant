import os
import time
from google import genai


def get_client():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is missing. Add it to the .env file."
        )

    return genai.Client(api_key=api_key)


def generate_quiz(topic, count=5):
    client = get_client()

    model = os.getenv(
        "GEMINI_MODEL",
        "gemini-3.8-flash"
    )

    prompt = f"""
You are EduGenie, an AI educational quiz generator.

Create {count} multiple-choice questions about:

{topic}

Requirements:
- Four options for each question.
- Clearly identify the correct answer.
- Give a short explanation for the correct answer.
- Focus on understanding, not memorization only.
- Avoid duplicate questions.
"""

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model=model,
                contents=prompt
            )

            if response.text:
                return response.text

            raise RuntimeError("Gemini returned an empty response.")

        except Exception as exc:
            error_text = str(exc)

            if "503" in error_text or "UNAVAILABLE" in error_text:
                if attempt < 2:
                    time.sleep(3)
                    continue

            raise RuntimeError(f"Gemini API error: {error_text}")