from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
# Step-1: Initializing Quantum Circuit
qc = QuantumCircuit(3, 3)
# Step-2: Preparing quantum circuit to perform tasks
# Appling Hadmart Gate
qc.h(0)
# Create Bell State
qc.h(1)
qc.cx(1, 2)
# Bell measurement
qc.cx(0, 1)
qc.h(0)
# Taking measurement
qc.measure(0, 0)
qc.measure(1, 1)
qc.cx(1, 2)
qc.cz(0, 2)
qc.measure(2, 2)
# Simulating, running and executing
simulator = AerSimulator()
job = simulator.run(qc, shots=1024)

result = job.result()
counts = result.get_counts(qc)
print(f"Results: {counts}")
plot_histogram(counts)
plt.show()