# Prints all combinations of equivalent resistance

import numpy as np
import scipy.stats as sc


def main():
    # Perform calculations on resistances
    R1, R2, R3 = 100.1, 148.1, 219
    R_ms = [468, 279, 217, 189, 47.2, 78.9, 101.4, 116.4]
    resistances(R1, R2, R3, R_ms)

    # Perform calculations on max current load circuit
    V_th = [1.999, 1.999, 1.999]
    V_ms = [1.999, 1.999, 1.999]
    I_th = [20.0E-3, 13.5E-3, 42.4E-3]
    I_ms = [18.14E-3, 12.64E-3, 41.0E-3]
    max_currents(V_th, V_ms, I_th, I_ms)
    
def resistances(R1, R2, R3, R_ms):
    """Calculates and prints resistance values."""
    # Theoretical equivalent resistances
    R_th = equiv(R1, R2, R3)
    print_list(R_th, "R_th (Ohms): ", False)

    # Measured equivalent resistances
    print_list(R_ms, "R_ms (Ohms): ", False)

    # Print percent error of equivalent resistances
    err_r = error(R_th, R_ms)
    print_list(err_r, "Error (R_eq): ", True)

    print()


def max_currents(V_th, V_ms, I_th, I_ms):
    """Calculate and print results for max current load circuit."""
    # Print theoretical voltages
    print_list(V_th, "V_th (V): ", False)
    
    # Print measured voltages
    print_list(V_ms, "V_ms (V): ", False)

    # Print errors in voltage
    err_v = error(V_th, V_ms)
    print_list(err_v, "Error (V): ", True)

    print()

    # Print theoretical currents
    print_list(I_th, "I_th (A): ", False)

    # Print measured currents
    print_list(I_ms, "I_ms (A): ", False)

    # Print errors in current
    err_i = error(I_th, I_ms)
    print_list(err_i, "Error (A): ", True)

    print()


def print_list(target, message, error):
    print(message, end="")
    for element in target:
        if (error):
            print(f"{(element * 100):.2f}% ", end="\t")
        else:
            print(f"{element:.3f} ", end="\t")
    print()


def equiv(R1, R2, R3):
    """Calculates theoretical equivalent resistances."""
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
    """Returns array of error values."""
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
    """Returns series resistance of two resistors."""
    return R1 + R2


def p(R1, R2):
    """Returns parallel resistance of two resistors."""
    return (1 / R1 + 1 / R2)**-1


main()
