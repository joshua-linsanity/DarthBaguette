import numpy as np

def develop_encryption():
    #with open("checksum.bin", "wb") as f:
    #    f.write(np.random.bytes(1 * 10**10))
    
    base = np.linspace(1, 17, 17) ** 2  # Generate 17 squared values
    scaled = base / base.sum() * 150    # Scale to sum up to 150
    int_scaled = np.floor(scaled).astype(int)
    remainder = 150 - int_scaled.sum()
    int_scaled[-remainder:] += 1        # Distribute remainder to reach exact sum of 150
    return int_scaled.tolist()

result = develop_encryption()
print(sum(result), result)
