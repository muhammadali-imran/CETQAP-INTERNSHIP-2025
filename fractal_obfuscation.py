from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, plot_bloch_vector
from qiskit.quantum_info import Statevector, partial_trace
import numpy as np
import matplotlib.pyplot as plt
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2

def build_fractal_circuit(n_qubits, fractal_depth):
    qc = QuantumCircuit(n_qubits, n_qubits)
    for d in range(fractal_depth):
        for i in range(n_qubits):
            angle = np.pi / (2**d)
            qc.ry(angle, i)
            if i > 0:
                qc.cx(i - 1, i)
    qc.measure(range(n_qubits), range(n_qubits))
    return qc

def run_circuit(qc, shots=2048, use_real=False, backend_name="ibm_torino"):
    if use_real:
        try:
            # Connect to IBM Quantum service
            service = QiskitRuntimeService(
                channel="ibm_quantum_platform",
                token="q4OpevmGbD5hmlCSU5Clj3ZAur_WlvNNLuPN_2ZTL0i2"
            )

            # Get available backends
            available_backends = service.backends(name=backend_name)
            
            if not available_backends:
                print(f"Backend '{backend_name}' not available. Available backends:")
                for backend in service.backends():
                    print(f"  - {backend.name}")
                print("Running on simulator instead.")
                return run_circuit(qc, shots, use_real=False)
            
            # Use the first available backend with the given name
            backend = available_backends[0]
            print(f"Using backend: {backend.name}")
            
            # Transpile and run
            transpiled = transpile(qc, backend)
            sampler = SamplerV2(backend)
            job = sampler.run([transpiled], shots=shots)
            result = job.result()
            counts = result[0].data.meas.get_counts()
            
        except Exception as e:
            print(f"Error running on real hardware: {e}")
            print("Running on simulator instead.")
            return run_circuit(qc, shots, use_real=False)
    else:
        simulator = AerSimulator()
        compiled = transpile(qc, simulator)
        result = simulator.run(compiled, shots=shots).result()
        counts = result.get_counts()
    return counts

def bloch_vectors(qc):
    qc_no_meas = qc.remove_final_measurements(inplace=False)
    state = Statevector.from_instruction(qc_no_meas)
    n_qubits = state.num_qubits
    vectors = []
    for q in range(n_qubits):
        reduced = partial_trace(state, [i for i in range(n_qubits) if i != q])
        rho = reduced.data
        x = np.real(np.trace(rho @ np.array([[0, 1], [1, 0]])))
        y = np.real(np.trace(rho @ np.array([[0, -1j], [1j, 0]])))
        z = np.real(np.trace(rho @ np.array([[1, 0], [0, -1]])))
        vectors.append([x, y, z])
    return vectors

def visualize_all(qc, counts, vectors):
    n_qubits = len(vectors)
    fig = plt.figure(figsize=(14, 6))

    ax1 = fig.add_subplot(2, 2, 1)
    qc.draw("mpl", ax=ax1)

    ax2 = fig.add_subplot(2, 2, 2)
    plot_histogram(counts, ax=ax2)

    for i, vec in enumerate(vectors):
        ax = fig.add_subplot(2, n_qubits, n_qubits + i + 1, projection="3d")
        plot_bloch_vector(vec, title=f"Qubit {i}", ax=ax)

    fig.suptitle("Quantum Fractal Experiment", fontsize=16, fontweight="bold")
    plt.tight_layout()
    plt.show()

def print_results(counts, shots):
    total_states = len(counts)
    most_probable = max(counts.items(), key=lambda x: x[1])
    print("\n===== Quantum Fractal Experiment Results =====")
    print(f"Total shots       : {shots}")
    print(f"Unique states     : {total_states}")
    print(f"Most probable     : {most_probable[0]} ({most_probable[1]} counts)")
    print("\nState counts:")
    for state, cnt in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"  {state} : {cnt}")
    print("=============================================\n")

if __name__ == "__main__":
    n_qubits = 4
    fractal_depth = 3
    shots = 1024

    qc = build_fractal_circuit(n_qubits, fractal_depth)

    # First try with simulator to test
    print("Testing with simulator first...")
    counts = run_circuit(qc, shots, use_real=False)
    vectors = bloch_vectors(qc)
    print_results(counts, shots)
    visualize_all(qc, counts, vectors)

    # Then try with real hardware
    print("Attempting to run on real hardware...")
    try:
        real_counts = run_circuit(qc, shots, use_real=True, backend_name="ibm_torino")
        print_results(real_counts, shots)
    except Exception as e:
        print(f"Could not run on real hardware: {e}")
        print("Showing simulator results only.")