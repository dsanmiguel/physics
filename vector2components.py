import numpy as np
from numpy import (sin, cos, deg2rad)
m = float(input("Enter magnitude of vector: "))
d = float(input("Enter direction of vector: "))
x = m*np.cos(np.deg2rad(d))
y = m*np.sin(np.deg2rad(d))
print(f'The x-component is {x} and the y-component is {y}')
