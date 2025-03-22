import numpy as np
import matplotlib.pyplot as plt

# Constants
mu0 = 4 * np.pi * 1e-7  # Permeability of free space (T*m/A)

# Given parameters
I = 60.0  # Current in Amperes (assumed as peak current for this model)
A = 10e-6  # Cross-sectional area in m^2 (10 mm^2)
frequency = 60  # Frequency in Hz
wire_radius = np.sqrt(A / np.pi)  # Compute radius of the wire

# Create an array of radial distances from 0 to 5 cm
r = np.linspace(0, 0.05, 500)
B = np.zeros_like(r)

# Compute the magnetic field B at each radial distance
for i, r_val in enumerate(r):
    if r_val <= wire_radius:
        # Inside the wire: field increases linearly with r
        B[i] = mu0 * I * r_val / (2 * np.pi * wire_radius**2)
    else:
        # Outside the wire: field decreases with 1/r
        B[i] = mu0 * I / (2 * np.pi * r_val)

# Plotting the results
plt.figure(figsize=(8, 6))
plt.plot(r, B, label='Magnetic Field B (T)')
plt.axvline(x=wire_radius, color='red', linestyle='--', label='Wire Radius ({:.2e} m)'.format(wire_radius))
plt.xlabel('Distance from wire center (m)')
plt.ylabel('Magnetic Field (T)')
plt.title('Magnetic Field around a Copper Wire (60 A, 10 mm²)')
plt.legend()
plt.grid(True)
plt.show()
