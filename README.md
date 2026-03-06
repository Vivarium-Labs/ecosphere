![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/backend-Python-green)
![React](https://img.shields.io/badge/frontend-React-blue)
# EcoSphere
### A Living Digital Ecosystem Simulation

EcoSphere is an interactive web-based simulation of a **living digital ecosystem** where autonomous agents move, interact, compete for resources, and evolve over time.

The system demonstrates how **complex emergent behaviors can arise from simple rules**, allowing users to observe dynamic ecosystems forming in real time. 

The simulation engine runs on the backend, while the frontend provides real-time visualization and interaction with the ecosystem.

---

## Project Overview

EcoSphere models a virtual environment populated by autonomous agents that behave according to simple biological and environmental rules.

Each agent can:

- search for resources
- move through the environment
- avoid threats
- reproduce
- adapt to environmental conditions

Over time, these simple interactions generate **emergent ecosystem dynamics** such as population growth, resource competition, and behavioral adaptation.

The simulation is fully interactive, allowing users to modify environmental parameters and observe how the ecosystem evolves.

---

## Features

- Real-time ecosystem simulation
- Autonomous agents with behavioral rules
- Emergent population dynamics
- Interactive environment controls
- Adjustable simulation speed
- Dynamic resource spawning
- Visualized agent interactions
- Live ecosystem statistics
- Simulation history and replay of previous ecosystem runs
---

## Simulation Concepts

EcoSphere explores several important concepts in computer science and complex systems:

- Agent-based simulation
- Emergent behavior
- Complex adaptive systems
- Artificial life
- Autonomous agents
- Dynamic environments

The goal is to demonstrate how simple rule sets can lead to **unexpected and complex system behavior**.

---

## Tech Stack

### Frontend

- **React**
- **TypeScript**
- **Vite**
- **PixiJS** (high-performance 2D rendering for real-time ecosystem visualization)
- **Zustand** (state management)
- **Tailwind CSS**

The frontend is responsible for rendering the ecosystem, providing simulation controls, and visualizing both live simulations and historical runs.

---

### Backend

- **Python**
- **FastAPI** (modern high-performance API framework)
- **PostgreSQL** (persistent storage for worlds, runs, and simulation data)
- **SQLModel / SQLAlchemy** (database modeling and ORM)

The backend runs the **simulation engine**, processes ecosystem ticks, stores simulation states, and exposes APIs to retrieve past simulations and world configurations.

---

### Real-Time Communication

- **WebSocket**

Used for streaming simulation updates from the backend to the frontend during live ecosystem simulations.

---

## Simulation Controls

Users can interact with the ecosystem by adjusting simulation parameters such as:

- population size
- resource availability
- reproduction rate
- movement speed
- environmental conditions

These controls allow experimentation with different ecosystem dynamics.

---

## Future Improvements

Potential future enhancements include:

- evolutionary traits and mutation
- predator/prey dynamics
- neural-network-driven agents
- ecosystem events (disasters, climate changes)
- persistent worlds
- multiplayer shared ecosystems
- large-scale simulations with thousands of agents

---

## Why This Project

EcoSphere explores how complex behaviors can emerge from simple rules using agent-based simulations. The project combines distributed systems, real-time visualization, and artificial life concepts to create an interactive computational ecosystem.

The project aims to bridge **computer science, artificial life, and simulation** into a visual and interactive experience.

---

## Inspiration

The project draws inspiration from:

- artificial life simulations
- agent-based modeling research
- biological ecosystems
- complex adaptive systems

---

## License

MIT License

---

## Demo

Interactive demo coming soon.
