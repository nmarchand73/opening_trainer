import { create } from 'zustand';
import { Chess } from 'chess.js';
import { ChessPosition, AnalysisResult } from '@/types/chess';

interface ChessStore {
  position: ChessPosition;
  analysis: AnalysisResult | null;
  isAnalyzing: boolean;
  
  // Actions
  makeMove: (move: string) => boolean;
  undoMove: () => void;
  setPosition: (fen: string) => void;
  setAnalysis: (analysis: AnalysisResult | null) => void;
  setAnalyzing: (analyzing: boolean) => void;
  reset: () => void;
}

const initialPosition: ChessPosition = {
  fen: 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1',
  moveHistory: [],
  currentMove: 0,
};

export const useChessStore = create<ChessStore>((set, get) => ({
  position: initialPosition,
  analysis: null,
  isAnalyzing: false,

  makeMove: (move: string) => {
    const { position } = get();
    const chess = new Chess(position.fen);
    
    try {
      const result = chess.move(move);
      if (result) {
        set({
          position: {
            fen: chess.fen(),
            moveHistory: [...position.moveHistory, move],
            currentMove: position.currentMove + 1,
          },
        });
        return true;
      }
      return false;
    } catch {
      return false;
    }
  },

  undoMove: () => {
    const { position } = get();
    if (position.moveHistory.length === 0) return;

    const chess = new Chess();
    const newHistory = position.moveHistory.slice(0, -1);
    
    // Replay moves to get the position
    newHistory.forEach(move => chess.move(move));
    
    set({
      position: {
        fen: chess.fen(),
        moveHistory: newHistory,
        currentMove: Math.max(0, position.currentMove - 1),
      },
    });
  },

  setPosition: (fen: string) => {
    set({
      position: {
        fen,
        moveHistory: [],
        currentMove: 0,
      },
    });
  },

  setAnalysis: (analysis: AnalysisResult | null) => {
    set({ analysis });
  },

  setAnalyzing: (analyzing: boolean) => {
    set({ isAnalyzing: analyzing });
  },

  reset: () => {
    set({
      position: initialPosition,
      analysis: null,
      isAnalyzing: false,
    });
  },
}));