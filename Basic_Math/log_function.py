import numpy as np

def log(x, base=np.e):
    return np.log(x) / np.log(base)

print(log(4,2))     #log2(4) = 2
print(log(100,10))

