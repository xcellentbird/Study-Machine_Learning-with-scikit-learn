def solution(priorities, location):
    answer = 0
    p = priorities
    loc = location
    
    while loc >= 0:
        answer+=1
        midx = p.index(max(p))
        n = loc - midx - 1
        if n < -1:
            loc = n+len(p)
        else:
            loc = n
        p = p[midx:] + p[:midx] 
        p.pop(0)

    return answer
