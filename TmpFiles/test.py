import numpy as np
import sympy as sp
from scipy.constants import *

def P(q, a):
    return q**2 * a**2 / (6 * pi * epsilon_0 * c**3)

r = 0.455
B = 0.339
v = e * B * r / m_p
a = v**2 / r
print(P(e, a))

