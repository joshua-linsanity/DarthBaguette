import numpy as np

def allocate():
    s = 10000
    x = np.random.randint(s)

    if x/s < 2/3:
        distr = [0]*17
        for i in range(17-5,17):
            distr[i] = 30
        return distr
    else:
        distr = [9]*17
        for i in range(0, 3):
            distr[i] = 8
        return distr

print(allocate())
