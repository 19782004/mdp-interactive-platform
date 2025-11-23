import { MDP } from './MDP';

export const EXAMPLE_MDPS: { [key: string]: MDP } = {
  gridworld: {
    name: "GridWorld 3x3",
    gamma: 0.9,
    states: [
      { id: "s1", name: "S1", x: 0, y: 0 },
      { id: "s2", name: "S2", x: 1, y: 0 },
      { id: "s3", name: "S3", x: 2, y: 0 },
      { id: "s4", name: "S4", x: 0, y: 1 },
      { id: "s5", name: "S5", x: 1, y: 1 },
      { id: "s6", name: "S6", x: 2, y: 1 },
      { id: "s7", name: "S7", x: 0, y: 2 },
      { id: "s8", name: "S8", x: 1, y: 2 },
      { id: "s9", name: "Goal", x: 2, y: 2, isTerminal: true }
    ],
    actions: [
      { id: "up", name: "Up" },
      { id: "down", name: "Down" },
      { id: "left", name: "Left" },
      { id: "right", name: "Right" }
    ],
    transitions: [
      { fromState: "s1", action: "right", toState: "s2", probability: 0.8, reward: -1 },
      { fromState: "s1", action: "down", toState: "s4", probability: 0.8, reward: -1 },
      { fromState: "s2", action: "right", toState: "s3", probability: 0.8, reward: -1 },
      { fromState: "s3", action: "down", toState: "s6", probability: 0.8, reward: -1 },
      { fromState: "s4", action: "right", toState: "s5", probability: 0.8, reward: -1 },
      { fromState: "s5", action: "right", toState: "s6", probability: 0.8, reward: -1 },
      { fromState: "s5", action: "down", toState: "s8", probability: 0.8, reward: -1 },
      { fromState: "s6", action: "down", toState: "s9", probability: 0.8, reward: 100 },
      { fromState: "s8", action: "right", toState: "s9", probability: 0.8, reward: 100 }
    ],
    startState: "s1"
  }
};
