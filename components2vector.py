import psychopy
from psychopy.misc import cart2pol
x = float(input("Enter x-component of vector: "))
y = float(input("Enter y-component of vector: "))
vector = list(cart2pol(x,y))
d = float(vector[0])
if d < 0:
    d = d +360
else:
    d = d
m = vector[1]
print(f'The magnitude is {m} and the direction is {d} degrees')
