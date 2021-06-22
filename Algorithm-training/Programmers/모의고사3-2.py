def solution(l, v):
    v.sort()
    gap = [v[0], l-v[-1]]
    for i in range(1,len(v)):
        gap.append((v[i] - v[i-1]) / 2)
    
    return round(max(gap)+0.1)
