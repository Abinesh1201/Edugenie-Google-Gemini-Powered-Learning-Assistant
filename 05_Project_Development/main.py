from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from dotenv import load_dotenv

from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations


# ==========================================
# Load environment variables
# ==========================================

load_dotenv()


# ==========================================
# Create FastAPI application
# ==========================================

app = FastAPI(
    title="EduGenie: Google Gemini Powered Learning Assistant",
    description="AI-powered educational assistant using Google Gemini",
    version="1.0.0",
)


# ==========================================
# Static files and templates
# ==========================================

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

templates = Jinja2Templates(directory="templates")


# ==========================================
# Request Models
# ==========================================

class QuestionRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=1,
        max_length=5000
    )


class ExplanationRequest(BaseModel):
    topic: str = Field(
        ...,
        min_length=1,
        max_length=500
    )
    level: str = "College"


class QuizRequest(BaseModel):
    topic: str = Field(
        ...,
        min_length=1,
        max_length=500
    )
    count: int = Field(
        default=5,
        ge=1,
        le=20
    )


class SummaryRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        max_length=20000
    )


class LearningPathRequest(BaseModel):
    subject: str = Field(
        ...,
        min_length=1,
        max_length=300
    )
    level: str = "College"
    goal: str = "Exam preparation"
    days: int = Field(
        default=7,
        ge=1,
        le=30
    )


# ==========================================
# Home Page
# ==========================================

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


# ==========================================
# Health Check
# ==========================================

@app.get("/api/health")
async def health():
    return {
        "status": "ok",
        "application": "EduGenie",
        "version": "1.0.0",
        "message": "EduGenie API is running"
    }


# ==========================================
# Q&A
# ==========================================

@app.post("/api/qna")
async def qna(request: QuestionRequest):

    try:
        answer = answer_question(request.question)

        return {
            "answer": answer
        }

    except Exception as exc:

        return JSONResponse(
            status_code=500,
            content={
                "error": str(exc)
            }
        )


# ==========================================
# Topic Explanation
# ==========================================

@app.post("/api/explain")
async def explain(request: ExplanationRequest):

    try:
        answer = explain_topic(
            request.topic,
            request.level
        )

        return {
            "answer": answer
        }

    except Exception as exc:

        return JSONResponse(
            status_code=500,
            content={
                "error": str(exc)
            }
        )


# ==========================================
# Quiz Generator
# ==========================================

@app.post("/api/quiz")
async def quiz(request: QuizRequest):

    try:
        answer = generate_quiz(
            request.topic,
            request.count
        )

        return {
            "answer": answer
        }

    except Exception as exc:

        return JSONResponse(
            status_code=500,
            content={
                "error": str(exc)
            }
        )


# ==========================================
# Text Summarizer
# ==========================================

@app.post("/api/summarize")
async def summarize(request: SummaryRequest):

    try:
        answer = summarize_text(
            request.text
        )

        return {
            "answer": answer
        }

    except Exception as exc:

        return JSONResponse(
            status_code=500,
            content={
                "error": str(exc)
            }
        )


# ==========================================
# Learning Path
# ==========================================

@app.post("/api/learning-path")
async def learning_path(
    request: LearningPathRequest
):

    try:

        answer = get_learning_recommendations(
            subject=request.subject,
            level=request.level,
            goal=request.goal,
            days=request.days
        )

        return {
            "answer": answer
        }

    except Exception as exc:

        return JSONResponse(
            status_code=500,
            content={
                "error": str(exc)
            }
        )


# ==========================================
# API Information
# ==========================================

@app.get("/api")
async def api_info():

    return {
        "application": "EduGenie",
        "version": "1.0.0",
        "description": "Google Gemini Powered Learning Assistant",

        "endpoints": [
            "GET /",
            "GET /api",
            "GET /api/health",
            "POST /api/qna",
            "POST /api/explain",
            "POST /api/quiz",
            "POST /api/summarize",
            "POST /api/learning-path"
        ]
    }