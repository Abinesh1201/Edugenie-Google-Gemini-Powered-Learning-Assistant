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


def explain_topic(topic, level="College"):
    client = get_client()

    model = os.getenv(
        "GEMINI_MODEL",
        "gemini-3.8-flash"
    )

    prompt = f"""
You are EduGenie, an AI educational assistant.

Explain the following topic for a {level} student.

Topic:
{topic}

Use this structure:

1. Simple Explanation
2. Key Concepts
3. Step-by-Step Understanding
4. Real-World Example
5. Common Mistakes
6. Quick Revision

Keep the explanation educational, clear, and easy to understand.
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