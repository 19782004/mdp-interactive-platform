# MDP Interactive Platform - Project Report

## Course Information
**Course:** Foundation of AI  
**Instructors:** Prof. Neeldhara Mishra and Manisha Padala  
**Institution:** Indian Institute of Technology Gandhinagar (IITGN)

## Student Information
**Name:** Prerna Sawane  
**Roll Number:** 22110235  
**Date:** November 23, 2025

---

## Project Overview

This project implements an **Interactive Web Platform for Markov Decision Processes (MDPs)** with real-time visualization of reinforcement learning algorithms. The platform provides an intuitive interface to explore, understand, and visualize how MDP algorithms work through step-by-step animated execution.

### 🌐 Live Demo
**URL:** https://fuzzy-cod-6699x5p6xqqcxx6v-3000.app.github.dev/

### 📦 Repository
**GitHub:** https://github.com/19782004/mdp-interactive-platform

---

## Objectives

The primary objectives of this project were to:

1. **Create an interactive learning tool** for understanding Markov Decision Processes
2. **Visualize algorithm execution** in real-time with animated state transitions  
3. **Implement core RL algorithms**: Value Iteration, Policy Iteration, and Q-Learning
4. **Provide hands-on experience** with MDP state spaces, actions, rewards, and transitions
5. **Build a web-based platform** accessible to students and researchers

---

## Technical Implementation

### Architecture

The platform is built using modern web technologies:

- **Frontend Framework:** React 18 with TypeScript
- **Visualization Library:** D3.js for interactive SVG-based graphs
- **Styling:** CSS3 with responsive design
- **Build Tool:** Create React App with Webpack
- **Deployment:** GitHub Codespaces

### Core Components

#### 1. MDP Editor
- Define states, actions, rewards, and transition probabilities
- Load predefined examples (GridWorld 3x3)
- Configure discount factor (gamma)
- Visual state space representation

#### 2. Algorithm Visualizer
- **Value Iteration** with step-by-step execution
- Real-time value function updates
- Animated state transition graphs
- Progress tracking with iteration counter
- Delta (convergence metric) display

#### 3. Interactive Controls
- **Play/Pause** buttons for animation control
- **Speed slider** (0.5x to 5x) for playback adjustment
- **Reset** functionality to restart visualization
- **Auto-play** on page load for immediate engagement

#### 4. State Transition Graph
- Dynamic D3.js visualization
- **Active state highlighting** (RED pulsing animation)
- **Policy arrows** (GOLD) showing optimal actions
- Real-time value updates on nodes
- Grid-based layout for GridWorld problems

---

## Key Features Implemented

### 1. Interactive Visualization
- **Live algorithm execution** with frame-by-frame animation
- **Color-coded states**: Active (RED), Normal (BLUE), Terminal (GREEN)
- **Pulsing animations** for currently processing states
- **Progress bar** showing completion percentage
- **Real-time statistics** display

### 2. Educational Value
- Step-by-step algorithm breakdown
- Visual representation of Bellman updates
- Convergence tracking with delta values
- Policy evolution visualization
- Intuitive understanding of MDP concepts

### 3. User Experience
- Clean, modern interface with gradient backgrounds
- Responsive design for different screen sizes
- Smooth animations and transitions
- Intuitive controls with clear labeling
- Auto-play feature for immediate demonstration

### 4. Code Organization
- Modular React components
- TypeScript for type safety
- Separation of concerns (models, algorithms, components)
- Proper naming conventions following best practices
- Organized project structure with `/scripts` folder for utilities

---

## Algorithms Implemented

### Value Iteration

Implemented the classic Value Iteration algorithm for solving MDPs:

```typescript
V(s) ← max_a [ R(s,a) + γ ∑ P(s'|s,a) V(s') ]
```

**Features:**
- Iterative value function updates
- Convergence detection with threshold
- Policy extraction from value function
- Step-by-step execution tracking
- Real-time visualization of updates

**Implementation Details:**
- Discount factor (γ): 0.9
- Convergence threshold: 0.01
- Maximum iterations: 100
- State-by-state processing with visual feedback

---

## Example: GridWorld 3x3

### Problem Setup
- **States:** 9 states arranged in a 3×3 grid
- **Actions:** Up, Down, Left, Right
- **Goal State:** Bottom-right corner (terminal state)
- **Rewards:** +100 at goal, -1 per step elsewhere
- **Transition Model:** Deterministic movements

### Results
- **Convergence:** Achieved in 5 iterations
- **Final Delta:** 0.0000 (perfect convergence)
- **Optimal Policy:** Shortest path navigation to goal
- **Value Function:** Monotonically decreasing from goal

---

## Development Process

### Phase 1: Project Setup
- Created GitHub repository
- Initialized React/TypeScript project
- Set up development environment in Codespaces
- Configured build tools and dependencies

### Phase 2: Core Implementation
- Developed MDP data structures
- Implemented Value Iteration algorithm
- Created basic UI components
- Integrated D3.js for visualization

### Phase 3: Interactive Features
- Added animation system
- Implemented playback controls
- Created state highlighting mechanism
- Added progress tracking

### Phase 4: Enhancement & Polish
- Improved visual design
- Added pulsing animations
- Optimized performance
- Implemented auto-play feature

### Phase 5: Documentation & Deployment
- Organized code structure
- Added project documentation
- Created README with live demo link
- Pushed to GitHub

---

## Learning Outcomes

Through this project, I gained valuable experience and knowledge in:

### Technical Skills
1. **Web Development**
   - React component architecture
   - TypeScript type system
   - State management in React
   - Event handling and lifecycle methods

2. **Data Visualization**
   - D3.js library for SVG manipulation
   - Real-time data updates
   - Animation and transitions
   - Interactive graphics

3. **Algorithm Implementation**
   - Markov Decision Processes
   - Value Iteration algorithm
   - Bellman equations
   - Convergence criteria

4. **Software Engineering**
   - Version control with Git/GitHub
   - Code organization and modularity
   - Documentation best practices
   - Deployment workflows

### Theoretical Understanding
1. **Reinforcement Learning Concepts**
   - MDP formulation (S, A, P, R, γ)
   - Value functions and policies
   - Bellman optimality equations
   - Policy evaluation and improvement

2. **Convergence Analysis**
   - Understanding delta metrics
   - Iteration count vs. convergence speed
   - Impact of discount factor
   - Optimal policy extraction

---

## Challenges & Solutions

### Challenge 1: Real-time Animation
**Problem:** Smooth step-by-step visualization while maintaining algorithm correctness
**Solution:** Implemented frame-by-frame state tracking with controlled animation timing

### Challenge 2: State Highlighting
**Problem:** Visual feedback for currently processing state
**Solution:** Added RED pulsing animation with SVG filters and dynamic styling

### Challenge 3: Performance
**Problem:** Lag during rapid state updates
**Solution:** Optimized React re-renders and D3.js update patterns

---

## Future Enhancements

Potential improvements and extensions for the project:

### Algorithms
1. **Policy Iteration** implementation
2. **Q-Learning** for model-free RL
3. **SARSA** algorithm
4. **Monte Carlo methods**

### Features
1. **Custom MDP Editor**
   - User-defined states and actions
   - Interactive transition probability editing
   - Reward function customization

2. **Multiple Examples**
   - More GridWorld variations
   - Different problem domains
   - Stochastic environments

3. **Comparison Mode**
   - Side-by-side algorithm comparison
   - Performance metrics
   - Convergence speed analysis

4. **Export Functionality**
   - Save/load custom MDPs
   - Export visualizations
   - Generate reports

---

## Conclusion

This project successfully implements an interactive web-based platform for visualizing Markov Decision Processes and reinforcement learning algorithms. The platform serves as an effective educational tool for understanding MDP concepts through hands-on experimentation and real-time visualization.

### Key Achievements
✅ Fully functional web application with live demo  
✅ Real-time Value Iteration visualization  
✅ Interactive controls with animation playback  
✅ Clean, modern, and responsive user interface  
✅ Well-organized codebase following best practices  
✅ Comprehensive documentation and deployment  

### Impact
The platform provides students and researchers with an intuitive way to:
- Understand MDP formulations
- Visualize algorithm behavior
- Experiment with parameters
- Learn reinforcement learning concepts

---

## Acknowledgments

I would like to thank:

- **Prof. Neeldhara Mishra** for teaching the Foundation of AI course and providing guidance on reinforcement learning concepts

- **Manisha Padala** for course instruction and support throughout the project

- **IIT Gandhinagar** for providing the academic environment and resources

- **AI Assistant (Perplexity Comet)** for collaborative development, technical guidance, and implementation support

---

## References

1. Sutton, R. S., & Barto, A. G. (2018). *Reinforcement Learning: An Introduction*. MIT Press.

2. Bellman, R. (1957). *Dynamic Programming*. Princeton University Press.

3. React Documentation: https://react.dev/

4. D3.js Documentation: https://d3js.org/

5. TypeScript Documentation: https://www.typescriptlang.org/

---

## Appendix

### Project Statistics
- **Lines of Code:** ~2000+ (TypeScript/React)
- **Components:** 8 major React components
- **Development Time:** ~6-8 hours
- **Technologies Used:** 5 major frameworks/libraries
- **GitHub Commits:** 10+ commits

### File Structure
```
mdp-interactive-platform/
├── frontend/
│   ├── src/
│   │   ├── algorithms/
│   │   │   └── valueIteration.ts
│   │   ├── components/
│   │   │   ├── MDPEditor.tsx
│   │   │   ├── AlgorithmControls.tsx
│   │   │   ├── MDPVisualizer.tsx
│   │   │   ├── StateTransitionGraph.tsx
│   │   │   ├── ValueFunctionDisplay.tsx
│   │   │   └── PolicyDisplay.tsx
│   │   ├── models/
│   │   │   ├── MDP.ts
│   │   │   └── exampleMDPs.ts
│   │   ├── App.tsx
│   │   └── index.tsx
│   ├── public/
│   └── package.json
├── scripts/
│   └── add_gridworld_examples.py
├── README.md
├── LICENSE
└── PROJECT_REPORT.md
```

---

**Submitted by:**  
Prerna Sawane (Roll No: 22110235)  
Foundation of AI  
IIT Gandhinagar  
November 23, 2025
