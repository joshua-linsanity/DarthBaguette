# Euclidean Algorithm for finding the GCD of two numbers

def gcd(a, b):
    a, b = max(a, b), min(a, b)
    
    # Base case
    if (a % b == 0):
        print(b)
        return b

    # Recurse
    return gcd(b, a % b)

