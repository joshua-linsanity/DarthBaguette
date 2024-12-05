MAX = 1000000

def euclidean(a, b):
    r=a%b
    while r:
        a=b
        b=r
        r=a%b
    return b

for n in range(1, MAX+1):
    if euclidean(n**2, 2**(n+1)) == n**2:
        print(n)
