N, M, V = map(int, input().split())
line = [list(map(int, input().split())) for _ in range(M)]
lines = [[] for _ in range(N)]
for l in line:
    lines[l[0]-1].append(l[1]-1)
    lines[l[1]-1].append(l[0]-1)

for l in lines:
    l.sort()

def dfs(start, gone, turn, lines):
    gone[start] = True
    turn.append(start+1)
    for can_go in lines[start]:
        if not gone[can_go]:
            cur = can_go
            dfs(cur, gone, turn, lines)
    return turn

def bfs(start, can_go):
    que = []
    turn = []
    visited = [False for _ in road]
    cur = start
    visited[cur-1] = True
    que.append(cur)
    turn.append(cur)
    while len(que) > 0:
        u = que.pop(0)
        for i, next in enumerate(can_go[u-1]):
            if next and visited[i] == False:
                visited[i] = True
                que.append(i+1)
                turn.append(i+1)
                print(i+1)
                print(que)
    print(turn)
            
cur = V - 1
gone = [False for _ in range(N)]
turn = []        

print(dfs(cur, gone, turn, lines))

cur = V - 1
gone = [False for _ in range(N)]
turn = []

print(bfs(cur, gone, turn, lines))
