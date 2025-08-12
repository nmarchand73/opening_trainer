import React from 'react';
import { Chessboard } from 'react-chessboard';
import { useChessStore } from '@/stores/chess';
import { Chess } from 'chess.js';

interface ChessBoardProps {
  className?: string;
}

export const ChessBoard: React.FC<ChessBoardProps> = ({ className }) => {
  const { position, makeMove } = useChessStore();

  const handleMove = (sourceSquare: string, targetSquare: string) => {
    const chess = new Chess(position.fen);
    const move = chess.move({
      from: sourceSquare,
      to: targetSquare,
      promotion: 'q', // Always promote to queen for simplicity
    });

    if (move) {
      makeMove(move.san);
      return true;
    }
    return false;
  };

  return (
    <div className={className}>
      <Chessboard
        position={position.fen}
        onPieceDrop={handleMove}
        boardWidth={400}
        arePiecesDraggable={true}
        customBoardStyle={{
          borderRadius: '8px',
          boxShadow: '0 8px 25px rgba(0, 0, 0, 0.15)',
        }}
        customDarkSquareStyle={{ backgroundColor: '#779952' }}
        customLightSquareStyle={{ backgroundColor: '#edeed1' }}
      />
    </div>
  );
};