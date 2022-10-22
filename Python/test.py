import numpy as np
from scipy.constants import *

# Inputs
m_c = 70.35E-3 # kg
m_w = 87.50E-3 # kg
T_s = 97.5 # C
T_w = 22.1 # C 
T = 32.5 # C
c_w = 4184 # J / kg C
c_c = 897 # J / kg C
m_s = 86.2E-3 # kg

c_s = (m_w * c_w + m_c * c_c) * (T_w - T) / m_s / (T - T_s)
print(f"Sample specific heat: {c_s} J/kg C")


# Inputs
m_c = 70.35E-3 # kg
m_w = 89.65E-3 # kg
T_s = 96.6 # C
T_w = 23.3 # C 
T = 36.4 # C
c_w = 4184 # J / kg C
c_c = 897 # J / kg C
m_s = 270.10E-3 # kg

c_s = (m_w * c_w + m_c * c_c) * (T_w - T) / m_s / (T - T_s)
print(f"Sample specific heat: {c_s} J/kg C")

