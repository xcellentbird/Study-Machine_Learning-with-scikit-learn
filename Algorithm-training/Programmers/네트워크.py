def dfs(cur, coms, gone):
    if gone[cur]: 
        return -1
    gone[cur] = True
    print(cur," is done")
    for i, com in enumerate(coms[cur]):
        if cur == i or gone[i] == True or com == 0:
            continue
        else:
            dfs(i, coms, gone)
    return gone

def solution(n, computers):
    answer = 0
    gone = [False for _ in range(n)]
    for N in range(n):
        tmp = dfs(N, computers, gone)
        if tmp != -1:
            answer+=1
            gone = tmp
    return answer
