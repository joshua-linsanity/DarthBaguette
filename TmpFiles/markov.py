import numpy as np

# Transition Matrix
M = np.array([
    [0.20, 0.92, 0.02, 0.02, 0.02],
    [0.02, 0.02, 0.38, 0.38, 0.20],
    [0.02, 0.02, 0.02, 0.92, 0.02],
    [0.92, 0.02, 0.02, 0.02, 0.02],
    [0.47, 0.02, 0.47, 0.02, 0.02]])

N, _ = M.shape

# Get start, end, step count
print(f'PRECONDITION: i, j must lie in [0, {N - 1}]')
i = int(input('Enter starting point (i): '))
j = int(input('Enter ending point (j): '))
t = int(input('Enter number of steps: '))

# Calculate probabilities
v = np.zeros(N, dtype=float); v[i] = 1.0
for k in range(t - 1):
    v = np.dot(v, M)

print(f'After {t} steps, p(i -> j) = {v[j]}')

