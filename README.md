# EduGenie: Google Gemini Powered Learning Assistant

This project is organized phase-wise for academic submission:

1. Brainstorming & Ideation
2. Requirement Analysis
3. Project Design
4. Project Planning
5. Project Development
6. Project Testing
7. Project Documentation
8. Project Demonstration

The runnable application is inside `05_Project_Development`.

## Run

Open a terminal in `05_Project_Development`:

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Create `.env` from `.env.example`, add your Gemini API key, then:

```powershell
uvicorn main:app --reload
```

Open http://127.0.0.1:8000

## Important

Do not commit or share `.env`. Keep your API key private.
