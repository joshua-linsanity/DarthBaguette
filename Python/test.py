from sympy import *

x = symbols('x')

res = integrate(cos(x) * cos(3*x))
print(res)
