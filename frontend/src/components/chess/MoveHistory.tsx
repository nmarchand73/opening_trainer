import React from 'react';
import { useChessStore } from '@/stores/chess';
import { Button } from '@/components/ui/button';
import { RotateCcw, SkipBack } from 'lucide-react';

export const MoveHistory: React.FC = () => {
  const { position, undoMove, reset } = useChessStore();

  return (
    <div className="bg-white rounded-lg p-4 shadow-md">
      <div className="flex items-center justify-between mb-4">
        <h3 className="font-semibold text-gray-800">Move History</h3>
        <div className="flex gap-2">
          <Button
            variant="outline"
            size="sm"
            onClick={undoMove}
            disabled={position.moveHistory.length === 0}
          >
            <RotateCcw className="w-4 h-4" />
          </Button>
          <Button
            variant="outline"
            size="sm"
            onClick={reset}
            disabled={position.moveHistory.length === 0}
          >
            <SkipBack className="w-4 h-4" />
          </Button>
        </div>
      </div>
      
      <div className="max-h-48 overflow-y-auto">
        {position.moveHistory.length === 0 ? (
          <p className="text-gray-500 text-sm">No moves yet</p>
        ) : (
          <div className="grid grid-cols-2 gap-2 text-sm">
            {position.moveHistory.map((move, index) => (
              <div
                key={index}
                className={`p-2 rounded ${
                  index === position.moveHistory.length - 1
                    ? 'bg-blue-100 text-blue-800'
                    : 'bg-gray-50'
                }`}
              >
                {Math.ceil((index + 1) / 2)}. {move}
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};