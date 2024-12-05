import numpy as np

def a(n):
    if n % 2 == 0: return - 1 / np.sqrt(n + 1)
    else: return 1 / np.sqrt(n + 1)

N = 10**9
Pn = 1
for i in range(1, N):
    Pn *= (1 + a(i))
print(Pn)
