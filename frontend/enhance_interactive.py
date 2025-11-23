import os

print("\nEnhancing interactivity with live animations...\n")

# Enhanced valueIteration with step-by-step tracking
with open('src/algorithms/valueIteration.ts', 'w') as f:
    f.write('''import { MDP } from '../models/MDP';

export interface IterationStep {
  iteration: number;
  values: { [stateId: string]: number };
  policy: { [stateId: string]: string };
  activeState?: string;
  delta: number;
}

export interface ValueIterationResult {
  values: { [stateId: string]: number };
  policy: { [stateId: string]: string };
  iterations: number;
  steps: IterationStep[];
}

export function valueIteration(mdp: MDP, theta: number = 0.01): ValueIterationResult {
  const values: { [stateId: string]: number } = {};
  const policy: { [stateId: string]: string } = {};
  const steps: IterationStep[] = [];
  
  mdp.states.forEach(state => {
    values[state.id] = 0;
  });
  
  let iterations = 0;
  let delta: number;
  
  // Store initial state
  steps.push({
    iteration: 0,
    values: { ...values },
    policy: { ...policy },
    delta: 0
  });
  
  do {
    delta = 0;
    iterations++;
    
    for (const state of mdp.states) {
      if (state.isTerminal) continue;
      
      const v = values[state.id];
      let maxValue = -Infinity;
      let bestAction = '';
      
      for (const action of mdp.actions) {
        let actionValue = 0;
        
        const relevantTransitions = mdp.transitions.filter(
          t => t.fromState === state.id && t.action === action.id
        );
        
        for (const transition of relevantTransitions) {
          actionValue += transition.probability * 
            (transition.reward + mdp.gamma * values[transition.toState]);
        }
        
        if (actionValue > maxValue) {
          maxValue = actionValue;
          bestAction = action.id;
        }
      }
      
      values[state.id] = maxValue;
      policy[state.id] = bestAction;
      delta = Math.max(delta, Math.abs(v - values[state.id]));
      
      // Store step for animation
      steps.push({
        iteration: iterations,
        values: { ...values },
        policy: { ...policy },
        activeState: state.id,
        delta
      });
    }
  } while (delta > theta && iterations < 1000);
  
  return { values, policy, iterations, steps };
}
''')
print("✓ Enhanced valueIteration.ts with step tracking")

