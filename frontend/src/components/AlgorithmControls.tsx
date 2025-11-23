import React from 'react';
import { MDP } from '../models/MDP';

interface Props {
  algorithm: string;
  onAlgorithmChange: (algorithm: string) => void;
  mdp: MDP | null;
  isPlaying: boolean;
  onPlayPause: () => void;
  onReset: () => void;
  speed: number;
  onSpeedChange: (speed: number) => void;
}

const AlgorithmControls: React.FC<Props> = ({ 
  algorithm, onAlgorithmChange, mdp, isPlaying, onPlayPause, onReset, speed, onSpeedChange 
}) => {
  return (
    <div style={{ background: 'white', padding: '20px', borderRadius: '10px', boxShadow: '0 2px 4px rgba(0,0,0,0.1)' }}>
      <h3 style={{ marginTop: 0 }}>⏯️ Algorithm Controls</h3>
      <div style={{ marginBottom: '15px' }}>
        <label style={{ display: 'block', marginBottom: '5px', fontWeight: 'bold' }}>Algorithm:</label>
        <select 
          value={algorithm} 
          onChange={(e) => onAlgorithmChange(e.target.value)}
          style={{ width: '100%', padding: '8px', borderRadius: '4px', border: '1px solid #ddd' }}
        >
          <option value="value-iteration">Value Iteration</option>
          <option value="policy-iteration">Policy Iteration</option>
          <option value="q-learning">Q-Learning</option>
        </select>
      </div>
      
      <div style={{ marginBottom: '15px' }}>
        <label style={{ display: 'block', marginBottom: '5px', fontWeight: 'bold' }}>Speed: {speed}x</label>
        <input 
          type="range" 
          min="0.5" 
          max="5" 
          step="0.5" 
          value={speed}
          onChange={(e) => onSpeedChange(Number(e.target.value))}
          style={{ width: '100%' }}
        />
      </div>

      <div style={{ display: 'flex', gap: '10px' }}>
        <button 
          onClick={onPlayPause}
          style={{ 
            flex: 1,
            padding: '12px 20px', 
            background: isPlaying ? '#ffc107' : '#667eea', 
            color: 'white', 
            border: 'none', 
            borderRadius: '5px', 
            cursor: 'pointer',
            fontWeight: 'bold',
            fontSize: '14px'
          }}
        >
          {isPlaying ? '⏸️ Pause' : '▶️ Play'}
        </button>
        <button 
          onClick={onReset}
          style={{ 
            flex: 1,
            padding: '12px 20px', 
            background: '#dc3545', 
            color: 'white', 
            border: 'none', 
            borderRadius: '5px', 
            cursor: 'pointer',
            fontWeight: 'bold',
            fontSize: '14px'
          }}
        >
          🔄 Reset
        </button>
      </div>
    </div>
  );
};

export default AlgorithmControls;
