def solution(n,signs):
    for start in range(n):
        now = start
        gone = set()
        stack = [i for i in range(n) if signs[now][i]]
        while stack:
            now = stack.pop()
            gone.add(now)
            stack += [i for i in range(n) if signs[now][i] and i not in gone]
        
        for i in gone:
            signs[start][i] = 1

    return signs
