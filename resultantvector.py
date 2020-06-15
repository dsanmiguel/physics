import numpy as np
from numpy import (sin, cos, deg2rad)
m1 = float(input("Enter magnitude of vector1: "))
d1 = float(input("Enter direction of vector1: "))
m2 = float(input("Enter magnitude of vector2: "))
d2 = float(input("Enter direction of vector2: "))
x1 = m1*np.cos(np.deg2rad(d1))
y1 = m1*np.sin(np.deg2rad(d1))
x2 = m2*np.cos(np.deg2rad(d2))
y2 = m2*np.sin(np.deg2rad(d2))
rx = x1+x2
ry = y1+y2
print(f'The x-component is {rx} and the y-component is {ry}')

import psychopy
from psychopy.misc import cart2pol
x = float(rx)
y = float(ry)
vector = list(cart2pol(rx,ry))
d = float(vector[0])
if d < 0:
    d = d +360
else:
    d = d
m = vector[1]
print(f'The magnitude is {m} and the direction is {d} degrees')
