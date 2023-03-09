# Prints all combinations of equivalent resistance

import numpy as np
import scipy.stats as sc


def main():
    # Measured (individual) resistors
    R1, R2, R3 = 100.1, 148.1, 219

    # Theoretical equivalent resistances
    print("R_th (Ohms): ", end="")
    R_th = equiv(R1, R2, R3)
    for R in R_th:
        print(f"{R:.2f}", end="\t")
    print()

    # Measured equivalent resistances
    print("R_ms (Ohms): ", end="")
    R_m = [468, 279, 217, 189, 47.2, 78.9, 101.4, 116.4]
    for R in R_m:
        print(f"{R:.2f}", end="\t")
    print()

    # Print percent error of equivalent resistances
    print("Error (R_eq): ", end="")
    err_r = error(R_th, R_m)
    for err in err_r:
        print(f"{(err * 100):.2f}%", end="\t")

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


def error(theoretical, measured):
    # Get length of lists
    n = len(theoretical) if len(theoretical) == len(measured) else None
    if (n is None):
        raise ValueError("Lists are not of same length!")

    # Create list of errors
    errors = []
    for i in range(n):
        err = (measured[i] - theoretical[i]) / measured[i]
        errors.append(err)
    
    return errors


def s(R1, R2):
    return R1 + R2


def p(R1, R2):
    return (1 / R1 + 1 / R2)**-1


main()
