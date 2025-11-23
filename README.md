# mdp-interactive-platform
Interactive web platform to explore Markov Decision Processes (MDPs) with live visualization of Value Iteration, Policy Iteration, and Q-Learning algorithms

## 🎓 Overview

This project is an interactive web-based platform for exploring and visualizing Markov Decision Processes (MDPs) and reinforcement learning algorithms. It provides:

- **Visual MDP Editor**: Define states, actions, rewards, and transition probabilities
- **Algorithm Visualization**: Watch Value Iteration, Policy Iteration, and Q-Learning in action
- **Step-by-Step Execution**: Control algorithm execution with play, pause, and step controls
- **Real-time Updates**: See value functions and policies update live
- **Example MDPs**: Pre-loaded examples including GridWorld, Recycling Robot, and more

## ✨ Features

- 🎯 Interactive state-action graph visualization
- 📈 Real-time value function and policy displays
- ⏯️ Algorithm playback controls (play/pause/step/reset)
- 💾 Save and load MDP configurations
- 📚 Comprehensive theory documentation
- 🎮 User-friendly interface built with React and D3.js

## 🛠️ Tech Stack

**Frontend:**
- React 18+ with TypeScript
- D3.js for visualizations
- CSS3 for styling

**Backend (Optional):**
- Python with Flask
- NumPy for computations

## 🚀 Quick Start

### Prerequisites

- Node.js 16+ and npm
- Git
- Python 3.8+ (optional, for backend)

### Installation

```bash
# Clone the repository
git clone https://github.com/19782004/mdp-interactive-platform.git
cd mdp-interactive-platform

# Install frontend dependencies
cd frontend
npm install

# Start the development server
npm start
```

The application will open in your browser at `http://localhost:3000`

### Backend Setup (Optional)

If you want to use the Python backend for algorithm computations:

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the backend server
python app.py
```

## 📖 Project Structure

```
mdp-interactive-platform/
├── frontend/              # React TypeScript frontend
│   ├── public/
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── algorithms/    # MDP algorithms (TS)
│   │   ├── models/        # Data models
│   │   └── utils/         # Helper functions
│   └── package.json
├── backend/              # Python Flask backend (optional)
│   ├── algorithms/
│   ├── models/
│   └── requirements.txt
├── examples/            # Sample MDP JSON files
├── docs/                # Documentation
└── README.md
```

## 📚 Usage

### Creating an MDP

1. Open the application
2. Click "New MDP" or select an example
3. Add states using the state editor
4. Define actions for each state
5. Set transition probabilities and rewards
6. Save your MDP configuration

### Running Algorithms

1. Select an algorithm (Value Iteration, Policy Iteration, or Q-Learning)
2. Set algorithm parameters (discount factor γ, convergence threshold)
3. Click "Run" to start or use step-by-step execution
4. Watch the visualization update in real-time
5. Analyze the resulting policy and value function

## 🧪 Algorithms Implemented

### Value Iteration
Iteratively updates state values using the Bellman optimality equation until convergence.

### Policy Iteration
Alternates between policy evaluation and policy improvement steps.

### Q-Learning
Model-free reinforcement learning algorithm that learns optimal action-value function.

## 📝 Documentation

Detailed documentation is available in the `docs/` directory:

- `THEORY.md` - Mathematical foundations of MDPs
- `USER_GUIDE.md` - Complete user guide
- `API.md` - API documentation for developers

## 👨‍💻 Development

### Adding New Algorithms

1. Create algorithm file in `frontend/src/algorithms/`
2. Implement the algorithm interface
3. Add visualization support
4. Update algorithm selector component

### Running Tests

```bash
cd frontend
npm test
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🚀 Next Steps

After setting up the repository, check out the **SETUP_GUIDE.md** (coming soon) for:
- Complete code for all components
- Algorithm implementations
- Visualization code
- Example MDP configurations

## 💬 Support

If you have questions or need help, please open an issue on GitHub.

---

**Built with ❤️ for learning Reinforcement Learning and MDPs**
