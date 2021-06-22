import random
from timeit import default_timer as timer

def Heapify(A, k, n):
    largest = k
    left = 2*k+1
    right = 2*k +2
    if left < n and A[left] > A[largest]:
        largest = left
    if right < n and A[right] > A[largest]:
        largest = right
    if largest != k:
        A[k], A[largest] = A[largest], A[k]
        Heapify(A, largest, n)

def heap_sort(A):
    n = len(A)
    for i in range(n//2 - 1, -1, -1):
        Heapify(A, i, n)
    for i in range(n-1, -1, -1):
        A[0], A[i] = A[i], A[0]
        Heapify(A, 0, i)

def test(A):
    for i in range(1, len(A)):
        if A[i-1] > A[i]:
            return False
    return True

x = random.sample(range(1000), 100)
start = timer()
heap_sort(x)
print(timer() - start)
print(x)
print(test(x))
