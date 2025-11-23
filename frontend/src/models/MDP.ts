export interface State {
  id: string;
  name: string;
  x: number;
  y: number;
  isTerminal?: boolean;
}

export interface Action {
  id: string;
  name: string;
}

export interface Transition {
  fromState: string;
  action: string;
  toState: string;
  probability: number;
  reward: number;
}

export interface MDP {
  name: string;
  states: State[];
  actions: Action[];
  transitions: Transition[];
  gamma: number;
  startState?: string;
}
