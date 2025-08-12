import React, { useEffect, useState } from 'react';
import { useChessStore } from '@/stores/chess';
import { chessApi } from '@/services/api';
import { Button } from '@/components/ui/button';
import { Activity, Loader2 } from 'lucide-react';

export const AnalysisPanel: React.FC = () => {
  const { position, analysis, setAnalysis, isAnalyzing, setAnalyzing } = useChessStore();
  const [error, setError] = useState<string | null>(null);

  const analyzePosition = async () => {
    setAnalyzing(true);
    setError(null);
    
    try {
      const result = await chessApi.analyzePosition(position.fen);
      setAnalysis(result);
    } catch (err) {
      setError('Failed to analyze position. Make sure the backend is running.');
      console.error('Analysis error:', err);
    } finally {
      setAnalyzing(false);
    }
  };

  useEffect(() => {
    // Auto-analyze after moves (with a small delay)
    const timer = setTimeout(() => {
      if (!isAnalyzing) {
        analyzePosition();
      }
    }, 500);

    return () => clearTimeout(timer);
  }, [position.fen]);

  const formatEvaluation = (evaluation: number) => {
    if (Math.abs(evaluation) > 5) {
      return evaluation > 0 ? '+999' : '-999';
    }
    return evaluation > 0 ? `+${evaluation.toFixed(2)}` : evaluation.toFixed(2);
  };

  return (
    <div className="bg-white rounded-lg p-4 shadow-md">
      <div className="flex items-center justify-between mb-4">
        <h3 className="font-semibold text-gray-800">Analysis</h3>
        <Button
          variant="outline"
          size="sm"
          onClick={analyzePosition}
          disabled={isAnalyzing}
        >
          {isAnalyzing ? (
            <Loader2 className="w-4 h-4 animate-spin" />
          ) : (
            <Activity className="w-4 h-4" />
          )}
        </Button>
      </div>

      {error && (
        <div className="bg-red-50 text-red-700 p-3 rounded-md mb-4 text-sm">
          {error}
        </div>
      )}

      {isAnalyzing && (
        <div className="flex items-center justify-center py-8">
          <Loader2 className="w-6 h-6 animate-spin text-blue-500" />
          <span className="ml-2 text-gray-600">Analyzing...</span>
        </div>
      )}

      {analysis && !isAnalyzing && (
        <div className="space-y-3">
          <div className="flex items-center justify-between">
            <span className="text-sm text-gray-600">Evaluation:</span>
            <span className={`font-mono font-semibold ${
              analysis.evaluation > 0 ? 'text-green-600' : 
              analysis.evaluation < 0 ? 'text-red-600' : 'text-gray-600'
            }`}>
              {analysis.mateIn 
                ? `M${analysis.mateIn}` 
                : formatEvaluation(analysis.evaluation)
              }
            </span>
          </div>

          {analysis.bestMove && (
            <div className="flex items-center justify-between">
              <span className="text-sm text-gray-600">Best move:</span>
              <span className="font-mono font-semibold text-blue-600">
                {analysis.bestMove}
              </span>
            </div>
          )}

          {analysis.principalVariation.length > 0 && (
            <div>
              <span className="text-sm text-gray-600 block mb-1">Principal variation:</span>
              <div className="text-sm font-mono bg-gray-50 p-2 rounded">
                {analysis.principalVariation.slice(0, 5).join(' ')}
                {analysis.principalVariation.length > 5 && '...'}
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
};