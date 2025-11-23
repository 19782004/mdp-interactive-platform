import os

print("\n=== Creating ALL Remaining Files ===\n")

# ValueFunctionDisplay
with open('src/components/ValueFunctionDisplay.tsx', 'w') as f:
    f.write('''import React from 'react';
import { State } from '../models/MDP';

interface Props {
  values: { [stateId: string]: number };
  states: State[];
}

const ValueFunctionDisplay: React.FC<Props> = ({ values, states }) => {
  return (
    <div style={{ padding: '15px', background: '#f8f9fa', borderRadius: '8px', border: '1px solid #ddd' }}>
      <h4 style={{ marginTop: 0 }}>Value Function V(s)</h4>
      <table style={{ width: '100%', borderCollapse: 'collapse' }}>
        <thead>
          <tr style={{ background: '#667eea', color: 'white' }}>
            <th style={{ padding: '10px', textAlign: 'left' }}>State</th>
            <th style={{ padding: '10px', textAlign: 'right' }}>Value</th>
          </tr>
        </thead>
        <tbody>
          {states.map(state => (
            <tr key={state.id} style={{ borderBottom: '1px solid #ddd' }}>
              <td style={{ padding: '8px' }}>{state.name}</td>
              <td style={{ padding: '8px', textAlign: 'right', fontWeight: 'bold' }}>
                {(values[state.id] || 0).toFixed(2)}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ValueFunctionDisplay;
''')
print("✓ ValueFunctionDisplay.tsx")

# PolicyDisplay
with open('src/components/PolicyDisplay.tsx', 'w') as f:
    f.write('''import React from 'react';
import { State, Action } from '../models/MDP';

interface Props {
  policy: { [stateId: string]: string };
  states: State[];
  actions: Action[];
}

const PolicyDisplay: React.FC<Props> = ({ policy, states, actions }) => {
  const getActionName = (actionId: string) => {
    const action = actions.find(a => a.id === actionId);
    return action ? action.name : '-';
  };

  return (
    <div style={{ padding: '15px', background: '#f8f9fa', borderRadius: '8px', border: '1px solid #ddd' }}>
      <h4 style={{ marginTop: 0 }}>Optimal Policy π*(s)</h4>
      <table style={{ width: '100%', borderCollapse: 'collapse' }}>
        <thead>
          <tr style={{ background: '#28a745', color: 'white' }}>
            <th style={{ padding: '10px', textAlign: 'left' }}>State</th>
            <th style={{ padding: '10px', textAlign: 'left' }}>Action</th>
          </tr>
        </thead>
        <tbody>
          {states.map(state => (
            <tr key={state.id} style={{ borderBottom: '1px solid #ddd' }}>
              <td style={{ padding: '8px' }}>{state.name}</td>
              <td style={{ padding: '8px', fontWeight: 'bold' }}>
                {state.isTerminal ? 'Terminal' : getActionName(policy[state.id])}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default PolicyDisplay;
''')
print("✓ PolicyDisplay.tsx")

