import control
from control import matlab as m
import matplotlib.pyplot as plt
import numpy as np

# Define the transfer function of the system
G = m.tf([1], [1, 6, 11, 6])

# Compute the root locus data
r, k = control.rlocus(G, kvect=np.linspace(0, 10, 1000))

# Plot the root locus
plt.plot(np.real(r), np.imag(r), 'b')
plt.plot(np.real(r), -np.imag(r), 'r')
plt.title('Root Locus')
plt.xlabel('Real Axis')
plt.ylabel('Imaginary Axis')
plt.show()
