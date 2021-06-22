from itertools import combinations

def solution(m, weights):
    answer = 0
    for n in range(1,len(weights)+1):
        for comb in combinations(weights, n):
            if sum(comb) == m:
                answer+=1
    return answer
