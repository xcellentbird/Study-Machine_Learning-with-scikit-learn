
def bt(visited, cnt, N):
    if cnt == len(visited)-1:
        print(' '.join(map(str,visited[1:])))
        return
    
    for i in range(N + 1):
        if i not in visited:
            cp = visited.copy()
            cp.append(i)
            bt(cp, cnt, N)


N, M = map(int, input().split())
bt([0], M, N)

