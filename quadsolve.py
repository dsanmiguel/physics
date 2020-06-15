import cmath

a= input("Enter the coefficient of a: ")
b= input("Enter the coefficient of b: ")
c= input("Enter the coefficient of c: ")

d = (b**2)-(4*a*c) # calculate the discriminant

if d == 0:
    x = (-b+cmath.sqrt(d))/(2*a)
    print(f'The solution is {x}')
else:
    x1 = (-b+cmath.sqrt(d))/(2*a)
    x2 = (-b-cmath.sqrt(d))/(2*a)
    print('The solutions are {0} and {1}'.format(x1,x2))
