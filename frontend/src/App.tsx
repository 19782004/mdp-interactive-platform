import React, { useState } from 'react';
import './App.css';
import MDPEditor from './components/MDPEditor';
import MDPVisualizer from './components/MDPVisualizer';
import AlgorithmControls from './components/AlgorithmControls';
import { MDP } from './models/MDP';
import { EXAMPLE_MDPS } from './models/exampleMDPs';

function App() {
  const [mdp, setMDP] = useState<MDP | null>(EXAMPLE_MDPS.gridworld);
  const [selectedAlgorithm, setSelectedAlgorithm] = useState<string>('value-iteration');
  const [isPlaying, setIsPlaying] = useState(true); // Auto-play on load
  const [speed, setSpeed] = useState(1);
  const [resetTrigger, setResetTrigger] = useState(0);
  
  const handlePlayPause = () => {
    setIsPlaying(!isPlaying);
  };
  
  const handleReset = () => {
    setIsPlaying(false);
    setResetTrigger(prev => prev + 1);
    // Auto-play after reset
    setTimeout(() => setIsPlaying(true), 500);
  };
  
  return (
    <div className="App">
      <header className="App-header">
        <h1>🎓 MDP Interactive Platform</h1>
        <p>Watch live algorithm visualization step-by-step</p>
      </header>
      
      <div className="main-container">
        <div className="sidebar">
          <MDPEditor mdp={mdp} onMDPChange={setMDP} />
          <AlgorithmControls 
            algorithm={selectedAlgorithm}
            onAlgorithmChange={setSelectedAlgorithm}
            mdp={mdp}
            isPlaying={isPlaying}
            onPlayPause={handlePlayPause}
            onReset={handleReset}
            speed={speed}
            onSpeedChange={setSpeed}
          />
        </div>
        
        <div className="visualization-area">
          <MDPVisualizer 
            mdp={mdp} 
            algorithm={selectedAlgorithm}
            isPlaying={isPlaying}
            speed={speed}
            onReset={() => resetTrigger}
          />
        </div>
      </div>
    </div>
  );
}

export default App;
