def check(loc, row):
    for i in range(row):
        gap = abs(loc[i] - loc[row])
        if not gap or gap == row-i:
            return False
    return True

def dfs(loc, row):
    n = len(loc)
    cnt = 0
    if row == n:
        return 1
    for col in range(n):
        loc[row] = col
        if check(loc, row):
            cnt += dfs(loc, row+1)
    return cnt

def solution(n):
    return dfs([0] * n, 0)
