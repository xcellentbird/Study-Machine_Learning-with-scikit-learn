"""
버블 정렬 n^2
차례로 2개씩({1,2},{2,3},{3,4})골라
작은 숫자가 왼쪽 큰 숫자가 오른쪽에 오도록 바꾸며 정렬
"""

import random
from timeit import default_timer as timer

def bubble_sort(A):
    for last in range(len(A)-1, 0, -1):
        for i in range(last):
            if A[i] > A[i+1]:
                A[i],A[i+1] = A[i+1],A[i]

def test(A):
    for i in range(1, len(A)):
        if A[i-1] > A[i]:
            return False
    return True

x = random.sample(range(10000), 100)
start = timer()
bubble_sort(x)
print(timer() - start) # 0.0005290000000000017
print(x)
print(test(x))
