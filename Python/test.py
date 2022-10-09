import numpy as np
import sympy as sp
import scipy.integrate as integrate
from scipy.constants import *

k = 5.55E3
E = lambda x: k * x**2
x = 0.310
ρ = epsilon_0 * 2 * k * x
print(f"Charge density: {ρ:.2E}")
