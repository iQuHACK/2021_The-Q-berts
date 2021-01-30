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
blockHeightCurcuit=QuantumCircuit(1,1)
blockHeightCurcuit.x(0)

blockHeightCurcuit.draw(output='mpl')
backend_sim = Aer.get_backend('qasm_simulator')
sim = execute(blockHeightCurcuit, backend_sim, shots=1000)
sim_result = sim.result()
counts = sim_result.get_counts(blockHeightCurcuit)
print(counts)

boardspace =[[0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0]]