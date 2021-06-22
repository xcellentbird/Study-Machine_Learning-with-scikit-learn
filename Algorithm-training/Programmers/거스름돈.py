# DP

def solution(n, money):
    dumb = [1] + [0] * n

    for m in money:
        for c in range(m, n+1):
            dumb[c] += dumb[c - m]

    return dumb[-1]

"""
# DFS Algorithm

def can_go_list(now, n, money):
    ret = []
    for m in money:
        if sum(now) + m <= n:
            if now:
                if now[-1] <= m:
                    ret.append(now + [m])
            else:
                ret.append(now + [m])
                
    return ret

def dfs(now, n, money):
    ret = 0
    if sum(now) == n:
        return 1
    
    for m in can_go_list(now, n, money):
        ret += dfs(m, n, money)
        
    return ret % 1000000007

def solution(n, money):
    return dfs([], n, money)

"""
"""
# Greedy Algorithm

from itertools import product
def solution(n, money):    
    cases = {i:[] for i in range(n+1)}
    cases[0].append({m: 0 for m in money})
    
    for case, m in product(range(1, n+1), money):
        gap = case - m
        if gap >= 0 and gap in cases:
            for c in cases[gap]:
                cc = c.copy()
                cc[m] += 1
                if cc not in cases[case]:
                    cases[case].append(cc)
    return len(cases[n])
"""
