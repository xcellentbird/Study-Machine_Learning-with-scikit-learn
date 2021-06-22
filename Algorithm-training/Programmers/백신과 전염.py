def solution(m, n, infests, vaccinateds):
    answer = 0
    done = [[False for _ in range(n)] for _ in range(m)]
    for check in infests + vaccinateds:
        done[check[0]-1][check[1]-1] = True
    dirs = [[-1,0],[1,0],[0,-1],[0,1]]
    nexts = infests
    while True:
        if False not in [False not in d for d in done]:
            return answer
        elif not nexts:
            return -1
        
        answer += 1
        tmp_nexts = []
        while nexts:
            now = nexts.pop()
            for dm, dn in dirs:
                M = now[0]+dm
                N = now[1]+dn
                if M*N == 0 or M > m or N > n:
                    continue
                if not done[M-1][N-1]:
                    done[M-1][N-1] = True
                    tmp_nexts.append([M,N])
        nexts = tmp_nexts
    return answer
