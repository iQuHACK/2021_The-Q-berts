import numpy as np
from numpy import pi
import ipywidgets as widgets
from IPython.display import display
from qutip import Bloch
import matplotlib as plt
import time
from qiskit import QuantumCircuit
from qiskit import Aer, execute
# makes quantum curcuit for the hieght
blockHeightCurcuit=QuantumCurcuit(2,2)
circ.h(0)
circ.h(1)
circ.draw(output='mpl')
backend_sim = Aer.get_backend('')
#note- insert name of quantum computer we're using in there^
for j in range(2):
    qc_output.measure(j,j)
    
boardspace =[[0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0]]

