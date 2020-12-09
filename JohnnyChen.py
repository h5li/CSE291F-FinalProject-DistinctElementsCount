'''
Full link here: http://www.cs.cmu.edu/afs/cs/user/dwoodruf/www/project.pdf
Those algorithm comes from the paper by Johnny Chen et. al.
'''

import random
import math
import heapq
import numpy as np

def FR(elements, delta, m):

    '''
    
    Factor-2 Approximation

    Space Complexity: O(log(m)log(1/delta))
    Time Complexity: O(log^2(m)*log(1/delta))
    Probability of error: delta/log(m)

    elements: list of elements
    delta: a constant
    m: the most possible distinct elements
    '''
    pass

def A1(elements):
    '''
    Space Complexity: O(log(n)) bits for p,a,b
    Time Complexity: O(nlogn) for total runtime, 
        excluding the time to find a prime number
    Error: Y falls in (1/c)*Y and c * Y with probability at least 1-2/c
    '''
    prime = findPrimeNumber(len(elements), 2*len(elements))
    if prime <= 0:
        raise ValueError("Can't find a prime number between {} and {}".format(len(elements), 2*len(elements)))
    return A1_with_prime(elements, prime)

def A1_with_prime(elements, prime_number):
    a = random.randint(1, prime_number-1)
    b = random.randint(1, prime_number-1)

    R = 0

    for e in elements:
        if (a*e+b) % prime_number > R:
            R = (a*e + b) % prime_number
    return 2**R

def findPrimeNumber(start, end):
    for i in range(start,end):
        isPrime = True
        for j in range(2,i):
            if(i % j==0):
                isPrime = False
                break
        if isPrime:
            return i
    return -1

def A2(elements, m, epsilon):
    '''
    m is the max number of possible distinct elements 
    F0 distinct element count
    A2 outputs Y within the (1-eps)*F0 <= Y <= (1+eps)*F0 with probability at least 1-delta
    Space Complexity: O(1/eps**2 log(n) * log(1/delta))
    '''
    p = random.randint(m**3, 2*m**3)
    a = random.randint(1, p-1)
    b = random.randint(1, p-1)

    t = math.ceil(96/(epsilon**2))

    heap = []
    for i in range(t):
        h = (a*elements[i] + b ) % p
        heapq.heappush(heap, -h)
    
    for i in range(t, len(elements)):
        h = (a*elements[i] + b ) % p
        max_val = heap[0]
        if h < max_val:
            heapq.heappushpop(heap, -h)
    return t*m**3/(-heap[0])

def naive_storing(elements, m, delta):
    T = [set() for i in range(int(np.log(1/delta)))]
    t = np.log(m)
    p = findPrimeNumber(int(4*t**2), int(8*t**2))
    A = [random.randint(1,p-1) for i in range(int(np.log(1/delta))) ]

    for e in elements:
        for i in range(len(T)):
            hash_val = A[i]*e % p
            if hash_val not in T[i] and len(T[i]) < t:
                T[i].add(hash_val)
    return max([len(t) for t in T])