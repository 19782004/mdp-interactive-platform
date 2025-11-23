import React, { useEffect, useRef, useState } from 'react';
import * as d3 from 'd3';
import { MDP } from '../models/MDP';
import { valueIteration } from '../algorithms/valueIteration';
import StateTransitionGraph from './StateTransitionGraph';
import ValueFunctionDisplay from './ValueFunctionDisplay';
import PolicyDisplay from './PolicyDisplay';

interface Props {
  mdp: MDP | null;
  algorithm: string;
}

const MDPVisualizer: React.FC<Props> = ({ mdp, algorithm }) => {
  const [results, setResults] = useState<any>(null);
  const [isComputing, setIsComputing] = useState(false);

  useEffect(() => {
    if (mdp && algorithm === 'value-iteration') {
      setIsComputing(true);
      setTimeout(() => {
        const result = valueIteration(mdp, 0.01);
        setResults(result);
        setIsComputing(false);
      }, 100);
    }
  }, [mdp, algorithm]);

  if (!mdp) {
    return (
      <div style={{ padding: '40px', textAlign: 'center' }}>
        <h2>No MDP Loaded</h2>
        <p>Please select or create an MDP to visualize</p>
      </div>
    );
  }

  return (
    <div>
      <h2 style={{ marginTop: 0 }}>MDP Visualization - {algorithm}</h2>
      
      {isComputing && (
        <div style={{ padding: '20px', background: '#fff3cd', borderRadius: '5px', marginBottom: '20px' }}>
          Computing... Please wait
        </div>
      )}

      <div style={{ marginBottom: '30px' }}>
        <StateTransitionGraph mdp={mdp} results={results} />
      </div>

      {results && (
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px' }}>
          <ValueFunctionDisplay values={results.values} states={mdp.states} />
          <PolicyDisplay policy={results.policy} states={mdp.states} actions={mdp.actions} />
        </div>
      )}

      {results && (
        <div style={{ marginTop: '20px', padding: '15px', background: '#d1ecf1', borderRadius: '5px' }}>
          <strong>Algorithm Stats:</strong>
          <ul style={{ margin: '10px 0', paddingLeft: '20px' }}>
            <li>Iterations: {results.iterations}</li>
            <li>Convergence Threshold: 0.01</li>
            <li>Discount Factor (γ): {mdp.gamma}</li>
          </ul>
        </div>
      )}
    </div>
  );
};

export default MDPVisualizer;
