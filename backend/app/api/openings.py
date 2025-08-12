from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.services.opening_service import OpeningService
from pydantic import BaseModel

router = APIRouter()

class OpeningSystem(BaseModel):
    name: str
    description: str
    key_moves: List[str]
    starting_fen: str

class LessonRequest(BaseModel):
    system: str  # "stonewall", "torre", "colle"
    lesson_id: int

@router.get("/systems")
async def get_opening_systems():
    return {
        "systems": [
            {
                "name": "Stonewall Attack",
                "description": "Aggressive pawn structure with f4, e3, d4, c3",
                "key_moves": ["d4", "e3", "f4", "c3", "Bd3"],
                "starting_fen": "rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq d3 0 1"
            },
            {
                "name": "Torre Attack",
                "description": "Flexible system with Bg5 and piece development",
                "key_moves": ["d4", "Nf3", "Bg5", "e3", "Bd3"],
                "starting_fen": "rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq d3 0 1"
            },
            {
                "name": "Colle System",
                "description": "Solid setup with e3, Bd3, Nbd2 for central control",
                "key_moves": ["d4", "Nf3", "e3", "Bd3", "Nbd2"],
                "starting_fen": "rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq d3 0 1"
            }
        ]
    }

@router.get("/lessons/{system}")
async def get_lessons(system: str, db: Session = Depends(get_db)):
    opening_service = OpeningService(db)
    try:
        lessons = opening_service.get_lessons_for_system(system)
        return {"lessons": lessons}
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"System '{system}' not found")