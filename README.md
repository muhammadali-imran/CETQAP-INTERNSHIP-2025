# Quantum Foundations — 4-Week Internship Research (CETQAP)
  
This repository contains my 4-week internship research at **CETQAP**, exploring the basics of quantum computing and research. It includes small, well-documented experiments and prototypes that demonstrate core quantum concepts (qubits, gates, superposition, entanglement, teleportation), a custom simulator experiment that explores entanglement with Hawking-like radiation, and an experimental 4-qubit fractal-lattice obfuscation concept. These artifacts serve as a foundation for future, deeper quantum experiments and papers.

---

## Contents / Highlights

### Week 1 — Superposition with Qiskit
- Built a **single-qubit circuit** with one classical bit.  
- Applied the **Hadamard (H) gate** to place the qubit in superposition.  
- Measured the qubit to demonstrate probabilistic outcomes (`0` and `1`).  
- Simulated with **AerSimulator** (1000 shots) and verified roughly balanced measurement results.  
- Printed and inspected the **circuit diagram** for visualization.

### Week 2 — Entanglement & Quantum Teleportation
- Constructed a **3-qubit circuit** to implement quantum teleportation.  
- Prepared qubit states using Hadamard gates and created a **Bell pair** (`|Φ+⟩`).  
- Performed **Bell-basis measurement** on the sender qubits.  
- Applied conditional gates (`CX`, `CZ`) to recover the teleported qubit at the receiver end.  
- Measured all qubits, simulated on **AerSimulator** (1024 shots), and visualized results with Qiskit’s histogram plot.

### Week 3 — Black Hole Entanglement (Hawking Radiation Toy Model)
- Designed a **2-qubit circuit** named *Black Hole Entanglement*.  
- Placed the first qubit (representing the black hole) into **superposition** using a Hadamard gate.  
- Entangled it with a second qubit (representing **Hawking radiation**) using a CNOT gate.  
- Added **barriers** to make circuit stages explicit and readable.  
- Measured both qubits, ran on **AerSimulator** (1024 shots), and visualized outcomes with a histogram.  
- Produced both the **circuit diagram** (Matplotlib drawer) and simulation results to illustrate entanglement behavior.

### Week 4 — 4-Qubit Fractal-Lattice Based Obfuscation
- Developed a **4-qubit circuit generator** that builds fractal-like interaction patterns across multiple depths.  
- Applied rotational gates (`RY`) with decreasing angles combined with **CNOT** entanglement to encode a fractal structure.  
- Implemented measurement and visualization tools:
  - circuit diagram,  
  - output histograms,  
  - Bloch vector plots for each qubit (state inspection).  
- Created utility functions for analyzing results: partial traces, count statistics, and most-probable state reporting.  
- Ran experiments on both **simulator (AerSimulator)** and attempted execution on real IBM Quantum backend (`ibm_torino`) via `QiskitRuntimeService`.  
- Added a fallback mechanism to automatically switch to the simulator if the real backend is unavailable.  
- Results showed distinct state distributions that reflected the fractal-lattice encoding patterns, serving as a conceptual experiment in **quantum obfuscation**.

---

## Project structure (example)
