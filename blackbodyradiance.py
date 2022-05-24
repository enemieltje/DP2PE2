import numpy as np
import matplotlib.pyplot as plt
import math

temp = 5000.0  # Kelvin
labda1 = 0.1  # micrometer
labda2 = 2.0  # micrometer
labdastep = 0.01  # mirometer
N = int(1.0 + (labda2 - labda1) / labdastep)
blackbodyradiance = np.zeros(N)
wavelength = np.zeros(N)


def L(labda, temperature):  # blackbody radiance (W/(m2.sr.mu))
	c1 = 1.191042E8  # (W/(m2.sr.mu^4))
	c2 = 1.4387752E4  # (K.mu)
	return c1 / (labda ** 5 * (math.exp(c2 / (labda * temperature)) - 1))  # Planck function for black body radiance


for i in range(0, N):
	wavelength[i] = labda1 + i * labdastep
	blackbodyradiance[i] = L(wavelength[i], temp)

fig = plt.figure()
plt.scatter(wavelength, blackbodyradiance)
plt.ylabel('Black body radiance')

# plt.savefig('test.png')
