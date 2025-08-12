# Chess Opening Trainer

A modern web application for mastering chess opening systems (Stonewall, Torre, and Colle) with AI-powered instruction and real-time analysis.

## Features

- **Interactive Chess Board** - Drag-and-drop moves with real-time validation
- **Stockfish Analysis** - Position evaluation and best move suggestions  
- **Opening Systems** - Comprehensive lessons for Stonewall, Torre, and Colle
- **AI Assistant** - Contextual explanations and Q&A (Ollama integration)
- **Progress Tracking** - Monitor learning advancement

## Tech Stack

**Frontend (Lean & Modern)**
- Vite + React + TypeScript
- Tailwind CSS + shadcn/ui components
- chess.js + react-chessboard
- Zustand state management

**Backend (Python)**
- FastAPI with auto-documentation
- Stockfish chess engine
- python-chess for move validation
- SQLite database
- Ollama AI integration

## Quick Start

### Prerequisites
- Node.js 18+
- Python 3.8+
- Git

### Installation

```bash
# Clone repository
git clone <repository-url>
cd opening_trainer

# Backend setup
cd backend
pip3 install -r requirements.txt

# Frontend setup  
cd ../frontend
npm install
```

### Running the Application

```bash
# Start backend (Terminal 1)
cd backend
python3 -m uvicorn app.main:app --reload

# Start frontend (Terminal 2)
cd frontend
npm run dev
```

**Access the application:**
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

## Project Structure

```
opening_trainer/
├── backend/              # Python FastAPI server
│   ├── app/
│   │   ├── api/          # REST endpoints
│   │   ├── core/         # Configuration
│   │   ├── models/       # Database models  
│   │   └── services/     # Business logic
│   └── requirements.txt
├── frontend/             # React application
│   ├── src/
│   │   ├── components/   # UI components
│   │   ├── services/     # API client
│   │   ├── stores/       # State management
│   │   └── types/        # TypeScript types
│   └── package.json
└── README.md
```

## API Endpoints

- `GET /` - API information
- `POST /api/chess/analyze` - Position analysis
- `POST /api/chess/validate-move` - Move validation
- `GET /api/openings/systems` - Available opening systems
- `GET /api/openings/lessons/{system}` - System lessons
- `GET /api/ai/status` - AI assistant status

## Configuration

**Backend (.env file):**
```
STOCKFISH_PATH=/path/to/stockfish
OLLAMA_URL=http://localhost:11434
```

**Frontend:** 
API base URL configured in `src/services/api.ts`

## Development

**Backend:**
```bash
cd backend
python3 -m uvicorn app.main:app --reload --host 0.0.0.0
```

**Frontend:**
```bash
cd frontend
npm run dev
```

**Testing:**
```bash
# Backend
cd backend && python3 -m pytest

# Frontend  
cd frontend && npm test
```

## Deployment

**Build frontend:**
```bash
cd frontend && npm run build
```

**Production backend:**
```bash
cd backend && python3 -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes with tests
4. Submit a pull request

## License

MIT License - see LICENSE file for details.

---

**Status:** ✅ Fully functional with comprehensive chess analysis and opening instruction capabilities.