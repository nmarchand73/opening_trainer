from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import chess, openings, ai
from app.core.config import settings

app = FastAPI(
    title="Chess Opening Trainer API",
    description="Backend API for the Interactive Chess Opening Systems Trainer",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chess.router, prefix="/api/chess", tags=["chess"])
app.include_router(openings.router, prefix="/api/openings", tags=["openings"])
app.include_router(ai.router, prefix="/api/ai", tags=["ai"])

@app.get("/")
async def root():
    return {"message": "Chess Opening Trainer API", "version": "1.0.0"}