import React from 'react';
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
