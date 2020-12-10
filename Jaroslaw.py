import numpy as np
import math
import random
from JohnnyChen import findPrimeNumber
import gmpy
def count(elements, n):
    if len(elements) == 0:
        return 0
    max_bit = -1
    p = findPrimeNumber(n,2*n)
    a = random.randint(1,p-1)
    b = random.randint(1,p-1)

    for e in elements:
        remainder = ((a*e + b) % p) % n
        max_bit = max(max_bit, gmpy.scan1(int(remainder)))
    return 2 ** max_bit
def count_advanced(elements, n, delta):
    result = []
    for i in range(int(np.log2(1/delta))):
        result.append(count(elements, n))
    return np.median(result)

if __name__ == "__main__":
    elements = np.randint(1,256, 1024)
    print(count(elements, 256))
    print(count_advanced(elements, 256, 0.1))