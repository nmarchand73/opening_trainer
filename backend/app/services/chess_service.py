import chess
import chess.engine
from stockfish import Stockfish
from typing import List, Optional, Dict
from app.core.config import settings

class ChessService:
    def __init__(self):
        self.stockfish = None
        self._init_stockfish()
    
    def _init_stockfish(self):
        try:
            stockfish_path = settings.stockfish_path or "stockfish"
            self.stockfish = Stockfish(path=stockfish_path)
        except Exception as e:
            print(f"Warning: Could not initialize Stockfish: {e}")
            self.stockfish = None
    
    def validate_move(self, fen: str, move: str) -> bool:
        try:
            board = chess.Board(fen)
            chess_move = chess.Move.from_uci(move)
            return chess_move in board.legal_moves
        except:
            return False
    
    def get_legal_moves(self, fen: str) -> List[str]:
        try:
            board = chess.Board(fen)
            return [move.uci() for move in board.legal_moves]
        except:
            return []
    
    async def analyze_position(self, fen: str, depth: int = 15) -> Dict:
        # Reinitialize Stockfish if needed
        if not self.stockfish:
            self._init_stockfish()
        
        if not self.stockfish:
            raise Exception("Stockfish engine not available")
        
        try:
            self.stockfish.set_fen_position(fen)
            evaluation = self.stockfish.get_evaluation()
            best_move = self.stockfish.get_best_move()
            
            # Get principal variation (simplified for now)
            pv = [best_move] if best_move else []
            
            return {
                "evaluation": evaluation.get("value", 0) / 100.0 if evaluation["type"] == "cp" else 0,
                "best_move": best_move,
                "principal_variation": pv,
                "mate_in": evaluation.get("value") if evaluation.get("type") == "mate" else None
            }
        except Exception as e:
            raise Exception(f"Analysis failed: {str(e)}")
    
    def make_move(self, fen: str, move: str) -> Optional[str]:
        try:
            board = chess.Board(fen)
            chess_move = chess.Move.from_uci(move)
            if chess_move in board.legal_moves:
                board.push(chess_move)
                return board.fen()
            return None
        except:
            return None