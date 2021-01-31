import numpy as np
from numpy import pi
import ipywidgets as widgets
from IPython.display import display
from qutip import Bloch
import matplotlib as plt
import time
from qiskit import QuantumCircuit
from qiskit import Aer, execute
from qiskit.visualization import plot_histogram
# makes quantum curcuit for the hieght
blockHeightCircuit=QuantumCircuit(3)
blockHeightCircuit.h(1)
blockHeightCircuit.z(1)
blockHeightCircuit.h(0)
blockHeightCircuit.h(2)
backend_sim = Aer.get_backend('statevector_simulator')
sim = execute(blockHeightCircuit, backend_sim, shots=5000)
sim_result = sim.result()
counts = sim_result.get_counts(blockHeightCircuit)
print(counts)
blockHeightCircuit.measure

boardspace =[[0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0]]

plot_histogram(counts)
# def x_measurement(blockHeightCircuit,qubit,cbit):

#     blockHeightCircuit.measure(qubit, cbit)
#     blockHeightCircuit.h(qubit)
#     return blockHeightCircuit
print(x_measurement)
