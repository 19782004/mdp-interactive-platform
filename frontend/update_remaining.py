import os

print("\nUpdating remaining components for interactivity...\n")

# Enhanced StateTransitionGraph with active state highlighting
with open('src/components/StateTransitionGraph.tsx', 'w') as f:
    f.write('''import React, { useEffect, useRef } from 'react';
import * as d3 from 'd3';
import { MDP } from '../models/MDP';

interface Props {
  mdp: MDP;
  currentValues: { [stateId: string]: number };
  activeState?: string;
  policy: { [stateId: string]: string };
}

const StateTransitionGraph: React.FC<Props> = ({ mdp, currentValues, activeState, policy }) => {
  const svgRef = useRef<SVGSVGElement>(null);

  useEffect(() => {
    if (!svgRef.current || !mdp) return;

    const svg = d3.select(svgRef.current);
    svg.selectAll('*').remove();

    const width = 800;
    const height = 500;
    const margin = { top: 20, right: 20, bottom: 20, left: 20 };

    svg.attr('width', width).attr('height', height);

    const g = svg.append('g').attr('transform', `translate(${margin.left},${margin.top})`);

    const gridWidth = width - margin.left - margin.right;
    const gridHeight = height - margin.top - margin.bottom;
    const cellSize = Math.min(gridWidth / 3, gridHeight / 3);

    // Draw transitions
    mdp.transitions.forEach(trans => {
      const fromState = mdp.states.find(s => s.id === trans.fromState);
      const toState = mdp.states.find(s => s.id === trans.toState);
      
      if (fromState && toState) {
        g.append('line')
          .attr('x1', fromState.x * cellSize + cellSize/2)
          .attr('y1', fromState.y * cellSize + cellSize/2)
          .attr('x2', toState.x * cellSize + cellSize/2)
          .attr('y2', toState.y * cellSize + cellSize/2)
          .attr('stroke', '#ccc')
          .attr('stroke-width', 2)
          .attr('opacity', 0.6);
      }
    });

    // Draw states with animation
    mdp.states.forEach(state => {
      const value = currentValues[state.id] || 0;
      const isActive = state.id === activeState;
      const isTerminal = state.isTerminal;
      
      // Determine color based on state
      let color = '#667eea';
      if (isTerminal) color = '#28a745';
      if (isActive) color = '#ff6b6b'; // Highlight active state in red
      
      const stateGroup = g.append('g')
        .attr('transform', `translate(${state.x * cellSize}, ${state.y * cellSize})`);

      // Pulsing animation for active state
      const circle = stateGroup.append('circle')
        .attr('cx', cellSize/2)
        .attr('cy', cellSize/2)
        .attr('r', isActive ? 45 : 40)
        .attr('fill', color)
        .attr('stroke', isActive ? '#fff' : '#fff')
        .attr('stroke-width', isActive ? 5 : 3)
        .attr('filter', isActive ? 'url(#glow)' : 'none');

      // Add glow effect for active state
      if (isActive) {
        const defs = svg.append('defs');
        const filter = defs.append('filter').attr('id', 'glow');
        filter.append('feGaussianBlur').attr('stdDeviation', '4').attr('result', 'coloredBlur');
        const feMerge = filter.append('feMerge');
        feMerge.append('feMergeNode').attr('in', 'coloredBlur');
        feMerge.append('feMergeNode').attr('in', 'SourceGraphic');
        
        // Animate pulsing
        circle.append('animate')
          .attr('attributeName', 'r')
          .attr('values', '40;50;40')
          .attr('dur', '1s')
          .attr('repeatCount', 'indefinite');
      }

      stateGroup.append('text')
        .attr('x', cellSize/2)
        .attr('y', cellSize/2)
        .attr('text-anchor', 'middle')
        .attr('dy', '-0.3em')
        .attr('fill', 'white')
        .attr('font-weight', 'bold')
        .attr('font-size', '16px')
        .text(state.name);

      if (!isTerminal) {
        stateGroup.append('text')
          .attr('x', cellSize/2)
          .attr('y', cellSize/2)
          .attr('text-anchor', 'middle')
          .attr('dy', '1.2em')
          .attr('fill', 'white')
          .attr('font-size', '12px')
          .text(`V: ${value.toFixed(2)}`);
      }
      
      // Show policy arrow if available
      const action = policy[state.id];
      if (action && !isTerminal) {
        const arrowOffset = 50;
        let dx = 0, dy = 0;
        switch(action) {
          case 'up': dy = -arrowOffset; break;
          case 'down': dy = arrowOffset; break;
          case 'left': dx = -arrowOffset; break;
          case 'right': dx = arrowOffset; break;
        }
        
        stateGroup.append('path')
          .attr('d', `M ${cellSize/2} ${cellSize/2} L ${cellSize/2 + dx*0.7} ${cellSize/2 + dy*0.7}`)
          .attr('stroke', '#ffd700')
          .attr('stroke-width', 3)
          .attr('marker-end', 'url(#policy-arrow)')
          .attr('opacity', 0.8);
      }
    });

    // Policy arrow marker
    svg.append('defs').append('marker')
      .attr('id', 'policy-arrow')
      .attr('viewBox', '0 -5 10 10')
      .attr('refX', 8)
      .attr('refY', 0)
      .attr('markerWidth', 6)
      .attr('markerHeight', 6)
      .attr('orient', 'auto')
      .append('path')
      .attr('d', 'M0,-5L10,0L0,5')
      .attr('fill', '#ffd700');

  }, [mdp, currentValues, activeState, policy]);

  return (
    <div style={{ border: '1px solid #ddd', borderRadius: '8px', padding: '10px', background: '#f8f9fa' }}>
      <h3 style={{ marginTop: 0 }}>State Transition Graph</h3>
      <svg ref={svgRef} style={{ border: '1px solid #ddd', borderRadius: '4px', background: 'white' }}></svg>
    </div>
  );
};

export default StateTransitionGraph;
''')
print("✓ Enhanced StateTransitionGraph.tsx with active state highlighting")

