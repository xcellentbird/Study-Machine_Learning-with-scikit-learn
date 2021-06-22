"""
삽입 정렬
앞에서부터 범위를 늘려가며 계속 정렬해나간다.
앞에서 정렬을 해놓기 때문에 늘린 범위에서 맨 마지막 원소만 크기 순서에 맞게
넣으면 된다.
"""

#!/usr/bin/env python
# coding: utf-8

import random
from timeit import default_timer as timer

def insertion_sort(A) :
    for i in range(1, len(A)):
        loc = i - 1
        new_item = A[i]
        while (loc >= 0 and new_item < A[loc]):
            A[loc+1] = A[loc]
            loc -= 1
        A[loc+1] = new_item
                
def test(A):
    for i in range(1, len(A)):
        if A[i-1] > A[i]:
            return False
    return True

x= random.sample(range(10000),100)
start = timer()
insertion_sort(x)
print(timer()-start) # 0.00022159999999998847
print(x)
print(test(x))
