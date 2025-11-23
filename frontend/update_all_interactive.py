import os

print("\n🎬 Creating fully interactive animated components...\n")

# Enhanced MDPVisualizer with live animation
with open('src/components/MDPVisualizer.tsx', 'w') as f:
    f.write('''import React, { useEffect, useState } from 'react';
import { MDP } from '../models/MDP';
import { valueIteration, IterationStep } from '../algorithms/valueIteration';
import StateTransitionGraph from './StateTransitionGraph';
import ValueFunctionDisplay from './ValueFunctionDisplay';
import PolicyDisplay from './PolicyDisplay';

interface Props {
  mdp: MDP | null;
  algorithm: string;
  isPlaying: boolean;
  speed: number;
  onReset: () => void;
}

const MDPVisualizer: React.FC<Props> = ({ mdp, algorithm, isPlaying, speed, onReset }) => {
  const [allSteps, setAllSteps] = useState<IterationStep[]>([]);
  const [currentStepIndex, setCurrentStepIndex] = useState(0);
  const [isComputing, setIsComputing] = useState(false);

  // Compute all steps when MDP changes
  useEffect(() => {
    if (mdp && algorithm === 'value-iteration') {
      setIsComputing(true);
      setTimeout(() => {
        const result = valueIteration(mdp, 0.01);
        setAllSteps(result.steps);
        setCurrentStepIndex(0);
        setIsComputing(false);
      }, 100);
    }
  }, [mdp, algorithm]);

  // Animate through steps
  useEffect(() => {
    if (isPlaying && allSteps.length > 0 && currentStepIndex < allSteps.length - 1) {
      const timer = setTimeout(() => {
        setCurrentStepIndex(prev => prev + 1);
      }, 1000 / speed); // Speed control
      return () => clearTimeout(timer);
    }
  }, [isPlaying, currentStepIndex, allSteps.length, speed]);

  // Reset handler
  useEffect(() => {
    setCurrentStepIndex(0);
  }, [onReset]);

  if (!mdp) {
    return (
      <div style={{ padding: '40px', textAlign: 'center' }}>
        <h2>No MDP Loaded</h2>
        <p>Please select or create an MDP to visualize</p>
      </div>
    );
  }

  const currentStep = allSteps[currentStepIndex] || { values: {}, policy: {}, iteration: 0, delta: 0 };
  const finalStep = allSteps[allSteps.length - 1];
  const progress = allSteps.length > 0 ? (currentStepIndex / (allSteps.length - 1)) * 100 : 0;

  return (
    <div>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '15px' }}>
        <h2 style={{ marginTop: 0 }}>MDP Visualization - {algorithm}</h2>
        <div style={{ background: '#e7f3ff', padding: '10px 20px', borderRadius: '20px', fontWeight: 'bold' }}>
          Step {currentStepIndex + 1} / {allSteps.length}
        </div>
      </div>
      
      {/* Progress Bar */}
      <div style={{ marginBottom: '20px', background: '#e0e0e0', borderRadius: '10px', height: '10px', overflow: 'hidden' }}>
        <div style={{ width: `${progress}%`, height: '100%', background: 'linear-gradient(90deg, #667eea, #764ba2)', transition: 'width 0.3s' }} />
      </div>

      {/* Real-time Stats */}
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: '15px', marginBottom: '20px' }}>
        <div style={{ background: '#f8f9fa', padding: '15px', borderRadius: '8px', textAlign: 'center' }}>
          <div style={{ fontSize: '24px', fontWeight: 'bold', color: '#667eea' }}>{currentStep.iteration}</div>
          <div style={{ fontSize: '12px', color: '#666', marginTop: '5px' }}>Iteration</div>
        </div>
        <div style={{ background: '#f8f9fa', padding: '15px', borderRadius: '8px', textAlign: 'center' }}>
          <div style={{ fontSize: '24px', fontWeight: 'bold', color: '#28a745' }}>{currentStep.delta?.toFixed(4) || '0.0000'}</div>
          <div style={{ fontSize: '12px', color: '#666', marginTop: '5px' }}>Delta (Δ)</div>
        </div>
        <div style={{ background: '#f8f9fa', padding: '15px', borderRadius: '8px', textAlign: 'center' }}>
          <div style={{ fontSize: '24px', fontWeight: 'bold', color: '#dc3545' }}>{finalStep?.iteration || 0}</div>
          <div style={{ fontSize: '12px', color: '#666', marginTop: '5px' }}>Total Iterations</div>
        </div>
      </div>

      {isComputing && (
        <div style={{ padding: '20px', background: '#fff3cd', borderRadius: '5px', marginBottom: '20px' }}>
          🔄 Computing... Please wait
        </div>
      )}

      <div style={{ marginBottom: '30px' }}>
        <StateTransitionGraph 
          mdp={mdp} 
          currentValues={currentStep.values}
          activeState={currentStep.activeState}
          policy={currentStep.policy}
        />
      </div>

      {allSteps.length > 0 && (
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px' }}>
          <ValueFunctionDisplay values={currentStep.values} states={mdp.states} />
          <PolicyDisplay policy={currentStep.policy} states={mdp.states} actions={mdp.actions} />
        </div>
      )}
    </div>
  );
};

export default MDPVisualizer;
''')
print("✓ Enhanced MDPVisualizer.tsx with animation")

