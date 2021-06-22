from itertools import combinations

def is_soinsu(n):
    for i in range(2, n):
        if not n%i:
            return False
    return True
    
def solution(nums):
    answer = 0
    for comb in combinations(nums, 3):
        if is_soinsu(sum(comb)):
            answer+=1
    return answer
