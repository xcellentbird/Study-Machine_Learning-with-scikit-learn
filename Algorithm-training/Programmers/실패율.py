def solution(N, stages):
    answer = range(1,N+1)
    fail = {i+1:0.0 for i in range(N)}
    
    stages.sort()
    while stages:
        now = stages[0]
        cnt = stages.count(now)
        fail[now] = cnt/len(stages)
        stages = stages[cnt:]

    return sorted(answer, reverse=True,key=lambda x: fail[x])
