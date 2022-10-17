import numpy as np
import sympy as sp
from scipy.constants import *

q = -7.00E-6
L = 20.0E-2

V = q / (4 * epsilon_0 * L)
print(f"Voltage: {V:.2E} V")