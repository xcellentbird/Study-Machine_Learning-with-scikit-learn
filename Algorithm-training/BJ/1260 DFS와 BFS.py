from collections import deque

def dfs(start, road, gone):
    gone.append(start)
    for i, can in enumerate(road[start-1]):
        if can and i+1 not in gone:
            dfs(i+1, road, gone)
    return gone


def bfs(start, road, gone):
    gone.append(start)
    stack = deque([start])
    while stack:
        now = stack.popleft()
        for i, can in enumerate(road[now-1]):
            if can and i+1 not in gone:
                gone.append(i+1)
                stack.append(i+1)
    return gone

N, M, start = map(int, input().split())
road = [[False] * N for _ in range(N)]

for _ in range(M):
    n1, n2 = map(int, input().split())
    road[n1-1][n2-1] = True
    road[n2-1][n1-1] = True

print(dfs(start, road, []))
print(bfs(start, road, []))
    
