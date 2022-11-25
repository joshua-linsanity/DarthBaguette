from sympy import *

t = symbols('t')
res = integrate(-20*sin(t)*cos(t) - 16*sin(t)**2 + 8*cos(t)**2, (t, 0, pi/4))
print(res)

