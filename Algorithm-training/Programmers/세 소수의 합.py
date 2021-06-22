from itertools import combinations

def sosu(n):
    ret = list(range(2, n+1))
    for ss in ret:
        for i, num in enumerate(ret):
            if num != ss and num%ss==0:
                del ret[i]
    return ret
    
def solution(n):
    answer = 0
    sosus = sosu(n)
    for comb in combinations(sosus, 3):
        if sum(comb) == n:
            answer+=1
    return answer
