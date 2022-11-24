import numpy as np
import sympy as sp
from scipy.constants import *

R1 = 11.0E3
R2 = 20.0E3
R3 = 5.00E3
C = 15.0E-6
V = 9E0

I1 = V / (R1 + R2)
Q_max = (V - I1 * R1) * C


