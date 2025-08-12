from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    database_url: str = "sqlite:///./chess_trainer.db"
    stockfish_path: Optional[str] = None  # Will use default stockfish installation
    ollama_url: str = "http://localhost:11434"
    ollama_model: str = "llama2"
    
    class Config:
        env_file = ".env"

settings = Settings()