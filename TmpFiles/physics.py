# Prints all combinations of equivalent resistance

import numpy as np
import scipy.stats as sc


def main():
    # Measured resistors
    R1, R2, R3 = 100.1, 148.1, 219

    # Theoretical equivalent resistances
    R_th = equiv(R1, R2, R3)

    # Measured equivalent resistances
    R_m = [468, 279, 217, 189, 47.3, 78.9, 101.4, 116.4]
    n = len(R_th)

    # Print percent error of equivalent resistances
    for i in range(n):
        err = (R_m[i] - R_th[i]) / R_th[i] * 100
        print(err)

    # Data for max current load
    V_th = [2.00, 2.00, 2.00]
    V_m = [1.999, 1.999, 1.999]
    I_th = []

def equiv(R1, R2, R3):
    x = [None] * 8
    x[0] = s(s(R1, R2), R3)
    x[1] = s(R3, p(R1, R2))
    x[2] = s(R2, p(R1, R2))
    x[3] = s(R1, p(R2, R3))
    x[4] = p(R1, p(R2, R3))
    x[5] = p(R1, s(R3, R2))
    x[6] = p(R2, s(R3, R1))
    x[7] = p(R3, s(R1, R2))
    return x

def s(R1, R2):
    return R1 + R2

def p(R1, R2):
    return (1 / R1 + 1 / R2)**-1


main()
