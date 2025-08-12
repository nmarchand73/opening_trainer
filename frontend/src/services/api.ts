import axios from 'axios';
import { AnalysisResult, OpeningSystem, Lesson } from '@/types/chess';

const API_BASE_URL = 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const chessApi = {
  validateMove: async (fen: string, move: string): Promise<{ valid: boolean }> => {
    const response = await api.post('/chess/validate-move', { fen, move });
    return response.data;
  },

  analyzePosition: async (fen: string, depth: number = 15): Promise<AnalysisResult> => {
    const response = await api.post('/chess/analyze', { fen, depth });
    return response.data;
  },

  getLegalMoves: async (fen: string): Promise<{ moves: string[] }> => {
    const response = await api.get(`/chess/legal-moves/${encodeURIComponent(fen)}`);
    return response.data;
  },
};

export const openingsApi = {
  getSystems: async (): Promise<{ systems: OpeningSystem[] }> => {
    const response = await api.get('/openings/systems');
    return response.data;
  },

  getLessons: async (system: string): Promise<{ lessons: Lesson[] }> => {
    const response = await api.get(`/openings/lessons/${system}`);
    return response.data;
  },
};