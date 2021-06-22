from sys import stdin
#from pprint import pprint
from itertools import product
from itertools import combinations
from copy import deepcopy


input = stdin.readline
MAX_LADDER_ADD = 3
# N: 세로 줄 개수, M: 기존에 있는 가로 줄 개수, H: 가로 점선 개수
N, M, H = map(int, input().split())
ladder = {col:[] for col in range(1, N+1)}
for _ in range(M):
    row, col = map(int, input().split())
    ladder[col].append([row, col+1])
    ladder[col+1].append([row, col])



def can_set_ladder(plus):
    if not plus:
        return []
    
    candidates = set(product(range(1,H+1), range(1,N))) - set(map(tuple, sum(ladder.values(), [])))

    if plus == 1:
        return [[c] for c in candidates]
        
    ret = []
    for comb in combinations(candidates, plus):
        stack = [[],[]]
        for j, i in comb:
            if (j, i+1) in comb:
                break
        else:
            ret.append(comb)
            
    return ret
    

def go_down(start, ladder):
    goal, cj = start, 0
    while cj <= H:
        for nj, to in ladder[goal]:
            if nj > cj:
                cj = nj
                goal = to
                break
        else:
            break
    return goal


def check_self_goal(ladder):
    for n in range(1, N+1):
        if n != go_down(n, ladder):
            return False
    return True


def play():
    for plus_ladder in range(MAX_LADDER_ADD + 1):
        if not plus_ladder and check_self_goal(ladder):
            return plus_ladder
        
        for more_set in can_set_ladder(plus_ladder):
            cp_ladder = deepcopy(ladder)
            
            for row, col in more_set:
                cp_ladder[col].append([row, col+1])
                cp_ladder[col+1].append([row, col])
                
            for i in cp_ladder:
                cp_ladder[i].sort()
            
            if check_self_goal(cp_ladder):
                return plus_ladder
    return -1

print(play())
