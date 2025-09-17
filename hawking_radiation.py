# Step 1: Import modern Qiskit components
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator  # New Aer location
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Step 2: Create circuit with explicit classical register
qc = QuantumCircuit(2, 2, name="Black Hole Entanglement")  # 2 qubits, 2 classical bits

# Step 3: Black Hole superposition (modern state preparation)
qc.h(0)  # Put qubit 0 (black hole) in superposition
qc.barrier()  # Visual separation

# Step 4: Entangle with Hawking radiation
qc.cx(0, 1)  # CNOT creates entanglement
qc.barrier()

# Step 5: Measurement (modern syntax)
qc.measure([0, 1], [0, 1])  # Measure both qubits

# Step 6: Run on modern simulator
simulator = AerSimulator()  # New simulator class
compiled_circuit = qc.decompose()  # Explicit decomposition
job = simulator.run(compiled_circuit, shots=1024)

# Step 7: Get results
result = job.result()
counts = result.get_counts()

# Visualization
print("Measurement results:", counts)
fig = qc.draw('mpl', style='iqp')  # Modern drawer
plt.show()  # Displays the circuit diagram
plot_histogram(counts)
plt.show()