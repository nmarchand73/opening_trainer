import React from 'react';
import { ChessBoard } from '@/components/chess/ChessBoard';
import { MoveHistory } from '@/components/chess/MoveHistory';
import { AnalysisPanel } from '@/components/chess/AnalysisPanel';

function App() {
  return (
    <div className="min-h-screen bg-gray-50 p-4">
      <div className="max-w-7xl mx-auto">
        <header className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-800 mb-2">
            Chess Opening Trainer
          </h1>
          <p className="text-gray-600">
            Master the Stonewall, Torre, and Colle opening systems
          </p>
        </header>

        <div className="grid lg:grid-cols-3 gap-6">
          {/* Chess Board */}
          <div className="lg:col-span-2 flex justify-center">
            <ChessBoard className="w-full max-w-lg" />
          </div>

          {/* Side Panel */}
          <div className="space-y-6">
            <MoveHistory />
            <AnalysisPanel />
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;