export interface ChessPosition {
  fen: string;
  moveHistory: string[];
  currentMove: number;
}

export interface ChessMove {
  from: string;
  to: string;
  promotion?: string;
}

export interface AnalysisResult {
  evaluation: number;
  bestMove: string | null;
  principalVariation: string[];
  mateIn: number | null;
}

export interface OpeningSystem {
  name: string;
  description: string;
  keyMoves: string[];
  startingFen: string;
}

export interface Lesson {
  id: number;
  title: string;
  description: string;
  startingFen: string;
  keyMoves: string[];
  objectives: string[];
}