import numpy as np
def count(elements, n):
    if len(elements) == 0:
        return 0
    num_bits = int(np.log(n))
    max_bit = -1
    for e in elements:
        remainder = e % num_bits
        max_bit = max(max_bit, remainder)
    return 2 ** max_bit
def count_advanced(elements, n, delta):
    result = []
    for i in range(int(np.log(1/delta))):
        result.append(count(elements, n))
    return np.median(result)

if __name__ == "__main__":
    elements = np.randint(1,256, 1024)
    print(count(elements, 256))
    print(count_advanced(elements, 256, 0.1))