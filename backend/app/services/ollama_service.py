import ollama
from typing import Optional, Dict, Any
from app.core.config import settings

class OllamaService:
    def __init__(self):
        self.client = ollama.Client(host=settings.ollama_url)
        self.model = settings.ollama_model
    
    async def generate_response(self, prompt: str, context: Optional[str] = None) -> str:
        """Generate a response using Ollama Python library"""
        try:
            full_prompt = self._build_chess_prompt(prompt, context)
            
            response = self.client.generate(
                model=self.model,
                prompt=full_prompt,
                stream=False,
                options={
                    'temperature': 0.7,
                    'top_p': 0.9,
                    'num_predict': 500
                }
            )
            
            return response.get('response', "Sorry, I couldn't generate a response.")
                
        except ollama.ResponseError as e:
            return f"Ollama error: {str(e)}"
        except Exception as e:
            return f"An error occurred: {str(e)}"
    
    def _build_chess_prompt(self, user_question: str, context: Optional[str] = None) -> str:
        """Build a chess-specific prompt for the AI"""
        base_prompt = """You are a chess instructor specializing in opening systems, particularly the Stonewall Attack, Torre System, and Colle System. 
        
Your role is to:
- Explain chess opening principles clearly
- Analyze positions and suggest improvements
- Answer questions about opening theory
- Provide strategic advice for the three opening systems
- Help students understand typical plans and piece placements

Keep your responses concise but informative, suitable for intermediate chess players learning these opening systems.
"""
        
        if context:
            full_prompt = f"{base_prompt}\n\nContext: {context}\n\nQuestion: {user_question}\n\nResponse:"
        else:
            full_prompt = f"{base_prompt}\n\nQuestion: {user_question}\n\nResponse:"
        
        return full_prompt
    
    async def explain_position(self, fen: str, opening_system: str) -> str:
        """Generate an explanation for a specific chess position"""
        context = f"Chess position (FEN): {fen}\nOpening system: {opening_system}"
        prompt = "Please explain this chess position, including the key strategic ideas and typical plans for both sides."
        
        return await self.generate_response(prompt, context)
    
    async def answer_opening_question(self, question: str, opening_system: str) -> str:
        """Answer a specific question about an opening system"""
        context = f"Opening system: {opening_system}"
        return await self.generate_response(question, context)
    
    def is_available(self) -> bool:
        """Check if Ollama service is available"""
        try:
            self.client.list()
            return True
        except:
            return False