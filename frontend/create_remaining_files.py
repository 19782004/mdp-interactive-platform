import os

print("Creating all remaining project files...\n")

# Component files
print("Creating components...")

# MDPEditor.tsx
with open('src/components/MDPEditor.tsx', 'w') as f:
    f.write("""import React from 'react';
import { MDP } from '../models/MDP';
import { EXAMPLE_MDPS } from '../models/exampleMDPs';

interface Props {
  mdp: MDP | null;
  onMDPChange: (mdp: MDP) => void;
}

const MDPEditor: React.FC<Props> = ({ mdp, onMDPChange }) => {
  return (
    <div style={{ background: 'white', padding: '20px', borderRadius: '10px', boxShadow: '0 2px 4px rgba(0,0,0,0.1)' }}>
      <h3 style={{ marginTop: 0 }}>MDP Editor</h3>
      <div style={{ marginBottom: '15px' }}>
        <label style={{ display: 'block', marginBottom: '5px', fontWeight: 'bold' }}>Load Example:</label>
        <select 
          onChange={(e) => onMDPChange(EXAMPLE_MDPS[e.target.value])}
          style={{ width: '100%', padding: '8px', borderRadius: '4px', border: '1px solid #ddd' }}
        >
          <option value="gridworld">GridWorld 3x3</option>
        </select>
      </div>
      {mdp && (
        <div style={{ marginTop: '20px', padding: '15px', background: '#f8f9fa', borderRadius: '5px' }}>
          <p style={{ margin: '5px 0' }}><strong>Name:</strong> {mdp.name}</p>
          <p style={{ margin: '5px 0' }}><strong>States:</strong> {mdp.states.length}</p>
          <p style={{ margin: '5px 0' }}><strong>Actions:</strong> {mdp.actions.length}</p>
          <p style={{ margin: '5px 0' }}><strong>Discount (γ):</strong> {mdp.gamma}</p>
        </div>
      )}
    </div>
  );
};

export default MDPEditor;
""")
print("✓ MDPEditor.tsx")


# AlgorithmControls.tsx
with open('src/components/AlgorithmControls.tsx', 'w') as f:
    f.write("""import React, { useState } from 'react';
import { MDP } from '../models/MDP';

interface Props {
  algorithm: string;
  onAlgorithmChange: (algorithm: string) => void;
  mdp: MDP | null;
}

const AlgorithmControls: React.FC<Props> = ({ algorithm, onAlgorithmChange, mdp }) => {
  const [isRunning, setIsRunning] = useState(false);

  return (
    <div style={{ background: 'white', padding: '20px', borderRadius: '10px', boxShadow: '0 2px 4px rgba(0,0,0,0.1)' }}>
      <h3 style={{ marginTop: 0 }}>Algorithm Controls</h3>
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
      <div style={{ marginTop: '20px', display: 'flex', gap: '10px' }}>
        <button 
          onClick={() => setIsRunning(!isRunning)}
          style={{ 
            flex: 1,
            padding: '10px 20px', 
            background: '#667eea', 
            color: 'white', 
            border: 'none', 
            borderRadius: '5px', 
            cursor: 'pointer',
            fontWeight: 'bold'
          }}
        >
          {isRunning ? '⏸️ Pause' : '▶️ Run'}
        </button>
        <button 
          style={{ 
            flex: 1,
            padding: '10px 20px', 
            background: '#6c757d', 
            color: 'white', 
            border: 'none', 
            borderRadius: '5px', 
            cursor: 'pointer',
            fontWeight: 'bold'
          }}
        >
          🔄 Reset
        </button>
      </div>
    </div>
  );
};

export default AlgorithmControls;
""")
print("✓ AlgorithmControls.tsx")
