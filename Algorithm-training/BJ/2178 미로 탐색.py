from collections import deque

def can_go(start, road):
    n, m = start
    ret = []
    for dy, dx in [[1, 0],[-1,0],[0,1],[0,-1]]:
        if 0 <= n+dy < len(road) and 0 <= m+dx < len(road[0]) and road[n+dy][m+dx]:
            ret.append([n+dy, m+dx])
    return ret

def dfs(start, road, gone, goal):
    gone.append(start)
    if start == goal:
        return [gone]

    ret = []
    for next_node in can_go(start, road):
        if next_node not in gone and not ret:
            ret += dfs(next_node, road, gone.copy(), goal)

    return ret

def bfs(start, goal, road, visited):
    stack = deque([start])
    visited[start[1]][start[0]] = 1
    
    while stack:
        y, x = stack.popleft()
        if [y, x] == goal:
            return visited[y][x]
            break

        for ny, nx in can_go([y, x], road):
            if not visited[ny][nx]:
                visited[ny][nx] = visited[y][x] + 1
                stack.append([ny, nx])
        
    

N, M = map(int, input().split())
road = []
for _ in range(N):
    road.append(list(map(int,list(input()))))

goal = [N-1, M-1]
visited = [[0] * M for _ in range(N)]   # 이 부분이 포인트다. 방문한 것을 True, False가 아닌 n번차를 집어넣는 것이다.
print(bfs([0, 0], goal, road, visited))
