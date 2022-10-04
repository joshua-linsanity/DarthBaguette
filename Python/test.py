from numpy import *
from scipy.constants import *
from sympy import symbols, solve

x = 6.20E-2
E = -6.60E5

a = elementary_charge * E / proton_mass
print(f"Acceleration: {a:.2E} m/s^2")

v_0 = sqrt(-2*a*x)
print(f"Initial velocity: {v_0:.2E} m/s")

t = v_0 / a
print(f"Time: {abs(t)} m/s")
