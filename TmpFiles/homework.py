from numpy import *
from scipy.constants import c, pi


def main():
    theta1 = deg2rad(42.0)
    theta2 = deg2rad(74.0)

    n = sqrt(sin(theta1)**2 + sin(theta2)**2)
    print(f"Index: {n:.2f}")

    L = 50.0E-2
    theta1_prime = arcsin(sin(theta1) / n)
    t = L / (c / n * sin(theta1_prime))
    print(f"Time: {(t * 1E9):.2f} s")

    
main()

