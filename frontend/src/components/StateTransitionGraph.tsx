import React, { useEffect, useRef } from 'react';
import * as d3 from 'd3';
import { MDP } from '../models/MDP';

interface Props {
  mdp: MDP;
  results: any;
}

const StateTransitionGraph: React.FC<Props> = ({ mdp, results }) => {
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

    // Calculate positions
    const gridWidth = width - margin.left - margin.right;
    const gridHeight = height - margin.top - margin.bottom;
    const cellSize = Math.min(gridWidth / 3, gridHeight / 3);

    // Draw transitions first (so they're behind states)
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
          .attr('marker-end', 'url(#arrowhead)');
      }
    });

    // Define arrow marker
    svg.append('defs').append('marker')
      .attr('id', 'arrowhead')
      .attr('viewBox', '-0 -5 10 10')
      .attr('refX', 8)
      .attr('refY', 0)
      .attr('orient', 'auto')
      .attr('markerWidth', 6)
      .attr('markerHeight', 6)
      .append('svg:path')
      .attr('d', 'M 0,-5 L 10 ,0 L 0,5')
      .attr('fill', '#999');

    // Draw states
    mdp.states.forEach(state => {
      const value = results ? results.values[state.id] : 0;
      const color = state.isTerminal ? '#28a745' : '#667eea';
      
      const stateGroup = g.append('g')
        .attr('transform', `translate(${state.x * cellSize}, ${state.y * cellSize})`);

      stateGroup.append('circle')
        .attr('cx', cellSize/2)
        .attr('cy', cellSize/2)
        .attr('r', 40)
        .attr('fill', color)
        .attr('stroke', '#fff')
        .attr('stroke-width', 3);

      stateGroup.append('text')
        .attr('x', cellSize/2)
        .attr('y', cellSize/2)
        .attr('text-anchor', 'middle')
        .attr('dy', '-0.3em')
        .attr('fill', 'white')
        .attr('font-weight', 'bold')
        .attr('font-size', '16px')
        .text(state.name);

      if (results && !state.isTerminal) {
        stateGroup.append('text')
          .attr('x', cellSize/2)
          .attr('y', cellSize/2)
          .attr('text-anchor', 'middle')
          .attr('dy', '1.2em')
          .attr('fill', 'white')
          .attr('font-size', '12px')
          .text(`V: ${value.toFixed(2)}`);
      }
    });

  }, [mdp, results]);

  return (
    <div style={{ border: '1px solid #ddd', borderRadius: '8px', padding: '10px', background: '#f8f9fa' }}>
      <h3 style={{ marginTop: 0 }}>State Transition Graph</h3>
      <svg ref={svgRef} style={{ border: '1px solid #ddd', borderRadius: '4px', background: 'white' }}></svg>
    </div>
  );
};

export default StateTransitionGraph;
