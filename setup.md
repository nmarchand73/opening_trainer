# Chess Opening Trainer Setup

## Prerequisites
- Python 3.8+ with pip
- Node.js 18+ with npm
- Stockfish chess engine

## Installation

### Backend (Python)
```bash
cd backend
pip install -r requirements.txt
```

### Frontend (Node.js)
```bash
cd frontend  
npm install
```

## Running the Application

### Start Backend
```bash
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Start Frontend
```bash
cd frontend
npm run dev
```

## Configuration
- Backend API runs on http://localhost:8000
- Frontend runs on http://localhost:5173
- Stockfish engine path can be configured in backend/.env