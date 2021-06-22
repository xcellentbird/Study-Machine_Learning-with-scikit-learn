def bt(N, visited, cnt):
    if len(visited) == cnt:
        print(' '.join(map(str, visited)))
        return

    for i in range(1, N+1):
        if not visited:
            bt(N, visited + [i], cnt)
        elif visited[-1] <= i:
            bt(N, visited + [i], cnt)


N, M = map(int, input().split())
bt(N, [], M)
            
