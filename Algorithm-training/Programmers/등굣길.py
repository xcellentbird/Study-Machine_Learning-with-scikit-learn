from pprint import *
def solution(m, n, puddles):
    loadmap = [[0] * (m+1) for _ in range(n+1)]
    for j in range(1,n+1):
        for i in range(1,m+1):
            if i*j == 1:
                loadmap[j][i] = 1
            elif [i, j] not in puddles:
                loadmap[j][i] = loadmap[j-1][i] + loadmap[j][i-1]
    return loadmap[n][m] % 1000000007



"""
def solution(m, n, puddles):
    answer = 0
    loadmap = [[1] * (m+1) for _ in range(n+1)]
    puddles += [[m+1, j] for j in range(1, n)] + [[i, n+1] for i in range(1, m)]
    dirs = [[-1, -1], [1, -1], [1, 1], [-1, 1]]
    while True:
        pred_len = len(puddles)
        for puddle in puddles:
            loadmap[puddle[1]-1][puddle[0]-1] = 0
            for dx, dy in dirs:
                if [puddle[0] + dx, puddle[1] + dy] in puddles:
                    if [puddle[0], puddle[1] + dy] not in puddles:
                        puddles.append([puddle[0], puddle[1] + dy])
                    if [puddle[0] + dx, puddle[1]] not in puddles:
                        puddles.append([puddle[0] + dx, puddle[1]])
        if len(puddles) - pred_len == 0:
            break

    if [1, 1] in puddles or [m, n] in puddles:
        return 0
    
    for j in range(1,n):
        for i in range(1,m):
            if [i+1,j+1] not in puddles:
                loadmap[j][i] = loadmap[j-1][i] + loadmap[j][i-1]
    return loadmap[n-1][m-1]
"""

"""
def solution(m, n, puddles):
    answer = 1
    for x in range(1,m+1):
        for y in range(1,n+1):
            if [x+1, y] in puddles and [x, y+1] in puddles:
                print('both puddles',x,y)
                if [x-1, y] in puddles and [x, y-1] in puddles:
                    pass
                elif [x-1, y] in puddles or [x, y-1] in puddles or x==1 or y==1:
                    answer-=1
                else:
                    answer-=2
                puddles.append([x+1, y+1])
            elif [x+1, y] in puddles or [x, y+1] in puddles or [x, y] in puddles:
                if x==m or y==n:
                    answer-=1
                continue
            elif x == m or y == n:
                continue
            else:
                print(x, y)
                answer+=1
    return answer%1000000007
"""
