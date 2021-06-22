def solution(m, n, infests, vaccinateds):
    answer = -1
    
    immunes = len(infests + vaccinateds)
    if  immunes == m * n:
        return 0
    
    # padding
    immune = [[1]+[0 for i in range(n)]+[1] for _ in range(m)]
    immune = [[1 for _ in range(n+2)]] + immune + [[1 for _ in range(n+2)]]
    for j, i in infests + vaccinateds:
        immune[j][i] = 1
    
    stack = infests
    dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    while stack:
        answer+=1
        next = []
        while stack:
            now_j, now_i = stack.pop()
            for dj, di in dirs:
                if not immune[now_j + dj][now_i + di]:
                    immune[now_j + dj][now_i + di] = 1
                    immunes +=1
                    next.append([now_j+dj, now_i+di])

        stack = next
    
    if immunes != m * n:
        return -1
    
    return answer
