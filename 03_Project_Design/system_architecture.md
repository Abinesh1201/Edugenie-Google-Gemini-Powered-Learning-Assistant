# Phase 3 - Project Design

## Architecture

Browser
   |
   v
FastAPI Backend
   |
   +--> Q&A Module ----------> Gemini API
   +--> Explanation Module --> Gemini API
   +--> Quiz Module ---------> Gemini API
   +--> Summary Module ------> Gemini API
   +--> Learning Path -------> Gemini API

## Main Components

### Frontend
HTML, CSS and JavaScript.

### Backend
FastAPI handles routes, validation and module orchestration.

### AI Layer
Google Gemini generates educational content.

### Configuration
Environment variables store the Gemini API key and model name.
