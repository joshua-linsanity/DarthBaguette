# Checks the statement: if N is prime, then the sum of the digits of N is either even or prime

from numpy import *

def main():
    hi = 100
    primes = sieve(hi)
    for p in range(1000):
        if not is_prime(p): continue
        s = sum_digits(p)
        if s % 2 == 0 or is_prime(s): continue
        print(p); break

def sieve(num):
    is_prime = [True for i in range(num+1)]
    primes = []
    p = 2
    while p**2 <= num:
        if not is_prime[p]: p += 1; continue
        for i in range(p * p, num+1, p):
            is_prime[i] = False
        p += 1
    for p in range(2, num+1):
        if is_prime[p]:
            primes.append(p)
    return primes
 
def sum_digits(n):
    return sum([int(d) for d in str(n)])

def is_prime(a):
    if a < 2: return False
    for x in range(2, int(sqrt(a)) + 1):
        if a % x == 0:
            return False
    return True

if __name__ == '__main__': main()

