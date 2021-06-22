from itertools import combinations

def is_sosu(num):
    for nn in range(2, num//2):
        if not num % nn:
            return False
    return True

def solution(nums):
    answer = 0
    for comb in combinations(nums, 3):
        if is_sosu(sum(comb)):
            answer+=1
    return answer
