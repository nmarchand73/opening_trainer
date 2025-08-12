# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Common Development Commands

**Frontend (React + Vite):**
```bash
cd frontend
npm install          # Install dependencies
npm run dev          # Start dev server (localhost:5173)
npm run build        # Build for production (TypeScript compilation + Vite build)
npm run preview      # Preview production build
```

**Backend (FastAPI + Python):**
```bash
cd backend
pip3 install -r requirements.txt        # Install dependencies
python3 -m uvicorn app.main:app --reload  # Start dev server (localhost:8000)
python3 -m pytest                       # Run tests
```

**Full Application:**
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

## Architecture Overview

**Technology Stack:**
- Frontend: Vite + React + TypeScript, Tailwind CSS, shadcn/ui, Zustand state management
- Chess Libraries: chess.js (game logic), react-chessboard (UI), python-chess (backend)
- Backend: FastAPI, SQLite + SQLAlchemy, Stockfish engine, Ollama AI integration

**Project Structure:**
```
frontend/src/
├── components/chess/  # ChessBoard, MoveHistory, AnalysisPanel
├── components/ui/     # shadcn/ui components (button, etc.)
├── services/          # API client (api.ts)
├── stores/           # Zustand state management (chess.ts)
├── types/            # TypeScript definitions (chess.ts)
└── lib/              # Utilities (utils.ts)

backend/app/
├── api/              # REST endpoints (chess.py, openings.py, ai.py)
├── core/             # Configuration (config.py, database.py)
├── models/           # SQLAlchemy database models
└── services/         # Business logic (chess_service.py, ollama_service.py, opening_service.py)
```

**Key API Endpoints:**
- `POST /api/chess/analyze` - Stockfish position analysis
- `POST /api/chess/validate-move` - Move validation
- `GET /api/openings/systems` - Opening systems (Stonewall, Torre, Colle)
- `GET /api/openings/lessons/{system}` - System-specific lessons
- `GET /api/ai/status` - Ollama AI assistant status

## Development Workflow

**State Management:**
- Frontend uses Zustand stores in `src/stores/chess.ts`
- Chess game state managed with chess.js library
- API calls handled through `src/services/api.ts` with Axios

**Chess Engine Integration:**
- Backend integrates Stockfish via python-chess and stockfish Python wrapper
- Stockfish binary located at `backend/stockfish_binary`
- Engine analysis provides position evaluation and best move suggestions

**AI Assistant:**
- Ollama Python client library for natural language chess explanations
- Default model: llama2, configurable via environment variables
- Local AI processing for privacy
- Uses ollama.Client for improved error handling and connection management

**Configuration:**
- Backend settings in `backend/app/core/config.py`
- Environment variables: `STOCKFISH_PATH`, `OLLAMA_URL`, `OLLAMA_MODEL`
- Frontend Vite config includes path alias `@` for `./src`

## Testing

**Backend:**
```bash
cd backend && python3 -m pytest
```

**Frontend:**
No test framework currently configured in package.json - tests would use Vitest if added.

## Key Dependencies

**Frontend:**
- chess.js: Chess game logic and move validation
- react-chessboard: Interactive chess board component
- zustand: Lightweight state management
- axios: HTTP client for API communication

**Backend:**
- python-chess: Chess position analysis and move validation
- stockfish: Stockfish engine Python wrapper
- ollama: Official Ollama Python client library
- fastapi: Modern async web framework
- sqlalchemy: Database ORM with SQLite

## Opening Systems Focus

This application specifically teaches three chess opening systems:
- Stonewall Attack/Defense
- Torre Attack  
- Colle System

The lesson structure and database schema are designed around these specific openings, with progressive learning modules and interactive exercises for each system.