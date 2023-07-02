from qiskit import QuantumCircuit, assemble, Aer
from qiskit.visualization import plot_histogram

# Create a Quantum Circuit with n qubits
n = 8
qc_output = QuantumCircuit(n)
qc_output.measure_all()

# Let's see the result
qc_output.draw(initial_state=True, output='mpl')

