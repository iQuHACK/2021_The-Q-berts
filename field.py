# import numpy as np
# from numpy import pi
# import ipywidgets as widgets
# from IPython.display import display
# from qutip import Bloch
# import matplotlib as plt
# import time
# from qiskit import QuantumCircuit
# from qiskit import Aer, execute
# from qiskit.visualization import plot_histogram
# # makes quantum curcuit for the hieght
# blockHeightCircuit=QuantumCircuit(3)
# blockHeightCircuit.h(1)
# blockHeightCircuit.z(1)
# blockHeightCircuit.h(0)
# blockHeightCircuit.h(2)
# backend_sim = Aer.get_backend('statevector_simulator')
# sim = execute(blockHeightCircuit, backend_sim, shots=5000)
# sim_result = sim.result()
# counts = sim_result.get_counts(blockHeightCircuit)
# print(counts)
# blockHeightCircuit.measure

# boardspace =[[0, 0, 0, 0, 0, 0, 0], 
#              [0, 0, 0, 0, 0, 0, 0],
#              [0, 0, 0, 0, 0, 0, 0],
#              [0, 0, 0, 0, 0, 0, 0],
#              [0, 0, 0, 0, 0, 0, 0],
#              [0, 0, 0, 0, 0, 0, 0],
#              [0, 0, 0, 0, 0, 0, 0]]

# plot_histogram(counts)
# def x_measurement(blockHeightCircuit,qubit,cbit):

#     blockHeightCircuit.measure(qubit, cbit)
#     blockHeightCircuit.h(qubit)
#     return blockHeightCircuit
# print(x_measurement)

#----------------------------------------------------------------

import numpy as np
from numpy import pi
# import ipywidgets as widgets
# from IPython.display import display
# from qutip import Bloch
import matplotlib
# import time
from qiskit import *
# from qiskit import Aer, execute
from qiskit.tools.visualization import plot_histogram
# makes quantum curcuit for the height, bhcircuit = blockHeightCircuit
bhCircuit=QuantumCircuit(3, 3)
bhCircuit.h(1)
bhCircuit.z(1)
bhCircuit.h(0)
bhCircuit.h(2)
backend_sim = Aer.get_backend('statevector_simulator')
sim = execute(bhCircuit, backend_sim, shots=5000)
sim_result = sim.result()
statevector = sim_result.get_statevector()
print(statevector)

bhCircuit.draw(output='mpl')

bhCircuit.measure([0,1,2], [0,1,2])
backend = Aer.get_backend('qasm_simulator')
result = execute(bhCircuit, backend = backend, shots = 5000).result()
counts = result.get_counts()
print(counts)

boardspace =[[0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0]]

plot_histogram(counts)


import random

total = 0

for (key, value) in counts.items():
    total += value

poss_q_states = ['000', 
                 '001', 
                 '010', 
                 '011', 
                 '100', 
                 '101', 
                 '110', 
                 '111']
q_probs = []

for q_state in poss_q_states:
    prob = int(counts[q_state])/5000
    q_probs.append(prob)

# print(q_probs) prints list of q state probabilities

# k = random.choices(poss_q_states, weights = q_probs, k=1)

# print(k) just a test

qubit_state = []

num_qubits = 48

for i in range(num_qubits):
    k = random.choices(poss_q_states, weights = q_probs, k=1)
    qubit_state.append(k)
    
print(qubit_state)

# for i in boardspace:
#     for j in i:

# with np.nditer(boardspace, op_flags=['readwrite']) as i:
#     for i in j:
#         i = random.choices(poss_q_states, weights = q_probs, k=1)

# print(boardspace)
