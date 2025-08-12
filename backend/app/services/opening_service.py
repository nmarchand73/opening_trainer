from sqlalchemy.orm import Session
from typing import List, Dict, Optional

class OpeningService:
    def __init__(self, db: Session):
        self.db = db
    
    def get_lessons_for_system(self, system: str) -> List[Dict]:
        # For now, return hardcoded lessons. Later we'll store these in the database
        lessons_data = {
            "stonewall": [
                {
                    "id": 1,
                    "title": "Basic Stonewall Formation",
                    "description": "Learn the fundamental pawn structure",
                    "starting_fen": "rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq d3 0 1",
                    "key_moves": ["d4", "e3", "f4", "c3"],
                    "objectives": [
                        "Establish the pawn chain d4-e3-f4-c3",
                        "Develop pieces to support the structure",
                        "Understand typical attacking plans"
                    ]
                },
                {
                    "id": 2,
                    "title": "Piece Development in Stonewall",
                    "description": "Optimal piece placement",
                    "starting_fen": "rnbqkbnr/pppppppp/8/8/3PP3/5P2/PPP3PP/RNBQKBNR b KQkq - 0 2",
                    "key_moves": ["Bd3", "Nf3", "Nd2"],
                    "objectives": [
                        "Place bishop on d3 for kingside attack",
                        "Develop knight to f3 for central control",
                        "Use Nd2 to support the center"
                    ]
                }
            ],
            "torre": [
                {
                    "id": 1,
                    "title": "Torre Attack Setup",
                    "description": "Basic Torre system formation",
                    "starting_fen": "rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq d3 0 1",
                    "key_moves": ["d4", "Nf3", "Bg5", "e3"],
                    "objectives": [
                        "Control the center with d4",
                        "Develop knight to f3",
                        "Pin opponent's knight with Bg5"
                    ]
                }
            ],
            "colle": [
                {
                    "id": 1,
                    "title": "Colle System Foundation",
                    "description": "Solid central setup",
                    "starting_fen": "rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq d3 0 1",
                    "key_moves": ["d4", "Nf3", "e3", "Bd3", "Nbd2"],
                    "objectives": [
                        "Establish solid central control",
                        "Develop pieces harmoniously",
                        "Prepare for central breakthrough"
                    ]
                }
            ]
        }
        
        return lessons_data.get(system.lower(), [])
    
    def get_lesson_details(self, system: str, lesson_id: int) -> Optional[Dict]:
        lessons = self.get_lessons_for_system(system)
        for lesson in lessons:
            if lesson["id"] == lesson_id:
                return lesson
        return None