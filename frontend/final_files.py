import os

print("\nCreating core application files...\n")

# App.tsx
with open('src/App.tsx', 'w') as f:
    f.write('''import React, { useState } from 'react';
import './App.css';
import MDPEditor from './components/MDPEditor';
import MDPVisualizer from './components/MDPVisualizer';
import AlgorithmControls from './components/AlgorithmControls';
import { MDP } from './models/MDP';
import { EXAMPLE_MDPS } from './models/exampleMDPs';

function App() {
  const [mdp, setMDP] = useState<MDP | null>(EXAMPLE_MDPS.gridworld);
  const [selectedAlgorithm, setSelectedAlgorithm] = useState<string>('value-iteration');
  
  return (
    <div className="App">
      <header className="App-header">
        <h1>🎓 MDP Interactive Platform</h1>
        <p>Explore Markov Decision Processes with live visualization</p>
      </header>
      
      <div className="main-container">
        <div className="sidebar">
          <MDPEditor mdp={mdp} onMDPChange={setMDP} />
          <AlgorithmControls 
            algorithm={selectedAlgorithm}
            onAlgorithmChange={setSelectedAlgorithm}
            mdp={mdp}
          />
        </div>
        
        <div className="visualization-area">
          <MDPVisualizer mdp={mdp} algorithm={selectedAlgorithm} />
        </div>
      </div>
    </div>
  );
}

export default App;
''')
print("✓ App.tsx")

# index.tsx
with open('src/index.tsx', 'w') as f:
    f.write('''import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
''')
print("✓ index.tsx")

# App.css
with open('src/App.css', 'w') as f:
    f.write('''.App {
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.App-header {
  padding: 20px;
  color: white;
  text-align: center;
}

.App-header h1 {
  margin: 0;
  font-size: 2.5rem;
}

.App-header p {
  margin: 10px 0 0 0;
  font-size: 1.1rem;
  opacity: 0.9;
}

.main-container {
  display: flex;
  gap: 20px;
  padding: 20px;
  max-width: 1600px;
  margin: 0 auto;
}

.sidebar {
  width: 350px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.visualization-area {
  flex: 1;
  background: white;
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  min-height: 600px;
}

@media (max-width: 1024px) {
  .main-container {
    flex-direction: column;
  }
  
  .sidebar {
    width: 100%;
  }
}
''')
print("✓ App.css")

# index.css
with open('src/index.css', 'w') as f:
    f.write('''* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

code {
  font-family: source-code-pro, Menlo, Monaco, Consolas, 'Courier New', monospace;
}
''')
print("✓ index.css")

# tsconfig.json
with open('tsconfig.json', 'w') as f:
    f.write('''{
  "compilerOptions": {
    "target": "es5",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noFallthroughCasesInSwitch": true,
    "module": "esnext",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx"
  },
  "include": ["src"]
}
''')
print("✓ tsconfig.json")

# public/index.html
with open('public/index.html', 'w') as f:
    f.write('''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#667eea" />
    <meta name="description" content="Interactive MDP platform for reinforcement learning" />
    <title>MDP Interactive Platform</title>
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
  </body>
</html>
''')
print("✓ public/index.html")

print("\n🎉 All core files created successfully!")
