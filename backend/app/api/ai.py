from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.ollama_service import OllamaService

router = APIRouter()
ollama_service = OllamaService()

class QuestionRequest(BaseModel):
    question: str
    opening_system: str = "general"
    context: str = ""

class PositionExplanationRequest(BaseModel):
    fen: str
    opening_system: str

@router.post("/ask")
async def ask_question(request: QuestionRequest):
    """Ask the AI assistant a question about chess openings"""
    try:
        if not ollama_service.is_available():
            raise HTTPException(status_code=503, detail="AI assistant is currently unavailable")
        
        response = await ollama_service.answer_opening_question(
            request.question, 
            request.opening_system
        )
        
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/explain-position")
async def explain_position(request: PositionExplanationRequest):
    """Get an AI explanation of a chess position"""
    try:
        if not ollama_service.is_available():
            raise HTTPException(status_code=503, detail="AI assistant is currently unavailable")
        
        explanation = await ollama_service.explain_position(
            request.fen,
            request.opening_system
        )
        
        return {"explanation": explanation}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/status")
async def ai_status():
    """Check if the AI assistant is available"""
    available = ollama_service.is_available()
    return {"available": available}