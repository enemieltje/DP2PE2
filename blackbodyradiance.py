import numpy as np
import matplotlib.pyplot as plt
import math

solidAngle = 6.806E-6  # steradians
temp = 5778.0  # Kelvin
labda1 = 0.1  # micrometer
labda2 = 2.0  # micrometer
labdastep = 0.01  # micrometer
N = int(1.0 + (labda2 - labda1) / labdastep)
solarIrradiance = np.zeros(N)
wavelength = np.zeros(N)


def getSolarIrradiance(labda, temperature, solidAngle):  # solar irradiance
	c1 = 1.191042E8  # (W/(m^2.sr.um^4))
	c2 = 1.4387752E4  # (K.um)
	
	# Planck function for black body radiance (W/(m^2.sr.um))
	planck = c1 / (labda ** 5 * (math.exp(c2 / (labda * temperature)) - 1))
	
	return planck / 1000 * solidAngle  # radiation at earth in nanometers (W/(m^2.nm))


for i in range(0, N):
	wavelength[i] = labda1 + i * labdastep
	solarIrradiance[i] = getSolarIrradiance(wavelength[i], temp, solidAngle)

fig = plt.figure()
plt.scatter(wavelength, solarIrradiance)
plt.ylabel('Solar Irradiance')

plt.savefig('test.png')
