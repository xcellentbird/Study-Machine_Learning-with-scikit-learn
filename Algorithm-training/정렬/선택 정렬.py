"""
선택 정렬
목록에서 가장 큰 데이터를 선택해
맨 뒤의 데이터와 자리를 맞바꾸는 식으로 정렬
"""

import random
# timeit 모듈에서 default_timer 클래스를 timer이름으로 불러온다
from timeit import default_timer as timer

def selection_sort(A):
    for last in range(len(A)-1, 0, -1): # len(A)-1부터 1까지 -1해가며
        largest = 0 # 가장 큰 원소의 index
        for i in range(1, last+1): # 1부터 last까지
            if A[i] > A[largest]: #현재 원소가 최대 원소보다 크면
                largest=i # 해당 원소의 index를 최대 원소 index로
        x[largest],x[last] = x[last],x[largest] # 나중 원소와 가장 큰 원소를 맞바꾼다

def test(A):
    for i in range(1, len(A)):
        if A[i-1] > A[i]:
            return False
    return True

# random.sample(범위, 개수)
x = random.sample(range(10000), 10)
print(x)
start = timer() # 현재 시간을 불러와 저장
selection_sort(x) # x 행렬 선택 정렬
print(timer() - start)
print(x)
print(test(x))
