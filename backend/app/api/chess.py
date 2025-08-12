from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import chess
import chess.engine
from app.services.chess_service import ChessService

router = APIRouter()
chess_service = ChessService()

class MoveRequest(BaseModel):
    fen: str
    move: str

class AnalysisRequest(BaseModel):
    fen: str
    depth: int = 15

class AnalysisResponse(BaseModel):
    evaluation: float
    best_move: Optional[str]
    principal_variation: List[str]
    mate_in: Optional[int]

@router.post("/validate-move")
async def validate_move(request: MoveRequest):
    try:
        is_valid = chess_service.validate_move(request.fen, request.move)
        return {"valid": is_valid}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/analyze", response_model=AnalysisResponse)
async def analyze_position(request: AnalysisRequest):
    try:
        analysis = await chess_service.analyze_position(request.fen, request.depth)
        return analysis
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/legal-moves/{fen}")
async def get_legal_moves(fen: str):
    try:
        moves = chess_service.get_legal_moves(fen)
        return {"moves": moves}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))