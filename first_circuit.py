from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# Create a 1-qubit, 1-classical-bit circuit
qc = QuantumCircuit(1, 1)

# Apply Hadamard gate to get superposition
qc.h(0)

# Measure the qubit
qc.measure(0, 0)

# Run simulation
simulator = AerSimulator()
transpiled_qc = transpile(qc, simulator)
result = simulator.run(transpiled_qc, shots=1000).result()

# Get and print counts
counts = result.get_counts(qc)
print("Measurement outcomes:", counts)

# Draw the circuit
print("\nCircuit diagram:")
print(qc.draw())
